#!/usr/bin/env python
# encoding: utf-8

name = "CO_Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.50424e+08,'m^3/(mol*s)'), n=-0.319767, w0=(554731,'J/mol'), E0=(51556.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0016473366032466322, var=1.5093311729901167, Tref=1000.0, N=13, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 13 training reactions at node Root
    Total Standard Deviation in ln(k): 2.467053109955428"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root
Total Standard Deviation in ln(k): 2.467053109955428""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root
Total Standard Deviation in ln(k): 2.467053109955428
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
    kinetics = ArrheniusBM(A=(1.07003e+08,'m^3/(mol*s)'), n=-0.197496, w0=(556375,'J/mol'), E0=(42832.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11670695366806721, var=1.483284502084561, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->N',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->N
    Total Standard Deviation in ln(k): 2.73480377059182"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->N
Total Standard Deviation in ln(k): 2.73480377059182""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->N
Total Standard Deviation in ln(k): 2.73480377059182
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
    kinetics = ArrheniusBM(A=(8.91879e+07,'m^3/(mol*s)'), n=-0.199685, w0=(556227,'J/mol'), E0=(38053.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1542009982792688, var=1.4652541492986535, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H',), comment="""BM rule fitted to 11 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H
    Total Standard Deviation in ln(k): 2.8141250501210964"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H
Total Standard Deviation in ln(k): 2.8141250501210964""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H
Total Standard Deviation in ln(k): 2.8141250501210964
""",
)

entry(
    index = 6,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R",
    kinetics = ArrheniusBM(A=(8.66768e+07,'m^3/(mol*s)'), n=-0.211541, w0=(555500,'J/mol'), E0=(35759.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18304785255687206, var=1.7684092321847347, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R
    Total Standard Deviation in ln(k): 3.125846982830696"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R
Total Standard Deviation in ln(k): 3.125846982830696""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R
Total Standard Deviation in ln(k): 3.125846982830696
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
    kinetics = ArrheniusBM(A=(6.25087e+07,'m^3/(mol*s)'), n=-3.44506e-07, w0=(552300,'J/mol'), E0=(55230,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.003035855795017244, var=1.0537930185332733, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C
    Total Standard Deviation in ln(k): 2.0655769680298164"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C
Total Standard Deviation in ln(k): 2.0655769680298164""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C
Total Standard Deviation in ln(k): 2.0655769680298164
""",
)

entry(
    index = 10,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.11393e+08,'m^3/(mol*s)'), n=-0.330374, w0=(559500,'J/mol'), E0=(31017.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.30376782766715116, var=1.5882125761374941, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C
    Total Standard Deviation in ln(k): 3.2896892209923085"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.2896892209923085""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.2896892209923085
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
    kinetics = ArrheniusBM(A=(6.23055e+07,'m^3/(mol*s)'), n=-3.48768e-07, w0=(555500,'J/mol'), E0=(55550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00011918107695963465, var=1.083592082729155, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO
    Total Standard Deviation in ln(k): 2.0871430462834097"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO
Total Standard Deviation in ln(k): 2.0871430462834097""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO
Total Standard Deviation in ln(k): 2.0871430462834097
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
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(2.31568e+06,'m^3/(mol*s)'), n=0.274147, w0=(555500,'J/mol'), E0=(18779.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.349762835877399, var=1.1191068111594877, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 2.999567127888949"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 2.999567127888949""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 2.999567127888949
""",
)

entry(
    index = 15,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.24e+17,'m^3/(mol*s)'), n=-3.29, w0=(571500,'J/mol'), E0=(57150,'J/mol'), Tmin=(1140,'K'), Tmax=(1650,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_N-5BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C",
    kinetics = ArrheniusBM(A=(4.30914e+07,'m^3/(mol*s)'), n=-7.5687e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.32890731525313555, var=0.22197044450561015, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_5R!H->C_Sp-5C-4CO_4CO->C
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
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C",
    kinetics = ArrheniusBM(A=(1.34165e+07,'m^3/(mol*s)'), n=-5.25438e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.5990137911088773e-17, var=0.6909863268735121, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C
    Total Standard Deviation in ln(k): 1.666447807467594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C
Total Standard Deviation in ln(k): 1.666447807467594""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C
Total Standard Deviation in ln(k): 1.666447807467594
""",
)

entry(
    index = 19,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->C",
    kinetics = ArrheniusBM(A=(5.12e+07,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(53142.9,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_N-4CO->C
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
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C_Sp-5O-4C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C_Sp-5O-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C_Sp-5O-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C_Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C_Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C_N-Sp-5O-4C",
    kinetics = ArrheniusBM(A=(1.8e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C_N-Sp-5O-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C_N-Sp-5O-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C_N-Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->N_N-4BrCClFHIOPSSi->H_Ext-4CO-R_N-5R!H->C_5BrClFINOPSSi->O_4CO->C_N-Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

