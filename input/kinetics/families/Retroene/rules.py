#!/usr/bin/env python
# encoding: utf-8

name = "Retroene/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(351.483,'s^-1'), n=2.72887, w0=(1.11181e+06,'J/mol'), E0=(141064,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13055717705123002, var=19.959654271360805, Tref=1000.0, N=68, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 68 training reactions at node Root
    Total Standard Deviation in ln(k): 9.284433424755495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 68 training reactions at node Root
Total Standard Deviation in ln(k): 9.284433424755495""",
    longDesc = 
"""
BM rule fitted to 68 training reactions at node Root
Total Standard Deviation in ln(k): 9.284433424755495
""",
)

entry(
    index = 2,
    label = "Root_1R!H->C",
    kinetics = ArrheniusBM(A=(1.75934e+14,'s^-1'), n=-0.752179, w0=(1.04926e+06,'J/mol'), E0=(177823,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09940871819346306, var=3.010161187748991, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_1R!H->C',), comment="""BM rule fitted to 31 training reactions at node Root_1R!H->C
    Total Standard Deviation in ln(k): 3.7279491413387"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 3.7279491413387""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 3.7279491413387
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H->C",
    kinetics = ArrheniusBM(A=(0.0523035,'s^-1'), n=3.89104, w0=(1.16422e+06,'J/mol'), E0=(117784,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.32245522758811473, var=39.144342334518626, Tref=1000.0, N=37, data_mean=0.0, correlation='Root_N-1R!H->C',), comment="""BM rule fitted to 37 training reactions at node Root_N-1R!H->C
    Total Standard Deviation in ln(k): 13.352902155690218"""),
    rank = 11,
    shortDesc = """BM rule fitted to 37 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 13.352902155690218""",
    longDesc = 
"""
BM rule fitted to 37 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 13.352902155690218
""",
)

entry(
    index = 4,
    label = "Root_1R!H->C_2R!H->C",
    kinetics = ArrheniusBM(A=(1.13656e+14,'s^-1'), n=-0.713758, w0=(1.0543e+06,'J/mol'), E0=(175246,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09769890056487542, var=2.561580468547625, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C',), comment="""BM rule fitted to 27 training reactions at node Root_1R!H->C_2R!H->C
    Total Standard Deviation in ln(k): 3.4540407270731786"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 3.4540407270731786""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 3.4540407270731786
""",
)

entry(
    index = 5,
    label = "Root_1R!H->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(4.66316e+09,'s^-1'), n=1.02661, w0=(1.01525e+06,'J/mol'), E0=(221066,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.6261064499336317, var=38.37240951049941, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-2R!H->C
    Total Standard Deviation in ln(k): 21.529245395988614"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 21.529245395988614""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 21.529245395988614
""",
)

entry(
    index = 6,
    label = "Root_N-1R!H->C_5R!H->N",
    kinetics = ArrheniusBM(A=(9.59135e+09,'s^-1'), n=0.736578, w0=(1.0955e+06,'J/mol'), E0=(70461.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H->C_N-5R!H->N",
    kinetics = ArrheniusBM(A=(4.02942e+10,'s^-1'), n=0.375329, w0=(1.16612e+06,'J/mol'), E0=(154169,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06684469846581474, var=24.965000021544366, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N',), comment="""BM rule fitted to 36 training reactions at node Root_N-1R!H->C_N-5R!H->N
    Total Standard Deviation in ln(k): 10.184607864683809"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_N-1R!H->C_N-5R!H->N
Total Standard Deviation in ln(k): 10.184607864683809""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_N-1R!H->C_N-5R!H->N
Total Standard Deviation in ln(k): 10.184607864683809
""",
)

entry(
    index = 8,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.46238e+12,'s^-1'), n=-0.158546, w0=(1.0845e+06,'J/mol'), E0=(176009,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09120859003038287, var=2.28830828228651, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 15 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.261761201768912"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.261761201768912""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.261761201768912
""",
)

entry(
    index = 9,
    label = "Root_1R!H->C_2R!H->C_5R!H->O",
    kinetics = ArrheniusBM(A=(3.94505e+09,'s^-1'), n=0.601596, w0=(1.0845e+06,'J/mol'), E0=(169425,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07591793873856297, var=4.052420941329839, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_5R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O
    Total Standard Deviation in ln(k): 4.226405752097704"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O
Total Standard Deviation in ln(k): 4.226405752097704""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O
Total Standard Deviation in ln(k): 4.226405752097704
""",
)

entry(
    index = 10,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->O",
    kinetics = ArrheniusBM(A=(1.32288e+18,'s^-1'), n=-2.21337, w0=(968000,'J/mol'), E0=(173278,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0927421085454212, var=3.278681656229481, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-5R!H->O',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O
    Total Standard Deviation in ln(k): 3.863020288060733"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O
Total Standard Deviation in ln(k): 3.863020288060733""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O
Total Standard Deviation in ln(k): 3.863020288060733
""",
)

entry(
    index = 11,
    label = "Root_1R!H->C_N-2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.8e+12,'s^-1'), n=0, w0=(1.0665e+06,'J/mol'), E0=(218338,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_1R!H->C_N-2R!H->C_2NOS->S",
    kinetics = ArrheniusBM(A=(5.6608e+10,'s^-1'), n=0, w0=(953500,'J/mol'), E0=(119669,'J/mol'), Tmin=(588,'K'), Tmax=(691,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_2NOS->S',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_2NOS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_2NOS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_2NOS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_1R!H->C_N-2R!H->C_N-2NOS->S",
    kinetics = ArrheniusBM(A=(3.11827e+11,'s^-1'), n=-0.293682, w0=(1.0205e+06,'J/mol'), E0=(160991,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.001642907944431047, var=4.049121298193099, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-2NOS->S',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S
    Total Standard Deviation in ln(k): 4.03814174042697"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S
Total Standard Deviation in ln(k): 4.03814174042697""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S
Total Standard Deviation in ln(k): 4.03814174042697
""",
)

entry(
    index = 14,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(4.82035e+06,'s^-1'), n=1.67734, w0=(1.17869e+06,'J/mol'), E0=(152460,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2285837836968013, var=2.96975919141528, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R',), comment="""BM rule fitted to 18 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R
    Total Standard Deviation in ln(k): 4.029088922385259"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.029088922385259""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.029088922385259
""",
)

entry(
    index = 15,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.42412e+12,'s^-1'), n=-0.284057, w0=(1.1575e+06,'J/mol'), E0=(165357,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11656939014923065, var=13.786674344573177, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 7.736551688175035"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 7.736551688175035""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 7.736551688175035
""",
)

entry(
    index = 16,
    label = "Root_N-1R!H->C_N-5R!H->N_N-1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(3.96843e+10,'s^-1'), n=0.78544, w0=(1.0865e+06,'J/mol'), E0=(108783,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_N-1BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_N-1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N",
    kinetics = ArrheniusBM(A=(1.03404e+08,'s^-1'), n=1.25673, w0=(1.0845e+06,'J/mol'), E0=(177221,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03936081494595298, var=1.4404859165336958, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N
    Total Standard Deviation in ln(k): 2.5049844677356727"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N
Total Standard Deviation in ln(k): 2.5049844677356727""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N
Total Standard Deviation in ln(k): 2.5049844677356727
""",
)

entry(
    index = 18,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N",
    kinetics = ArrheniusBM(A=(1.18472e+12,'s^-1'), n=-0.0115244, w0=(1.0845e+06,'J/mol'), E0=(169271,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07049718312528079, var=2.319532999988916, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N',), comment="""BM rule fitted to 10 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N
    Total Standard Deviation in ln(k): 3.230342756293489"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N
Total Standard Deviation in ln(k): 3.230342756293489""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N
Total Standard Deviation in ln(k): 3.230342756293489
""",
)

entry(
    index = 19,
    label = "Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(4.16228e+08,'s^-1'), n=0.988266, w0=(1.0845e+06,'J/mol'), E0=(162518,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0025626047091315556, var=9.251604624994211, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R
    Total Standard Deviation in ln(k): 6.104131234895419"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 6.104131234895419""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 6.104131234895419
""",
)

entry(
    index = 20,
    label = "Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(7.24523e+06,'s^-1'), n=1.35008, w0=(1.0845e+06,'J/mol'), E0=(171424,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.024461205742499107, var=5.078314475822991, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R
    Total Standard Deviation in ln(k): 4.579154043078822"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.579154043078822""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.579154043078822
""",
)

entry(
    index = 21,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.54595e+20,'s^-1'), n=-3.0326, w0=(968000,'J/mol'), E0=(170265,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12749579816800816, var=3.8667024035834454, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R
    Total Standard Deviation in ln(k): 4.2624387205240515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.2624387205240515""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.2624387205240515
""",
)

entry(
    index = 22,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-5C-R",
    kinetics = ArrheniusBM(A=(3.23333e+11,'s^-1'), n=0, w0=(968000,'J/mol'), E0=(182946,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->O",
    kinetics = ArrheniusBM(A=(4.1009e+10,'s^-1'), n=0, w0=(1.0665e+06,'J/mol'), E0=(167048,'J/mol'), Tmin=(725,'K'), Tmax=(810,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->O",
    kinetics = ArrheniusBM(A=(7.8141e+10,'s^-1'), n=0, w0=(974500,'J/mol'), E0=(160561,'J/mol'), Tmin=(602,'K'), Tmax=(694,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.39378e+10,'s^-1'), n=0.636142, w0=(1.183e+06,'J/mol'), E0=(153232,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0820842374791673, var=3.1024987137828046, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 3.737364386568372"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 3.737364386568372""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 3.737364386568372
""",
)

entry(
    index = 26,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_N-1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.15515e+06,'s^-1'), n=1.91844, w0=(1.1055e+06,'J/mol'), E0=(160816,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_N-1BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_N-1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_3R!H-inRing",
    kinetics = ArrheniusBM(A=(7.51733e+12,'s^-1'), n=-0.801522, w0=(1.0245e+06,'J/mol'), E0=(143090,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.010065863716581231, var=81.8360764684643, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_3R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_3R!H-inRing
    Total Standard Deviation in ln(k): 18.160785079462567"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_3R!H-inRing
Total Standard Deviation in ln(k): 18.160785079462567""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_3R!H-inRing
Total Standard Deviation in ln(k): 18.160785079462567
""",
)

entry(
    index = 28,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(5.71204e+08,'s^-1'), n=0.79256, w0=(1.17523e+06,'J/mol'), E0=(163842,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06341933757336864, var=14.689759202912304, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing
    Total Standard Deviation in ln(k): 7.842937637670613"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing
Total Standard Deviation in ln(k): 7.842937637670613""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing
Total Standard Deviation in ln(k): 7.842937637670613
""",
)

entry(
    index = 29,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(8.30743e+07,'s^-1'), n=1.34294, w0=(1.0845e+06,'J/mol'), E0=(186642,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.014692611028300074, var=6.989117524371048, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R
    Total Standard Deviation in ln(k): 5.336822036500276"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 5.336822036500276""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 5.336822036500276
""",
)

entry(
    index = 30,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R",
    kinetics = ArrheniusBM(A=(5.08779e+07,'s^-1'), n=1.30493, w0=(1.0845e+06,'J/mol'), E0=(168720,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00044315246718255245, var=0.04701835067671197, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R
    Total Standard Deviation in ln(k): 0.43581449398144884"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 0.43581449398144884""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 0.43581449398144884
""",
)

entry(
    index = 31,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.10319e+11,'s^-1'), n=0.204824, w0=(1.0845e+06,'J/mol'), E0=(175924,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.061353959294217005, var=3.4900972510040535, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R
    Total Standard Deviation in ln(k): 3.899362049801037"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.899362049801037""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.899362049801037
""",
)

entry(
    index = 32,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R",
    kinetics = ArrheniusBM(A=(9.59974e+09,'s^-1'), n=0.653804, w0=(1.0845e+06,'J/mol'), E0=(159613,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006151428258272596, var=1.8383731639583567, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R
    Total Standard Deviation in ln(k): 2.7336083899052577"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 2.7336083899052577""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 2.7336083899052577
""",
)

entry(
    index = 33,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFIOPSSi->O",
    kinetics = ArrheniusBM(A=(1.2535e+06,'s^-1'), n=1.80968, w0=(1.0845e+06,'J/mol'), E0=(155867,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFIOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFIOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFIOPSSi->O",
    kinetics = ArrheniusBM(A=(11.5839,'s^-1'), n=3.09547, w0=(1.0845e+06,'J/mol'), E0=(137668,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFIOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFIOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(21.2645,'s^-1'), n=2.97303, w0=(1.0845e+06,'J/mol'), E0=(145085,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(3.78363e+11,'s^-1'), n=0.169307, w0=(1.0845e+06,'J/mol'), E0=(163318,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(6.80655,'s^-1'), n=3.07798, w0=(1.0845e+06,'J/mol'), E0=(148263,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2419.21,'s^-1'), n=2.3826, w0=(1.0845e+06,'J/mol'), E0=(171107,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_5R!H->O_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.5405e+21,'s^-1'), n=-3.24953, w0=(968000,'J/mol'), E0=(163723,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12977356299501228, var=2.998907670868144, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 3.797735031217385"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 3.797735031217385""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 3.797735031217385
""",
)

entry(
    index = 40,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(7.30229e+08,'s^-1'), n=0.995367, w0=(1.183e+06,'J/mol'), E0=(138104,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9718999266707798, var=2.1443634364201256, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_Ext-2R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_Ext-2R!H-R
    Total Standard Deviation in ln(k): 5.377622526546486"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.377622526546486""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.377622526546486
""",
)

entry(
    index = 41,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_7R!H->O",
    kinetics = ArrheniusBM(A=(6.63512e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(94204,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_7R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O",
    kinetics = ArrheniusBM(A=(6.01185e+09,'s^-1'), n=0.754214, w0=(1.183e+06,'J/mol'), E0=(159151,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09510809546145511, var=0.3875877430471234, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O
    Total Standard Deviation in ln(k): 1.4870438652189866"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O
Total Standard Deviation in ln(k): 1.4870438652189866""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O
Total Standard Deviation in ln(k): 1.4870438652189866
""",
)

entry(
    index = 43,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_3R!H-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(550000,'s^-1'), n=0.9, w0=(1.0245e+06,'J/mol'), E0=(131295,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_3R!H-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_3R!H-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_3R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_3R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(9.86666e+06,'s^-1'), n=1.56749, w0=(1.183e+06,'J/mol'), E0=(173559,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.017669062395274753, var=0.3308386397993182, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 1.1974896656222527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.1974896656222527""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.1974896656222527
""",
)

entry(
    index = 45,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.01976e+11,'s^-1'), n=-0.0738756, w0=(1.183e+06,'J/mol'), E0=(160257,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0038772587838617587, var=47.426029943831864, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R
    Total Standard Deviation in ln(k): 13.815662571697391"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 13.815662571697391""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 13.815662571697391
""",
)

entry(
    index = 46,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_5CO->O",
    kinetics = ArrheniusBM(A=(3.96667e+10,'s^-1'), n=0.59, w0=(1.183e+06,'J/mol'), E0=(179850,'J/mol'), Tmin=(500,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_5CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_5CO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_5CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_5CO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_N-5CO->O",
    kinetics = ArrheniusBM(A=(3.33333e+07,'s^-1'), n=1.2, w0=(1.0665e+06,'J/mol'), E0=(165353,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_N-5CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_N-5CO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_N-5CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_N-5CO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_8R!H->C",
    kinetics = ArrheniusBM(A=(1708.21,'s^-1'), n=2.62955, w0=(1.0845e+06,'J/mol'), E0=(162976,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(85500.5,'s^-1'), n=2.19797, w0=(1.0845e+06,'J/mol'), E0=(186561,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(111514,'s^-1'), n=2.05353, w0=(1.0845e+06,'J/mol'), E0=(161295,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(6.3077e+06,'s^-1'), n=1.41637, w0=(1.0845e+06,'J/mol'), E0=(156860,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->O",
    kinetics = ArrheniusBM(A=(2.01084e+12,'s^-1'), n=0.0883205, w0=(1.0845e+06,'J/mol'), E0=(183925,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.021492990850914453, var=5.303057773824753, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->O
    Total Standard Deviation in ln(k): 4.670580394351897"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 4.670580394351897""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 4.670580394351897
""",
)

entry(
    index = 53,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->O",
    kinetics = ArrheniusBM(A=(9.58447e+09,'s^-1'), n=0.427548, w0=(1.0845e+06,'J/mol'), E0=(167154,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.023199101818381307, var=14.082287951603485, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->O
    Total Standard Deviation in ln(k): 7.581333161482922"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 7.581333161482922""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 7.581333161482922
""",
)

entry(
    index = 54,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(2.6009e+07,'s^-1'), n=1.28561, w0=(1.0845e+06,'J/mol'), E0=(152714,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0072034781886713035, var=1.112822940211039, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C
    Total Standard Deviation in ln(k): 2.1329027100545948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 2.1329027100545948""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 2.1329027100545948
""",
)

entry(
    index = 55,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(5.01614e+11,'s^-1'), n=0.272082, w0=(1.0845e+06,'J/mol'), E0=(164653,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0004677404420120619, var=2.2953718575893025, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 3.038446033140682"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 3.038446033140682""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 3.038446033140682
""",
)

entry(
    index = 56,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.84364e+21,'s^-1'), n=-3.37687, w0=(968000,'J/mol'), E0=(155107,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12158036022019265, var=4.26315521405602, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 4.4447369115914395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 4.4447369115914395""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 4.4447369115914395
""",
)

entry(
    index = 57,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_Ext-2R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.45626e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(142579,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_Ext-2R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_Ext-2R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_Ext-2R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_Ext-2R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_Ext-2R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.82163e+08,'s^-1'), n=0.989298, w0=(1.183e+06,'J/mol'), E0=(138899,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9397855924827363, var=2.0052075611816607, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_Ext-2R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_Ext-2R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 5.200082488575585"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 5.200082488575585""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 5.200082488575585
""",
)

entry(
    index = 59,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R",
    kinetics = ArrheniusBM(A=(8.60674e+08,'s^-1'), n=0.975857, w0=(1.183e+06,'J/mol'), E0=(154165,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.810653195545372, var=2.4765646224643563, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R
    Total Standard Deviation in ln(k): 5.191689641779036"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R
Total Standard Deviation in ln(k): 5.191689641779036""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R
Total Standard Deviation in ln(k): 5.191689641779036
""",
)

entry(
    index = 60,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.09881e+10,'s^-1'), n=0.632458, w0=(1.183e+06,'J/mol'), E0=(164532,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.140869378589362, var=0.05370776408169411, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-4R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.8185392257471298"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.8185392257471298""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.8185392257471298
""",
)

entry(
    index = 61,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.32388e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(156130,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(4.72908e+06,'s^-1'), n=1.66491, w0=(1.183e+06,'J/mol'), E0=(172562,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.062098400931787215, var=0.15842678078199102, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 0.9539680653938947"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 0.9539680653938947""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C
Total Standard Deviation in ln(k): 0.9539680653938947
""",
)

entry(
    index = 63,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(5.40789e+14,'s^-1'), n=-0.823434, w0=(1.183e+06,'J/mol'), E0=(200846,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.3172441301014085e-15, var=0.04558127893527205, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 0.4280063799185306"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 0.4280063799185306""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 0.4280063799185306
""",
)

entry(
    index = 64,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(6.72258e+12,'s^-1'), n=-0.0948649, w0=(1.183e+06,'J/mol'), E0=(172576,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0053888710926292245, var=0.5959934258564467, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 1.5612075953824893"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C
Total Standard Deviation in ln(k): 1.5612075953824893""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C
Total Standard Deviation in ln(k): 1.5612075953824893
""",
)

entry(
    index = 65,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(58002.5,'s^-1'), n=0.286, w0=(1.183e+06,'J/mol'), E0=(125149,'J/mol'), Tmin=(500,'K'), Tmax=(1300,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->O_8R!H->C",
    kinetics = ArrheniusBM(A=(6.1395e+07,'s^-1'), n=1.36832, w0=(1.0845e+06,'J/mol'), E0=(163924,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->O_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->O_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->O_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->O_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->O_N-8R!H->C",
    kinetics = ArrheniusBM(A=(2.87851e+08,'s^-1'), n=1.30992, w0=(1.0845e+06,'J/mol'), E0=(187582,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->O_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->O_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->O_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_7BrCClFIOPSSi->O_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->O_8R!H->C",
    kinetics = ArrheniusBM(A=(459.236,'s^-1'), n=2.68918, w0=(1.0845e+06,'J/mol'), E0=(145855,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->O_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->O_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->O_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->O_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->O_N-8R!H->C",
    kinetics = ArrheniusBM(A=(6552.1,'s^-1'), n=2.29082, w0=(1.0845e+06,'J/mol'), E0=(167773,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->O_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->O_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->O_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4R!H-R_N-7BrCClFIOPSSi->O_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFIOPSSi->O",
    kinetics = ArrheniusBM(A=(1.65185e+07,'s^-1'), n=1.51788, w0=(1.0845e+06,'J/mol'), E0=(159604,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFIOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFIOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFIOPSSi->O",
    kinetics = ArrheniusBM(A=(1017.11,'s^-1'), n=2.55399, w0=(1.0845e+06,'J/mol'), E0=(143955,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFIOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFIOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFIOPSSi->O",
    kinetics = ArrheniusBM(A=(8.27867e+08,'s^-1'), n=1.04991, w0=(1.0845e+06,'J/mol'), E0=(160247,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFIOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFIOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFIOPSSi->O",
    kinetics = ArrheniusBM(A=(2.0173e+12,'s^-1'), n=0.0499164, w0=(1.0845e+06,'J/mol'), E0=(158672,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFIOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFIOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.34275e+16,'s^-1'), n=-2.11924, w0=(968000,'J/mol'), E0=(122130,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0013608568101268583, var=1.6674726433047609, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 2.5921468035711666"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.5921468035711666""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.5921468035711666
""",
)

entry(
    index = 75,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.39881e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(136330,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.2598e+13,'s^-1'), n=-0.459377, w0=(1.183e+06,'J/mol'), E0=(156365,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0006121978434024415, var=0.049410262461096775, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.4471591044090268"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.4471591044090268""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.4471591044090268
""",
)

entry(
    index = 77,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.2699e+13,'s^-1'), n=-0.442692, w0=(1.183e+06,'J/mol'), E0=(141989,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008973758145679172, var=1.7601354275190648, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 2.682231075380441"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.682231075380441""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.682231075380441
""",
)

entry(
    index = 78,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(2.4107e+13,'s^-1'), n=-0.432391, w0=(1.183e+06,'J/mol'), E0=(160784,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0010628098785811556, var=0.16224599752348345, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 0.8101730807390738"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.8101730807390738""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.8101730807390738
""",
)

entry(
    index = 79,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_7C-inRing",
    kinetics = ArrheniusBM(A=(7.92445e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(165471,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_7C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing",
    kinetics = ArrheniusBM(A=(3.93467e+06,'s^-1'), n=1.69077, w0=(1.183e+06,'J/mol'), E0=(172691,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.047594001962377265, var=0.10410275187919844, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing
    Total Standard Deviation in ln(k): 0.7664098514942174"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing
Total Standard Deviation in ln(k): 0.7664098514942174""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing
Total Standard Deviation in ln(k): 0.7664098514942174
""",
)

entry(
    index = 81,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(7.92445e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(193178,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R",
    kinetics = ArrheniusBM(A=(6.26357e+11,'s^-1'), n=0.219784, w0=(1.183e+06,'J/mol'), E0=(170925,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.6694644050553874e-15, var=2.116729755416145, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R
    Total Standard Deviation in ln(k): 2.9166861328622327"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 2.9166861328622327""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 2.9166861328622327
""",
)

entry(
    index = 83,
    label = "Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(6.5e+10,'s^-1'), n=0, w0=(968000,'J/mol'), E0=(139431,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_2R!H->C_N-5R!H->O_Ext-4R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_7C-inRing",
    kinetics = ArrheniusBM(A=(1.25594e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(155092,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_7C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_N-7C-inRing",
    kinetics = ArrheniusBM(A=(1.98582e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(160232,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_N-7C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_N-7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-4R!H-R_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.32702e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(116943,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 87,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(8.37297e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(151179,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(8.84721e+12,'s^-1'), n=-0.302094, w0=(1.183e+06,'J/mol'), E0=(150154,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.255606157999161e-05, var=0.017017844750293856, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 0.2616044249499389"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 0.2616044249499389""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 0.2616044249499389
""",
)

entry(
    index = 89,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H",
    kinetics = ArrheniusBM(A=(1.11936e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(158970,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H",
    kinetics = ArrheniusBM(A=(1.99054e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(166153,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-4R!H-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R",
    kinetics = ArrheniusBM(A=(139248,'s^-1'), n=2.06526, w0=(1.183e+06,'J/mol'), E0=(165686,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6647699949854299, var=1.1672292911792304, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R
    Total Standard Deviation in ln(k): 3.8361597962833978"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R
Total Standard Deviation in ln(k): 3.8361597962833978""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R
Total Standard Deviation in ln(k): 3.8361597962833978
""",
)

entry(
    index = 92,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.16053e+06,'s^-1'), n=1.87467, w0=(1.183e+06,'J/mol'), E0=(182477,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(6.96433e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(174127,'J/mol'), Tmin=(900,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing",
    kinetics = ArrheniusBM(A=(1.32702e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(152192,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing",
    kinetics = ArrheniusBM(A=(1.32702e+12,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(151418,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O_N-7R!H->O_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(7.94328e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(172170,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 97,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R",
    kinetics = ArrheniusBM(A=(7.92445e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(170162,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(7.92445e+11,'s^-1'), n=0, w0=(1.183e+06,'J/mol'), E0=(168938,'J/mol'), Tmin=(500,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-5R!H->N_1BrClFINOPSSi->O_N-3R!H-inRing_Ext-4R!H-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

