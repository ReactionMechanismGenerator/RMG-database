#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(117.402,'m^3/(mol*s)'), n=1.48761, w0=(570117,'J/mol'), E0=(-4726.64,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0004221327775445474, var=2.2567826401570867, Tref=1000.0, N=261, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 261 training reactions at node Root
    Total Standard Deviation in ln(k): 3.012692306109207"""),
    rank = 11,
    shortDesc = """BM rule fitted to 261 training reactions at node Root
Total Standard Deviation in ln(k): 3.012692306109207""",
    longDesc = 
"""
BM rule fitted to 261 training reactions at node Root
Total Standard Deviation in ln(k): 3.012692306109207
""",
)

entry(
    index = 2,
    label = "Root_Ext-4R-R",
    kinetics = ArrheniusBM(A=(16.9982,'m^3/(mol*s)'), n=1.74368, w0=(569306,'J/mol'), E0=(4176.63,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1526936704914103, var=3.728449174670692, Tref=1000.0, N=116, data_mean=0.0, correlation='Root_Ext-4R-R',), comment="""BM rule fitted to 116 training reactions at node Root_Ext-4R-R
    Total Standard Deviation in ln(k): 4.254634003307434"""),
    rank = 11,
    shortDesc = """BM rule fitted to 116 training reactions at node Root_Ext-4R-R
Total Standard Deviation in ln(k): 4.254634003307434""",
    longDesc = 
"""
BM rule fitted to 116 training reactions at node Root_Ext-4R-R
Total Standard Deviation in ln(k): 4.254634003307434
""",
)

entry(
    index = 3,
    label = "Root_4R->C",
    kinetics = ArrheniusBM(A=(25.4294,'m^3/(mol*s)'), n=1.49968, w0=(549943,'J/mol'), E0=(73329.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1573255112936277, var=1.0988610670396857, Tref=1000.0, N=35, data_mean=0.0, correlation='Root_4R->C',), comment="""BM rule fitted to 35 training reactions at node Root_4R->C
    Total Standard Deviation in ln(k): 2.4967853339357835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 35 training reactions at node Root_4R->C
Total Standard Deviation in ln(k): 2.4967853339357835""",
    longDesc = 
"""
BM rule fitted to 35 training reactions at node Root_4R->C
Total Standard Deviation in ln(k): 2.4967853339357835
""",
)

entry(
    index = 4,
    label = "Root_N-4R->C",
    kinetics = ArrheniusBM(A=(907.891,'m^3/(mol*s)'), n=1.27509, w0=(577391,'J/mol'), E0=(52213.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05102129554290216, var=1.1721711800071382, Tref=1000.0, N=110, data_mean=0.0, correlation='Root_N-4R->C',), comment="""BM rule fitted to 110 training reactions at node Root_N-4R->C
    Total Standard Deviation in ln(k): 2.2986578208100665"""),
    rank = 11,
    shortDesc = """BM rule fitted to 110 training reactions at node Root_N-4R->C
Total Standard Deviation in ln(k): 2.2986578208100665""",
    longDesc = 
"""
BM rule fitted to 110 training reactions at node Root_N-4R->C
Total Standard Deviation in ln(k): 2.2986578208100665
""",
)

entry(
    index = 5,
    label = "Root_Ext-4R-R_5R!H-u0",
    kinetics = ArrheniusBM(A=(12.7333,'m^3/(mol*s)'), n=1.8456, w0=(568731,'J/mol'), E0=(15458.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07304503226612491, var=2.5251974228462277, Tref=1000.0, N=80, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0',), comment="""BM rule fitted to 80 training reactions at node Root_Ext-4R-R_5R!H-u0
    Total Standard Deviation in ln(k): 3.3692286371447917"""),
    rank = 11,
    shortDesc = """BM rule fitted to 80 training reactions at node Root_Ext-4R-R_5R!H-u0
Total Standard Deviation in ln(k): 3.3692286371447917""",
    longDesc = 
"""
BM rule fitted to 80 training reactions at node Root_Ext-4R-R_5R!H-u0
Total Standard Deviation in ln(k): 3.3692286371447917
""",
)

entry(
    index = 6,
    label = "Root_Ext-4R-R_N-5R!H-u0",
    kinetics = ArrheniusBM(A=(789280,'m^3/(mol*s)'), n=-0.29166, w0=(570583,'J/mol'), E0=(30927.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1210837340392117, var=5.494145081621931, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0',), comment="""BM rule fitted to 36 training reactions at node Root_Ext-4R-R_N-5R!H-u0
    Total Standard Deviation in ln(k): 7.515810679653067"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_Ext-4R-R_N-5R!H-u0
Total Standard Deviation in ln(k): 7.515810679653067""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_Ext-4R-R_N-5R!H-u0
Total Standard Deviation in ln(k): 7.515810679653067
""",
)

entry(
    index = 7,
    label = "Root_4R->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(412790,'m^3/(mol*s)'), n=-0.0180494, w0=(537647,'J/mol'), E0=(54872.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0629801988686796, var=0.8591103216422448, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R',), comment="""BM rule fitted to 17 training reactions at node Root_4R->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 2.0163946499159495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.0163946499159495""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.0163946499159495
""",
)

entry(
    index = 8,
    label = "Root_4R->C_2R!H->C",
    kinetics = ArrheniusBM(A=(42.5674,'m^3/(mol*s)'), n=1.42312, w0=(560045,'J/mol'), E0=(56004.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08726592646601207, var=0.8090639017036623, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_4R->C_2R!H->C',), comment="""BM rule fitted to 11 training reactions at node Root_4R->C_2R!H->C
    Total Standard Deviation in ln(k): 2.0224798183184474"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_4R->C_2R!H->C
Total Standard Deviation in ln(k): 2.0224798183184474""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_4R->C_2R!H->C
Total Standard Deviation in ln(k): 2.0224798183184474
""",
)

entry(
    index = 9,
    label = "Root_4R->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(18.9422,'m^3/(mol*s)'), n=1.54277, w0=(563929,'J/mol'), E0=(73729.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10216535735278572, var=1.5902534649614286, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_4R->C_N-2R!H->C
    Total Standard Deviation in ln(k): 2.784773104426826"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_4R->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.784773104426826""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_4R->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.784773104426826
""",
)

entry(
    index = 10,
    label = "Root_N-4R->C_4BrClFHNOS->N",
    kinetics = ArrheniusBM(A=(135.128,'m^3/(mol*s)'), n=1.35032, w0=(569125,'J/mol'), E0=(45279.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0878760628512102, var=0.3426554930674657, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->C_4BrClFHNOS->N
    Total Standard Deviation in ln(k): 1.3943015440412758"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->C_4BrClFHNOS->N
Total Standard Deviation in ln(k): 1.3943015440412758""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->C_4BrClFHNOS->N
Total Standard Deviation in ln(k): 1.3943015440412758
""",
)

entry(
    index = 11,
    label = "Root_N-4R->C_N-4BrClFHNOS->N",
    kinetics = ArrheniusBM(A=(1186.67,'m^3/(mol*s)'), n=1.28666, w0=(578039,'J/mol'), E0=(49020.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04314565667996649, var=0.661668492901669, Tref=1000.0, N=102, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N',), comment="""BM rule fitted to 102 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N
    Total Standard Deviation in ln(k): 1.739117984300388"""),
    rank = 11,
    shortDesc = """BM rule fitted to 102 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N
Total Standard Deviation in ln(k): 1.739117984300388""",
    longDesc = 
"""
BM rule fitted to 102 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N
Total Standard Deviation in ln(k): 1.739117984300388
""",
)

entry(
    index = 12,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(927.381,'m^3/(mol*s)'), n=0.855533, w0=(542539,'J/mol'), E0=(-21008.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.0343988567935423, var=32.89097493672838, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R',), comment="""BM rule fitted to 38 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R
    Total Standard Deviation in ln(k): 16.60884165917055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R
Total Standard Deviation in ln(k): 16.60884165917055""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R
Total Standard Deviation in ln(k): 16.60884165917055
""",
)

entry(
    index = 13,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.01406e+15,'m^3/(mol*s)'), n=-2.6518, w0=(547450,'J/mol'), E0=(98093.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19817893304755343, var=2.685594580518956, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.783253521247228"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.783253521247228""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.783253521247228
""",
)

entry(
    index = 14,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O",
    kinetics = ArrheniusBM(A=(12.4764,'m^3/(mol*s)'), n=1.90962, w0=(626450,'J/mol'), E0=(-1544.65,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16932990987661106, var=0.7219026662879217, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O
    Total Standard Deviation in ln(k): 2.1287722956754958"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O
Total Standard Deviation in ln(k): 2.1287722956754958""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O
Total Standard Deviation in ln(k): 2.1287722956754958
""",
)

entry(
    index = 15,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O",
    kinetics = ArrheniusBM(A=(48.6081,'m^3/(mol*s)'), n=1.60722, w0=(597409,'J/mol'), E0=(24025.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4668752249235713, var=5.379515027487191, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O',), comment="""BM rule fitted to 22 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O
    Total Standard Deviation in ln(k): 5.822792074713624"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O
Total Standard Deviation in ln(k): 5.822792074713624""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O
Total Standard Deviation in ln(k): 5.822792074713624
""",
)

entry(
    index = 16,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(752801,'m^3/(mol*s)'), n=-0.432205, w0=(569967,'J/mol'), E0=(-1979.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12346143515422116, var=7.154851495153441, Tref=1000.0, N=30, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H',), comment="""BM rule fitted to 30 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 5.672581089846829"""),
    rank = 11,
    shortDesc = """BM rule fitted to 30 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 5.672581089846829""",
    longDesc = 
"""
BM rule fitted to 30 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 5.672581089846829
""",
)

entry(
    index = 17,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(603797,'m^3/(mol*s)'), n=-0.252586, w0=(573667,'J/mol'), E0=(58914.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.0974356926028035, var=6.090517001843564, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 10.217419177750209"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 10.217419177750209""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 10.217419177750209
""",
)

entry(
    index = 18,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1",
    kinetics = ArrheniusBM(A=(463468,'m^3/(mol*s)'), n=-0.0491774, w0=(537562,'J/mol'), E0=(46255,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03679849302046633, var=0.6324206272155354, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1',), comment="""BM rule fitted to 16 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1
    Total Standard Deviation in ln(k): 1.6867216561565224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1
Total Standard Deviation in ln(k): 1.6867216561565224""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1
Total Standard Deviation in ln(k): 1.6867216561565224
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
    kinetics = ArrheniusBM(A=(1.09946e+07,'m^3/(mol*s)'), n=-0.4, w0=(536700,'J/mol'), E0=(53670,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.8901034371418295e-09, var=3.9478985007336416, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_4R->C_2R!H->C_Ext-2C-R',), comment="""BM rule fitted to 5 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 3.983272144382623"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 3.983272144382623""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 3.983272144382623
""",
)

entry(
    index = 21,
    label = "Root_4R->C_2R!H->C_1R!H->N",
    kinetics = ArrheniusBM(A=(34.41,'m^3/(mol*s)'), n=1.44661, w0=(544000,'J/mol'), E0=(54400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.43780050013999694, var=0.5999111817527254, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_2R!H->C_1R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_1R!H->N
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
    kinetics = ArrheniusBM(A=(6.75617e+07,'m^3/(mol*s)'), n=-0.0357893, w0=(597250,'J/mol'), E0=(59725,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.1140300975885116, var=16.478303783487792, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N
    Total Standard Deviation in ln(k): 13.449550144949319"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N
Total Standard Deviation in ln(k): 13.449550144949319""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N
Total Standard Deviation in ln(k): 13.449550144949319
""",
)

entry(
    index = 23,
    label = "Root_4R->C_N-2R!H->C_1R!H->C",
    kinetics = ArrheniusBM(A=(112.108,'m^3/(mol*s)'), n=1.32982, w0=(553333,'J/mol'), E0=(46062.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0717197421632481, var=0.9019355839057234, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_1R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C
    Total Standard Deviation in ln(k): 2.0841030587678717"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C
Total Standard Deviation in ln(k): 2.0841030587678717""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C
Total Standard Deviation in ln(k): 2.0841030587678717
""",
)

entry(
    index = 24,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C",
    kinetics = ArrheniusBM(A=(1.3412,'m^3/(mol*s)'), n=1.86465, w0=(571875,'J/mol'), E0=(75550.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3126929772038274, var=0.8180504301847403, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C
    Total Standard Deviation in ln(k): 2.5988662482268197"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C
Total Standard Deviation in ln(k): 2.5988662482268197""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C
Total Standard Deviation in ln(k): 2.5988662482268197
""",
)

entry(
    index = 25,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1",
    kinetics = ArrheniusBM(A=(123.068,'m^3/(mol*s)'), n=1.35445, w0=(577357,'J/mol'), E0=(43871.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08389730555039457, var=0.3778871149952897, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1
    Total Standard Deviation in ln(k): 1.4431584924233987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1
Total Standard Deviation in ln(k): 1.4431584924233987""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1
Total Standard Deviation in ln(k): 1.4431584924233987
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
    kinetics = ArrheniusBM(A=(369.642,'m^3/(mol*s)'), n=1.46442, w0=(674250,'J/mol'), E0=(39890.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.25108916160271877, var=1.7016564312025784, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O
    Total Standard Deviation in ln(k): 3.2460051605980356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O
Total Standard Deviation in ln(k): 3.2460051605980356""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O
Total Standard Deviation in ln(k): 3.2460051605980356
""",
)

entry(
    index = 28,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O",
    kinetics = ArrheniusBM(A=(1351.57,'m^3/(mol*s)'), n=1.2667, w0=(569851,'J/mol'), E0=(48747.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04457660364156392, var=0.7127097352225874, Tref=1000.0, N=94, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O',), comment="""BM rule fitted to 94 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O
    Total Standard Deviation in ln(k): 1.8044417264284958"""),
    rank = 11,
    shortDesc = """BM rule fitted to 94 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O
Total Standard Deviation in ln(k): 1.8044417264284958""",
    longDesc = 
"""
BM rule fitted to 94 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O
Total Standard Deviation in ln(k): 1.8044417264284958
""",
)

entry(
    index = 29,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S",
    kinetics = ArrheniusBM(A=(3.12126e-13,'m^3/(mol*s)'), n=4.70087, w0=(527000,'J/mol'), E0=(18952.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=10.214760863631724, var=288.9982061655396, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S
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
    kinetics = ArrheniusBM(A=(10877.4,'m^3/(mol*s)'), n=0.589799, w0=(543403,'J/mol'), E0=(12326,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0653032817649546, var=8.068653946952884, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S',), comment="""BM rule fitted to 36 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S
    Total Standard Deviation in ln(k): 8.371166808584357"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S
Total Standard Deviation in ln(k): 8.371166808584357""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S
Total Standard Deviation in ln(k): 8.371166808584357
""",
)

entry(
    index = 31,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F",
    kinetics = ArrheniusBM(A=(1.41422e+07,'m^3/(mol*s)'), n=-2.73693e-07, w0=(533250,'J/mol'), E0=(53325,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F
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
    kinetics = ArrheniusBM(A=(4.60111e+10,'m^3/(mol*s)'), n=-1.50942, w0=(551000,'J/mol'), E0=(79150.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.035191120264449004, var=1.51276769435368, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F
    Total Standard Deviation in ln(k): 2.5541362227675948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F
Total Standard Deviation in ln(k): 2.5541362227675948""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F
Total Standard Deviation in ln(k): 2.5541362227675948
""",
)

entry(
    index = 33,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(15.3304,'m^3/(mol*s)'), n=1.9099, w0=(626125,'J/mol'), E0=(2484.78,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1407769403985442, var=3.37967505049648, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 6.551757143687097"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 6.551757143687097""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 6.551757143687097
""",
)

entry(
    index = 34,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(7.45181,'m^3/(mol*s)'), n=1.90892, w0=(627750,'J/mol'), E0=(62775,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9020850168172384, var=0.018792661167653626, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 2.541367037610754"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.541367037610754""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.541367037610754
""",
)

entry(
    index = 35,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_5R!H->N",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(598500,'J/mol'), E0=(25539.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_5R!H->N
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
    kinetics = ArrheniusBM(A=(26.9307,'m^3/(mol*s)'), n=1.7319, w0=(597357,'J/mol'), E0=(6978.32,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06672288957484286, var=0.8966671555641027, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N',), comment="""BM rule fitted to 21 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N
    Total Standard Deviation in ln(k): 2.0659794260000552"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N
Total Standard Deviation in ln(k): 2.0659794260000552""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N
Total Standard Deviation in ln(k): 2.0659794260000552
""",
)

entry(
    index = 37,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C",
    kinetics = ArrheniusBM(A=(35432.5,'m^3/(mol*s)'), n=-0.0782154, w0=(566190,'J/mol'), E0=(-6444.19,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3074895951892539, var=5.898287006844586, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C',), comment="""BM rule fitted to 29 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 5.64136455711653"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 5.64136455711653""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 5.64136455711653
""",
)

entry(
    index = 38,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_N-1R!H->C",
    kinetics = ArrheniusBM(A=(5.7209e+06,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(21251.9,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_N-1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_N-1R!H->C
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
    kinetics = ArrheniusBM(A=(1.1728e+06,'m^3/(mol*s)'), n=0.0395251, w0=(551500,'J/mol'), E0=(88327.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.019980832352546246, var=5.109907527584295, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 4.581927702938342"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.581927702938342""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.581927702938342
""",
)

entry(
    index = 40,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_1R!H->C",
    kinetics = ArrheniusBM(A=(2.6e+09,'m^3/(mol*s)'), n=-1.26, w0=(551500,'J/mol'), E0=(36171.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_N-1R!H->C",
    kinetics = ArrheniusBM(A=(1.2e+06,'m^3/(mol*s)'), n=-0.34, w0=(684500,'J/mol'), E0=(61489.3,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_N-1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_N-1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(8.75589e+07,'m^3/(mol*s)'), n=-0.747098, w0=(539000,'J/mol'), E0=(79266.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07702656740044439, var=0.33570438571816813, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H',), comment="""BM rule fitted to 14 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.3550776372806772"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.3550776372806772""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.3550776372806772
""",
)

entry(
    index = 43,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(1.70881e+08,'m^3/(mol*s)'), n=-0.472801, w0=(527500,'J/mol'), E0=(84970.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5979439084933458, var=3.7234503612782164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 5.370757369061902"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 5.370757369061902""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 5.370757369061902
""",
)

entry(
    index = 44,
    label = "Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H",
    kinetics = ArrheniusBM(A=(1.12583e+07,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.1325748326963947e-10, var=0.7152290114772514, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H
    Total Standard Deviation in ln(k): 1.6954287784336384"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H
Total Standard Deviation in ln(k): 1.6954287784336384""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H
Total Standard Deviation in ln(k): 1.6954287784336384
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
    kinetics = ArrheniusBM(A=(8.11905e+07,'m^3/(mol*s)'), n=-0.34, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=14.717775896447819, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N_1CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C
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
    kinetics = ArrheniusBM(A=(6.61167e+07,'m^3/(mol*s)'), n=2.77409e-07, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.7507532944488107, var=36.13951493076956, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C
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
    kinetics = ArrheniusBM(A=(87.4311,'m^3/(mol*s)'), n=1.32982, w0=(547000,'J/mol'), E0=(26923.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6145937820984377, var=1.0855875416035785, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C
    Total Standard Deviation in ln(k): 3.632969679603918"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C
Total Standard Deviation in ln(k): 3.632969679603918""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C
Total Standard Deviation in ln(k): 3.632969679603918
""",
)

entry(
    index = 52,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1",
    kinetics = ArrheniusBM(A=(0.000300457,'m^3/(mol*s)'), n=2.90916, w0=(587833,'J/mol'), E0=(53336.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06537920785741069, var=0.4178197286624608, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1
    Total Standard Deviation in ln(k): 1.460109602607063"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1
Total Standard Deviation in ln(k): 1.460109602607063""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1
Total Standard Deviation in ln(k): 1.460109602607063
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
    kinetics = ArrheniusBM(A=(97.18,'m^3/(mol*s)'), n=1.38035, w0=(581125,'J/mol'), E0=(36409.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11829132718474578, var=0.9716962311524417, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 2.273375045931692"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.273375045931692""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.273375045931692
""",
)

entry(
    index = 56,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(82.6213,'m^3/(mol*s)'), n=1.38035, w0=(591250,'J/mol'), E0=(59125,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5787018105298811, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H
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
    kinetics = ArrheniusBM(A=(367.482,'m^3/(mol*s)'), n=1.46504, w0=(675714,'J/mol'), E0=(39255.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.23040060453207614, var=1.604970773965762, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl
    Total Standard Deviation in ln(k): 3.118643562240369"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl
Total Standard Deviation in ln(k): 3.118643562240369""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl
Total Standard Deviation in ln(k): 3.118643562240369
""",
)

entry(
    index = 59,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl",
    kinetics = ArrheniusBM(A=(1.44239e+07,'m^3/(mol*s)'), n=-2.48375e-07, w0=(551367,'J/mol'), E0=(55136.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=6.097474536866056e-08, var=1.7133390373383008, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl',), comment="""BM rule fitted to 15 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl
    Total Standard Deviation in ln(k): 2.6240896592663483"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl
Total Standard Deviation in ln(k): 2.6240896592663483""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl
Total Standard Deviation in ln(k): 2.6240896592663483
""",
)

entry(
    index = 60,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl",
    kinetics = ArrheniusBM(A=(1342.12,'m^3/(mol*s)'), n=1.26766, w0=(573361,'J/mol'), E0=(48754.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.038130115588318, var=0.7134943170659944, Tref=1000.0, N=79, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl',), comment="""BM rule fitted to 79 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl
    Total Standard Deviation in ln(k): 1.7891758198905598"""),
    rank = 11,
    shortDesc = """BM rule fitted to 79 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl
Total Standard Deviation in ln(k): 1.7891758198905598""",
    longDesc = 
"""
BM rule fitted to 79 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl
Total Standard Deviation in ln(k): 1.7891758198905598
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
    kinetics = ArrheniusBM(A=(175315,'m^3/(mol*s)'), n=-0.0266151, w0=(563000,'J/mol'), E0=(47386.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.016941222855406207, var=0.25108833239472356, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O
    Total Standard Deviation in ln(k): 1.0471128740072233"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O
Total Standard Deviation in ln(k): 1.0471128740072233""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O
Total Standard Deviation in ln(k): 1.0471128740072233
""",
)

entry(
    index = 63,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O",
    kinetics = ArrheniusBM(A=(9661,'m^3/(mol*s)'), n=0.617407, w0=(534780,'J/mol'), E0=(12165.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1848182904711855, var=9.185274718448706, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O',), comment="""BM rule fitted to 25 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O
    Total Standard Deviation in ln(k): 9.052724709936838"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O
Total Standard Deviation in ln(k): 9.052724709936838""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O
Total Standard Deviation in ln(k): 9.052724709936838
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
    kinetics = ArrheniusBM(A=(3.17823e+11,'m^3/(mol*s)'), n=-1.70222, w0=(539000,'J/mol'), E0=(77696.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7296759618564476, var=5.577703322483751, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R
    Total Standard Deviation in ln(k): 6.567971960206649"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R
Total Standard Deviation in ln(k): 6.567971960206649""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R
Total Standard Deviation in ln(k): 6.567971960206649
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
    kinetics = ArrheniusBM(A=(173205,'m^3/(mol*s)'), n=4.78218e-08, w0=(563000,'J/mol'), E0=(46720.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02717882471367332, var=0.9016442819744953, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C
    Total Standard Deviation in ln(k): 1.9718837253164718"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C
Total Standard Deviation in ln(k): 1.9718837253164718""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C
Total Standard Deviation in ln(k): 1.9718837253164718
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
    kinetics = ArrheniusBM(A=(15.2824,'m^3/(mol*s)'), n=1.91038, w0=(621929,'J/mol'), E0=(2870.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1415685882747755, var=3.382093009292552, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br
    Total Standard Deviation in ln(k): 6.555064346336348"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br
Total Standard Deviation in ln(k): 6.555064346336348""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br
Total Standard Deviation in ln(k): 6.555064346336348
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
    kinetics = ArrheniusBM(A=(11.5345,'m^3/(mol*s)'), n=1.89876, w0=(644100,'J/mol'), E0=(-9546.99,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07560329521445057, var=1.0459132763509869, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O
    Total Standard Deviation in ln(k): 2.2401986182117053"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O
Total Standard Deviation in ln(k): 2.2401986182117053""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O
Total Standard Deviation in ln(k): 2.2401986182117053
""",
)

entry(
    index = 74,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O",
    kinetics = ArrheniusBM(A=(146.337,'m^3/(mol*s)'), n=1.39949, w0=(554864,'J/mol'), E0=(49607.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19047884493463266, var=0.47713960910107933, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O
    Total Standard Deviation in ln(k): 1.8633666894886218"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O
Total Standard Deviation in ln(k): 1.8633666894886218""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O
Total Standard Deviation in ln(k): 1.8633666894886218
""",
)

entry(
    index = 75,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.012927,'m^3/(mol*s)'), n=1.69628, w0=(567205,'J/mol'), E0=(-19047.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.9351199177640503, var=3.7808423270872993, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R',), comment="""BM rule fitted to 22 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.272757869730851"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.272757869730851""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.272757869730851
""",
)

entry(
    index = 76,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.83577e+15,'m^3/(mol*s)'), n=-3.11592, w0=(563000,'J/mol'), E0=(47359.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.42719562175432013, var=21.080487329451405, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 10.277794595290711"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 10.277794595290711""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 10.277794595290711
""",
)

entry(
    index = 77,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.95203e+06,'m^3/(mol*s)'), n=0.050255, w0=(551500,'J/mol'), E0=(97203.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.025047528400067427, var=6.658095631177459, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 5.235808723554527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C
Total Standard Deviation in ln(k): 5.235808723554527""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C
Total Standard Deviation in ln(k): 5.235808723554527
""",
)

entry(
    index = 78,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(300000,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(62482.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_N-6R!H->C
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
    kinetics = ArrheniusBM(A=(1.99882e+07,'m^3/(mol*s)'), n=-0.370164, w0=(539000,'J/mol'), E0=(90186,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6037507179253697, var=1.5551483149344354, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C
    Total Standard Deviation in ln(k): 4.0169782264072875"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 4.0169782264072875""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 4.0169782264072875
""",
)

entry(
    index = 80,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.85258e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.5776908135481615e-09, var=0.1268395936700701, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C',), comment="""BM rule fitted to 11 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C
    Total Standard Deviation in ln(k): 0.7139773143291225"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 0.7139773143291225""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 0.7139773143291225
""",
)

entry(
    index = 81,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_5R!H->C",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(80439.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_5R!H->C
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
    kinetics = ArrheniusBM(A=(1.12583e+07,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=2.413897921625164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H_Ext-2C-R
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
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(547000,'J/mol'), E0=(47204.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R
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
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->O",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(638000,'J/mol'), E0=(77300.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O",
    kinetics = ArrheniusBM(A=(0.000102789,'m^3/(mol*s)'), n=3.02936, w0=(562750,'J/mol'), E0=(46662.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7670379154643546, var=0.03800384237125995, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O
    Total Standard Deviation in ln(k): 2.3180455107971594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O
Total Standard Deviation in ln(k): 2.3180455107971594""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O
Total Standard Deviation in ln(k): 2.3180455107971594
""",
)

entry(
    index = 91,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N",
    kinetics = ArrheniusBM(A=(81.7183,'m^3/(mol*s)'), n=1.38035, w0=(550250,'J/mol'), E0=(15501.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6277682977428172, var=3.9952970257614115, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N
    Total Standard Deviation in ln(k): 5.58441968796261"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N
Total Standard Deviation in ln(k): 5.58441968796261""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N
Total Standard Deviation in ln(k): 5.58441968796261
""",
)

entry(
    index = 92,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N",
    kinetics = ArrheniusBM(A=(1181.95,'m^3/(mol*s)'), n=1.09226, w0=(612000,'J/mol'), E0=(51896.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8795514576303777, var=0.27427177062219643, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N
    Total Standard Deviation in ln(k): 3.2598273397788256"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N
Total Standard Deviation in ln(k): 3.2598273397788256""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N
Total Standard Deviation in ln(k): 3.2598273397788256
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
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C",
    kinetics = ArrheniusBM(A=(7.34951e+07,'m^3/(mol*s)'), n=-7.11037e-07, w0=(689375,'J/mol'), E0=(68937.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9201383257063358, var=2.9037194220213784, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C
    Total Standard Deviation in ln(k): 5.728034749677716"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C
Total Standard Deviation in ln(k): 5.728034749677716""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C
Total Standard Deviation in ln(k): 5.728034749677716
""",
)

entry(
    index = 96,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C",
    kinetics = ArrheniusBM(A=(332.977,'m^3/(mol*s)'), n=1.47687, w0=(657500,'J/mol'), E0=(38236.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.017984135041135677, var=0.8031311668451452, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C
    Total Standard Deviation in ln(k): 1.8417814451854784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C
Total Standard Deviation in ln(k): 1.8417814451854784""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C
Total Standard Deviation in ln(k): 1.8417814451854784
""",
)

entry(
    index = 97,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(8.87803e+06,'m^3/(mol*s)'), n=-4.10123e-07, w0=(545200,'J/mol'), E0=(54520,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=9.303196595140881e-08, var=1.034892855629619, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.0394108880485278"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.0394108880485278""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.0394108880485278
""",
)

entry(
    index = 98,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(2.15444e+07,'m^3/(mol*s)'), n=-5.00893e-07, w0=(543667,'J/mol'), E0=(54366.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=9.301008691979127e-08, var=3.9764239945747235, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R
    Total Standard Deviation in ln(k): 3.9976370149681917"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R
Total Standard Deviation in ln(k): 3.9976370149681917""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R
Total Standard Deviation in ln(k): 3.9976370149681917
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
    kinetics = ArrheniusBM(A=(740.831,'m^3/(mol*s)'), n=1.33202, w0=(572735,'J/mol'), E0=(39712.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03918368284625255, var=0.9135322140998403, Tref=1000.0, N=66, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1',), comment="""BM rule fitted to 66 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1
    Total Standard Deviation in ln(k): 2.014554781487788"""),
    rank = 11,
    shortDesc = """BM rule fitted to 66 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1
Total Standard Deviation in ln(k): 2.014554781487788""",
    longDesc = 
"""
BM rule fitted to 66 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1
Total Standard Deviation in ln(k): 2.014554781487788
""",
)

entry(
    index = 102,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1",
    kinetics = ArrheniusBM(A=(7616.49,'m^3/(mol*s)'), n=1.07269, w0=(576538,'J/mol'), E0=(57268.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.030828607100139734, var=0.3548071229103219, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1',), comment="""BM rule fitted to 13 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1
    Total Standard Deviation in ln(k): 1.2715930603362295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1
Total Standard Deviation in ln(k): 1.2715930603362295""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1
Total Standard Deviation in ln(k): 1.2715930603362295
""",
)

entry(
    index = 103,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(100000,'m^3/(mol*s)'), n=-1.67043e-08, w0=(563000,'J/mol'), E0=(36356.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04041381052546226, var=0.00816637992065566, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.28270618685229504"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.28270618685229504""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.28270618685229504
""",
)

entry(
    index = 104,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(8.57466e+07,'m^3/(mol*s)'), n=-0.753162, w0=(563000,'J/mol'), E0=(63389.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06065952962909553, var=0.46336969559087504, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.517059381574501"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.517059381574501""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.517059381574501
""",
)

entry(
    index = 105,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H",
    kinetics = ArrheniusBM(A=(166.08,'m^3/(mol*s)'), n=1.15846, w0=(539000,'J/mol'), E0=(74778.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.26697665507436175, var=8.057689119723543, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H
    Total Standard Deviation in ln(k): 6.361450434535762"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H
Total Standard Deviation in ln(k): 6.361450434535762""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H
Total Standard Deviation in ln(k): 6.361450434535762
""",
)

entry(
    index = 106,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H",
    kinetics = ArrheniusBM(A=(14342.3,'m^3/(mol*s)'), n=0.567352, w0=(533725,'J/mol'), E0=(11809,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.164262613991866, var=9.375172181691621, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H',), comment="""BM rule fitted to 20 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H
    Total Standard Deviation in ln(k): 9.063561828254608"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H
Total Standard Deviation in ln(k): 9.063561828254608""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H
Total Standard Deviation in ln(k): 9.063561828254608
""",
)

entry(
    index = 107,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-4R-R",
    kinetics = ArrheniusBM(A=(50000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(28607.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-4R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-4R-R
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
    kinetics = ArrheniusBM(A=(173209,'m^3/(mol*s)'), n=-2.95014e-06, w0=(563000,'J/mol'), E0=(47270.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=2.413897921625164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C_Ext-2R!H-R
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
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(55904.1,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_2R!H->C
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
    kinetics = ArrheniusBM(A=(15.2296,'m^3/(mol*s)'), n=1.91087, w0=(612333,'J/mol'), E0=(2965.54,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1395481231662083, var=3.3805976305003753, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C
    Total Standard Deviation in ln(k): 6.549172658499261"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C
Total Standard Deviation in ln(k): 6.549172658499261""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C
Total Standard Deviation in ln(k): 6.549172658499261
""",
)

entry(
    index = 112,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS",
    kinetics = ArrheniusBM(A=(16.4899,'m^3/(mol*s)'), n=1.89829, w0=(646000,'J/mol'), E0=(-10447.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6480263322841945, var=1.293750506036768, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS
    Total Standard Deviation in ln(k): 3.9084557695133912"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS
Total Standard Deviation in ln(k): 3.9084557695133912""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS
Total Standard Deviation in ln(k): 3.9084557695133912
""",
)

entry(
    index = 113,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS",
    kinetics = ArrheniusBM(A=(8.061,'m^3/(mol*s)'), n=1.89922, w0=(641250,'J/mol'), E0=(12420.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.3711567153290467, var=11.658515309510786, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS
    Total Standard Deviation in ln(k): 12.802761527155994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS
Total Standard Deviation in ln(k): 12.802761527155994""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS
Total Standard Deviation in ln(k): 12.802761527155994
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
    kinetics = ArrheniusBM(A=(144.129,'m^3/(mol*s)'), n=1.40126, w0=(547200,'J/mol'), E0=(49527.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1691271190160095, var=0.19213928126014665, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O
    Total Standard Deviation in ln(k): 1.3036919683868717"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O
Total Standard Deviation in ln(k): 1.3036919683868717""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O
Total Standard Deviation in ln(k): 1.3036919683868717
""",
)

entry(
    index = 116,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.91603,'m^3/(mol*s)'), n=1.11255, w0=(563000,'J/mol'), E0=(-5574.81,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3246410927130465, var=1.207216089304916, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 3.0183514420362267"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 3.0183514420362267""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 3.0183514420362267
""",
)

entry(
    index = 117,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.65069e+08,'m^3/(mol*s)'), n=-1.27319, w0=(570115,'J/mol'), E0=(-11134.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3230279596810188, var=3.8343474292594264, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 13 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 7.249760801148101"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 7.249760801148101""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 7.249760801148101
""",
)

entry(
    index = 118,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(7.23e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(98206,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_6R!H->C
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
    kinetics = ArrheniusBM(A=(8.76105e+09,'m^3/(mol*s)'), n=-1.65753, w0=(563000,'J/mol'), E0=(5326.41,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10875162242360512, var=17.37066161063481, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 8.628605335626894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 8.628605335626894""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 8.628605335626894
""",
)

entry(
    index = 120,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(300000,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(63328.3,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C_Ext-1R!H-R
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
    kinetics = ArrheniusBM(A=(8.32046e+06,'m^3/(mol*s)'), n=-0.32, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.610921668180418e-17, var=0.8378904353806431, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H
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
    kinetics = ArrheniusBM(A=(3.01e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(98876.6,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_N-Sp-5C-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_N-Sp-5C-1R!H
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
    kinetics = ArrheniusBM(A=(6.5e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.776356839400249e-15, var=4.861730685829018e-62, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 4.463208139196606e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 4.463208139196606e-15""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 4.463208139196606e-15
""",
)

entry(
    index = 124,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(9.19239e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.9900208155345065e-10, var=0.2847128973348199, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.0696964641597664"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.0696964641597664""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.0696964641597664
""",
)

entry(
    index = 125,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_2NO->O",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(601500,'J/mol'), E0=(74546.6,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 126,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_N-2NO->O",
    kinetics = ArrheniusBM(A=(0.82,'m^3/(mol*s)'), n=1.87, w0=(524000,'J/mol'), E0=(52400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 127,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->O",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(589000,'J/mol'), E0=(44850.4,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 128,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->O",
    kinetics = ArrheniusBM(A=(0.46,'m^3/(mol*s)'), n=1.94, w0=(511500,'J/mol'), E0=(51150,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 129,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->O",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(598500,'J/mol'), E0=(35265.4,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 130,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->O",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(625500,'J/mol'), E0=(51836,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1",
    kinetics = ArrheniusBM(A=(2.43626e+07,'m^3/(mol*s)'), n=-3.94121e-07, w0=(692667,'J/mol'), E0=(69266.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-6.387022933619493e-08, var=0.0926741995759308, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1
    Total Standard Deviation in ln(k): 0.6102903817479576"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1
Total Standard Deviation in ln(k): 0.6102903817479576""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1
Total Standard Deviation in ln(k): 0.6102903817479576
""",
)

entry(
    index = 132,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_N-4BrFHO-u1",
    kinetics = ArrheniusBM(A=(9.04e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(67950,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_N-4BrFHO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_N-4BrFHO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_N-4BrFHO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_N-4BrFHO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O",
    kinetics = ArrheniusBM(A=(583.069,'m^3/(mol*s)'), n=1.37285, w0=(662000,'J/mol'), E0=(38263.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.677782331949925, var=4.796931240730101, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O
    Total Standard Deviation in ln(k): 6.0937209469057585"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O
Total Standard Deviation in ln(k): 6.0937209469057585""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O
Total Standard Deviation in ln(k): 6.0937209469057585
""",
)

entry(
    index = 134,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_N-4BrFHO->O",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(648500,'J/mol'), E0=(59054.4,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_N-4BrFHO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_N-4BrFHO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_N-4BrFHO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_N-4BrFHO->O
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
    kinetics = ArrheniusBM(A=(7.58362e+06,'m^3/(mol*s)'), n=-7.78049e-08, w0=(544944,'J/mol'), E0=(54494.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.8883145633511746e-08, var=0.8399501805428713, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O
    Total Standard Deviation in ln(k): 1.8373157090604704"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O
Total Standard Deviation in ln(k): 1.8373157090604704""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O
Total Standard Deviation in ln(k): 1.8373157090604704
""",
)

entry(
    index = 137,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=5.5633e-08, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN
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
    kinetics = ArrheniusBM(A=(6.31766e+06,'m^3/(mol*s)'), n=0.108145, w0=(619889,'J/mol'), E0=(61988.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.010247370673702226, var=0.5940640460165689, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F
    Total Standard Deviation in ln(k): 1.5709077562510265"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F
Total Standard Deviation in ln(k): 1.5709077562510265""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F
Total Standard Deviation in ln(k): 1.5709077562510265
""",
)

entry(
    index = 140,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F",
    kinetics = ArrheniusBM(A=(736.578,'m^3/(mol*s)'), n=1.3328, w0=(565289,'J/mol'), E0=(38951.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03919591860533826, var=0.913679429666748, Tref=1000.0, N=57, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F',), comment="""BM rule fitted to 57 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F
    Total Standard Deviation in ln(k): 2.0147399082496906"""),
    rank = 11,
    shortDesc = """BM rule fitted to 57 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F
Total Standard Deviation in ln(k): 2.0147399082496906""",
    longDesc = 
"""
BM rule fitted to 57 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F
Total Standard Deviation in ln(k): 2.0147399082496906
""",
)

entry(
    index = 141,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(31748.8,'m^3/(mol*s)'), n=0.921032, w0=(572250,'J/mol'), E0=(64773.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05804281371033715, var=0.39010212525224314, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.397956777635269"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.397956777635269""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.397956777635269
""",
)

entry(
    index = 142,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(5519.78,'m^3/(mol*s)'), n=1.06696, w0=(583400,'J/mol'), E0=(58340,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04094681569454899, var=0.00022216925571612398, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 0.1327627108093306"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.1327627108093306""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.1327627108093306
""",
)

entry(
    index = 143,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(100000,'m^3/(mol*s)'), n=-2.68823e-08, w0=(563000,'J/mol'), E0=(35294.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06575491895535468, var=0.012971124571770375, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 0.3935343361482046"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.3935343361482046""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.3935343361482046
""",
)

entry(
    index = 144,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(141423,'m^3/(mol*s)'), n=-1.48867e-06, w0=(563000,'J/mol'), E0=(42592.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R_Ext-2R!H-R
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
    kinetics = ArrheniusBM(A=(84300,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(76690.3,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-5BrCClFNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-5BrCClFNO-R
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
    kinetics = ArrheniusBM(A=(0.000740847,'m^3/(mol*s)'), n=2.91991, w0=(539000,'J/mol'), E0=(35253.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004220313209984355, var=8.94173911161422, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R
    Total Standard Deviation in ln(k): 6.005311154003196"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R
Total Standard Deviation in ln(k): 6.005311154003196""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R
Total Standard Deviation in ln(k): 6.005311154003196
""",
)

entry(
    index = 147,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Sp-5BrCClFNO-4BrCCClFNOS",
    kinetics = ArrheniusBM(A=(964000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(93078.1,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Sp-5BrCClFNO-4BrCCClFNOS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Sp-5BrCClFNO-4BrCCClFNOS
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
    kinetics = ArrheniusBM(A=(27604.4,'m^3/(mol*s)'), n=0.515881, w0=(537029,'J/mol'), E0=(28652.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4187770672773609, var=0.5880256007401398, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C',), comment="""BM rule fitted to 17 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C
    Total Standard Deviation in ln(k): 2.589491224458921"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C
Total Standard Deviation in ln(k): 2.589491224458921""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C
Total Standard Deviation in ln(k): 2.589491224458921
""",
)

entry(
    index = 150,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C",
    kinetics = ArrheniusBM(A=(6.41947,'m^3/(mol*s)'), n=1.17357, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.5769113207128034, var=36.01419836199652, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C
    Total Standard Deviation in ln(k): 21.017996600377636"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C
Total Standard Deviation in ln(k): 21.017996600377636""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C
Total Standard Deviation in ln(k): 21.017996600377636
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
    kinetics = ArrheniusBM(A=(15.1785,'m^3/(mol*s)'), n=1.91136, w0=(603700,'J/mol'), E0=(3168.34,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1404052888457155, var=3.3839331448169303, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C
    Total Standard Deviation in ln(k): 6.553144308026429"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C
Total Standard Deviation in ln(k): 6.553144308026429""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C
Total Standard Deviation in ln(k): 6.553144308026429
""",
)

entry(
    index = 153,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_Ext-5BrCClOS-R",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(57605.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_Ext-5BrCClOS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_Ext-5BrCClOS-R
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
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C",
    kinetics = ArrheniusBM(A=(1.25258e+07,'m^3/(mol*s)'), n=-0.25, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.1810001589909576e-08, var=0.029912994917102368, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C
    Total Standard Deviation in ln(k): 0.3467264768243492"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C
Total Standard Deviation in ln(k): 0.3467264768243492""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C
Total Standard Deviation in ln(k): 0.3467264768243492
""",
)

entry(
    index = 155,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C",
    kinetics = ArrheniusBM(A=(15.3833,'m^3/(mol*s)'), n=1.90892, w0=(627000,'J/mol'), E0=(3567.89,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.5381307692919615, var=13.508926399484995, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C
    Total Standard Deviation in ln(k): 21.283203251633662"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C
Total Standard Deviation in ln(k): 21.283203251633662""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C
Total Standard Deviation in ln(k): 21.283203251633662
""",
)

entry(
    index = 156,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C",
    kinetics = ArrheniusBM(A=(7.88926,'m^3/(mol*s)'), n=1.90164, w0=(636500,'J/mol'), E0=(6189.33,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.770444177625181, var=0.8389362826639978, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C
    Total Standard Deviation in ln(k): 8.797121340169468"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C
Total Standard Deviation in ln(k): 8.797121340169468""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C
Total Standard Deviation in ln(k): 8.797121340169468
""",
)

entry(
    index = 157,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C",
    kinetics = ArrheniusBM(A=(1.81e+08,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(57517.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C
Total Standard Deviation in ln(k): 11.540182761524994
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
    kinetics = ArrheniusBM(A=(142.296,'m^3/(mol*s)'), n=1.40303, w0=(548111,'J/mol'), E0=(49521.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2522282775466774, var=0.23998003463305903, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS
    Total Standard Deviation in ln(k): 1.6158141411644942"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS
Total Standard Deviation in ln(k): 1.6158141411644942""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS
Total Standard Deviation in ln(k): 1.6158141411644942
""",
)

entry(
    index = 160,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C",
    kinetics = ArrheniusBM(A=(197748,'m^3/(mol*s)'), n=-0.281594, w0=(563000,'J/mol'), E0=(39565.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0626457718590481, var=0.3132846222734017, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C
    Total Standard Deviation in ln(k): 1.2794884303248724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C
Total Standard Deviation in ln(k): 1.2794884303248724""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C
Total Standard Deviation in ln(k): 1.2794884303248724
""",
)

entry(
    index = 161,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_N-Sp-6C-1C",
    kinetics = ArrheniusBM(A=(602200,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(41171.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_N-Sp-6C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_N-Sp-6C-1C
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
    kinetics = ArrheniusBM(A=(3.0021e+13,'m^3/(mol*s)'), n=-2.85939, w0=(563000,'J/mol'), E0=(-4729.27,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6296620029244422, var=1.6509959419220757, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 4.157971224895596"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.157971224895596""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.157971224895596
""",
)

entry(
    index = 163,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C",
    kinetics = ArrheniusBM(A=(6.16313e+13,'m^3/(mol*s)'), n=-2.80189, w0=(563000,'J/mol'), E0=(5291.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4255240777775006, var=13.821651684987778, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C
    Total Standard Deviation in ln(k): 8.52225620149561"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C
Total Standard Deviation in ln(k): 8.52225620149561""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C
Total Standard Deviation in ln(k): 8.52225620149561
""",
)

entry(
    index = 164,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(300000,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(58373.3,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_N-2R!H->C
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
    kinetics = ArrheniusBM(A=(4.23154e+13,'m^3/(mol*s)'), n=-2.80189, w0=(563000,'J/mol'), E0=(3228.53,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.5413776977322353, var=14.920781743222996, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 11.616584221080103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.616584221080103""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.616584221080103
""",
)

entry(
    index = 166,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(250000,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(44954.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFINOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFINOPSSi->F
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
    kinetics = ArrheniusBM(A=(6.5e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.3306690738754637e-15, var=2.3336307291979278e-61, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 8.368515260993628e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 8.368515260993628e-15""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 8.368515260993628e-15
""",
)

entry(
    index = 169,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(9.19239e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R_Ext-2R!H-R
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
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_4BrFHO->F",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(732500,'J/mol'), E0=(73250,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_4BrFHO->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_4BrFHO->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_4BrFHO->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_4BrFHO->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F",
    kinetics = ArrheniusBM(A=(2.19545e+07,'m^3/(mol*s)'), n=-8.3404e-08, w0=(672750,'J/mol'), E0=(67275,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=6.458191251135313e-17, var=0.06954925777421293, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F
    Total Standard Deviation in ln(k): 0.5286926091131748"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F
Total Standard Deviation in ln(k): 0.5286926091131748""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F
Total Standard Deviation in ln(k): 0.5286926091131748
""",
)

entry(
    index = 172,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O_4O-u1",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(662000,'J/mol'), E0=(66200,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O_4O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O_4O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O_4O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O_4O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 173,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O_N-4O-u1",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(662000,'J/mol'), E0=(47796.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O_N-4O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O_N-4O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O_N-4O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O_N-4O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 174,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.10064e+07,'m^3/(mol*s)'), n=-1.78124e-08, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.922311953607987e-09, var=0.6944265498726213, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.6705910549111327"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.6705910549111327""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.6705910549111327
""",
)

entry(
    index = 175,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(7.46843e+06,'m^3/(mol*s)'), n=-5.5568e-08, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4459791400965826e-08, var=1.435194410242175, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 2.401664635278017"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 2.401664635278017""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 2.401664635278017
""",
)

entry(
    index = 176,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(4.47213e+06,'m^3/(mol*s)'), n=1.22363e-07, w0=(536000,'J/mol'), E0=(53600,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.7221843336360836e-16, var=5.180580787960471, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 4.56295530433249"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 4.56295530433249""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 4.56295530433249
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
    kinetics = ArrheniusBM(A=(928951,'m^3/(mol*s)'), n=0.324434, w0=(608333,'J/mol'), E0=(60833.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.030742105113024276, var=1.1012302894203079, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R
    Total Standard Deviation in ln(k): 2.1810008410965263"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R
Total Standard Deviation in ln(k): 2.1810008410965263""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R
Total Standard Deviation in ln(k): 2.1810008410965263
""",
)

entry(
    index = 179,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.15443e+07,'m^3/(mol*s)'), n=7.58759e-08, w0=(612167,'J/mol'), E0=(61216.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.454125948319283e-08, var=1.4663744066546285, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.4276129495279983"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.4276129495279983""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.4276129495279983
""",
)

entry(
    index = 180,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_2R!H->C",
    kinetics = ArrheniusBM(A=(1.41422e+07,'m^3/(mol*s)'), n=-2.73693e-07, w0=(604500,'J/mol'), E0=(60450,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_2R!H->C
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
    kinetics = ArrheniusBM(A=(2007.91,'m^3/(mol*s)'), n=1.24075, w0=(556260,'J/mol'), E0=(5113.95,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09347690683235675, var=6.199315581217347, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R',), comment="""BM rule fitted to 25 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 5.226341159340728"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.226341159340728""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.226341159340728
""",
)

entry(
    index = 183,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(16913.2,'m^3/(mol*s)'), n=0.796338, w0=(558273,'J/mol'), E0=(55827.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07545790308104353, var=2.197613351053908, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R',), comment="""BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R
    Total Standard Deviation in ln(k): 3.1614820452932446"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R
Total Standard Deviation in ln(k): 3.1614820452932446""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R
Total Standard Deviation in ln(k): 3.1614820452932446
""",
)

entry(
    index = 184,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H",
    kinetics = ArrheniusBM(A=(11848.2,'m^3/(mol*s)'), n=1.05839, w0=(578650,'J/mol'), E0=(67832,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01071672945664871, var=0.31255637084490123, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H
    Total Standard Deviation in ln(k): 1.1477085068199595"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H
Total Standard Deviation in ln(k): 1.1477085068199595""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H
Total Standard Deviation in ln(k): 1.1477085068199595
""",
)

entry(
    index = 185,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H",
    kinetics = ArrheniusBM(A=(188.44,'m^3/(mol*s)'), n=1.42021, w0=(580682,'J/mol'), E0=(52364.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0309169092026573, var=0.27972890794902555, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H',), comment="""BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H
    Total Standard Deviation in ln(k): 1.137973115152647"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H
Total Standard Deviation in ln(k): 1.137973115152647""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H
Total Standard Deviation in ln(k): 1.137973115152647
""",
)

entry(
    index = 186,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C",
    kinetics = ArrheniusBM(A=(16691.8,'m^3/(mol*s)'), n=1.06281, w0=(569750,'J/mol'), E0=(56975,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17212421231842373, var=0.2098488348088565, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C
    Total Standard Deviation in ln(k): 1.350827209327121"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 1.350827209327121""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 1.350827209327121
""",
)

entry(
    index = 187,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C",
    kinetics = ArrheniusBM(A=(18025.9,'m^3/(mol*s)'), n=0.976731, w0=(574750,'J/mol'), E0=(61506.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12388961528846384, var=0.3650578432012104, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C
    Total Standard Deviation in ln(k): 1.5225417112954849"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 1.5225417112954849""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 1.5225417112954849
""",
)

entry(
    index = 188,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3083.04,'m^3/(mol*s)'), n=1.1631, w0=(551500,'J/mol'), E0=(55150,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.202693327970796, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_Ext-2R!H-R
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
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->C",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 190,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C",
    kinetics = ArrheniusBM(A=(5522.51,'m^3/(mol*s)'), n=1.06688, w0=(621500,'J/mol'), E0=(62150,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4478648794535599, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C
    Total Standard Deviation in ln(k): 1.1252886418431154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 1.1252886418431154""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 1.1252886418431154
""",
)

entry(
    index = 191,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(100000,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(34326,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
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
    kinetics = ArrheniusBM(A=(2.89e+07,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(85952.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R_Ext-4CS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R_Ext-4CS-R
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
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=-5.78148e-08, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
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
    kinetics = ArrheniusBM(A=(26224,'m^3/(mol*s)'), n=0.520794, w0=(536767,'J/mol'), E0=(10825.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22921274464481153, var=0.21137083693004927, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C',), comment="""BM rule fitted to 15 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
    Total Standard Deviation in ln(k): 1.4975900589830373"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
Total Standard Deviation in ln(k): 1.4975900589830373""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
Total Standard Deviation in ln(k): 1.4975900589830373
""",
)

entry(
    index = 195,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(6.55713e+06,'m^3/(mol*s)'), n=-0.267658, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27677043112298655, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.6954030932738355"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.6954030932738355""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.6954030932738355
""",
)

entry(
    index = 196,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O",
    kinetics = ArrheniusBM(A=(1.61026e-31,'m^3/(mol*s)'), n=11.0657, w0=(648500,'J/mol'), E0=(-42067.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.2161474031403197, var=3.9048845960022436, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O
    Total Standard Deviation in ln(k): 9.529722607276149"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O
Total Standard Deviation in ln(k): 9.529722607276149""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O
Total Standard Deviation in ln(k): 9.529722607276149
""",
)

entry(
    index = 197,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O",
    kinetics = ArrheniusBM(A=(15.137,'m^3/(mol*s)'), n=1.91136, w0=(573833,'J/mol'), E0=(25162,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04219251724153787, var=0.002993508762106159, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O
    Total Standard Deviation in ln(k): 0.21569635406258736"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O
Total Standard Deviation in ln(k): 0.21569635406258736""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O
Total Standard Deviation in ln(k): 0.21569635406258736
""",
)

entry(
    index = 198,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(2.85561e+07,'m^3/(mol*s)'), n=-0.375, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.305460834090209e-17, var=0.06912283083491383, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_Ext-4CNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_Ext-4CNS-R
    Total Standard Deviation in ln(k): 0.5270693322083513"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.5270693322083513""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.5270693322083513
""",
)

entry(
    index = 199,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C_2R!H->C",
    kinetics = ArrheniusBM(A=(4.82e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 200,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(598500,'J/mol'), E0=(12737.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 201,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C",
    kinetics = ArrheniusBM(A=(1.90316e+07,'m^3/(mol*s)'), n=4.59272e-07, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=1.6812080230698707, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C
    Total Standard Deviation in ln(k): 2.599367689841769"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C
Total Standard Deviation in ln(k): 2.599367689841769""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C
Total Standard Deviation in ln(k): 2.599367689841769
""",
)

entry(
    index = 202,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(598500,'J/mol'), E0=(16284.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_2CNS->S",
    kinetics = ArrheniusBM(A=(979000,'m^3/(mol*s)'), n=0, w0=(537500,'J/mol'), E0=(38210.6,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_2CNS->S',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_2CNS->S
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
    kinetics = ArrheniusBM(A=(139.69,'m^3/(mol*s)'), n=1.40572, w0=(549438,'J/mol'), E0=(42012.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17454073129629247, var=0.11803036545376881, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S
    Total Standard Deviation in ln(k): 1.1272822658262969"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S
Total Standard Deviation in ln(k): 1.1272822658262969""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S
Total Standard Deviation in ln(k): 1.1272822658262969
""",
)

entry(
    index = 205,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=-4.54695e-08, w0=(563000,'J/mol'), E0=(20049.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0995900706403493e-09, var=3.2373231707220126e-17, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R
    Total Standard Deviation in ln(k): 1.4169226414297233e-08"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R
Total Standard Deviation in ln(k): 1.4169226414297233e-08""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R
Total Standard Deviation in ln(k): 1.4169226414297233e-08
""",
)

entry(
    index = 206,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(10974.6,'m^3/(mol*s)'), n=-5.34527e-07, w0=(563000,'J/mol'), E0=(19979,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.2290956255676566e-17, var=0.06917824979652494, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-1C-R
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
    kinetics = ArrheniusBM(A=(3.0307e+11,'m^3/(mol*s)'), n=-2.27927, w0=(563000,'J/mol'), E0=(-10868.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.43306595333064035, var=3.6164591051866672, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 4.9005081121201695"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.9005081121201695""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.9005081121201695
""",
)

entry(
    index = 208,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.63887e+13,'m^3/(mol*s)'), n=-2.80189, w0=(563000,'J/mol'), E0=(-2927.31,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.9625539661448137, var=2.873931729472119, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 8.329602239965505"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 8.329602239965505""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 8.329602239965505
""",
)

entry(
    index = 209,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.32924e+13,'m^3/(mol*s)'), n=-2.80189, w0=(563000,'J/mol'), E0=(7698.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.9625539661448181, var=15.771671451551667, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 12.892557544298018"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 12.892557544298018""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 12.892557544298018
""",
)

entry(
    index = 210,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(4.23154e+13,'m^3/(mol*s)'), n=-2.80189, w0=(563000,'J/mol'), E0=(3303.27,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.9625539661448104, var=30.52594293923304, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F_Ext-2R!H-R
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
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F_4HO->O",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(67950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F_4HO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F_4HO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F_4HO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F_4HO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 213,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F_N-4HO->O",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(666000,'J/mol'), E0=(66600,'J/mol'), Tmin=(295,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F_N-4HO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F_N-4HO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F_N-4HO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F_N-4HO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 214,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1.41422e+07,'m^3/(mol*s)'), n=-2.73693e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R
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
    kinetics = ArrheniusBM(A=(1.41422e+07,'m^3/(mol*s)'), n=-2.73693e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R
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
    kinetics = ArrheniusBM(A=(1.41422e+07,'m^3/(mol*s)'), n=-2.73693e-07, w0=(616000,'J/mol'), E0=(61600,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
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
    kinetics = ArrheniusBM(A=(2060.82,'m^3/(mol*s)'), n=1.14711, w0=(561071,'J/mol'), E0=(56107.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10869531361862755, var=0.3368659888145768, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN',), comment="""BM rule fitted to 14 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.4366552003926638"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.4366552003926638""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.4366552003926638
""",
)

entry(
    index = 223,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(2007.44,'m^3/(mol*s)'), n=1.24159, w0=(550136,'J/mol'), E0=(2509.05,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08615057082658226, var=6.438366245739957, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 5.303260661689328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 5.303260661689328""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 5.303260661689328
""",
)

entry(
    index = 224,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN",
    kinetics = ArrheniusBM(A=(98204.3,'m^3/(mol*s)'), n=0.583981, w0=(557800,'J/mol'), E0=(55780,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.055335798014313015, var=1.3598222086802618, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN
    Total Standard Deviation in ln(k): 2.476784607280254"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN
Total Standard Deviation in ln(k): 2.476784607280254""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN
Total Standard Deviation in ln(k): 2.476784607280254
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
    kinetics = ArrheniusBM(A=(85796.8,'m^3/(mol*s)'), n=0.835908, w0=(573286,'J/mol'), E0=(74548.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005970836226809338, var=0.30460465695705496, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.1214354537229818"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.1214354537229818""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.1214354537229818
""",
)

entry(
    index = 227,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(7796.49,'m^3/(mol*s)'), n=1.06688, w0=(591167,'J/mol'), E0=(59116.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04104070874570528, var=0.0, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 0.10311735865755094"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.10311735865755094""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.10311735865755094
""",
)

entry(
    index = 228,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(237.713,'m^3/(mol*s)'), n=1.42105, w0=(571688,'J/mol'), E0=(59638,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18482246020973167, var=0.6092348615723725, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 2.0291439027027534"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 2.0291439027027534""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 2.0291439027027534
""",
)

entry(
    index = 229,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(126.016,'m^3/(mol*s)'), n=1.42089, w0=(604667,'J/mol'), E0=(60466.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05487466445996819, var=7.222237291452136e-35, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 0.137876041356704"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.137876041356704""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.137876041356704
""",
)

entry(
    index = 230,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.73206e+07,'m^3/(mol*s)'), n=-4.41572e-07, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.610921668180418e-17, var=2.413897921625164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.1147015559000413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.1147015559000413""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.1147015559000413
""",
)

entry(
    index = 231,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 232,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(577500,'J/mol'), E0=(57750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 233,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(11125.3,'m^3/(mol*s)'), n=1.02912, w0=(573833,'J/mol'), E0=(59041.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.299248606283007, var=0.7060555812172096, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 2.4364019402425674"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.4364019402425674""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.4364019402425674
""",
)

entry(
    index = 234,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(558500,'J/mol'), E0=(55850,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 235,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
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
    kinetics = ArrheniusBM(A=(340826,'m^3/(mol*s)'), n=-2.03079e-07, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O
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
    kinetics = ArrheniusBM(A=(25585.2,'m^3/(mol*s)'), n=0.525802, w0=(536423,'J/mol'), E0=(16667.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3908773333449694, var=0.27500524975255697, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O',), comment="""BM rule fitted to 13 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O
    Total Standard Deviation in ln(k): 2.033405830868172"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O
Total Standard Deviation in ln(k): 2.033405830868172""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O
Total Standard Deviation in ln(k): 2.033405830868172
""",
)

entry(
    index = 239,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R_Ext-5BrCClFNO-R",
    kinetics = ArrheniusBM(A=(763000,'m^3/(mol*s)'), n=0, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R_Ext-5BrCClFNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R_Ext-5BrCClFNO-R
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
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O_2NO->O",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(635000,'J/mol'), E0=(5024.25,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 241,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O_N-2NO->O",
    kinetics = ArrheniusBM(A=(0.0294,'m^3/(mol*s)'), n=2.69, w0=(662000,'J/mol'), E0=(32779.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 242,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_2NO->O",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(625500,'J/mol'), E0=(25430.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 243,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O",
    kinetics = ArrheniusBM(A=(15.137,'m^3/(mol*s)'), n=1.91136, w0=(548000,'J/mol'), E0=(30276.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1875435576844586, var=0.2924491380841903, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O
    Total Standard Deviation in ln(k): 4.067909779950639"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O
Total Standard Deviation in ln(k): 4.067909779950639""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O
Total Standard Deviation in ln(k): 4.067909779950639
""",
)

entry(
    index = 244,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_Ext-4CNS-R_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(3.47e+08,'m^3/(mol*s)'), n=-0.75, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_Ext-4CNS-R_Ext-4CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_Ext-4CNS-R_Ext-4CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 245,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C_Sp-5C=4CNS",
    kinetics = ArrheniusBM(A=(3.01e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C_Sp-5C=4CNS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C_Sp-5C=4CNS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C_Sp-5C=4CNS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C_Sp-5C=4CNS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 246,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C_N-Sp-5C=4CNS",
    kinetics = ArrheniusBM(A=(1.20333e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C_N-Sp-5C=4CNS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C_N-Sp-5C=4CNS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C_N-Sp-5C=4CNS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C_N-Sp-5C=4CNS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 247,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O",
    kinetics = ArrheniusBM(A=(127.638,'m^3/(mol*s)'), n=1.41908, w0=(593500,'J/mol'), E0=(49929.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2786278929612721, var=0.671686074395935, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O
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
    kinetics = ArrheniusBM(A=(1.38436e+07,'m^3/(mol*s)'), n=-0.304179, w0=(534750,'J/mol'), E0=(27148.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1610975619575171, var=0.25986302638912895, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O
    Total Standard Deviation in ln(k): 1.4267167727232863"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O
Total Standard Deviation in ln(k): 1.4267167727232863""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O
Total Standard Deviation in ln(k): 1.4267167727232863
""",
)

entry(
    index = 249,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=1.04025e-08, w0=(563000,'J/mol'), E0=(20462.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0028364088007472965, var=1.6090429769913437e-05, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.015168224625318876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.015168224625318876""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.015168224625318876
""",
)

entry(
    index = 250,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.80955e+17,'m^3/(mol*s)'), n=-4.02589, w0=(563000,'J/mol'), E0=(-16292.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.0479857729357676, var=0.6986086580074955, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 6.821306861840784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.821306861840784""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.821306861840784
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
    kinetics = ArrheniusBM(A=(572.743,'m^3/(mol*s)'), n=1.33829, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12681119225473717, var=0.23881573391697927, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O
    Total Standard Deviation in ln(k): 1.2983105950839768"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O
Total Standard Deviation in ln(k): 1.2983105950839768""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O
Total Standard Deviation in ln(k): 1.2983105950839768
""",
)

entry(
    index = 255,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O",
    kinetics = ArrheniusBM(A=(4.47213e+06,'m^3/(mol*s)'), n=1.22363e-07, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.7221843336360836e-16, var=5.180580787960471, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O
    Total Standard Deviation in ln(k): 4.56295530433249"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O
Total Standard Deviation in ln(k): 4.56295530433249""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O
Total Standard Deviation in ln(k): 4.56295530433249
""",
)

entry(
    index = 256,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl",
    kinetics = ArrheniusBM(A=(3.53554e+06,'m^3/(mol*s)'), n=-1.09028e-07, w0=(551500,'J/mol'), E0=(55150,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl
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
    kinetics = ArrheniusBM(A=(1988.48,'m^3/(mol*s)'), n=1.24316, w0=(549833,'J/mol'), E0=(2404.15,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0853766345119742, var=6.4772112735667235, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl
    Total Standard Deviation in ln(k): 5.316638293761892"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl
Total Standard Deviation in ln(k): 5.316638293761892""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl
Total Standard Deviation in ln(k): 5.316638293761892
""",
)

entry(
    index = 258,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O",
    kinetics = ArrheniusBM(A=(30664.3,'m^3/(mol*s)'), n=0.834259, w0=(561357,'J/mol'), E0=(56135.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07905113352128393, var=0.3453609181023778, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O
    Total Standard Deviation in ln(k): 1.3767519407346676"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O
Total Standard Deviation in ln(k): 1.3767519407346676""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O
Total Standard Deviation in ln(k): 1.3767519407346676
""",
)

entry(
    index = 259,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O",
    kinetics = ArrheniusBM(A=(1.48465e+06,'m^3/(mol*s)'), n=2.29799e-07, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.867666109535814e-08, var=0.4209387762059027, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O
    Total Standard Deviation in ln(k): 1.3006680748136894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O
Total Standard Deviation in ln(k): 1.3006680748136894""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O
Total Standard Deviation in ln(k): 1.3006680748136894
""",
)

entry(
    index = 260,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1",
    kinetics = ArrheniusBM(A=(195914,'m^3/(mol*s)'), n=0.728106, w0=(579750,'J/mol'), E0=(75748.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11458226821384726, var=0.5473307149387985, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1
    Total Standard Deviation in ln(k): 1.7710342984077196"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1
Total Standard Deviation in ln(k): 1.7710342984077196""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1
Total Standard Deviation in ln(k): 1.7710342984077196
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
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->C",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(557500,'J/mol'), E0=(55750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 263,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C",
    kinetics = ArrheniusBM(A=(7796.49,'m^3/(mol*s)'), n=1.06688, w0=(608000,'J/mol'), E0=(60800,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4478648794535599, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C
    Total Standard Deviation in ln(k): 1.1252886418431154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 1.1252886418431154""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 1.1252886418431154
""",
)

entry(
    index = 264,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C",
    kinetics = ArrheniusBM(A=(397.28,'m^3/(mol*s)'), n=1.41402, w0=(568625,'J/mol'), E0=(74091.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.4609729313402307, var=2.0491971481854323, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C
    Total Standard Deviation in ln(k): 6.540567952752803"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 6.540567952752803""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 6.540567952752803
""",
)

entry(
    index = 265,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C",
    kinetics = ArrheniusBM(A=(211.933,'m^3/(mol*s)'), n=1.42089, w0=(574750,'J/mol'), E0=(57475,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05487466092377532, var=0.21353467425975017, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C
    Total Standard Deviation in ln(k): 1.064260346634528"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 1.064260346634528""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 1.064260346634528
""",
)

entry(
    index = 266,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->C",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 267,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C",
    kinetics = ArrheniusBM(A=(126.016,'m^3/(mol*s)'), n=1.42089, w0=(621500,'J/mol'), E0=(62150,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570073, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C
    Total Standard Deviation in ln(k): 1.5045994199924806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 1.5045994199924806""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 1.5045994199924806
""",
)

entry(
    index = 268,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 269,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1",
    kinetics = ArrheniusBM(A=(323.865,'m^3/(mol*s)'), n=1.46107, w0=(586750,'J/mol'), E0=(41163.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2542472977095757, var=0.697260485871222, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1
    Total Standard Deviation in ln(k): 2.3128086935501897"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1
Total Standard Deviation in ln(k): 2.3128086935501897""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1
Total Standard Deviation in ln(k): 2.3128086935501897
""",
)

entry(
    index = 270,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_N-2NO-u1",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_N-2NO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_N-2NO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_N-2NO-u1
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
    kinetics = ArrheniusBM(A=(19988.7,'m^3/(mol*s)'), n=0.559386, w0=(505500,'J/mol'), E0=(12064,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.511937133666525, var=0.2069864860586801, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R
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
    kinetics = ArrheniusBM(A=(4.00744e+06,'m^3/(mol*s)'), n=-0.141163, w0=(545700,'J/mol'), E0=(31056.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22296204600083722, var=0.4436300115667286, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R
    Total Standard Deviation in ln(k): 1.8954710942084847"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R
Total Standard Deviation in ln(k): 1.8954710942084847""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R
Total Standard Deviation in ln(k): 1.8954710942084847
""",
)

entry(
    index = 274,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(974410,'m^3/(mol*s)'), n=-0.0210882, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00199823545031128, var=3.088879903029536e-05, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.01616254705267359"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.01616254705267359""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.01616254705267359
""",
)

entry(
    index = 275,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C",
    kinetics = ArrheniusBM(A=(1.8697e+06,'m^3/(mol*s)'), n=-0.0316323, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0327092327690802, var=0.00213978781668374, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C
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
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O_2N-u1",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(548000,'J/mol'), E0=(35623.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 278,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O_N-2N-u1",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 279,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_1CNS->C",
    kinetics = ArrheniusBM(A=(2.89e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 280,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_N-1CNS->C",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(648000,'J/mol'), E0=(54367.6,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_N-1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_N-1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 281,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS",
    kinetics = ArrheniusBM(A=(8.57298e+06,'m^3/(mol*s)'), n=-0.225015, w0=(533900,'J/mol'), E0=(31128.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19506345554400223, var=0.22967145394007588, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS
    Total Standard Deviation in ln(k): 1.4508594195758966"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS
Total Standard Deviation in ln(k): 1.4508594195758966""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS
Total Standard Deviation in ln(k): 1.4508594195758966
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
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(22326.1,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R_Ext-8R!H-R
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
    kinetics = ArrheniusBM(A=(215.206,'m^3/(mol*s)'), n=1.45995, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13833948165421717, var=0.15570236834851095, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R
    Total Standard Deviation in ln(k): 1.1386378464411426"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R
Total Standard Deviation in ln(k): 1.1386378464411426""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R
Total Standard Deviation in ln(k): 1.1386378464411426
""",
)

entry(
    index = 285,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F",
    kinetics = ArrheniusBM(A=(305.778,'m^3/(mol*s)'), n=1.45995, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13833949465947395, var=0.7152290144266888, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F
    Total Standard Deviation in ln(k): 2.04301545139227"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F
Total Standard Deviation in ln(k): 2.04301545139227""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F
Total Standard Deviation in ln(k): 2.04301545139227
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
    kinetics = ArrheniusBM(A=(254.888,'m^3/(mol*s)'), n=1.41958, w0=(555400,'J/mol'), E0=(55540,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4881063299421182, var=0.994178810217759, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O
    Total Standard Deviation in ln(k): 3.2252894032194144"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O
Total Standard Deviation in ln(k): 3.2252894032194144""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O
Total Standard Deviation in ln(k): 3.2252894032194144
""",
)

entry(
    index = 290,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O",
    kinetics = ArrheniusBM(A=(15553.5,'m^3/(mol*s)'), n=1.06652, w0=(542875,'J/mol'), E0=(31432.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.6445312294543435, var=4.3725426070167535, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O
    Total Standard Deviation in ln(k): 8.324014465824444"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O
Total Standard Deviation in ln(k): 8.324014465824444""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O
Total Standard Deviation in ln(k): 8.324014465824444
""",
)

entry(
    index = 291,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(13119.3,'m^3/(mol*s)'), n=0.973302, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09222632417491634, var=0.25758957263443955, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.249193298066019"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.249193298066019""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.249193298066019
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
    kinetics = ArrheniusBM(A=(1.27916e+06,'m^3/(mol*s)'), n=-3.7648e-08, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9639738002758667, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C
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
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C",
    kinetics = ArrheniusBM(A=(23739.9,'m^3/(mol*s)'), n=1.06417, w0=(589333,'J/mol'), E0=(58933.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4757799687165822, var=4.841357739016837, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C
    Total Standard Deviation in ln(k): 8.119025613270948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C
Total Standard Deviation in ln(k): 8.119025613270948""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C
Total Standard Deviation in ln(k): 8.119025613270948
""",
)

entry(
    index = 296,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C",
    kinetics = ArrheniusBM(A=(13543.8,'m^3/(mol*s)'), n=1.04025, w0=(570167,'J/mol'), E0=(67908.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03528808515442663, var=0.6782750349712002, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C
    Total Standard Deviation in ln(k): 1.7397123143732096"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C
Total Standard Deviation in ln(k): 1.7397123143732096""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C
Total Standard Deviation in ln(k): 1.7397123143732096
""",
)

entry(
    index = 297,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(545000,'J/mol'), E0=(54500,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 298,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(671000,'J/mol'), E0=(67100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 299,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(7.55757e+06,'m^3/(mol*s)'), n=9.49857e-08, w0=(538750,'J/mol'), E0=(53875,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04203615609740776, var=10.372060585311102, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 6.562004850526279"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C
Total Standard Deviation in ln(k): 6.562004850526279""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C
Total Standard Deviation in ln(k): 6.562004850526279
""",
)

entry(
    index = 300,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(382.985,'m^3/(mol*s)'), n=1.41908, w0=(598500,'J/mol'), E0=(59850,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4209805867496146, var=1.043249572366644, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 3.105368344405712"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 3.105368344405712""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 3.105368344405712
""",
)

entry(
    index = 301,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N",
    kinetics = ArrheniusBM(A=(178.214,'m^3/(mol*s)'), n=1.42089, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570074, var=0.9609060278364029, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N
    Total Standard Deviation in ln(k): 3.469757305105129"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N
Total Standard Deviation in ln(k): 3.469757305105129""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N
Total Standard Deviation in ln(k): 3.469757305105129
""",
)

entry(
    index = 302,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N",
    kinetics = ArrheniusBM(A=(252.033,'m^3/(mol*s)'), n=1.42089, w0=(601500,'J/mol'), E0=(52123.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570073, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N
    Total Standard Deviation in ln(k): 1.5045994199924806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N
Total Standard Deviation in ln(k): 1.5045994199924806""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N
Total Standard Deviation in ln(k): 1.5045994199924806
""",
)

entry(
    index = 303,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(558500,'J/mol'), E0=(55850,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 304,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 305,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_2NO->O",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(625500,'J/mol'), E0=(51297.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 306,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_N-2NO->O",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_N-2NO->O
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
    kinetics = ArrheniusBM(A=(1.7641e+06,'m^3/(mol*s)'), n=-0.0462318, w0=(561500,'J/mol'), E0=(18649.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16712083957064092, var=1.3564218651914435, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C
    Total Standard Deviation in ln(k): 2.7547268516181598"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C
Total Standard Deviation in ln(k): 2.7547268516181598""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C
Total Standard Deviation in ln(k): 2.7547268516181598
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
    kinetics = ArrheniusBM(A=(7.76827e+08,'m^3/(mol*s)'), n=-0.9, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0763652085225523e-17, var=0.04891149884417046, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R
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
    kinetics = ArrheniusBM(A=(2.95928e+07,'m^3/(mol*s)'), n=-0.381632, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.032709232769080235, var=0.0016076635746038646, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C
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
    kinetics = ArrheniusBM(A=(644,'m^3/(mol*s)'), n=1.19, w0=(513500,'J/mol'), E0=(42507.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_N-1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_N-1CNS->C
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
    kinetics = ArrheniusBM(A=(176.541,'m^3/(mol*s)'), n=1.45995, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13833949944090015, var=1.1555579666323413e-33, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 0.347586682012312"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 0.347586682012312""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 0.347586682012312
""",
)

entry(
    index = 321,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(249.667,'m^3/(mol*s)'), n=1.45995, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.5096568970344717, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-2R!H-R
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
    kinetics = ArrheniusBM(A=(305.778,'m^3/(mol*s)'), n=1.45995, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.5096568970344721, var=2.413897921625164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F_Ext-2R!H-R
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
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=-4.1835e-08, w0=(551500,'J/mol'), E0=(55150,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R
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
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_2R!H->C",
    kinetics = ArrheniusBM(A=(0.268845,'m^3/(mol*s)'), n=2.32619, w0=(551500,'J/mol'), E0=(55150,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.4053866559415926, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_2R!H->C
    Total Standard Deviation in ln(k): 8.008842950292529"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_2R!H->C
Total Standard Deviation in ln(k): 8.008842950292529""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_2R!H->C
Total Standard Deviation in ln(k): 8.008842950292529
""",
)

entry(
    index = 325,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_N-2R!H->C",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 326,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(3.716e+06,'m^3/(mol*s)'), n=0.200126, w0=(538000,'J/mol'), E0=(76600,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00914657571632494, var=0.13660130397161369, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R
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
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_2R!H->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(538000,'J/mol'), E0=(53800,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 328,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_N-2R!H->C",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(557500,'J/mol'), E0=(45883,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 329,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C",
    kinetics = ArrheniusBM(A=(1.70765e+07,'m^3/(mol*s)'), n=7.53848e-07, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9494596051172368, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C
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
    kinetics = ArrheniusBM(A=(363.634,'m^3/(mol*s)'), n=1.45995, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1383394886283895, var=0.14441168010692462, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C
    Total Standard Deviation in ln(k): 1.1094167935267798"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C
Total Standard Deviation in ln(k): 1.1094167935267798""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C
Total Standard Deviation in ln(k): 1.1094167935267798
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
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(3.61e+06,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 333,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(23588.5,'m^3/(mol*s)'), n=1.06552, w0=(609250,'J/mol'), E0=(60925,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6761713695632989, var=0.41113237262952895, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 2.984351249045606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.984351249045606""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.984351249045606
""",
)

entry(
    index = 334,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(400,'m^3/(mol*s)'), n=1.5, w0=(564000,'J/mol'), E0=(56400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 335,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(32.8605,'m^3/(mol*s)'), n=1.78781, w0=(573250,'J/mol'), E0=(49857.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1392954809911636, var=0.23695775095232388, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 1.3258597282725029"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 1.3258597282725029""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 1.3258597282725029
""",
)

entry(
    index = 336,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C_4BrO->O",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C_4BrO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C_4BrO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C_4BrO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C_4BrO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 337,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C_N-4BrO->O",
    kinetics = ArrheniusBM(A=(2.37e+06,'m^3/(mol*s)'), n=0, w0=(514500,'J/mol'), E0=(51450,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C_N-4BrO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C_N-4BrO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C_N-4BrO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C_N-4BrO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 338,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C_2NO->O",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(607000,'J/mol'), E0=(60700,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 339,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C_N-2NO->O",
    kinetics = ArrheniusBM(A=(3.6,'m^3/(mol*s)'), n=2, w0=(590000,'J/mol'), E0=(59000,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 340,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N_2N-u1",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 341,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N_N-2N-u1",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 342,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N_2CO->C",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(577500,'J/mol'), E0=(57750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N_2CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N_2CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 343,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N_N-2CO->C",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(625500,'J/mol'), E0=(55145.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N_N-2CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N_N-2CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N_N-2CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N_N-2CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 344,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C_Ext-7R!H-R_Ext-5CF-R",
    kinetics = ArrheniusBM(A=(1.94e+06,'m^3/(mol*s)'), n=0, w0=(561500,'J/mol'), E0=(38508.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C_Ext-7R!H-R_Ext-5CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C_Ext-7R!H-R_Ext-5CF-R
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
    kinetics = ArrheniusBM(A=(353.082,'m^3/(mol*s)'), n=1.45995, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.509656897034472, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C_Ext-1CN-R
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
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C_2NO->O",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(642000,'J/mol'), E0=(64200,'J/mol'), Tmin=(300,'K'), Tmax=(1000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 355,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C_N-2NO->O",
    kinetics = ArrheniusBM(A=(720,'m^3/(mol*s)'), n=1.5, w0=(576500,'J/mol'), E0=(57650,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 356,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C_2NO->O",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(612000,'J/mol'), E0=(62760.6,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 357,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C_N-2NO->O",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

