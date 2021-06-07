#!/usr/bin/env python
# encoding: utf-8

name = "CO_Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.29348e+08,'m^3/(mol*s)'), n=-0.306961, w0=(554731,'J/mol'), E0=(51511.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0007517332959459186, var=1.4486037996689085, Tref=1000.0, N=13, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 13 training reactions at node Root
    Total Standard Deviation in ln(k): 2.414746974819662"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root
Total Standard Deviation in ln(k): 2.414746974819662""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root
Total Standard Deviation in ln(k): 2.414746974819662
""",
)

entry(
    index = 2,
    label = "Root_4R->N",
    kinetics = ArrheniusBM(A=(7.1e+06,'m^3/(mol*s)'), n=0, w0=(535000,'J/mol'), E0=(32802.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->N',), comment="""BM rule fitted to 1 training reactions at node Root_4R->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_N-4R->N",
    kinetics = ArrheniusBM(A=(8.38033e+07,'m^3/(mol*s)'), n=-0.159505, w0=(556375,'J/mol'), E0=(44765.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09920204661675033, var=1.474353864336599, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->N',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->N
    Total Standard Deviation in ln(k): 2.6834603275433544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->N
Total Standard Deviation in ln(k): 2.6834603275433544""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->N
Total Standard Deviation in ln(k): 2.6834603275433544
""",
)

entry(
    index = 4,
    label = "Root_N-4R->N_4BrCClFHIOPSSi->H",
    kinetics = ArrheniusBM(A=(9.03e+07,'m^3/(mol*s)'), n=0, w0=(558000,'J/mol'), E0=(55800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_4BrCClFHIOPSSi->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_4BrCClFHIOPSSi->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_4BrCClFHIOPSSi->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_4BrCClFHIOPSSi->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H",
    kinetics = ArrheniusBM(A=(6.61788e+07,'m^3/(mol*s)'), n=-0.153133, w0=(556227,'J/mol'), E0=(41225.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13684351688887905, var=1.473861144377546, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H',), comment="""BM rule fitted to 11 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H
    Total Standard Deviation in ln(k): 2.7776301032250843"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H
Total Standard Deviation in ln(k): 2.7776301032250843""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H
Total Standard Deviation in ln(k): 2.7776301032250843
""",
)

entry(
    index = 6,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R",
    kinetics = ArrheniusBM(A=(6.22674e+07,'m^3/(mol*s)'), n=-0.159943, w0=(555500,'J/mol'), E0=(38705.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16465055438058515, var=1.7864081759488528, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R
    Total Standard Deviation in ln(k): 3.093155231420864"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R
Total Standard Deviation in ln(k): 3.093155231420864""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R
Total Standard Deviation in ln(k): 3.093155231420864
""",
)

entry(
    index = 7,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_4CO->C",
    kinetics = ArrheniusBM(A=(4e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(1004,'K'), Tmax=(1006,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_N-4CO->C",
    kinetics = ArrheniusBM(A=(3.01e+07,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(57150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C",
    kinetics = ArrheniusBM(A=(6.25086e+07,'m^3/(mol*s)'), n=-9.38684e-08, w0=(552300,'J/mol'), E0=(55230,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.003035865944037245, var=1.0537932494619016, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C
    Total Standard Deviation in ln(k): 2.0655772190197634"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C
Total Standard Deviation in ln(k): 2.0655772190197634""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C
Total Standard Deviation in ln(k): 2.0655772190197634
""",
)

entry(
    index = 10,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.90776e+07,'m^3/(mol*s)'), n=-0.209862, w0=(559500,'J/mol'), E0=(34468.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.290962749744308, var=1.5863982214809924, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C
    Total Standard Deviation in ln(k): 3.256072151191948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.256072151191948""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.256072151191948
""",
)

entry(
    index = 11,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Ext-4CO-R",
    kinetics = ArrheniusBM(A=(1.2e+08,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Ext-4CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Ext-4CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Ext-4CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Ext-4CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO",
    kinetics = ArrheniusBM(A=(6.23054e+07,'m^3/(mol*s)'), n=-9.73051e-08, w0=(555500,'J/mol'), E0=(55550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0001191721661824122, var=1.0835923253238533, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO
    Total Standard Deviation in ln(k): 2.0871432574958804"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO
Total Standard Deviation in ln(k): 2.0871432574958804""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO
Total Standard Deviation in ln(k): 2.0871432574958804
""",
)

entry(
    index = 13,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_N-Sp-5C-4CO",
    kinetics = ArrheniusBM(A=(9.033e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_N-Sp-5C-4CO',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_N-Sp-5C-4CO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_N-Sp-5C-4CO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_N-Sp-5C-4CO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(1.24e+17,'m^3/(mol*s)'), n=-3.29, w0=(571500,'J/mol'), E0=(57150,'J/mol'), Tmin=(1140,'K'), Tmax=(1650,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(1.46682e+06,'m^3/(mol*s)'), n=0.34128, w0=(555500,'J/mol'), E0=(24469.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3426295535272028, var=1.1310263282658846, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 2.9929084486563107"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N
Total Standard Deviation in ln(k): 2.9929084486563107""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N
Total Standard Deviation in ln(k): 2.9929084486563107
""",
)

entry(
    index = 16,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C",
    kinetics = ArrheniusBM(A=(4.30916e+07,'m^3/(mol*s)'), n=-1.45648e-06, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.32890731525313555, var=0.22197044450561015, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C
    Total Standard Deviation in ln(k): 1.7709059506268878"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C
Total Standard Deviation in ln(k): 1.7709059506268878""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C
Total Standard Deviation in ln(k): 1.7709059506268878
""",
)

entry(
    index = 17,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->C",
    kinetics = ArrheniusBM(A=(9.03e+07,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(57150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_4CO->C",
    kinetics = ArrheniusBM(A=(1.34165e+07,'m^3/(mol*s)'), n=-4.9914e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.5990137911088773e-17, var=0.6909863268735121, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_4CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_4CO->C
    Total Standard Deviation in ln(k): 1.666447807467594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_4CO->C
Total Standard Deviation in ln(k): 1.666447807467594""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_4CO->C
Total Standard Deviation in ln(k): 1.666447807467594
""",
)

entry(
    index = 19,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_N-4CO->C",
    kinetics = ArrheniusBM(A=(5.12e+07,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(53142.9,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(6e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_4CO->C_Sp-5O-4C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_4CO->C_Sp-5O-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_4CO->C_Sp-5O-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_4CO->C_Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_4CO->C_Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_4CO->C_N-Sp-5O-4C",
    kinetics = ArrheniusBM(A=(1.8e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_4CO->C_N-Sp-5O-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_4CO->C_N-Sp-5O-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_4CO->C_N-Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->N_4CO->C_N-Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

