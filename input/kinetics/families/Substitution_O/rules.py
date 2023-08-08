#!/usr/bin/env python
# encoding: utf-8

name = "Substitution_O/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(6.55119e+27,'m^3/(mol*s)'), n=-6.11682, w0=(358180,'J/mol'), E0=(207844,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5463359680076466, var=20.1987031246014, Tref=1000.0, N=256, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 256 training reactions at node Root
    Total Standard Deviation in ln(k): 10.382577746145477"""),
    rank = 11,
    shortDesc = """BM rule fitted to 256 training reactions at node Root
Total Standard Deviation in ln(k): 10.382577746145477""",
    longDesc = 
"""
BM rule fitted to 256 training reactions at node Root
Total Standard Deviation in ln(k): 10.382577746145477
""",
)

entry(
    index = 2,
    label = "Root_4CHNOS->H",
    kinetics = ArrheniusBM(A=(9.8037e+19,'m^3/(mol*s)'), n=-3.65027, w0=(383384,'J/mol'), E0=(180499,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.37579408313068696, var=8.886853840220207, Tref=1000.0, N=86, data_mean=0.0, correlation='Root_4CHNOS->H',), comment="""BM rule fitted to 86 training reactions at node Root_4CHNOS->H
    Total Standard Deviation in ln(k): 6.920487220999841"""),
    rank = 11,
    shortDesc = """BM rule fitted to 86 training reactions at node Root_4CHNOS->H
Total Standard Deviation in ln(k): 6.920487220999841""",
    longDesc = 
"""
BM rule fitted to 86 training reactions at node Root_4CHNOS->H
Total Standard Deviation in ln(k): 6.920487220999841
""",
)

entry(
    index = 3,
    label = "Root_N-4CHNOS->H",
    kinetics = ArrheniusBM(A=(1.53497e+29,'m^3/(mol*s)'), n=-6.59831, w0=(345429,'J/mol'), E0=(215995,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5885890386701873, var=22.325821675822468, Tref=1000.0, N=170, data_mean=0.0, correlation='Root_N-4CHNOS->H',), comment="""BM rule fitted to 170 training reactions at node Root_N-4CHNOS->H
    Total Standard Deviation in ln(k): 10.95128189498786"""),
    rank = 11,
    shortDesc = """BM rule fitted to 170 training reactions at node Root_N-4CHNOS->H
Total Standard Deviation in ln(k): 10.95128189498786""",
    longDesc = 
"""
BM rule fitted to 170 training reactions at node Root_N-4CHNOS->H
Total Standard Deviation in ln(k): 10.95128189498786
""",
)

entry(
    index = 4,
    label = "Root_4CHNOS->H_2R->C",
    kinetics = ArrheniusBM(A=(1.43426e-09,'m^3/(mol*s)'), n=4.8121, w0=(408500,'J/mol'), E0=(120961,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07400025666129262, var=8.478133467381243, Tref=1000.0, N=66, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C',), comment="""BM rule fitted to 66 training reactions at node Root_4CHNOS->H_2R->C
    Total Standard Deviation in ln(k): 6.0231644352363185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 66 training reactions at node Root_4CHNOS->H_2R->C
Total Standard Deviation in ln(k): 6.0231644352363185""",
    longDesc = 
"""
BM rule fitted to 66 training reactions at node Root_4CHNOS->H_2R->C
Total Standard Deviation in ln(k): 6.0231644352363185
""",
)

entry(
    index = 5,
    label = "Root_4CHNOS->H_N-2R->C",
    kinetics = ArrheniusBM(A=(1.81827e-15,'m^3/(mol*s)'), n=6.88882, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2479913172266217, var=3.244866877676848, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_4CHNOS->H_N-2R->C',), comment="""BM rule fitted to 20 training reactions at node Root_4CHNOS->H_N-2R->C
    Total Standard Deviation in ln(k): 4.234326106509686"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_4CHNOS->H_N-2R->C
Total Standard Deviation in ln(k): 4.234326106509686""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_4CHNOS->H_N-2R->C
Total Standard Deviation in ln(k): 4.234326106509686
""",
)

entry(
    index = 6,
    label = "Root_N-4CHNOS->H_2R->O",
    kinetics = ArrheniusBM(A=(2.00671e-25,'m^3/(mol*s)'), n=9.39607, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.37117423813409506, var=28.94339288358343, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-4CHNOS->H_2R->O',), comment="""BM rule fitted to 20 training reactions at node Root_N-4CHNOS->H_2R->O
    Total Standard Deviation in ln(k): 11.717885663470227"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-4CHNOS->H_2R->O
Total Standard Deviation in ln(k): 11.717885663470227""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-4CHNOS->H_2R->O
Total Standard Deviation in ln(k): 11.717885663470227
""",
)

entry(
    index = 7,
    label = "Root_N-4CHNOS->H_N-2R->O",
    kinetics = ArrheniusBM(A=(1.91396e+28,'m^3/(mol*s)'), n=-6.33851, w0=(358153,'J/mol'), E0=(217607,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.581329753862537, var=19.663821631330414, Tref=1000.0, N=150, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O',), comment="""BM rule fitted to 150 training reactions at node Root_N-4CHNOS->H_N-2R->O
    Total Standard Deviation in ln(k): 10.350406275206042"""),
    rank = 11,
    shortDesc = """BM rule fitted to 150 training reactions at node Root_N-4CHNOS->H_N-2R->O
Total Standard Deviation in ln(k): 10.350406275206042""",
    longDesc = 
"""
BM rule fitted to 150 training reactions at node Root_N-4CHNOS->H_N-2R->O
Total Standard Deviation in ln(k): 10.350406275206042
""",
)

entry(
    index = 8,
    label = "Root_4CHNOS->H_2R->C_3R->C",
    kinetics = ArrheniusBM(A=(1.66581e-07,'m^3/(mol*s)'), n=4.1913, w0=(408500,'J/mol'), E0=(127136,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.028423931102659013, var=6.705510770974052, Tref=1000.0, N=42, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C',), comment="""BM rule fitted to 42 training reactions at node Root_4CHNOS->H_2R->C_3R->C
    Total Standard Deviation in ln(k): 5.262678596893785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 42 training reactions at node Root_4CHNOS->H_2R->C_3R->C
Total Standard Deviation in ln(k): 5.262678596893785""",
    longDesc = 
"""
BM rule fitted to 42 training reactions at node Root_4CHNOS->H_2R->C_3R->C
Total Standard Deviation in ln(k): 5.262678596893785
""",
)

entry(
    index = 9,
    label = "Root_4CHNOS->H_2R->C_N-3R->C",
    kinetics = ArrheniusBM(A=(1.51363e-24,'m^3/(mol*s)'), n=9.26527, w0=(408500,'J/mol'), E0=(84208.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24765017039072237, var=13.09244115504936, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_N-3R->C',), comment="""BM rule fitted to 24 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C
    Total Standard Deviation in ln(k): 7.8760654637619405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C
Total Standard Deviation in ln(k): 7.8760654637619405""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C
Total Standard Deviation in ln(k): 7.8760654637619405
""",
)

entry(
    index = 10,
    label = "Root_4CHNOS->H_N-2R->C_3R->H",
    kinetics = ArrheniusBM(A=(1.59989e-08,'m^3/(mol*s)'), n=4.77812, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15507623209804272, var=0.8276858626111769, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_4CHNOS->H_N-2R->C_3R->H',), comment="""BM rule fitted to 6 training reactions at node Root_4CHNOS->H_N-2R->C_3R->H
    Total Standard Deviation in ln(k): 2.2134914640072205"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_4CHNOS->H_N-2R->C_3R->H
Total Standard Deviation in ln(k): 2.2134914640072205""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_4CHNOS->H_N-2R->C_3R->H
Total Standard Deviation in ln(k): 2.2134914640072205
""",
)

entry(
    index = 11,
    label = "Root_4CHNOS->H_N-2R->C_N-3R->H",
    kinetics = ArrheniusBM(A=(1.92076e-18,'m^3/(mol*s)'), n=7.7934, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.28781206895182193, var=3.3701678133535276, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_4CHNOS->H_N-2R->C_N-3R->H',), comment="""BM rule fitted to 14 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H
    Total Standard Deviation in ln(k): 4.403441927688372"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H
Total Standard Deviation in ln(k): 4.403441927688372""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H
Total Standard Deviation in ln(k): 4.403441927688372
""",
)

entry(
    index = 12,
    label = "Root_N-4CHNOS->H_2R->O_Ext-3R-R",
    kinetics = ArrheniusBM(A=(3.53443e-16,'m^3/(mol*s)'), n=6.84248, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.20691103823411686, var=215.39322411628353, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_2R->O_Ext-3R-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_2R->O_Ext-3R-R
    Total Standard Deviation in ln(k): 29.941932315440123"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_2R->O_Ext-3R-R
Total Standard Deviation in ln(k): 29.941932315440123""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_2R->O_Ext-3R-R
Total Standard Deviation in ln(k): 29.941932315440123
""",
)

entry(
    index = 13,
    label = "Root_N-4CHNOS->H_2R->O_3R->H",
    kinetics = ArrheniusBM(A=(3.68038e-22,'m^3/(mol*s)'), n=8.49155, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.317243774255274, var=0.9436959691563134, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4CHNOS->H_2R->O_3R->H',), comment="""BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_2R->O_3R->H
    Total Standard Deviation in ln(k): 2.7445750587387443"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_2R->O_3R->H
Total Standard Deviation in ln(k): 2.7445750587387443""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_2R->O_3R->H
Total Standard Deviation in ln(k): 2.7445750587387443
""",
)

entry(
    index = 14,
    label = "Root_N-4CHNOS->H_2R->O_N-3R->H",
    kinetics = ArrheniusBM(A=(4.42698e-31,'m^3/(mol*s)'), n=10.9602, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.46923780439320084, var=4.697483834121373, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4CHNOS->H_2R->O_N-3R->H',), comment="""BM rule fitted to 10 training reactions at node Root_N-4CHNOS->H_2R->O_N-3R->H
    Total Standard Deviation in ln(k): 5.523988014847429"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4CHNOS->H_2R->O_N-3R->H
Total Standard Deviation in ln(k): 5.523988014847429""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4CHNOS->H_2R->O_N-3R->H
Total Standard Deviation in ln(k): 5.523988014847429
""",
)

entry(
    index = 15,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C",
    kinetics = ArrheniusBM(A=(7.44809,'m^3/(mol*s)'), n=1.67624, w0=(388300,'J/mol'), E0=(166999,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.15869581339153738, var=13.392109916361292, Tref=1000.0, N=110, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C',), comment="""BM rule fitted to 110 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C
    Total Standard Deviation in ln(k): 7.735107688082778"""),
    rank = 11,
    shortDesc = """BM rule fitted to 110 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C
Total Standard Deviation in ln(k): 7.735107688082778""",
    longDesc = 
"""
BM rule fitted to 110 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C
Total Standard Deviation in ln(k): 7.735107688082778
""",
)

entry(
    index = 16,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C",
    kinetics = ArrheniusBM(A=(1.0248e-23,'m^3/(mol*s)'), n=9.09284, w0=(275250,'J/mol'), E0=(27525,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.33125683819068164, var=15.849770220832504, Tref=1000.0, N=40, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C',), comment="""BM rule fitted to 40 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C
    Total Standard Deviation in ln(k): 8.813508773484925"""),
    rank = 11,
    shortDesc = """BM rule fitted to 40 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C
Total Standard Deviation in ln(k): 8.813508773484925""",
    longDesc = 
"""
BM rule fitted to 40 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C
Total Standard Deviation in ln(k): 8.813508773484925
""",
)

entry(
    index = 17,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000109096,'m^3/(mol*s)'), n=3.4686, w0=(408500,'J/mol'), E0=(139964,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.030993107187788565, var=5.270933651777116, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R',), comment="""BM rule fitted to 18 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R
    Total Standard Deviation in ln(k): 4.68044596306779"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R
Total Standard Deviation in ln(k): 4.68044596306779""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R
Total Standard Deviation in ln(k): 4.68044596306779
""",
)

entry(
    index = 18,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(5.15724e-09,'m^3/(mol*s)'), n=4.50472, w0=(408500,'J/mol'), E0=(118113,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06270356334068002, var=7.861754078202395, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R',), comment="""BM rule fitted to 22 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 5.778587171294428"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R
Total Standard Deviation in ln(k): 5.778587171294428""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R
Total Standard Deviation in ln(k): 5.778587171294428
""",
)

entry(
    index = 19,
    label = "Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.04093e-18,'m^3/(mol*s)'), n=7.45988, w0=(408500,'J/mol'), E0=(97539.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21645050376620725, var=10.172020076543076, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R',), comment="""BM rule fitted to 22 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 6.937668254324242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R
Total Standard Deviation in ln(k): 6.937668254324242""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R
Total Standard Deviation in ln(k): 6.937668254324242
""",
)

entry(
    index = 20,
    label = "Root_4CHNOS->H_N-2R->C_3R->H_Ext-2HO-R",
    kinetics = ArrheniusBM(A=(1.27509e-08,'m^3/(mol*s)'), n=4.77359, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15123725181098066, var=0.8032817741836769, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4CHNOS->H_N-2R->C_3R->H_Ext-2HO-R',), comment="""BM rule fitted to 4 training reactions at node Root_4CHNOS->H_N-2R->C_3R->H_Ext-2HO-R
    Total Standard Deviation in ln(k): 2.1767567167851953"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4CHNOS->H_N-2R->C_3R->H_Ext-2HO-R
Total Standard Deviation in ln(k): 2.1767567167851953""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4CHNOS->H_N-2R->C_3R->H_Ext-2HO-R
Total Standard Deviation in ln(k): 2.1767567167851953
""",
)

entry(
    index = 21,
    label = "Root_4CHNOS->H_N-2R->C_N-3R->H_Ext-3CO-R",
    kinetics = ArrheniusBM(A=(3.86638e-22,'m^3/(mol*s)'), n=9.25894, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3325210079357712, var=1.6319949296771972, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4CHNOS->H_N-2R->C_N-3R->H_Ext-3CO-R',), comment="""BM rule fitted to 4 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_Ext-3CO-R
    Total Standard Deviation in ln(k): 3.396520098503286"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_Ext-3CO-R
Total Standard Deviation in ln(k): 3.396520098503286""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_Ext-3CO-R
Total Standard Deviation in ln(k): 3.396520098503286
""",
)

entry(
    index = 22,
    label = "Root_4CHNOS->H_N-2R->C_N-3R->H_3CO->C",
    kinetics = ArrheniusBM(A=(7.57501e-14,'m^3/(mol*s)'), n=6.23413, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.23886407240749444, var=4.70560310000867, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_4CHNOS->H_N-2R->C_N-3R->H_3CO->C',), comment="""BM rule fitted to 6 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_3CO->C
    Total Standard Deviation in ln(k): 4.948912931463684"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_3CO->C
Total Standard Deviation in ln(k): 4.948912931463684""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_3CO->C
Total Standard Deviation in ln(k): 4.948912931463684
""",
)

entry(
    index = 23,
    label = "Root_4CHNOS->H_N-2R->C_N-3R->H_N-3CO->C",
    kinetics = ArrheniusBM(A=(1.21837e-21,'m^3/(mol*s)'), n=8.66677, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.31652512583426634, var=0.3478872262322527, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4CHNOS->H_N-2R->C_N-3R->H_N-3CO->C',), comment="""BM rule fitted to 4 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_N-3CO->C
    Total Standard Deviation in ln(k): 1.9777214139781636"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_N-3CO->C
Total Standard Deviation in ln(k): 1.9777214139781636""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_N-3CO->C
Total Standard Deviation in ln(k): 1.9777214139781636
""",
)

entry(
    index = 24,
    label = "Root_N-4CHNOS->H_2R->O_Ext-3R-R_Ext-2O-R",
    kinetics = ArrheniusBM(A=(644.03,'m^3/(mol*s)'), n=1.82837, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.6559119116384915, var=138.25538294607418, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_2R->O_Ext-3R-R_Ext-2O-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_2R->O_Ext-3R-R_Ext-2O-R
    Total Standard Deviation in ln(k): 27.73266854332841"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_2R->O_Ext-3R-R_Ext-2O-R
Total Standard Deviation in ln(k): 27.73266854332841""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_2R->O_Ext-3R-R_Ext-2O-R
Total Standard Deviation in ln(k): 27.73266854332841
""",
)

entry(
    index = 25,
    label = "Root_N-4CHNOS->H_2R->O_3R->H_Ext-2O-R",
    kinetics = ArrheniusBM(A=(2.66018e-22,'m^3/(mol*s)'), n=8.49511, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3111673622210768, var=1.053290953833996, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_2R->O_3R->H_Ext-2O-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_2R->O_3R->H_Ext-2O-R
    Total Standard Deviation in ln(k): 2.8392864341992854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_2R->O_3R->H_Ext-2O-R
Total Standard Deviation in ln(k): 2.8392864341992854""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_2R->O_3R->H_Ext-2O-R
Total Standard Deviation in ln(k): 2.8392864341992854
""",
)

entry(
    index = 26,
    label = "Root_N-4CHNOS->H_2R->O_N-3R->H_3CO->C",
    kinetics = ArrheniusBM(A=(6.64007e-29,'m^3/(mol*s)'), n=10.1402, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.45257963307010973, var=6.934123102279733, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4CHNOS->H_2R->O_N-3R->H_3CO->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_2R->O_N-3R->H_3CO->C
    Total Standard Deviation in ln(k): 6.41614814126729"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_2R->O_N-3R->H_3CO->C
Total Standard Deviation in ln(k): 6.41614814126729""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_2R->O_N-3R->H_3CO->C
Total Standard Deviation in ln(k): 6.41614814126729
""",
)

entry(
    index = 27,
    label = "Root_N-4CHNOS->H_2R->O_N-3R->H_N-3CO->C",
    kinetics = ArrheniusBM(A=(2.40995e-34,'m^3/(mol*s)'), n=12.1902, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4942250642563781, var=2.037070050847072, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_2R->O_N-3R->H_N-3CO->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_2R->O_N-3R->H_N-3CO->C
    Total Standard Deviation in ln(k): 4.103048962633876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_2R->O_N-3R->H_N-3CO->C
Total Standard Deviation in ln(k): 4.103048962633876""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_2R->O_N-3R->H_N-3CO->C
Total Standard Deviation in ln(k): 4.103048962633876
""",
)

entry(
    index = 28,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C",
    kinetics = ArrheniusBM(A=(2.78533e-09,'m^3/(mol*s)'), n=4.5039, w0=(358000,'J/mol'), E0=(162270,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02755460769460829, var=18.053023900900865, Tref=1000.0, N=44, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C',), comment="""BM rule fitted to 44 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C
    Total Standard Deviation in ln(k): 8.587121519161343"""),
    rank = 11,
    shortDesc = """BM rule fitted to 44 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C
Total Standard Deviation in ln(k): 8.587121519161343""",
    longDesc = 
"""
BM rule fitted to 44 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C
Total Standard Deviation in ln(k): 8.587121519161343
""",
)

entry(
    index = 29,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C",
    kinetics = ArrheniusBM(A=(8.8647e-06,'m^3/(mol*s)'), n=3.40187, w0=(408500,'J/mol'), E0=(144446,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08335661501158179, var=8.704601758202381, Tref=1000.0, N=66, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C',), comment="""BM rule fitted to 66 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C
    Total Standard Deviation in ln(k): 6.124121313569174"""),
    rank = 11,
    shortDesc = """BM rule fitted to 66 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C
Total Standard Deviation in ln(k): 6.124121313569174""",
    longDesc = 
"""
BM rule fitted to 66 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C
Total Standard Deviation in ln(k): 6.124121313569174
""",
)

entry(
    index = 30,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C",
    kinetics = ArrheniusBM(A=(4.80906e-26,'m^3/(mol*s)'), n=9.76377, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.40150221246574647, var=28.04918217145505, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C',), comment="""BM rule fitted to 20 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C
    Total Standard Deviation in ln(k): 11.626172921933922"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C
Total Standard Deviation in ln(k): 11.626172921933922""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C
Total Standard Deviation in ln(k): 11.626172921933922
""",
)

entry(
    index = 31,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C",
    kinetics = ArrheniusBM(A=(2.18382e-21,'m^3/(mol*s)'), n=8.42191, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.261011424131942, var=5.279338912795264, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C',), comment="""BM rule fitted to 20 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C
    Total Standard Deviation in ln(k): 5.262049703593883"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C
Total Standard Deviation in ln(k): 5.262049703593883""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C
Total Standard Deviation in ln(k): 5.262049703593883
""",
)

entry(
    index = 32,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_Sp-5R!H=3C",
    kinetics = ArrheniusBM(A=(2.42997e-06,'m^3/(mol*s)'), n=3.85727, w0=(408500,'J/mol'), E0=(143980,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0115720877268912, var=7.319284323070408, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_Sp-5R!H=3C',), comment="""BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_Sp-5R!H=3C
    Total Standard Deviation in ln(k): 5.452721134081123"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_Sp-5R!H=3C
Total Standard Deviation in ln(k): 5.452721134081123""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_Sp-5R!H=3C
Total Standard Deviation in ln(k): 5.452721134081123
""",
)

entry(
    index = 33,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C",
    kinetics = ArrheniusBM(A=(2.40576e-07,'m^3/(mol*s)'), n=4.28286, w0=(408500,'J/mol'), E0=(132201,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.014899433877812647, var=4.8802979342213915, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C',), comment="""BM rule fitted to 14 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C
    Total Standard Deviation in ln(k): 4.466175483967575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C
Total Standard Deviation in ln(k): 4.466175483967575""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C
Total Standard Deviation in ln(k): 4.466175483967575
""",
)

entry(
    index = 34,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_Sp-5R!H=2C",
    kinetics = ArrheniusBM(A=(166.128,'m^3/(mol*s)'), n=1.19792, w0=(408500,'J/mol'), E0=(131392,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01689152605436392, var=5.14079037722758, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_Sp-5R!H=2C',), comment="""BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_Sp-5R!H=2C
    Total Standard Deviation in ln(k): 4.587839235087786"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_Sp-5R!H=2C
Total Standard Deviation in ln(k): 4.587839235087786""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_Sp-5R!H=2C
Total Standard Deviation in ln(k): 4.587839235087786
""",
)

entry(
    index = 35,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C",
    kinetics = ArrheniusBM(A=(4.2766e-14,'m^3/(mol*s)'), n=6.05411, w0=(408500,'J/mol'), E0=(108956,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1330092063348389, var=9.23537129480433, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C',), comment="""BM rule fitted to 18 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C
    Total Standard Deviation in ln(k): 6.42653450780394"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C
Total Standard Deviation in ln(k): 6.42653450780394""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C
Total Standard Deviation in ln(k): 6.42653450780394
""",
)

entry(
    index = 36,
    label = "Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_Sp-5R!H=2C",
    kinetics = ArrheniusBM(A=(0.784015,'m^3/(mol*s)'), n=2.13369, w0=(408500,'J/mol'), E0=(135859,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008094064209885355, var=5.199065064237215, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_Sp-5R!H=2C',), comment="""BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_Sp-5R!H=2C
    Total Standard Deviation in ln(k): 4.591425197295706"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_Sp-5R!H=2C
Total Standard Deviation in ln(k): 4.591425197295706""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_Sp-5R!H=2C
Total Standard Deviation in ln(k): 4.591425197295706
""",
)

entry(
    index = 37,
    label = "Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C",
    kinetics = ArrheniusBM(A=(3.11398e-41,'m^3/(mol*s)'), n=14.1913, w0=(408500,'J/mol'), E0=(19856.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6256950352328052, var=9.173846404170822, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C',), comment="""BM rule fitted to 18 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C
    Total Standard Deviation in ln(k): 7.644111483763453"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C
Total Standard Deviation in ln(k): 7.644111483763453""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C
Total Standard Deviation in ln(k): 7.644111483763453
""",
)

entry(
    index = 38,
    label = "Root_4CHNOS->H_N-2R->C_3R->H_Ext-2HO-R_5R!H->C",
    kinetics = ArrheniusBM(A=(7.41884e-08,'m^3/(mol*s)'), n=4.54057, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.1075472886258257, var=2.516027630880507, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_N-2R->C_3R->H_Ext-2HO-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_N-2R->C_3R->H_Ext-2HO-R_5R!H->C
    Total Standard Deviation in ln(k): 8.475253950890938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_N-2R->C_3R->H_Ext-2HO-R_5R!H->C
Total Standard Deviation in ln(k): 8.475253950890938""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_N-2R->C_3R->H_Ext-2HO-R_5R!H->C
Total Standard Deviation in ln(k): 8.475253950890938
""",
)

entry(
    index = 39,
    label = "Root_4CHNOS->H_N-2R->C_3R->H_Ext-2HO-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2.19153e-09,'m^3/(mol*s)'), n=5.0066, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.4427810069120968, var=2.8184455791669754, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_N-2R->C_3R->H_Ext-2HO-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_N-2R->C_3R->H_Ext-2HO-R_N-5R!H->C
    Total Standard Deviation in ln(k): 9.503235429210624"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_N-2R->C_3R->H_Ext-2HO-R_N-5R!H->C
Total Standard Deviation in ln(k): 9.503235429210624""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_N-2R->C_3R->H_Ext-2HO-R_N-5R!H->C
Total Standard Deviation in ln(k): 9.503235429210624
""",
)

entry(
    index = 40,
    label = "Root_4CHNOS->H_N-2R->C_N-3R->H_Ext-3CO-R_Ext-2HO-R",
    kinetics = ArrheniusBM(A=(6.38428e-23,'m^3/(mol*s)'), n=9.62765, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.164860898201447, var=0.29032588654061886, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_N-2R->C_N-3R->H_Ext-3CO-R_Ext-2HO-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_Ext-3CO-R_Ext-2HO-R
    Total Standard Deviation in ln(k): 14.057226729834872"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_Ext-3CO-R_Ext-2HO-R
Total Standard Deviation in ln(k): 14.057226729834872""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_Ext-3CO-R_Ext-2HO-R
Total Standard Deviation in ln(k): 14.057226729834872
""",
)

entry(
    index = 41,
    label = "Root_4CHNOS->H_N-2R->C_N-3R->H_3CO->C_Ext-2HO-R",
    kinetics = ArrheniusBM(A=(3.51118e-14,'m^3/(mol*s)'), n=6.37831, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24947683639480853, var=9.201735362749968, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4CHNOS->H_N-2R->C_N-3R->H_3CO->C_Ext-2HO-R',), comment="""BM rule fitted to 4 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_3CO->C_Ext-2HO-R
    Total Standard Deviation in ln(k): 6.708062237837496"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_3CO->C_Ext-2HO-R
Total Standard Deviation in ln(k): 6.708062237837496""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_3CO->C_Ext-2HO-R
Total Standard Deviation in ln(k): 6.708062237837496
""",
)

entry(
    index = 42,
    label = "Root_4CHNOS->H_N-2R->C_N-3R->H_N-3CO->C_Ext-2HO-R",
    kinetics = ArrheniusBM(A=(2.37554e-22,'m^3/(mol*s)'), n=8.88894, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.836744037853101, var=0.05265130258582928, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_N-2R->C_N-3R->H_N-3CO->C_Ext-2HO-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_N-3CO->C_Ext-2HO-R
    Total Standard Deviation in ln(k): 12.612627148502522"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_N-3CO->C_Ext-2HO-R
Total Standard Deviation in ln(k): 12.612627148502522""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_N-3CO->C_Ext-2HO-R
Total Standard Deviation in ln(k): 12.612627148502522
""",
)

entry(
    index = 43,
    label = "Root_N-4CHNOS->H_2R->O_3R->H_Ext-2O-R_5R!H->C",
    kinetics = ArrheniusBM(A=(4.03411e-22,'m^3/(mol*s)'), n=8.34754, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.804840468385934, var=0.8152680348924375, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_2R->O_3R->H_Ext-2O-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_2R->O_3R->H_Ext-2O-R_5R!H->C
    Total Standard Deviation in ln(k): 13.882582779400911"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_2R->O_3R->H_Ext-2O-R_5R!H->C
Total Standard Deviation in ln(k): 13.882582779400911""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_2R->O_3R->H_Ext-2O-R_5R!H->C
Total Standard Deviation in ln(k): 13.882582779400911
""",
)

entry(
    index = 44,
    label = "Root_N-4CHNOS->H_2R->O_3R->H_Ext-2O-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.75418e-22,'m^3/(mol*s)'), n=8.64268, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.5573612976276685, var=0.9913363035130653, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_2R->O_3R->H_Ext-2O-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_2R->O_3R->H_Ext-2O-R_N-5R!H->C
    Total Standard Deviation in ln(k): 13.446688504714261"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_2R->O_3R->H_Ext-2O-R_N-5R!H->C
Total Standard Deviation in ln(k): 13.446688504714261""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_2R->O_3R->H_Ext-2O-R_N-5R!H->C
Total Standard Deviation in ln(k): 13.446688504714261
""",
)

entry(
    index = 45,
    label = "Root_N-4CHNOS->H_2R->O_N-3R->H_3CO->C_Ext-2O-R",
    kinetics = ArrheniusBM(A=(3.64965e-29,'m^3/(mol*s)'), n=10.2631, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4576147084823968, var=11.954857775403, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_2R->O_N-3R->H_3CO->C_Ext-2O-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_2R->O_N-3R->H_3CO->C_Ext-2O-R
    Total Standard Deviation in ln(k): 8.081317121272537"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_2R->O_N-3R->H_3CO->C_Ext-2O-R
Total Standard Deviation in ln(k): 8.081317121272537""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_2R->O_N-3R->H_3CO->C_Ext-2O-R
Total Standard Deviation in ln(k): 8.081317121272537
""",
)

entry(
    index = 46,
    label = "Root_N-4CHNOS->H_2R->O_N-3R->H_N-3CO->C_Ext-2O-R",
    kinetics = ArrheniusBM(A=(7.0316e-34,'m^3/(mol*s)'), n=11.9215, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=7.542330420409649, var=0.9027213886151817, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_2R->O_N-3R->H_N-3CO->C_Ext-2O-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_2R->O_N-3R->H_N-3CO->C_Ext-2O-R
    Total Standard Deviation in ln(k): 20.855310847333982"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_2R->O_N-3R->H_N-3CO->C_Ext-2O-R
Total Standard Deviation in ln(k): 20.855310847333982""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_2R->O_N-3R->H_N-3CO->C_Ext-2O-R
Total Standard Deviation in ln(k): 20.855310847333982
""",
)

entry(
    index = 47,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.97825e-10,'m^3/(mol*s)'), n=4.75822, w0=(358000,'J/mol'), E0=(157165,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0357508964029921, var=22.27032747558651, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R',), comment="""BM rule fitted to 22 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R
    Total Standard Deviation in ln(k): 9.550461453096625"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R
Total Standard Deviation in ln(k): 9.550461453096625""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R
Total Standard Deviation in ln(k): 9.550461453096625
""",
)

entry(
    index = 48,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(4.44718e-09,'m^3/(mol*s)'), n=4.40385, w0=(358000,'J/mol'), E0=(169636,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.009771559898976647, var=19.546912845822714, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 8.88786448250495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 8.88786448250495""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 8.88786448250495
""",
)

entry(
    index = 49,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(3.649e-08,'m^3/(mol*s)'), n=4.11279, w0=(358000,'J/mol'), E0=(159649,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05408146823870986, var=7.328407810176719, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 5.562907856862024"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 5.562907856862024""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 5.562907856862024
""",
)

entry(
    index = 50,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Sp-5R!H-4C",
    kinetics = ArrheniusBM(A=(3.41333e-05,'m^3/(mol*s)'), n=3.98861, w0=(358000,'J/mol'), E0=(169003,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.4443686672721673e-15, var=20.683932768451992, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Sp-5R!H-4C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Sp-5R!H-4C
    Total Standard Deviation in ln(k): 9.117453313140095"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Sp-5R!H-4C
Total Standard Deviation in ln(k): 9.117453313140095""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Sp-5R!H-4C
Total Standard Deviation in ln(k): 9.117453313140095
""",
)

entry(
    index = 51,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_N-Sp-5R!H-4C",
    kinetics = ArrheniusBM(A=(2.7086e-06,'m^3/(mol*s)'), n=4.28663, w0=(358000,'J/mol'), E0=(173337,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.272150233908559e-15, var=15.487830282103237, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_N-Sp-5R!H-4C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_N-Sp-5R!H-4C
    Total Standard Deviation in ln(k): 7.889550854175168"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_N-Sp-5R!H-4C
Total Standard Deviation in ln(k): 7.889550854175168""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_N-Sp-5R!H-4C
Total Standard Deviation in ln(k): 7.889550854175168
""",
)

entry(
    index = 52,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R",
    kinetics = ArrheniusBM(A=(7.07951e-11,'m^3/(mol*s)'), n=4.83419, w0=(408500,'J/mol'), E0=(140156,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04383030783566628, var=7.599589921619549, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R',), comment="""BM rule fitted to 18 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R
    Total Standard Deviation in ln(k): 5.636650504714254"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R
Total Standard Deviation in ln(k): 5.636650504714254""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R
Total Standard Deviation in ln(k): 5.636650504714254
""",
)

entry(
    index = 53,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.14874e-05,'m^3/(mol*s)'), n=3.34839, w0=(408500,'J/mol'), E0=(142511,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06831758408846694, var=6.990659188932617, Tref=1000.0, N=44, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R',), comment="""BM rule fitted to 44 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R
    Total Standard Deviation in ln(k): 5.472142646013853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 44 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R
Total Standard Deviation in ln(k): 5.472142646013853""",
    longDesc = 
"""
BM rule fitted to 44 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R
Total Standard Deviation in ln(k): 5.472142646013853
""",
)

entry(
    index = 54,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_3R->C",
    kinetics = ArrheniusBM(A=(4.86838e-11,'m^3/(mol*s)'), n=5.23405, w0=(408500,'J/mol'), E0=(133119,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.788805533999384e-15, var=34.85644552711061, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_3R->C
    Total Standard Deviation in ln(k): 11.835825087097328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_3R->C
Total Standard Deviation in ln(k): 11.835825087097328""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_3R->C
Total Standard Deviation in ln(k): 11.835825087097328
""",
)

entry(
    index = 55,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_N-3R->C",
    kinetics = ArrheniusBM(A=(1.62178e-11,'m^3/(mol*s)'), n=5.94511, w0=(408500,'J/mol'), E0=(121705,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.85134815865879e-15, var=0.6013548967573131, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_N-3R->C
    Total Standard Deviation in ln(k): 1.5546134303716974"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_N-3R->C
Total Standard Deviation in ln(k): 1.5546134303716974""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_N-3R->C
Total Standard Deviation in ln(k): 1.5546134303716974
""",
)

entry(
    index = 56,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-3R-R",
    kinetics = ArrheniusBM(A=(1.38953e-16,'m^3/(mol*s)'), n=7.20774, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21676604818864503, var=185.85694608661862, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-3R-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-3R-R
    Total Standard Deviation in ln(k): 27.875063473984042"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-3R-R
Total Standard Deviation in ln(k): 27.875063473984042""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-3R-R
Total Standard Deviation in ln(k): 27.875063473984042
""",
)

entry(
    index = 57,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R",
    kinetics = ArrheniusBM(A=(1.62045e-28,'m^3/(mol*s)'), n=10.3756, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.44918919483996894, var=9.819918060174412, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R
    Total Standard Deviation in ln(k): 7.410803958669211"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R
Total Standard Deviation in ln(k): 7.410803958669211""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R
Total Standard Deviation in ln(k): 7.410803958669211
""",
)

entry(
    index = 58,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_3R->C",
    kinetics = ArrheniusBM(A=(3.24026e-27,'m^3/(mol*s)'), n=9.97561, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=6.442381975556188, var=14.690837822475178, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_3R->C
    Total Standard Deviation in ln(k): 23.87076403919945"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_3R->C
Total Standard Deviation in ln(k): 23.87076403919945""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_3R->C
Total Standard Deviation in ln(k): 23.87076403919945
""",
)

entry(
    index = 59,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_N-3R->C",
    kinetics = ArrheniusBM(A=(9.72857e-29,'m^3/(mol*s)'), n=10.6844, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4342567719304089, var=8.577405365040638, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_N-3R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_N-3R->C
    Total Standard Deviation in ln(k): 6.962406682039154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_N-3R->C
Total Standard Deviation in ln(k): 6.962406682039154""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_N-3R->C
Total Standard Deviation in ln(k): 6.962406682039154
""",
)

entry(
    index = 60,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_3R->O",
    kinetics = ArrheniusBM(A=(3.98232e-28,'m^3/(mol*s)'), n=10.4979, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.32805957772347716, var=2.013382386564213, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_3R->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_3R->O
    Total Standard Deviation in ln(k): 3.6688631970506758"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_3R->O
Total Standard Deviation in ln(k): 3.6688631970506758""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_3R->O
Total Standard Deviation in ln(k): 3.6688631970506758
""",
)

entry(
    index = 61,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O",
    kinetics = ArrheniusBM(A=(6.79107e-17,'m^3/(mol*s)'), n=7.03791, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21631265649873888, var=6.845647659372997, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O',), comment="""BM rule fitted to 12 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O
    Total Standard Deviation in ln(k): 5.788725805950735"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O
Total Standard Deviation in ln(k): 5.788725805950735""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O
Total Standard Deviation in ln(k): 5.788725805950735
""",
)

entry(
    index = 62,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_Sp-5R!H=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.17293e-06,'m^3/(mol*s)'), n=3.88542, w0=(408500,'J/mol'), E0=(145841,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.5304778839539717e-15, var=0.41967860569660015, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_Sp-5R!H=3C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_Sp-5R!H=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 1.2987196291337588"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_Sp-5R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 1.2987196291337588""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_Sp-5R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 1.2987196291337588
""",
)

entry(
    index = 63,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.81042e-07,'m^3/(mol*s)'), n=4.11282, w0=(408500,'J/mol'), E0=(135547,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0034449362319538142, var=3.0977966249169895, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R',), comment="""BM rule fitted to 10 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 3.5371013363110935"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 3.5371013363110935""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 3.5371013363110935
""",
)

entry(
    index = 64,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(0.000751553,'m^3/(mol*s)'), n=3.23604, w0=(408500,'J/mol'), E0=(132150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.6048038046245765e-15, var=0.17180945703678555, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.830960771988795"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.830960771988795""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.830960771988795
""",
)

entry(
    index = 65,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_Sp-5R!H=2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(137.613,'m^3/(mol*s)'), n=1.37801, w0=(408500,'J/mol'), E0=(133410,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.894402766999692e-15, var=13.171442230618501, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_Sp-5R!H=2C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_Sp-5R!H=2C_Ext-2C-R
    Total Standard Deviation in ln(k): 7.275681097481084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_Sp-5R!H=2C_Ext-2C-R
Total Standard Deviation in ln(k): 7.275681097481084""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_Sp-5R!H=2C_Ext-2C-R
Total Standard Deviation in ln(k): 7.275681097481084
""",
)

entry(
    index = 66,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(9.10796e-48,'m^3/(mol*s)'), n=16.0973, w0=(408500,'J/mol'), E0=(25189.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5586031142587401, var=11.607249581144787, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R',), comment="""BM rule fitted to 12 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R
    Total Standard Deviation in ln(k): 8.233540308055263"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R
Total Standard Deviation in ln(k): 8.233540308055263""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R
Total Standard Deviation in ln(k): 8.233540308055263
""",
)

entry(
    index = 67,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.07095e-05,'m^3/(mol*s)'), n=3.76622, w0=(408500,'J/mol'), E0=(128521,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02389804099545244, var=0.39136826726813456, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.314196229171648"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.314196229171648""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.314196229171648
""",
)

entry(
    index = 68,
    label = "Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_Sp-5R!H=2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.764093,'m^3/(mol*s)'), n=2.2555, w0=(408500,'J/mol'), E0=(132994,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=3.8851035172601924, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_Sp-5R!H=2C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_Sp-5R!H=2C_Ext-2C-R
    Total Standard Deviation in ln(k): 3.9514663405041266"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_Sp-5R!H=2C_Ext-2C-R
Total Standard Deviation in ln(k): 3.9514663405041266""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_Sp-5R!H=2C_Ext-2C-R
Total Standard Deviation in ln(k): 3.9514663405041266
""",
)

entry(
    index = 69,
    label = "Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.20178e-41,'m^3/(mol*s)'), n=14.2801, w0=(408500,'J/mol'), E0=(-18578,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8355228933801246, var=14.398198672869608, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R',), comment="""BM rule fitted to 12 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R
    Total Standard Deviation in ln(k): 9.706262661860725"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R
Total Standard Deviation in ln(k): 9.706262661860725""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R
Total Standard Deviation in ln(k): 9.706262661860725
""",
)

entry(
    index = 70,
    label = "Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(7.40828e-08,'m^3/(mol*s)'), n=4.34188, w0=(408500,'J/mol'), E0=(124898,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.012813086005903224, var=2.0939466844861636, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 2.933140715812223"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.933140715812223""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.933140715812223
""",
)

entry(
    index = 71,
    label = "Root_4CHNOS->H_N-2R->C_N-3R->H_3CO->C_Ext-2HO-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.57103e-10,'m^3/(mol*s)'), n=5.03148, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.201380206059647, var=46.179221387725455, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_N-2R->C_N-3R->H_3CO->C_Ext-2HO-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_3CO->C_Ext-2HO-R_5R!H->C
    Total Standard Deviation in ln(k): 21.66690524741116"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_3CO->C_Ext-2HO-R_5R!H->C
Total Standard Deviation in ln(k): 21.66690524741116""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_3CO->C_Ext-2HO-R_5R!H->C
Total Standard Deviation in ln(k): 21.66690524741116
""",
)

entry(
    index = 72,
    label = "Root_4CHNOS->H_N-2R->C_N-3R->H_3CO->C_Ext-2HO-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.84734e-18,'m^3/(mol*s)'), n=7.72513, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.304717019884775, var=0.889909376613053, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_N-2R->C_N-3R->H_3CO->C_Ext-2HO-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_3CO->C_Ext-2HO-R_N-5R!H->C
    Total Standard Deviation in ln(k): 12.707038908272597"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_3CO->C_Ext-2HO-R_N-5R!H->C
Total Standard Deviation in ln(k): 12.707038908272597""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_N-2R->C_N-3R->H_3CO->C_Ext-2HO-R_N-5R!H->C
Total Standard Deviation in ln(k): 12.707038908272597
""",
)

entry(
    index = 73,
    label = "Root_N-4CHNOS->H_2R->O_N-3R->H_3CO->C_Ext-2O-R_5R!H->C",
    kinetics = ArrheniusBM(A=(4.50009e-26,'m^3/(mol*s)'), n=9.01183, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=6.369266989558501, var=4.359521971533268, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_2R->O_N-3R->H_3CO->C_Ext-2O-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_2R->O_N-3R->H_3CO->C_Ext-2O-R_5R!H->C
    Total Standard Deviation in ln(k): 20.18896364386646"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_2R->O_N-3R->H_3CO->C_Ext-2O-R_5R!H->C
Total Standard Deviation in ln(k): 20.18896364386646""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_2R->O_N-3R->H_3CO->C_Ext-2O-R_5R!H->C
Total Standard Deviation in ln(k): 20.18896364386646
""",
)

entry(
    index = 74,
    label = "Root_N-4CHNOS->H_2R->O_N-3R->H_3CO->C_Ext-2O-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2.95992e-32,'m^3/(mol*s)'), n=11.5144, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=7.399147545427611, var=29.483253305695115, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_2R->O_N-3R->H_3CO->C_Ext-2O-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_2R->O_N-3R->H_3CO->C_Ext-2O-R_N-5R!H->C
    Total Standard Deviation in ln(k): 29.476230467870984"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_2R->O_N-3R->H_3CO->C_Ext-2O-R_N-5R!H->C
Total Standard Deviation in ln(k): 29.476230467870984""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_2R->O_N-3R->H_3CO->C_Ext-2O-R_N-5R!H->C
Total Standard Deviation in ln(k): 29.476230467870984
""",
)

entry(
    index = 75,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_Sp-5R!H=2C",
    kinetics = ArrheniusBM(A=(0.000608758,'m^3/(mol*s)'), n=2.85199, w0=(358000,'J/mol'), E0=(163461,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0027999286253727247, var=8.15175008544043, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_Sp-5R!H=2C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_Sp-5R!H=2C
    Total Standard Deviation in ln(k): 5.730808208511869"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_Sp-5R!H=2C
Total Standard Deviation in ln(k): 5.730808208511869""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_Sp-5R!H=2C
Total Standard Deviation in ln(k): 5.730808208511869
""",
)

entry(
    index = 76,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C",
    kinetics = ArrheniusBM(A=(7.86583e-13,'m^3/(mol*s)'), n=5.46523, w0=(358000,'J/mol'), E0=(153825,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05828351017764454, var=26.88833094657964, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C',), comment="""BM rule fitted to 18 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C
    Total Standard Deviation in ln(k): 10.54178609056609"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C
Total Standard Deviation in ln(k): 10.54178609056609""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C
Total Standard Deviation in ln(k): 10.54178609056609
""",
)

entry(
    index = 77,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(6.8221e-10,'m^3/(mol*s)'), n=4.62956, w0=(358000,'J/mol'), E0=(184095,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03217909194215576, var=22.65413723356873, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 9.622661736080317"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 9.622661736080317""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 9.622661736080317
""",
)

entry(
    index = 78,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(2.65124e-05,'m^3/(mol*s)'), n=3.30313, w0=(358000,'J/mol'), E0=(161282,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0033132116704030936, var=14.378111501569988, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 7.609975411337787"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 7.609975411337787""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 7.609975411337787
""",
)

entry(
    index = 79,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.20185e-05,'m^3/(mol*s)'), n=3.33293, w0=(358000,'J/mol'), E0=(165869,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.4443686672721672e-16, var=25.014461451747124, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 10.026574105793202"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 10.026574105793202""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 10.026574105793202
""",
)

entry(
    index = 80,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-4C-R_Sp-5R!H=4C",
    kinetics = ArrheniusBM(A=(0.0159381,'m^3/(mol*s)'), n=2.11123, w0=(358000,'J/mol'), E0=(169615,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.477679267453817e-15, var=7.542488711961111, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-4C-R_Sp-5R!H=4C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-4C-R_Sp-5R!H=4C
    Total Standard Deviation in ln(k): 5.505722571002713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-4C-R_Sp-5R!H=4C
Total Standard Deviation in ln(k): 5.505722571002713""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-4C-R_Sp-5R!H=4C
Total Standard Deviation in ln(k): 5.505722571002713
""",
)

entry(
    index = 81,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-4C-R_N-Sp-5R!H=4C",
    kinetics = ArrheniusBM(A=(3.89394e-06,'m^3/(mol*s)'), n=3.80787, w0=(358000,'J/mol'), E0=(164966,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=6.088045200938366, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-4C-R_N-Sp-5R!H=4C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-4C-R_N-Sp-5R!H=4C
    Total Standard Deviation in ln(k): 4.946476196685929"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-4C-R_N-Sp-5R!H=4C
Total Standard Deviation in ln(k): 4.946476196685929""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-4C-R_N-Sp-5R!H=4C
Total Standard Deviation in ln(k): 4.946476196685929
""",
)

entry(
    index = 82,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R",
    kinetics = ArrheniusBM(A=(1.03569e-13,'m^3/(mol*s)'), n=5.68295, w0=(408500,'J/mol'), E0=(136388,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.014560530005585964, var=3.0604070079408388, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R
    Total Standard Deviation in ln(k): 3.543671599759603"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R
Total Standard Deviation in ln(k): 3.543671599759603""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R
Total Standard Deviation in ln(k): 3.543671599759603
""",
)

entry(
    index = 83,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Sp-5R!H-3R",
    kinetics = ArrheniusBM(A=(1.77714e-11,'m^3/(mol*s)'), n=5.2168, w0=(408500,'J/mol'), E0=(128631,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0035439811521246712, var=7.847869614323852, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Sp-5R!H-3R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Sp-5R!H-3R
    Total Standard Deviation in ln(k): 5.624979216039648"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Sp-5R!H-3R
Total Standard Deviation in ln(k): 5.624979216039648""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Sp-5R!H-3R
Total Standard Deviation in ln(k): 5.624979216039648
""",
)

entry(
    index = 84,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_N-Sp-5R!H-3R",
    kinetics = ArrheniusBM(A=(9.20267e-13,'m^3/(mol*s)'), n=4.91903, w0=(408500,'J/mol'), E0=(143501,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.788805533999384e-15, var=49.031612587006606, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_N-Sp-5R!H-3R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_N-Sp-5R!H-3R
    Total Standard Deviation in ln(k): 14.037671587737917"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_N-Sp-5R!H-3R
Total Standard Deviation in ln(k): 14.037671587737917""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_N-Sp-5R!H-3R
Total Standard Deviation in ln(k): 14.037671587737917
""",
)

entry(
    index = 85,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(4.4565e-08,'m^3/(mol*s)'), n=4.06918, w0=(408500,'J/mol'), E0=(137823,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.040204092043915896, var=9.099261077629937, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R',), comment="""BM rule fitted to 24 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 6.148294955079777"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.148294955079777""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.148294955079777
""",
)

entry(
    index = 86,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C",
    kinetics = ArrheniusBM(A=(4.77849e-05,'m^3/(mol*s)'), n=3.00218, w0=(408500,'J/mol'), E0=(142579,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03358028900189916, var=7.007666066020115, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C',), comment="""BM rule fitted to 8 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C
    Total Standard Deviation in ln(k): 5.391306610588608"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C
Total Standard Deviation in ln(k): 5.391306610588608""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C
Total Standard Deviation in ln(k): 5.391306610588608
""",
)

entry(
    index = 87,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C",
    kinetics = ArrheniusBM(A=(4.57869e-08,'m^3/(mol*s)'), n=4.15283, w0=(408500,'J/mol'), E0=(137172,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03184252911622509, var=4.730419516340826, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C',), comment="""BM rule fitted to 12 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C
    Total Standard Deviation in ln(k): 4.440210447947845"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C
Total Standard Deviation in ln(k): 4.440210447947845""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C
Total Standard Deviation in ln(k): 4.440210447947845
""",
)

entry(
    index = 88,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-3R-R_Ext-4O-R",
    kinetics = ArrheniusBM(A=(56.1538,'m^3/(mol*s)'), n=2.27709, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.1979341195816136, var=138.2553829460727, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-3R-R_Ext-4O-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-3R-R_Ext-4O-R
    Total Standard Deviation in ln(k): 29.094533387406482"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-3R-R_Ext-4O-R
Total Standard Deviation in ln(k): 29.094533387406482""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-3R-R_Ext-4O-R
Total Standard Deviation in ln(k): 29.094533387406482
""",
)

entry(
    index = 89,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_3R->O",
    kinetics = ArrheniusBM(A=(4.66523e-35,'m^3/(mol*s)'), n=12.2252, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=7.083617203099816, var=0.9027213886149646, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_3R->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_3R->O
    Total Standard Deviation in ln(k): 19.702765075198492"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_3R->O
Total Standard Deviation in ln(k): 19.702765075198492""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_3R->O
Total Standard Deviation in ln(k): 19.702765075198492
""",
)

entry(
    index = 90,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O",
    kinetics = ArrheniusBM(A=(6.99562e-27,'m^3/(mol*s)'), n=9.91317, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4306594227155341, var=11.065095266983871, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O
    Total Standard Deviation in ln(k): 7.75065731607563"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O
Total Standard Deviation in ln(k): 7.75065731607563""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O
Total Standard Deviation in ln(k): 7.75065731607563
""",
)

entry(
    index = 91,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_N-3R->C_3HO->H",
    kinetics = ArrheniusBM(A=(3.39796e-22,'m^3/(mol*s)'), n=8.77321, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.49053641815453, var=1.5062994684414635, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_N-3R->C_3HO->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_N-3R->C_3HO->H
    Total Standard Deviation in ln(k): 13.74319409422517"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_N-3R->C_3HO->H
Total Standard Deviation in ln(k): 13.74319409422517""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_N-3R->C_3HO->H
Total Standard Deviation in ln(k): 13.74319409422517
""",
)

entry(
    index = 92,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_N-3R->C_N-3HO->H",
    kinetics = ArrheniusBM(A=(2.78535e-35,'m^3/(mol*s)'), n=12.5956, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=7.063951129786145, var=6.214001089983171, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_N-3R->C_N-3HO->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_N-3R->C_N-3HO->H
    Total Standard Deviation in ln(k): 22.746004123157867"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_N-3R->C_N-3HO->H
Total Standard Deviation in ln(k): 22.746004123157867""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_N-3R->C_N-3HO->H
Total Standard Deviation in ln(k): 22.746004123157867
""",
)

entry(
    index = 93,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_3R->O_Ext-4O-R",
    kinetics = ArrheniusBM(A=(2.24113e-29,'m^3/(mol*s)'), n=10.8768, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3370555076804646, var=3.4370756215328893, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_3R->O_Ext-4O-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_3R->O_Ext-4O-R
    Total Standard Deviation in ln(k): 4.563522005157647"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_3R->O_Ext-4O-R
Total Standard Deviation in ln(k): 4.563522005157647""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_3R->O_Ext-4O-R
Total Standard Deviation in ln(k): 4.563522005157647
""",
)

entry(
    index = 94,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_3R->O_Ext-3O-R",
    kinetics = ArrheniusBM(A=(1.20049e-27,'m^3/(mol*s)'), n=10.52, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.2492061772580687, var=0.30679881899917105, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_3R->O_Ext-3O-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_3R->O_Ext-3O-R
    Total Standard Deviation in ln(k): 9.2742458100323"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 9.2742458100323""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 9.2742458100323
""",
)

entry(
    index = 95,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R",
    kinetics = ArrheniusBM(A=(1.23252e-17,'m^3/(mol*s)'), n=7.22409, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.22565498576506257, var=9.211869048003942, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R
    Total Standard Deviation in ln(k): 6.651555991544714"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R
Total Standard Deviation in ln(k): 6.651555991544714""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R
Total Standard Deviation in ln(k): 6.651555991544714
""",
)

entry(
    index = 96,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_3CH->C",
    kinetics = ArrheniusBM(A=(3.36623e-18,'m^3/(mol*s)'), n=7.37123, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7632797126129418, var=0.256761780630496, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_3CH->C
    Total Standard Deviation in ln(k): 5.446183713380566"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_3CH->C
Total Standard Deviation in ln(k): 5.446183713380566""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_3CH->C
Total Standard Deviation in ln(k): 5.446183713380566
""",
)

entry(
    index = 97,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_N-3CH->C",
    kinetics = ArrheniusBM(A=(1.26273e-12,'m^3/(mol*s)'), n=5.95987, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.3515163322944126, var=3.025723951393575, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_N-3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_N-3CH->C
    Total Standard Deviation in ln(k): 6.882927804817453"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_N-3CH->C
Total Standard Deviation in ln(k): 6.882927804817453""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_N-3CH->C
Total Standard Deviation in ln(k): 6.882927804817453
""",
)

entry(
    index = 98,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.37212e-07,'m^3/(mol*s)'), n=4.05281, w0=(408500,'J/mol'), E0=(140478,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01209498312423001, var=2.5318952761140214, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 3.2203098979377542"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.2203098979377542""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.2203098979377542
""",
)

entry(
    index = 99,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(8.67735e-07,'m^3/(mol*s)'), n=4.08811, w0=(408500,'J/mol'), E0=(131555,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00782509971878515, var=1.6847967234419545, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 2.621801565772041"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.621801565772041""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.621801565772041
""",
)

entry(
    index = 100,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.24201e-45,'m^3/(mol*s)'), n=15.6087, w0=(408500,'J/mol'), E0=(30246.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5272852970143278, var=11.343918939901586, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 6 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 8.07693247031189"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 8.07693247031189""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 8.07693247031189
""",
)

entry(
    index = 101,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.25027e-09,'m^3/(mol*s)'), n=4.00731, w0=(408500,'J/mol'), E0=(115171,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07369423928363301, var=18.146317823108024, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 8.725031136531191"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 8.725031136531191""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 8.725031136531191
""",
)

entry(
    index = 102,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(2.3248e-08,'m^3/(mol*s)'), n=4.68886, w0=(408500,'J/mol'), E0=(121404,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.6791297252951817e-15, var=0.19326543300958057, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 0.8813209247295316"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.8813209247295316""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.8813209247295316
""",
)

entry(
    index = 103,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(2.30605e-05,'m^3/(mol*s)'), n=3.70277, w0=(408500,'J/mol'), E0=(129136,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.826194709884929e-16, var=0.1888423352238241, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 0.8711775405803621"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.8711775405803621""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.8711775405803621
""",
)

entry(
    index = 104,
    label = "Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.48657e-10,'m^3/(mol*s)'), n=4.75626, w0=(408500,'J/mol'), E0=(117555,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2263353412554899, var=19.17635660151086, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 9.347580467874552"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 9.347580467874552""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 9.347580467874552
""",
)

entry(
    index = 105,
    label = "Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.193539,'m^3/(mol*s)'), n=2.66115, w0=(408500,'J/mol'), E0=(126373,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.610921668180418e-16, var=17.859291852440148, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 8.472061635085925"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 8.472061635085925""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 8.472061635085925
""",
)

entry(
    index = 106,
    label = "Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(1.73213e-36,'m^3/(mol*s)'), n=12.7728, w0=(408500,'J/mol'), E0=(40850,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=7.625725766690818, var=0.13598378724147653, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 19.899380690119006"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 19.899380690119006""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 19.899380690119006
""",
)

entry(
    index = 107,
    label = "Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.00113688,'m^3/(mol*s)'), n=3.17993, w0=(408500,'J/mol'), E0=(134722,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7221843336360837e-15, var=9.853979008189649, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 6.29307352423148"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 6.29307352423148""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 6.29307352423148
""",
)

entry(
    index = 108,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_Sp-5R!H=2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.00534127,'m^3/(mol*s)'), n=2.27685, w0=(358000,'J/mol'), E0=(160143,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.894402766999692e-15, var=7.542488711960811, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_Sp-5R!H=2C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_Sp-5R!H=2C_Ext-2C-R
    Total Standard Deviation in ln(k): 5.505722571002596"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_Sp-5R!H=2C_Ext-2C-R
Total Standard Deviation in ln(k): 5.505722571002596""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_Sp-5R!H=2C_Ext-2C-R
Total Standard Deviation in ln(k): 5.505722571002596
""",
)

entry(
    index = 109,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.75947e-14,'m^3/(mol*s)'), n=5.83289, w0=(358000,'J/mol'), E0=(153168,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06371273532479245, var=33.91183443128452, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.834430141557341"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R
Total Standard Deviation in ln(k): 11.834430141557341""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R
Total Standard Deviation in ln(k): 11.834430141557341
""",
)

entry(
    index = 110,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(9.043e-10,'m^3/(mol*s)'), n=4.57602, w0=(358000,'J/mol'), E0=(154111,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03807871881364993, var=7.416085768449204, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 5.555068207828819"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R
Total Standard Deviation in ln(k): 5.555068207828819""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R
Total Standard Deviation in ln(k): 5.555068207828819
""",
)

entry(
    index = 111,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R",
    kinetics = ArrheniusBM(A=(6.79446e-15,'m^3/(mol*s)'), n=6.07852, w0=(358000,'J/mol'), E0=(186849,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00463530035855201, var=23.487912792182154, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R
    Total Standard Deviation in ln(k): 9.727460712178365"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R
Total Standard Deviation in ln(k): 9.727460712178365""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R
Total Standard Deviation in ln(k): 9.727460712178365
""",
)

entry(
    index = 112,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.68609e-05,'m^3/(mol*s)'), n=3.28247, w0=(358000,'J/mol'), E0=(160678,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.009967683513496445, var=25.41387038087345, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-4C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-4C-R
    Total Standard Deviation in ln(k): 10.131349289756225"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-4C-R
Total Standard Deviation in ln(k): 10.131349289756225""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-4C-R
Total Standard Deviation in ln(k): 10.131349289756225
""",
)

entry(
    index = 113,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_Ext-3R-R",
    kinetics = ArrheniusBM(A=(1.45027e-15,'m^3/(mol*s)'), n=6.13905, w0=(408500,'J/mol'), E0=(135771,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.004703991462611054, var=2.5337696728254016, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_Ext-3R-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_Ext-3R-R
    Total Standard Deviation in ln(k): 3.20292011956624"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_Ext-3R-R
Total Standard Deviation in ln(k): 3.20292011956624""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_Ext-3R-R
Total Standard Deviation in ln(k): 3.20292011956624
""",
)

entry(
    index = 114,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_Sp-5R!H=3R",
    kinetics = ArrheniusBM(A=(1.50254e-14,'m^3/(mol*s)'), n=5.86253, w0=(408500,'J/mol'), E0=(142692,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.2399727202179802e-14, var=0.41967860569681004, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_Sp-5R!H=3R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_Sp-5R!H=3R
    Total Standard Deviation in ln(k): 1.298719629134106"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_Sp-5R!H=3R
Total Standard Deviation in ln(k): 1.298719629134106""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_Sp-5R!H=3R
Total Standard Deviation in ln(k): 1.298719629134106
""",
)

entry(
    index = 115,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_N-Sp-5R!H=3R",
    kinetics = ArrheniusBM(A=(7.86855e-15,'m^3/(mol*s)'), n=6.09841, w0=(408500,'J/mol'), E0=(129098,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.008167778179000421, var=2.222401575449742, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_N-Sp-5R!H=3R',), comment="""BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_N-Sp-5R!H=3R
    Total Standard Deviation in ln(k): 3.009125258564138"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_N-Sp-5R!H=3R
Total Standard Deviation in ln(k): 3.009125258564138""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_N-Sp-5R!H=3R
Total Standard Deviation in ln(k): 3.009125258564138
""",
)

entry(
    index = 116,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Sp-5R!H-3R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.07835e-13,'m^3/(mol*s)'), n=5.54885, w0=(408500,'J/mol'), E0=(123193,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.5089505797835206e-15, var=0.17180945703685627, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Sp-5R!H-3R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Sp-5R!H-3R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.8309607719889683"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Sp-5R!H-3R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.8309607719889683""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Sp-5R!H-3R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.8309607719889683
""",
)

entry(
    index = 117,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(4.0587e-09,'m^3/(mol*s)'), n=4.27776, w0=(408500,'J/mol'), E0=(136690,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01339442728365351, var=11.539863105393591, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R',), comment="""BM rule fitted to 16 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R
    Total Standard Deviation in ln(k): 6.843814377385518"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R
Total Standard Deviation in ln(k): 6.843814377385518""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R
Total Standard Deviation in ln(k): 6.843814377385518
""",
)

entry(
    index = 118,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_3R->C",
    kinetics = ArrheniusBM(A=(5.8992e-09,'m^3/(mol*s)'), n=4.54372, w0=(408500,'J/mol'), E0=(134335,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06573017981924933, var=3.9620489598316126, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_3R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_3R->C
    Total Standard Deviation in ln(k): 4.155555584347169"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_3R->C
Total Standard Deviation in ln(k): 4.155555584347169""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_3R->C
Total Standard Deviation in ln(k): 4.155555584347169
""",
)

entry(
    index = 119,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_N-3R->C",
    kinetics = ArrheniusBM(A=(2.97161e-09,'m^3/(mol*s)'), n=4.60006, w0=(408500,'J/mol'), E0=(132117,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.012489486278519653, var=1.4821077657835369, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_N-3R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_N-3R->C
    Total Standard Deviation in ln(k): 2.4719821580259644"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_N-3R->C
Total Standard Deviation in ln(k): 2.4719821580259644""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_N-3R->C
Total Standard Deviation in ln(k): 2.4719821580259644
""",
)

entry(
    index = 120,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C_3R->C",
    kinetics = ArrheniusBM(A=(8.12598e-07,'m^3/(mol*s)'), n=3.2336, w0=(408500,'J/mol'), E0=(137315,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.014755821013003108, var=4.602680811805856, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C_3R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C_3R->C
    Total Standard Deviation in ln(k): 4.338005366409822"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C_3R->C
Total Standard Deviation in ln(k): 4.338005366409822""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C_3R->C
Total Standard Deviation in ln(k): 4.338005366409822
""",
)

entry(
    index = 121,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C_N-3R->C",
    kinetics = ArrheniusBM(A=(4.49437e-09,'m^3/(mol*s)'), n=4.48407, w0=(408500,'J/mol'), E0=(136000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01111317357622405, var=2.410210855251492, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C_N-3R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C_N-3R->C
    Total Standard Deviation in ln(k): 3.1402444451904286"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C_N-3R->C
Total Standard Deviation in ln(k): 3.1402444451904286""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C_N-3R->C
Total Standard Deviation in ln(k): 3.1402444451904286
""",
)

entry(
    index = 122,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_3R->C",
    kinetics = ArrheniusBM(A=(6.25839e-12,'m^3/(mol*s)'), n=5.15075, w0=(408500,'J/mol'), E0=(132670,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.008863011607672718, var=2.7941256929150415, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_3R->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_3R->C
    Total Standard Deviation in ln(k): 3.3733115505620295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_3R->C
Total Standard Deviation in ln(k): 3.3733115505620295""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_3R->C
Total Standard Deviation in ln(k): 3.3733115505620295
""",
)

entry(
    index = 123,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_N-3R->C",
    kinetics = ArrheniusBM(A=(1.31956e-09,'m^3/(mol*s)'), n=4.75437, w0=(408500,'J/mol'), E0=(130295,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.015236246919643169, var=2.612383918165138, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_N-3R->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_N-3R->C
    Total Standard Deviation in ln(k): 3.278509427628024"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_N-3R->C
Total Standard Deviation in ln(k): 3.278509427628024""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_N-3R->C
Total Standard Deviation in ln(k): 3.278509427628024
""",
)

entry(
    index = 124,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_5R!H->C",
    kinetics = ArrheniusBM(A=(3.51797e-24,'m^3/(mol*s)'), n=8.78083, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.41512609224412195, var=17.0668177813121, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_5R!H->C
    Total Standard Deviation in ln(k): 9.324992987601274"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_5R!H->C
Total Standard Deviation in ln(k): 9.324992987601274""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_5R!H->C
Total Standard Deviation in ln(k): 9.324992987601274
""",
)

entry(
    index = 125,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.39111e-29,'m^3/(mol*s)'), n=11.0455, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.446192750856968, var=5.8147381732858845, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_N-5R!H->C
    Total Standard Deviation in ln(k): 5.9552590117634985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_N-5R!H->C
Total Standard Deviation in ln(k): 5.9552590117634985""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_N-5R!H->C
Total Standard Deviation in ln(k): 5.9552590117634985
""",
)

entry(
    index = 126,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_3R->O_Ext-4O-R_Ext-3O-R",
    kinetics = ArrheniusBM(A=(1.60996e-30,'m^3/(mol*s)'), n=11.4244, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.3791799165305854, var=0.29032588654073194, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_3R->O_Ext-4O-R_Ext-3O-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_3R->O_Ext-4O-R_Ext-3O-R
    Total Standard Deviation in ln(k): 9.570591097496234"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_3R->O_Ext-4O-R_Ext-3O-R
Total Standard Deviation in ln(k): 9.570591097496234""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_3R->O_Ext-4O-R_Ext-3O-R
Total Standard Deviation in ln(k): 9.570591097496234
""",
)

entry(
    index = 127,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.31269e-14,'m^3/(mol*s)'), n=6.00126, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1992172546777876, var=24.408018403528438, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_5R!H->C
    Total Standard Deviation in ln(k): 10.40483363900353"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_5R!H->C
Total Standard Deviation in ln(k): 10.40483363900353""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_5R!H->C
Total Standard Deviation in ln(k): 10.40483363900353
""",
)

entry(
    index = 128,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(6.56855e-21,'m^3/(mol*s)'), n=8.44692, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.25209271513929965, var=0.8153092438275525, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_N-5R!H->C
    Total Standard Deviation in ln(k): 2.443563819758589"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_N-5R!H->C
Total Standard Deviation in ln(k): 2.443563819758589""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_N-5R!H->C
Total Standard Deviation in ln(k): 2.443563819758589
""",
)

entry(
    index = 129,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-3C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.21013e-09,'m^3/(mol*s)'), n=4.66608, w0=(408500,'J/mol'), E0=(142283,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.3387714342718596e-15, var=4.57629712674147, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-3C-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-3C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 4.288585733808529"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.288585733808529""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.288585733808529
""",
)

entry(
    index = 130,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-5R!H-R_Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(2.97097e-07,'m^3/(mol*s)'), n=4.12731, w0=(408500,'J/mol'), E0=(131303,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.610921668180418e-17, var=1.1754200036087414, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-5R!H-R_Sp-7R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-5R!H-R_Sp-7R!H=5R!H
    Total Standard Deviation in ln(k): 2.173469389530991"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-5R!H-R_Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 2.173469389530991""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-5R!H-R_Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 2.173469389530991
""",
)

entry(
    index = 131,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(2.53442e-06,'m^3/(mol*s)'), n=4.04892, w0=(408500,'J/mol'), E0=(131807,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.85134815865879e-15, var=0.6583144973402549, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
    Total Standard Deviation in ln(k): 1.626573524246915"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 1.626573524246915""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-3C-R_N-Sp-5R!H=3C_Ext-3C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 1.626573524246915
""",
)

entry(
    index = 132,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.45668e-09,'m^3/(mol*s)'), n=4.83119, w0=(408500,'J/mol'), E0=(126713,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.008891754438617552, var=12.116261016509727, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 7.000507144234648"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 7.000507144234648""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 7.000507144234648
""",
)

entry(
    index = 133,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(2.77437e-06,'m^3/(mol*s)'), n=2.93586, w0=(408500,'J/mol'), E0=(118024,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.4443686672721673e-15, var=83.57248431980375, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H
    Total Standard Deviation in ln(k): 18.326884617399312"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 18.326884617399312""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 18.326884617399312
""",
)

entry(
    index = 134,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.000142732,'m^3/(mol*s)'), n=2.83496, w0=(408500,'J/mol'), E0=(128824,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.477679267453817e-15, var=17.782799085244648, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
    Total Standard Deviation in ln(k): 8.453898909271437"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 8.453898909271437""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 8.453898909271437
""",
)

entry(
    index = 135,
    label = "Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.00124577,'m^3/(mol*s)'), n=2.41948, w0=(408500,'J/mol'), E0=(135822,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03241567681588407, var=18.367531361259907, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H',), comment="""BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H
    Total Standard Deviation in ln(k): 8.673211318105558"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 8.673211318105558""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 8.673211318105558
""",
)

entry(
    index = 136,
    label = "Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(0.0407584,'m^3/(mol*s)'), n=2.67701, w0=(408500,'J/mol'), E0=(132570,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.024876134273208506, var=8.568266739398778, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H',), comment="""BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
    Total Standard Deviation in ln(k): 5.93068354678599"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 5.93068354678599""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 5.93068354678599
""",
)

entry(
    index = 137,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.52151e-15,'m^3/(mol*s)'), n=5.82443, w0=(358000,'J/mol'), E0=(159766,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0352144133754723, var=38.19486176009814, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 12.478140483578848"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 12.478140483578848""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 12.478140483578848
""",
)

entry(
    index = 138,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(4.07943e-05,'m^3/(mol*s)'), n=3.24471, w0=(358000,'J/mol'), E0=(154064,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.788805533999384e-15, var=25.01446145174554, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 10.026574105792893"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 10.026574105792893""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 10.026574105792893
""",
)

entry(
    index = 139,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(2.97245e-10,'m^3/(mol*s)'), n=4.56697, w0=(358000,'J/mol'), E0=(156296,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.305460834090209e-17, var=0.4327461083854015, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 1.318783712890312"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.318783712890312""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.318783712890312
""",
)

entry(
    index = 140,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(3.50033e-05,'m^3/(mol*s)'), n=3.3723, w0=(358000,'J/mol'), E0=(160344,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.3387714342718596e-15, var=15.324179403336194, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 7.847758017295911"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 7.847758017295911""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 7.847758017295911
""",
)

entry(
    index = 141,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.26592e-15,'m^3/(mol*s)'), n=6.49874, w0=(358000,'J/mol'), E0=(190388,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.3777474669088669e-15, var=45.77036934838706, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 13.56279501334311"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 13.56279501334311""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 13.56279501334311
""",
)

entry(
    index = 142,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.00039172,'m^3/(mol*s)'), n=2.45435, w0=(358000,'J/mol'), E0=(160765,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.788805533999384e-15, var=30.302267079558682, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.035564418888958"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.035564418888958""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-4C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.035564418888958
""",
)

entry(
    index = 143,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_Ext-3R-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.02635e-17,'m^3/(mol*s)'), n=6.75702, w0=(408500,'J/mol'), E0=(137549,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=7.0609557679079435e-15, var=4.5762971267410935, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_Ext-3R-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_Ext-3R-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 4.288585733808357"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_Ext-3R-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.288585733808357""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_Ext-3R-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.288585733808357
""",
)

entry(
    index = 144,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_N-Sp-5R!H=3R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.76813e-15,'m^3/(mol*s)'), n=6.17942, w0=(408500,'J/mol'), E0=(126805,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.009238027234393655, var=1.6847967076449655, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_N-Sp-5R!H=3R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_N-Sp-5R!H=3R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 2.6253516227076426"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_N-Sp-5R!H=3R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.6253516227076426""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_N-Sp-5R!H=3R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.6253516227076426
""",
)

entry(
    index = 145,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(2.48969e-10,'m^3/(mol*s)'), n=4.54159, w0=(408500,'J/mol'), E0=(134568,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013384799627570686, var=14.694362174874586, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 8 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 7.718426434027268"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 7.718426434027268""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 7.718426434027268
""",
)

entry(
    index = 146,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(1.79312e-05,'m^3/(mol*s)'), n=3.29367, w0=(408500,'J/mol'), E0=(144047,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07663217615212796, var=12.083399998197983, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 8 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 7.1612398959323365"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 7.1612398959323365""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 7.1612398959323365
""",
)

entry(
    index = 147,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_3R->C_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(5.22562e-13,'m^3/(mol*s)'), n=5.89137, w0=(408500,'J/mol'), E0=(123004,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.2916382502270627e-16, var=0.193265433009702, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_3R->C_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_3R->C_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 0.8813209247298046"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_3R->C_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.8813209247298046""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_3R->C_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.8813209247298046
""",
)

entry(
    index = 148,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_3R->C_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(1.49601e-13,'m^3/(mol*s)'), n=5.75556, w0=(408500,'J/mol'), E0=(126608,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.638114404806227e-15, var=0.18884233522366933, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_3R->C_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_3R->C_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 0.8711775405800122"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_3R->C_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.8711775405800122""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_3R->C_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.8711775405800122
""",
)

entry(
    index = 149,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_N-3R->C_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(6.47642e-41,'m^3/(mol*s)'), n=14.015, w0=(408500,'J/mol'), E0=(40850,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=6.307530140282123, var=0.13598378724137047, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_N-3R->C_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_N-3R->C_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 16.587331377534056"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_N-3R->C_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 16.587331377534056""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_N-3R->C_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 16.587331377534056
""",
)

entry(
    index = 150,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_N-3R->C_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(3.29327e-11,'m^3/(mol*s)'), n=5.16786, w0=(408500,'J/mol'), E0=(128572,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=9.853979008190628, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_N-3R->C_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_N-3R->C_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 6.293073524231788"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_N-3R->C_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 6.293073524231788""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_N-3R->C_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 6.293073524231788
""",
)

entry(
    index = 151,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C_3R->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.71273e-06,'m^3/(mol*s)'), n=3.19421, w0=(408500,'J/mol'), E0=(139570,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=13.17144223061928, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C_3R->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C_3R->C_Ext-4C-R
    Total Standard Deviation in ln(k): 7.275681097481295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C_3R->C_Ext-4C-R
Total Standard Deviation in ln(k): 7.275681097481295""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C_3R->C_Ext-4C-R
Total Standard Deviation in ln(k): 7.275681097481295
""",
)

entry(
    index = 152,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C_N-3R->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(3.25295e-08,'m^3/(mol*s)'), n=4.11416, w0=(408500,'J/mol'), E0=(134424,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=7.0609557679079435e-15, var=3.885103517260717, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C_N-3R->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C_N-3R->C_Ext-4C-R
    Total Standard Deviation in ln(k): 3.9514663405044117"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C_N-3R->C_Ext-4C-R
Total Standard Deviation in ln(k): 3.9514663405044117""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Sp-5R!H=4C_N-3R->C_Ext-4C-R
Total Standard Deviation in ln(k): 3.9514663405044117
""",
)

entry(
    index = 153,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_3R->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.99611e-13,'m^3/(mol*s)'), n=5.59236, w0=(408500,'J/mol'), E0=(131081,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.009120208301138733, var=4.677449740176582, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_3R->C_Ext-4C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_3R->C_Ext-4C-R
    Total Standard Deviation in ln(k): 4.358638355359051"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_3R->C_Ext-4C-R
Total Standard Deviation in ln(k): 4.358638355359051""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_3R->C_Ext-4C-R
Total Standard Deviation in ln(k): 4.358638355359051
""",
)

entry(
    index = 154,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_N-3R->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(8.73222e-10,'m^3/(mol*s)'), n=4.8601, w0=(408500,'J/mol'), E0=(131681,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.014212097260132513, var=3.0867931849971484, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_N-3R->C_Ext-4C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_N-3R->C_Ext-4C-R
    Total Standard Deviation in ln(k): 3.557882372724508"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_N-3R->C_Ext-4C-R
Total Standard Deviation in ln(k): 3.557882372724508""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_N-3R->C_Ext-4C-R
Total Standard Deviation in ln(k): 3.557882372724508
""",
)

entry(
    index = 155,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_5R!H->C_3CH->C",
    kinetics = ArrheniusBM(A=(2.48299e-26,'m^3/(mol*s)'), n=9.11484, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=6.042917235632146, var=4.359521971532825, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_5R!H->C_3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_5R!H->C_3CH->C
    Total Standard Deviation in ln(k): 19.36898938776988"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_5R!H->C_3CH->C
Total Standard Deviation in ln(k): 19.36898938776988""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_5R!H->C_3CH->C
Total Standard Deviation in ln(k): 19.36898938776988
""",
)

entry(
    index = 156,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_5R!H->C_N-3CH->C",
    kinetics = ArrheniusBM(A=(4.98435e-22,'m^3/(mol*s)'), n=8.44682, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.425932628017854, var=0.8152680348923296, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_5R!H->C_N-3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_5R!H->C_N-3CH->C
    Total Standard Deviation in ln(k): 12.93055302973225"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_5R!H->C_N-3CH->C
Total Standard Deviation in ln(k): 12.93055302973225""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_5R!H->C_N-3CH->C
Total Standard Deviation in ln(k): 12.93055302973225
""",
)

entry(
    index = 157,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_N-5R!H->C_3CH->C",
    kinetics = ArrheniusBM(A=(2.76864e-34,'m^3/(mol*s)'), n=12.5558, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=6.142640360635298, var=29.48325330569553, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_N-5R!H->C_3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_N-5R!H->C_3CH->C
    Total Standard Deviation in ln(k): 26.319177239749667"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_N-5R!H->C_3CH->C
Total Standard Deviation in ln(k): 26.319177239749667""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_N-5R!H->C_3CH->C
Total Standard Deviation in ln(k): 26.319177239749667
""",
)

entry(
    index = 158,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_N-5R!H->C_N-3CH->C",
    kinetics = ArrheniusBM(A=(6.98965e-25,'m^3/(mol*s)'), n=9.53523, w0=(250000,'J/mol'), E0=(25000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.3316050170269342, var=0.9913363035128316, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_N-5R!H->C_N-3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_N-5R!H->C_N-3CH->C
    Total Standard Deviation in ln(k): 10.366898854963438"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_N-5R!H->C_N-3CH->C
Total Standard Deviation in ln(k): 10.366898854963438""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_2CH->C_Ext-4O-R_N-3R->O_N-5R!H->C_N-3CH->C
Total Standard Deviation in ln(k): 10.366898854963438
""",
)

entry(
    index = 159,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_5R!H->C_3CH->C",
    kinetics = ArrheniusBM(A=(5.61405e-17,'m^3/(mol*s)'), n=6.47875, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.5788135919638437, var=46.17922138772341, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_5R!H->C_3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_5R!H->C_3CH->C
    Total Standard Deviation in ln(k): 17.590104709481707"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_5R!H->C_3CH->C
Total Standard Deviation in ln(k): 17.590104709481707""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_5R!H->C_3CH->C
Total Standard Deviation in ln(k): 17.590104709481707
""",
)

entry(
    index = 160,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_5R!H->C_N-3CH->C",
    kinetics = ArrheniusBM(A=(9.5271e-12,'m^3/(mol*s)'), n=5.52376, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0965336461797257, var=2.516027630879999, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_5R!H->C_N-3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_5R!H->C_N-3CH->C
    Total Standard Deviation in ln(k): 5.935018668362727"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_5R!H->C_N-3CH->C
Total Standard Deviation in ln(k): 5.935018668362727""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_5R!H->C_N-3CH->C
Total Standard Deviation in ln(k): 5.935018668362727
""",
)

entry(
    index = 161,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_N-5R!H->C_3CH->C",
    kinetics = ArrheniusBM(A=(4.75386e-26,'m^3/(mol*s)'), n=10.1108, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7519929749229846, var=0.8899093766133183, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_N-5R!H->C_3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_N-5R!H->C_3CH->C
    Total Standard Deviation in ln(k): 6.293159398318633"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_N-5R!H->C_3CH->C
Total Standard Deviation in ln(k): 6.293159398318633""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_N-5R!H->C_3CH->C
Total Standard Deviation in ln(k): 6.293159398318633
""",
)

entry(
    index = 162,
    label = "Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_N-5R!H->C_N-3CH->C",
    kinetics = ArrheniusBM(A=(9.07595e-16,'m^3/(mol*s)'), n=6.78306, w0=(300500,'J/mol'), E0=(30050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5849189242333245, var=2.8184455791666254, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_N-5R!H->C_N-3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_N-5R!H->C_N-3CH->C
    Total Standard Deviation in ln(k): 4.835240246600434"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_N-5R!H->C_N-3CH->C
Total Standard Deviation in ln(k): 4.835240246600434""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_N-4CNOS->C_N-2CH->C_N-3R->O_Ext-4O-R_N-5R!H->C_N-3CH->C
Total Standard Deviation in ln(k): 4.835240246600434
""",
)

entry(
    index = 163,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R_Sp-8R!H=5R!H",
    kinetics = ArrheniusBM(A=(3.51104e-10,'m^3/(mol*s)'), n=4.95105, w0=(408500,'J/mol'), E0=(132236,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0333106001816501e-15, var=38.1600957941085, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R_Sp-8R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R_Sp-8R!H=5R!H
    Total Standard Deviation in ln(k): 12.3840220764559"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R_Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 12.3840220764559""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R_Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 12.3840220764559
""",
)

entry(
    index = 164,
    label = "Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R_N-Sp-8R!H=5R!H",
    kinetics = ArrheniusBM(A=(1.49454e-06,'m^3/(mol*s)'), n=4.00249, w0=(408500,'J/mol'), E0=(126423,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.411058067090517e-15, var=19.62838145157177, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R_N-Sp-8R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R_N-Sp-8R!H=5R!H
    Total Standard Deviation in ln(k): 8.88176409924183"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R_N-Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 8.88176409924183""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R_N-Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 8.88176409924183
""",
)

entry(
    index = 165,
    label = "Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.75387e-05,'m^3/(mol*s)'), n=2.80126, w0=(408500,'J/mol'), E0=(138023,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=6.8887373345443345e-16, var=35.878528751097186, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-2C-R
    Total Standard Deviation in ln(k): 12.008100177674606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-2C-R
Total Standard Deviation in ln(k): 12.008100177674606""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-2C-R
Total Standard Deviation in ln(k): 12.008100177674606
""",
)

entry(
    index = 166,
    label = "Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.000428992,'m^3/(mol*s)'), n=3.382, w0=(408500,'J/mol'), E0=(128356,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.411058067090517e-15, var=22.365422355603318, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-2C-R
    Total Standard Deviation in ln(k): 9.480812143473372"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-2C-R
Total Standard Deviation in ln(k): 9.480812143473372""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4CHNOS->H_2R->C_N-3R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-2C-R
Total Standard Deviation in ln(k): 9.480812143473372
""",
)

entry(
    index = 167,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(3.19444e-19,'m^3/(mol*s)'), n=6.93921, w0=(358000,'J/mol'), E0=(175648,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0008293619198202665, var=20.47288951925894, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H
    Total Standard Deviation in ln(k): 9.07290407151811"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 9.07290407151811""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 9.07290407151811
""",
)

entry(
    index = 168,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(6.86222e-07,'m^3/(mol*s)'), n=3.57002, w0=(358000,'J/mol'), E0=(151804,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0056948444249981175, var=25.39881092215003, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
    Total Standard Deviation in ln(k): 10.117618730542493"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 10.117618730542493""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 10.117618730542493
""",
)

entry(
    index = 169,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_N-Sp-5R!H=3R_Ext-5R!H-R_Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(9.47687e-16,'m^3/(mol*s)'), n=6.21863, w0=(408500,'J/mol'), E0=(126553,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.5304778839539717e-15, var=1.1754200036084723, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_N-Sp-5R!H=3R_Ext-5R!H-R_Sp-7R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_N-Sp-5R!H=3R_Ext-5R!H-R_Sp-7R!H=5R!H
    Total Standard Deviation in ln(k): 2.1734693895307506"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_N-Sp-5R!H=3R_Ext-5R!H-R_Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 2.1734693895307506""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_N-Sp-5R!H=3R_Ext-5R!H-R_Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 2.1734693895307506
""",
)

entry(
    index = 170,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_N-Sp-5R!H=3R_Ext-5R!H-R_N-Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(8.08547e-15,'m^3/(mol*s)'), n=6.14022, w0=(408500,'J/mol'), E0=(127058,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.2957168259309574e-15, var=0.658314497339961, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_N-Sp-5R!H=3R_Ext-5R!H-R_N-Sp-7R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_N-Sp-5R!H=3R_Ext-5R!H-R_N-Sp-7R!H=5R!H
    Total Standard Deviation in ln(k): 1.6265735242465607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_N-Sp-5R!H=3R_Ext-5R!H-R_N-Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 1.6265735242465607""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-3R-R_Ext-3R-R_N-Sp-5R!H=3R_Ext-5R!H-R_N-Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 1.6265735242465607
""",
)

entry(
    index = 171,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_Ext-4C-R",
    kinetics = ArrheniusBM(A=(7.49006e-13,'m^3/(mol*s)'), n=5.55721, w0=(408500,'J/mol'), E0=(137783,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.37835889066399125, var=15.303338792080408, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_Ext-4C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_Ext-4C-R
    Total Standard Deviation in ln(k): 8.793070275145837"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_Ext-4C-R
Total Standard Deviation in ln(k): 8.793070275145837""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_Ext-4C-R
Total Standard Deviation in ln(k): 8.793070275145837
""",
)

entry(
    index = 172,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_3R->C",
    kinetics = ArrheniusBM(A=(2.39149e-11,'m^3/(mol*s)'), n=4.34105, w0=(408500,'J/mol'), E0=(122864,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.0666212003633003e-15, var=83.57248431980602, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_3R->C
    Total Standard Deviation in ln(k): 18.326884617399557"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_3R->C
Total Standard Deviation in ln(k): 18.326884617399557""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_3R->C
Total Standard Deviation in ln(k): 18.326884617399557
""",
)

entry(
    index = 173,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_N-3R->C",
    kinetics = ArrheniusBM(A=(1.04133e-09,'m^3/(mol*s)'), n=4.32143, w0=(408500,'J/mol'), E0=(127702,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=68.92620431629227, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_N-3R->C
    Total Standard Deviation in ln(k): 16.64367286101185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_N-3R->C
Total Standard Deviation in ln(k): 16.64367286101185""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_N-3R->C
Total Standard Deviation in ln(k): 16.64367286101185
""",
)

entry(
    index = 174,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H_3R->C",
    kinetics = ArrheniusBM(A=(5.18338e-10,'m^3/(mol*s)'), n=4.43393, w0=(408500,'J/mol'), E0=(137889,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.025805170381271, var=13.912378328597864, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H_3R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H_3R->C
    Total Standard Deviation in ln(k): 7.542358759472052"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H_3R->C
Total Standard Deviation in ln(k): 7.542358759472052""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H_3R->C
Total Standard Deviation in ln(k): 7.542358759472052
""",
)

entry(
    index = 175,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H_N-3R->C",
    kinetics = ArrheniusBM(A=(1.29753e-08,'m^3/(mol*s)'), n=4.42685, w0=(408500,'J/mol'), E0=(133526,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0034576659251904394, var=8.56530087888059, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H_N-3R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H_N-3R->C
    Total Standard Deviation in ln(k): 5.875852591817552"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H_N-3R->C
Total Standard Deviation in ln(k): 5.875852591817552""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H_N-3R->C
Total Standard Deviation in ln(k): 5.875852591817552
""",
)

entry(
    index = 176,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_3R->C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(5.09336e-14,'m^3/(mol*s)'), n=5.77473, w0=(408500,'J/mol'), E0=(128508,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7221843336360837e-15, var=28.06236757279499, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_3R->C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_3R->C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 10.61986861527119"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_3R->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 10.61986861527119""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_3R->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 10.61986861527119
""",
)

entry(
    index = 177,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_N-3R->C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.5204e-09,'m^3/(mol*s)'), n=4.77043, w0=(408500,'J/mol'), E0=(130438,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=17.859291852441334, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_N-3R->C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_N-3R->C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 8.472061635086204"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_N-3R->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 8.472061635086204""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_N-Sp-5R!H=4C_N-3R->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 8.472061635086204
""",
)

entry(
    index = 178,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.57115e-21,'m^3/(mol*s)'), n=7.6108, w0=(358000,'J/mol'), E0=(176543,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.4443686672721673e-15, var=45.77036934838402, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-2C-R
    Total Standard Deviation in ln(k): 13.562795013342665"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-2C-R
Total Standard Deviation in ln(k): 13.562795013342665""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-2C-R
Total Standard Deviation in ln(k): 13.562795013342665
""",
)

entry(
    index = 179,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.06118e-06,'m^3/(mol*s)'), n=3.09816, w0=(358000,'J/mol'), E0=(149729,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=30.30226707955695, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-2C-R
    Total Standard Deviation in ln(k): 11.035564418888635"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-2C-R
Total Standard Deviation in ln(k): 11.035564418888635""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_2CH->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-2C-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-2C-R
Total Standard Deviation in ln(k): 11.035564418888635
""",
)

entry(
    index = 180,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_Ext-4C-R_3R->C",
    kinetics = ArrheniusBM(A=(3.15865e-13,'m^3/(mol*s)'), n=5.93444, w0=(408500,'J/mol'), E0=(141999,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.166553000908251e-15, var=38.16009579411033, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_Ext-4C-R_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_Ext-4C-R_3R->C
    Total Standard Deviation in ln(k): 12.384022076456208"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_Ext-4C-R_3R->C
Total Standard Deviation in ln(k): 12.384022076456208""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_Ext-4C-R_3R->C
Total Standard Deviation in ln(k): 12.384022076456208
""",
)

entry(
    index = 181,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_Ext-4C-R_N-3R->C",
    kinetics = ArrheniusBM(A=(1.69912e-07,'m^3/(mol*s)'), n=3.7055, w0=(408500,'J/mol'), E0=(144464,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.5109898676354676e-15, var=35.878528751098656, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_Ext-4C-R_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_Ext-4C-R_N-3R->C
    Total Standard Deviation in ln(k): 12.008100177674862"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_Ext-4C-R_N-3R->C
Total Standard Deviation in ln(k): 12.008100177674862""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_Sp-6R!H=5R!H_Ext-4C-R_N-3R->C
Total Standard Deviation in ln(k): 12.008100177674862
""",
)

entry(
    index = 182,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H_3R->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.75135e-12,'m^3/(mol*s)'), n=5.44783, w0=(408500,'J/mol'), E0=(133263,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=19.628381451573674, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H_3R->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H_3R->C_Ext-4C-R
    Total Standard Deviation in ln(k): 8.881764099242254"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H_3R->C_Ext-4C-R
Total Standard Deviation in ln(k): 8.881764099242254""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H_3R->C_Ext-4C-R
Total Standard Deviation in ln(k): 8.881764099242254
""",
)

entry(
    index = 183,
    label = "Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H_N-3R->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.48351e-09,'m^3/(mol*s)'), n=4.75042, w0=(408500,'J/mol'), E0=(131832,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.0666212003633003e-15, var=22.36542235560455, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H_N-3R->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H_N-3R->C_Ext-4C-R
    Total Standard Deviation in ln(k): 9.480812143473633"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H_N-3R->C_Ext-4C-R
Total Standard Deviation in ln(k): 9.480812143473633""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4CHNOS->H_N-2R->O_4CNOS->C_N-2CH->C_Ext-4C-R_Ext-5R!H-R_Ext-4C-R_N-Sp-6R!H=5R!H_N-3R->C_Ext-4C-R
Total Standard Deviation in ln(k): 9.480812143473633
""",
)

