#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Exocyclic/rules"
shortDesc = ""
longDesc = """
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')
"""
entry(
    index = 0,
    label = "Root",
    kinetics = ArrheniusBM(A=(0.0020548,'s^-1'), n=4.08615, w0=(298536,'J/mol'), E0=(33139.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2567177210013423, var=31.29233349131318, Tref=1000.0, N=374, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 374 training reactions at node Root
    Total Standard Deviation in ln(k): 11.85941737946586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 374 training reactions at node Root
Total Standard Deviation in ln(k): 11.85941737946586""",
    longDesc = 
"""
BM rule fitted to 374 training reactions at node Root
Total Standard Deviation in ln(k): 11.85941737946586
""",
)

entry(
    index = 1,
    label = "Backbone1_Sp-4R!H=1R!H",
    kinetics = ArrheniusBM(A=(10913.5,'s^-1'), n=2.37603, w0=(301000,'J/mol'), E0=(-6647.57,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3197344302163777, var=8.442027167455935, Tref=1000.0, N=69, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H',), comment="""BM rule fitted to 69 training reactions at node Backbone1_Sp-4R!H=1R!H
    Total Standard Deviation in ln(k): 6.628144042535227"""),
    rank = 11,
    shortDesc = """BM rule fitted to 69 training reactions at node Backbone1_Sp-4R!H=1R!H
Total Standard Deviation in ln(k): 6.628144042535227""",
    longDesc = 
"""
BM rule fitted to 69 training reactions at node Backbone1_Sp-4R!H=1R!H
Total Standard Deviation in ln(k): 6.628144042535227
""",
)

entry(
    index = 2,
    label = "Backbone1_N-Sp-4R!H=1R!H",
    kinetics = ArrheniusBM(A=(3.36241e+17,'s^-1'), n=-1.39821, w0=(263467,'J/mol'), E0=(69969.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19505543961688857, var=3.9202767307107353, Tref=1000.0, N=15, data_mean=0.0, correlation='Backbone1_N-Sp-4R!H=1R!H',), comment="""BM rule fitted to 15 training reactions at node Backbone1_N-Sp-4R!H=1R!H
    Total Standard Deviation in ln(k): 4.459402092400199"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Backbone1_N-Sp-4R!H=1R!H
Total Standard Deviation in ln(k): 4.459402092400199""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Backbone1_N-Sp-4R!H=1R!H
Total Standard Deviation in ln(k): 4.459402092400199
""",
)

entry(
    index = 3,
    label = "Backbone2_Sp-3R!H=1R!H",
    kinetics = ArrheniusBM(A=(1e+10,'s^-1'), n=0, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_Sp-3R!H=1R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone2_Sp-3R!H=1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_Sp-3R!H=1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_Sp-3R!H=1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Backbone2_N-Sp-3R!H=1R!H",
    kinetics = ArrheniusBM(A=(2.30474e+07,'s^-1'), n=1.25423, w0=(299932,'J/mol'), E0=(54385.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.044600886996416, var=2.977542237062531, Tref=1000.0, N=73, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H',), comment="""BM rule fitted to 73 training reactions at node Backbone2_N-Sp-3R!H=1R!H
    Total Standard Deviation in ln(k): 3.571344432407959"""),
    rank = 11,
    shortDesc = """BM rule fitted to 73 training reactions at node Backbone2_N-Sp-3R!H=1R!H
Total Standard Deviation in ln(k): 3.571344432407959""",
    longDesc = 
"""
BM rule fitted to 73 training reactions at node Backbone2_N-Sp-3R!H=1R!H
Total Standard Deviation in ln(k): 3.571344432407959
""",
)

entry(
    index = 5,
    label = "Backbone3_Sp-2R!H=1R!H",
    kinetics = ArrheniusBM(A=(3.93569e-41,'s^-1'), n=14.9828, w0=(285083,'J/mol'), E0=(3592.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.793163867707345, var=372.86333950066455, Tref=1000.0, N=6, data_mean=0.0, correlation='Backbone3_Sp-2R!H=1R!H',), comment="""BM rule fitted to 6 training reactions at node Backbone3_Sp-2R!H=1R!H
    Total Standard Deviation in ln(k): 53.266460060732996"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Backbone3_Sp-2R!H=1R!H
Total Standard Deviation in ln(k): 53.266460060732996""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Backbone3_Sp-2R!H=1R!H
Total Standard Deviation in ln(k): 53.266460060732996
""",
)

entry(
    index = 6,
    label = "Backbone3_N-Sp-2R!H=1R!H",
    kinetics = ArrheniusBM(A=(1.75999e+16,'s^-1'), n=-1.47613, w0=(300287,'J/mol'), E0=(91038.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.291972445091156, var=15.035434705198913, Tref=1000.0, N=134, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H',), comment="""BM rule fitted to 134 training reactions at node Backbone3_N-Sp-2R!H=1R!H
    Total Standard Deviation in ln(k): 8.507070129478414"""),
    rank = 11,
    shortDesc = """BM rule fitted to 134 training reactions at node Backbone3_N-Sp-2R!H=1R!H
Total Standard Deviation in ln(k): 8.507070129478414""",
    longDesc = 
"""
BM rule fitted to 134 training reactions at node Backbone3_N-Sp-2R!H=1R!H
Total Standard Deviation in ln(k): 8.507070129478414
""",
)

entry(
    index = 7,
    label = "Backbone4_Sp-5R!H-2R!H",
    kinetics = ArrheniusBM(A=(418599,'s^-1'), n=1.25542, w0=(299727,'J/mol'), E0=(61515.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11674955006940649, var=5.065014140634441, Tref=1000.0, N=66, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H',), comment="""BM rule fitted to 66 training reactions at node Backbone4_Sp-5R!H-2R!H
    Total Standard Deviation in ln(k): 4.805114404491737"""),
    rank = 11,
    shortDesc = """BM rule fitted to 66 training reactions at node Backbone4_Sp-5R!H-2R!H
Total Standard Deviation in ln(k): 4.805114404491737""",
    longDesc = 
"""
BM rule fitted to 66 training reactions at node Backbone4_Sp-5R!H-2R!H
Total Standard Deviation in ln(k): 4.805114404491737
""",
)

entry(
    index = 8,
    label = "Backbone4_N-Sp-5R!H-2R!H",
    kinetics = ArrheniusBM(A=(749672,'s^-1'), n=1.66937, w0=(300389,'J/mol'), E0=(99832.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18073698559408868, var=12.353557890520888, Tref=1000.0, N=9, data_mean=0.0, correlation='Backbone4_N-Sp-5R!H-2R!H',), comment="""BM rule fitted to 9 training reactions at node Backbone4_N-Sp-5R!H-2R!H
    Total Standard Deviation in ln(k): 7.500281402899942"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Backbone4_N-Sp-5R!H-2R!H
Total Standard Deviation in ln(k): 7.500281402899942""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Backbone4_N-Sp-5R!H-2R!H
Total Standard Deviation in ln(k): 7.500281402899942
""",
)

entry(
    index = 9,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.06161e+19,'s^-1'), n=-1.86572, w0=(301000,'J/mol'), E0=(47750.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.49403718031912697, var=3.103579123214929, Tref=1000.0, N=44, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R',), comment="""BM rule fitted to 44 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 4.773036814755078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 44 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.773036814755078""",
    longDesc = 
"""
BM rule fitted to 44 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.773036814755078
""",
)

entry(
    index = 10,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(15940.8,'s^-1'), n=2.2802, w0=(301000,'J/mol'), E0=(-10045.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.8266327752959066, var=34.21558582618729, Tref=1000.0, N=11, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R',), comment="""BM rule fitted to 11 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 18.828607834880962"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 18.828607834880962""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 18.828607834880962
""",
)

entry(
    index = 11,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.25433e+06,'s^-1'), n=1.76828, w0=(301000,'J/mol'), E0=(11514.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09787770320324662, var=3.6226158776236295, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 4.061570375593237"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.061570375593237""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.061570375593237
""",
)

entry(
    index = 12,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(8.52e+08,'s^-1'), n=0.89, w0=(301000,'J/mol'), E0=(27513.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H",
    kinetics = ArrheniusBM(A=(5.58438e+11,'s^-1'), n=0.208491, w0=(266444,'J/mol'), E0=(54660.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06228064242978371, var=2.5487563791983914, Tref=1000.0, N=9, data_mean=0.0, correlation='Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H',), comment="""BM rule fitted to 9 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H
    Total Standard Deviation in ln(k): 3.3570084984147375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H
Total Standard Deviation in ln(k): 3.3570084984147375""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H
Total Standard Deviation in ln(k): 3.3570084984147375
""",
)

entry(
    index = 14,
    label = "Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H",
    kinetics = ArrheniusBM(A=(6.15689e+20,'s^-1'), n=-2.25685, w0=(259000,'J/mol'), E0=(79140.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2476913364880919, var=7.837909023260463, Tref=1000.0, N=6, data_mean=0.0, correlation='Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H',), comment="""BM rule fitted to 6 training reactions at node Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H
    Total Standard Deviation in ln(k): 6.234849662782468"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H
Total Standard Deviation in ln(k): 6.234849662782468""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H
Total Standard Deviation in ln(k): 6.234849662782468
""",
)

entry(
    index = 15,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.12775e+09,'s^-1'), n=0.806211, w0=(299174,'J/mol'), E0=(57796.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15654166287080606, var=4.3217732387615575, Tref=1000.0, N=46, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R',), comment="""BM rule fitted to 46 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 4.560939454721064"""),
    rank = 11,
    shortDesc = """BM rule fitted to 46 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.560939454721064""",
    longDesc = 
"""
BM rule fitted to 46 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.560939454721064
""",
)

entry(
    index = 16,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.9105e+06,'s^-1'), n=1.40015, w0=(301000,'J/mol'), E0=(53631.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05769489231401571, var=8.7672953073919, Tref=1000.0, N=9, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R',), comment="""BM rule fitted to 9 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 6.080906202452237"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 6.080906202452237""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 6.080906202452237
""",
)

entry(
    index = 17,
    label = "Backbone2_N-Sp-3R!H=1R!H_1R!H-inRing",
    kinetics = ArrheniusBM(A=(4.713e+10,'s^-1'), n=0.481, w0=(301000,'J/mol'), E0=(71883.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(1170.09,'s^-1'), n=2.45582, w0=(301353,'J/mol'), E0=(43039.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05746961799775472, var=3.19047794699412, Tref=1000.0, N=17, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing',), comment="""BM rule fitted to 17 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing
    Total Standard Deviation in ln(k): 3.7252355861114426"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing
Total Standard Deviation in ln(k): 3.7252355861114426""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing
Total Standard Deviation in ln(k): 3.7252355861114426
""",
)

entry(
    index = 19,
    label = "Backbone3_Sp-2R!H=1R!H_3R!H-inRing",
    kinetics = ArrheniusBM(A=(2.84704e+10,'s^-1'), n=0.407843, w0=(259000,'J/mol'), E0=(65064.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.6645352591003792e-15, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_Sp-2R!H=1R!H_3R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Backbone3_Sp-2R!H=1R!H_3R!H-inRing
    Total Standard Deviation in ln(k): 6.694812208794923e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_Sp-2R!H=1R!H_3R!H-inRing
Total Standard Deviation in ln(k): 6.694812208794923e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_Sp-2R!H=1R!H_3R!H-inRing
Total Standard Deviation in ln(k): 6.694812208794923e-15
""",
)

entry(
    index = 20,
    label = "Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(2.3252e+10,'s^-1'), n=0.454315, w0=(298125,'J/mol'), E0=(263935,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.2636091769821403, var=44.288653107665674, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing',), comment="""BM rule fitted to 4 training reactions at node Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing
    Total Standard Deviation in ln(k): 19.028916169669117"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing
Total Standard Deviation in ln(k): 19.028916169669117""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing
Total Standard Deviation in ln(k): 19.028916169669117
""",
)

entry(
    index = 21,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H",
    kinetics = ArrheniusBM(A=(3.10316e+13,'s^-1'), n=-0.783809, w0=(299709,'J/mol'), E0=(68097.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21353465980451758, var=1.3677056902374396, Tref=1000.0, N=74, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H',), comment="""BM rule fitted to 74 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H
    Total Standard Deviation in ln(k): 2.881035868714586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 74 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H
Total Standard Deviation in ln(k): 2.881035868714586""",
    longDesc = 
"""
BM rule fitted to 74 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H
Total Standard Deviation in ln(k): 2.881035868714586
""",
)

entry(
    index = 22,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H",
    kinetics = ArrheniusBM(A=(2.12134e+12,'s^-1'), n=-0.112792, w0=(301000,'J/mol'), E0=(118782,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10501157002249409, var=57.132827740420815, Tref=1000.0, N=60, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H',), comment="""BM rule fitted to 60 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H
    Total Standard Deviation in ln(k): 15.416890942133504"""),
    rank = 11,
    shortDesc = """BM rule fitted to 60 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H
Total Standard Deviation in ln(k): 15.416890942133504""",
    longDesc = 
"""
BM rule fitted to 60 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H
Total Standard Deviation in ln(k): 15.416890942133504
""",
)

entry(
    index = 23,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(3.93286e+06,'s^-1'), n=0.974575, w0=(299688,'J/mol'), E0=(63433,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15277748886155745, var=4.360386141744415, Tref=1000.0, N=64, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H',), comment="""BM rule fitted to 64 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 4.570058134849762"""),
    rank = 11,
    shortDesc = """BM rule fitted to 64 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 4.570058134849762""",
    longDesc = 
"""
BM rule fitted to 64 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 4.570058134849762
""",
)

entry(
    index = 24,
    label = "Backbone4_Sp-5R!H-2R!H_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(1.33261e+11,'s^-1'), n=0.184149, w0=(301000,'J/mol'), E0=(199378,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.554703876831384, var=255.15095993332153, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 53.516757271189604"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 53.516757271189604""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 53.516757271189604
""",
)

entry(
    index = 25,
    label = "Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(2.23513e+10,'s^-1'), n=0.463786, w0=(301857,'J/mol'), E0=(113268,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08450609420467824, var=13.863788001181506, Tref=1000.0, N=7, data_mean=0.0, correlation='Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H',), comment="""BM rule fitted to 7 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 7.676779112375474"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 7.676779112375474""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 7.676779112375474
""",
)

entry(
    index = 26,
    label = "Backbone4_N-Sp-5R!H-2R!H_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(6.2251e+16,'s^-1'), n=-1.96433, w0=(295250,'J/mol'), E0=(113272,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-9.265726051782504, var=384.15931340395673, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone4_N-Sp-5R!H-2R!H_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone4_N-Sp-5R!H-2R!H_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 62.573491126634735"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone4_N-Sp-5R!H-2R!H_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 62.573491126634735""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone4_N-Sp-5R!H-2R!H_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 62.573491126634735
""",
)

entry(
    index = 27,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.08149e+13,'s^-1'), n=-0.212456, w0=(301000,'J/mol'), E0=(36210.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07458405659496045, var=1.0584748032894722, Tref=1000.0, N=28, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 28 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 2.249912772064937"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.249912772064937""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.249912772064937
""",
)

entry(
    index = 28,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.41068e+22,'s^-1'), n=-2.68765, w0=(301000,'J/mol'), E0=(41498,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2512204761702186, var=0.8564290054134424, Tref=1000.0, N=12, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 12 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.486458221465853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.486458221465853""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.486458221465853
""",
)

entry(
    index = 29,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.64477e+07,'s^-1'), n=1.43279, w0=(301000,'J/mol'), E0=(18863.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.4137206761135945, var=4.541200809277449, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 7.824171175430521"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 7.824171175430521""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 7.824171175430521
""",
)

entry(
    index = 30,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.50332e+13,'s^-1'), n=-0.379232, w0=(301000,'J/mol'), E0=(53716.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.472827584500098, var=60.86667793033365, Tref=1000.0, N=7, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 7 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 24.366059021469706"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 24.366059021469706""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 24.366059021469706
""",
)

entry(
    index = 31,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.8565e+08,'s^-1'), n=1.2092, w0=(301000,'J/mol'), E0=(21841,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3984913043232801, var=0.1674976106506139, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.8217017721514084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.8217017721514084""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.8217017721514084
""",
)

entry(
    index = 32,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_Sp-3R!H-2R!H",
    kinetics = ArrheniusBM(A=(8.09677e+13,'s^-1'), n=-0.528193, w0=(301000,'J/mol'), E0=(27010.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09347253615071249, var=1.1474635620768345, Tref=1000.0, N=3, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_Sp-3R!H-2R!H',), comment="""BM rule fitted to 3 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_Sp-3R!H-2R!H
    Total Standard Deviation in ln(k): 2.382322333143214"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_Sp-3R!H-2R!H
Total Standard Deviation in ln(k): 2.382322333143214""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_Sp-3R!H-2R!H
Total Standard Deviation in ln(k): 2.382322333143214
""",
)

entry(
    index = 33,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_N-Sp-3R!H-2R!H",
    kinetics = ArrheniusBM(A=(2.54e+10,'s^-1'), n=0.69, w0=(301000,'J/mol'), E0=(53221.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_N-Sp-3R!H-2R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_N-Sp-3R!H-2R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_N-Sp-3R!H-2R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_N-Sp-3R!H-2R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.48903e+09,'s^-1'), n=0.90916, w0=(266625,'J/mol'), E0=(46750.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15269322097800286, var=8.408288325045906, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 6.196791373184827"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.196791373184827""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.196791373184827
""",
)

entry(
    index = 35,
    label = "Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.31702e+10,'s^-1'), n=0.640594, w0=(260500,'J/mol'), E0=(53373.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.021789919562598, var=0.4678341992788073, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing',), comment="""BM rule fitted to 4 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing
    Total Standard Deviation in ln(k): 1.4259553863214343"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing
Total Standard Deviation in ln(k): 1.4259553863214343""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing
Total Standard Deviation in ln(k): 1.4259553863214343
""",
)

entry(
    index = 36,
    label = "Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(8.443e+10,'s^-1'), n=0.474, w0=(289500,'J/mol'), E0=(43573.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_N-1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_N-1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(0.000188337,'s^-1'), n=4.8063, w0=(259000,'J/mol'), E0=(-38513.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.017472284481237308, var=32.570319773942586, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.48500598456916"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.48500598456916""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.48500598456916
""",
)

entry(
    index = 38,
    label = "Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.44163e+11,'s^-1'), n=0.436872, w0=(259000,'J/mol'), E0=(54069.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0006592123094507745, var=0.9216470842205743, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.926251148187319"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.926251148187319""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.926251148187319
""",
)

entry(
    index = 39,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2.27635e+06,'s^-1'), n=1.20282, w0=(259000,'J/mol'), E0=(50810.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.72129e+08,'s^-1'), n=1.18271, w0=(299552,'J/mol'), E0=(57950.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24226749500492925, var=1.3465636789642512, Tref=1000.0, N=29, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 29 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 2.9350375643236055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.9350375643236055""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.9350375643236055
""",
)

entry(
    index = 41,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.35716e+13,'s^-1'), n=-0.0812523, w0=(301000,'J/mol'), E0=(61480.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05032393189232418, var=0.7072572128493868, Tref=1000.0, N=12, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 12 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 1.8123958884516396"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.8123958884516396""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.8123958884516396
""",
)

entry(
    index = 42,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(34212.8,'s^-1'), n=1.96906, w0=(301000,'J/mol'), E0=(43009.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2531813912948866, var=3.5683821790906824, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 6.935673987813629"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.935673987813629""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.935673987813629
""",
)

entry(
    index = 43,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.3387e+12,'s^-1'), n=-0.189849, w0=(301000,'J/mol'), E0=(83280.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.019055664978612, var=23.51695280309779, Tref=1000.0, N=5, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 5 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 17.30738559538069"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 17.30738559538069""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 17.30738559538069
""",
)

entry(
    index = 44,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4080,'s^-1'), n=2.33335, w0=(301000,'J/mol'), E0=(34944.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1150155255466325, var=2.824914554736722, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 6.171001445011375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 6.171001445011375""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 6.171001445011375
""",
)

entry(
    index = 45,
    label = "Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C",
    kinetics = ArrheniusBM(A=(27917.2,'s^-1'), n=2.04123, w0=(301000,'J/mol'), E0=(42708.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.009352805687208449, var=1.6815920192771276, Tref=1000.0, N=16, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C',), comment="""BM rule fitted to 16 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C
    Total Standard Deviation in ln(k): 2.623164038872463"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C
Total Standard Deviation in ln(k): 2.623164038872463""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C
Total Standard Deviation in ln(k): 2.623164038872463
""",
)

entry(
    index = 46,
    label = "Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_N-4R!H->C",
    kinetics = ArrheniusBM(A=(2.724e+10,'s^-1'), n=0.478, w0=(307000,'J/mol'), E0=(104963,'J/mol'), Tmin=(600,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing_4R!H-inRing",
    kinetics = ArrheniusBM(A=(2.992e+11,'s^-1'), n=0.67, w0=(289500,'J/mol'), E0=(28950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing_4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing_4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(2.70375e+32,'s^-1'), n=-6.3765, w0=(301000,'J/mol'), E0=(270815,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=18.864417623968293, var=829.5742977147573, Tref=1000.0, N=3, data_mean=0.0, correlation='Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing_N-4R!H-inRing',), comment="""BM rule fitted to 3 training reactions at node Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing_N-4R!H-inRing
    Total Standard Deviation in ln(k): 105.13907842604121"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing_N-4R!H-inRing
Total Standard Deviation in ln(k): 105.13907842604121""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing_N-4R!H-inRing
Total Standard Deviation in ln(k): 105.13907842604121
""",
)

entry(
    index = 49,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.11696e+08,'s^-1'), n=0.630287, w0=(300067,'J/mol'), E0=(57150.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1361235808842085, var=0.9383010107667864, Tref=1000.0, N=45, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R',), comment="""BM rule fitted to 45 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 2.283924501452803"""),
    rank = 11,
    shortDesc = """BM rule fitted to 45 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.283924501452803""",
    longDesc = 
"""
BM rule fitted to 45 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.283924501452803
""",
)

entry(
    index = 50,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(199.593,'s^-1'), n=2.40238, w0=(296333,'J/mol'), E0=(36427.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09374319157856256, var=0.08917176550331497, Tref=1000.0, N=9, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R',), comment="""BM rule fitted to 9 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 0.8341824664396189"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.8341824664396189""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.8341824664396189
""",
)

entry(
    index = 51,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_1R!H-inRing",
    kinetics = ArrheniusBM(A=(196017,'s^-1'), n=1.88276, w0=(295250,'J/mol'), E0=(29525,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.5358242832497362, var=1.316646002880678, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_1R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_1R!H-inRing
    Total Standard Deviation in ln(k): 6.159192178949002"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_1R!H-inRing
Total Standard Deviation in ln(k): 6.159192178949002""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_1R!H-inRing
Total Standard Deviation in ln(k): 6.159192178949002
""",
)

entry(
    index = 52,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(2.13915e+06,'s^-1'), n=1.21071, w0=(301000,'J/mol'), E0=(46833.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05054861662160608, var=1.0265850540293897, Tref=1000.0, N=18, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing',), comment="""BM rule fitted to 18 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing
    Total Standard Deviation in ln(k): 2.1582148532266796"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing
Total Standard Deviation in ln(k): 2.1582148532266796""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing
Total Standard Deviation in ln(k): 2.1582148532266796
""",
)

entry(
    index = 53,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.55506e+10,'s^-1'), n=0.694175, w0=(301000,'J/mol'), E0=(105595,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.048612293980556255, var=1.196464785779032, Tref=1000.0, N=44, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R',), comment="""BM rule fitted to 44 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 2.3149814688040977"""),
    rank = 11,
    shortDesc = """BM rule fitted to 44 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.3149814688040977""",
    longDesc = 
"""
BM rule fitted to 44 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.3149814688040977
""",
)

entry(
    index = 54,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(9.63265e+08,'s^-1'), n=0.782425, w0=(301000,'J/mol'), E0=(102557,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0190204554368931, var=3.6177411753009525, Tref=1000.0, N=6, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R',), comment="""BM rule fitted to 6 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 3.8608684979158"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.8608684979158""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.8608684979158
""",
)

entry(
    index = 55,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.55008e-05,'s^-1'), n=3.88153, w0=(273000,'J/mol'), E0=(29962.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17154732911826479, var=7.530104082740153, Tref=1000.0, N=3, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-4R!H-R',), comment="""BM rule fitted to 3 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 5.9322240058338"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 5.9322240058338""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 5.9322240058338
""",
)

entry(
    index = 56,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5.16142e+06,'s^-1'), n=1.09899, w0=(301000,'J/mol'), E0=(66167.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.37962540689349733, var=4.754570143717217, Tref=1000.0, N=44, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R',), comment="""BM rule fitted to 44 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 5.325152871072694"""),
    rank = 11,
    shortDesc = """BM rule fitted to 44 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 5.325152871072694""",
    longDesc = 
"""
BM rule fitted to 44 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 5.325152871072694
""",
)

entry(
    index = 57,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(2.0908e+06,'s^-1'), n=1.03171, w0=(301000,'J/mol'), E0=(61430,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2773119666625037, var=1.1946986637981478, Tref=1000.0, N=8, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R',), comment="""BM rule fitted to 8 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 2.8879847200864197"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.8879847200864197""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.8879847200864197
""",
)

entry(
    index = 58,
    label = "Backbone4_Sp-5R!H-2R!H_N-Sp-2R!H-1R!H_1R!H-inRing",
    kinetics = ArrheniusBM(A=(1e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(211407,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_N-Sp-2R!H-1R!H_1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_N-Sp-2R!H-1R!H_1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_N-Sp-2R!H-1R!H_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_N-Sp-2R!H-1R!H_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Backbone4_Sp-5R!H-2R!H_N-Sp-2R!H-1R!H_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(1e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_N-Sp-2R!H-1R!H_N-1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_N-Sp-2R!H-1R!H_N-1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_N-Sp-2R!H-1R!H_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_N-Sp-2R!H-1R!H_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_3R!H-inRing",
    kinetics = ArrheniusBM(A=(6.69e+11,'s^-1'), n=0.22, w0=(301000,'J/mol'), E0=(166035,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_3R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_3R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(1.61599e+09,'s^-1'), n=0.7619, w0=(302000,'J/mol'), E0=(102104,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06886151332487789, var=9.580474939628678, Tref=1000.0, N=6, data_mean=0.0, correlation='Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing',), comment="""BM rule fitted to 6 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing
    Total Standard Deviation in ln(k): 6.378143511677608"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing
Total Standard Deviation in ln(k): 6.378143511677608""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing
Total Standard Deviation in ln(k): 6.378143511677608
""",
)

entry(
    index = 62,
    label = "Backbone4_N-Sp-5R!H-2R!H_N-Sp-2R!H-1R!H_1R!H-inRing",
    kinetics = ArrheniusBM(A=(1e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(219004,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_N-Sp-5R!H-2R!H_N-Sp-2R!H-1R!H_1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Backbone4_N-Sp-5R!H-2R!H_N-Sp-2R!H-1R!H_1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_N-Sp-5R!H-2R!H_N-Sp-2R!H-1R!H_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_N-Sp-5R!H-2R!H_N-Sp-2R!H-1R!H_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Backbone4_N-Sp-5R!H-2R!H_N-Sp-2R!H-1R!H_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(2.05e+09,'s^-1'), n=0.155, w0=(289500,'J/mol'), E0=(28950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_N-Sp-5R!H-2R!H_N-Sp-2R!H-1R!H_N-1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Backbone4_N-Sp-5R!H-2R!H_N-Sp-2R!H-1R!H_N-1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_N-Sp-5R!H-2R!H_N-Sp-2R!H-1R!H_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_N-Sp-5R!H-2R!H_N-Sp-2R!H-1R!H_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.51485e+12,'s^-1'), n=0.191941, w0=(301000,'J/mol'), E0=(32243.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.031146401934730564, var=0.6565817960195416, Tref=1000.0, N=24, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 24 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.7026888127031428"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.7026888127031428""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.7026888127031428
""",
)

entry(
    index = 65,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(9.07985e+08,'s^-1'), n=0.931559, w0=(301000,'J/mol'), E0=(26984.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004423964593252763, var=0.21471553090034456, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 0.940057745666803"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.940057745666803""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.940057745666803
""",
)

entry(
    index = 66,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(1.22728e+09,'s^-1'), n=0.96751, w0=(301000,'J/mol'), E0=(27985.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.275960749131821e-05, var=0.8943487563765848, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 1.8959856812295448"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.8959856812295448""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.8959856812295448
""",
)

entry(
    index = 67,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(3.06119e+20,'s^-1'), n=-2.10738, w0=(301000,'J/mol'), E0=(30288.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15730063929578955, var=1.298783937195343, Tref=1000.0, N=8, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 8 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 2.67990807312102"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.67990807312102""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.67990807312102
""",
)

entry(
    index = 68,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(6.29966e+11,'s^-1'), n=0.364528, w0=(301000,'J/mol'), E0=(16545.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1477351294418367, var=0.15145886879099577, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.151390914376989"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.151390914376989""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.151390914376989
""",
)

entry(
    index = 69,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.53e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(22334.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H",
    kinetics = ArrheniusBM(A=(2.20876e+23,'s^-1'), n=-3.21146, w0=(301000,'J/mol'), E0=(41189.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.554225271598829, var=2.416923504474888, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H
    Total Standard Deviation in ln(k): 9.53430436633193"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H
Total Standard Deviation in ln(k): 9.53430436633193""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H
Total Standard Deviation in ln(k): 9.53430436633193
""",
)

entry(
    index = 71,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H",
    kinetics = ArrheniusBM(A=(9.15112e+12,'s^-1'), n=-0.319069, w0=(301000,'J/mol'), E0=(53956.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.4908653393090368, var=61.70492160824152, Tref=1000.0, N=5, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H',), comment="""BM rule fitted to 5 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H
    Total Standard Deviation in ln(k): 24.51870970726304"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H
Total Standard Deviation in ln(k): 24.51870970726304""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H
Total Standard Deviation in ln(k): 24.51870970726304
""",
)

entry(
    index = 72,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_Sp-3R!H-2R!H_1R!H-inRing",
    kinetics = ArrheniusBM(A=(6.32e+10,'s^-1'), n=0.35, w0=(301000,'J/mol'), E0=(11247.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_Sp-3R!H-2R!H_1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_Sp-3R!H-2R!H_1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_Sp-3R!H-2R!H_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_Sp-3R!H-2R!H_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_Sp-3R!H-2R!H_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.67082e+07,'s^-1'), n=1.41523, w0=(301000,'J/mol'), E0=(12870.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004861188433814168, var=0.05005056033725098, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_Sp-3R!H-2R!H_N-1R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_Sp-3R!H-2R!H_N-1R!H-inRing
    Total Standard Deviation in ln(k): 0.46071302304878453"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_Sp-3R!H-2R!H_N-1R!H-inRing
Total Standard Deviation in ln(k): 0.46071302304878453""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_Sp-3R!H-2R!H_N-1R!H-inRing
Total Standard Deviation in ln(k): 0.46071302304878453
""",
)

entry(
    index = 74,
    label = "Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_Sp-5R!H-2R!H",
    kinetics = ArrheniusBM(A=(6.05189e+11,'s^-1'), n=0.197426, w0=(269167,'J/mol'), E0=(50931,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08798563182803865, var=14.157730908728785, Tref=1000.0, N=3, data_mean=0.0, correlation='Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_Sp-5R!H-2R!H',), comment="""BM rule fitted to 3 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_Sp-5R!H-2R!H
    Total Standard Deviation in ln(k): 7.764238049445441"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_Sp-5R!H-2R!H
Total Standard Deviation in ln(k): 7.764238049445441""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_Sp-5R!H-2R!H
Total Standard Deviation in ln(k): 7.764238049445441
""",
)

entry(
    index = 75,
    label = "Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_N-Sp-5R!H-2R!H",
    kinetics = ArrheniusBM(A=(5.925e+10,'s^-1'), n=0.586, w0=(259000,'J/mol'), E0=(25900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_N-Sp-5R!H-2R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_N-Sp-5R!H-2R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_N-Sp-5R!H-2R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_N-Sp-5R!H-2R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
    label = "Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_2R!H->C",
    kinetics = ArrheniusBM(A=(2.02628e+08,'s^-1'), n=1.08398, w0=(259000,'J/mol'), E0=(44951.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03961874681586119, var=0.5643340712744636, Tref=1000.0, N=3, data_mean=0.0, correlation='Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_2R!H->C',), comment="""BM rule fitted to 3 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_2R!H->C
    Total Standard Deviation in ln(k): 1.6055451212055927"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_2R!H->C
Total Standard Deviation in ln(k): 1.6055451212055927""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_2R!H->C
Total Standard Deviation in ln(k): 1.6055451212055927
""",
)

entry(
    index = 77,
    label = "Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_N-2R!H->C",
    kinetics = ArrheniusBM(A=(7.785e+11,'s^-1'), n=0.342, w0=(265000,'J/mol'), E0=(67814,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 78,
    label = "Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H_Ext-3R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.233e+11,'s^-1'), n=0.39, w0=(259000,'J/mol'), E0=(92284.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H_Ext-3R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H_Ext-3R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H_Ext-2R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(9.423e+09,'s^-1'), n=0.834, w0=(259000,'J/mol'), E0=(48878.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H_Ext-2R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H_Ext-2R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H_Ext-2R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_N-Sp-3R!H-2R!H_Ext-2R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(9.74655e+07,'s^-1'), n=1.32185, w0=(299320,'J/mol'), E0=(56249.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21454469521596467, var=0.8249693631505569, Tref=1000.0, N=25, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 25 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 2.3599142730066607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.3599142730066607""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.3599142730066607
""",
)

entry(
    index = 81,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.01823e+07,'s^-1'), n=1.2623, w0=(301000,'J/mol'), E0=(62964,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00139442645167558, var=0.24460264796958056, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.9949918219926736"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.9949918219926736""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.9949918219926736
""",
)

entry(
    index = 82,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.49925e+07,'s^-1'), n=1.36128, w0=(301000,'J/mol'), E0=(63543.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2526545083361467e-05, var=0.8906410654621427, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.8919757774506523"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8919757774506523""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8919757774506523
""",
)

entry(
    index = 83,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.53993e+11,'s^-1'), n=0.474646, w0=(301000,'J/mol'), E0=(54339.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.006087434912687983, var=1.0065213893314322, Tref=1000.0, N=8, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 8 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 2.026556346269392"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.026556346269392""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.026556346269392
""",
)

entry(
    index = 84,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.74772e+10,'s^-1'), n=0.574276, w0=(301000,'J/mol'), E0=(57844.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0005540984563063593, var=0.20264207511403293, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.9038394064750148"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.9038394064750148""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.9038394064750148
""",
)

entry(
    index = 85,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.79e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(61099.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_3R!H-inRing",
    kinetics = ArrheniusBM(A=(5.932e+07,'s^-1'), n=1.035, w0=(301000,'J/mol'), E0=(74396.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_3R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_3R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 87,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(5.66021e+09,'s^-1'), n=0.600792, w0=(301000,'J/mol'), E0=(55451.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.018313768983990623, var=1.7384121076088834, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing',), comment="""BM rule fitted to 4 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing
    Total Standard Deviation in ln(k): 2.6892347791315556"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing
Total Standard Deviation in ln(k): 2.6892347791315556""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing
Total Standard Deviation in ln(k): 2.6892347791315556
""",
)

entry(
    index = 88,
    label = "Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(12838.4,'s^-1'), n=2.12349, w0=(301000,'J/mol'), E0=(40459.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0006636444470941442, var=0.02722612278518736, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.33245555692848255"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.33245555692848255""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.33245555692848255
""",
)

entry(
    index = 89,
    label = "Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(24319,'s^-1'), n=2.04309, w0=(301000,'J/mol'), E0=(38093.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00020612686478981598, var=0.33072414114526205, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.1534133908356352"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.1534133908356352""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.1534133908356352
""",
)

entry(
    index = 90,
    label = "Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(6.48e+06,'s^-1'), n=1.25, w0=(301000,'J/mol'), E0=(51111.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Sp-4C-3R!H",
    kinetics = ArrheniusBM(A=(11224.9,'s^-1'), n=2.24934, w0=(301000,'J/mol'), E0=(43613,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.189245678857944, var=42.29657088493216, Tref=1000.0, N=9, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Sp-4C-3R!H',), comment="""BM rule fitted to 9 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Sp-4C-3R!H
    Total Standard Deviation in ln(k): 21.051137837093275"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Sp-4C-3R!H
Total Standard Deviation in ln(k): 21.051137837093275""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Sp-4C-3R!H
Total Standard Deviation in ln(k): 21.051137837093275
""",
)

entry(
    index = 92,
    label = "Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_N-Sp-4C-3R!H",
    kinetics = ArrheniusBM(A=(1.96901e+08,'s^-1'), n=0.937279, w0=(301000,'J/mol'), E0=(59606.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-7.771561172376099e-16, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_N-Sp-4C-3R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_N-Sp-4C-3R!H
    Total Standard Deviation in ln(k): 1.9526535608985173e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_N-Sp-4C-3R!H
Total Standard Deviation in ln(k): 1.9526535608985173e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_N-Sp-4C-3R!H
Total Standard Deviation in ln(k): 1.9526535608985173e-15
""",
)

entry(
    index = 93,
    label = "Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing_N-4R!H-inRing_Sp-4R!H-1R!H",
    kinetics = ArrheniusBM(A=(2.23514e+06,'s^-1'), n=1.08303, w0=(301000,'J/mol'), E0=(211756,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=11.476385067684125, var=299.26347221058796, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing_N-4R!H-inRing_Sp-4R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing_N-4R!H-inRing_Sp-4R!H-1R!H
    Total Standard Deviation in ln(k): 63.51551813726193"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing_N-4R!H-inRing_Sp-4R!H-1R!H
Total Standard Deviation in ln(k): 63.51551813726193""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing_N-4R!H-inRing_Sp-4R!H-1R!H
Total Standard Deviation in ln(k): 63.51551813726193
""",
)

entry(
    index = 94,
    label = "Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing_N-4R!H-inRing_N-Sp-4R!H-1R!H",
    kinetics = ArrheniusBM(A=(1e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing_N-4R!H-inRing_N-Sp-4R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing_N-4R!H-inRing_N-Sp-4R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing_N-4R!H-inRing_N-Sp-4R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_Sp-2R!H=1R!H_N-3R!H-inRing_N-4R!H-inRing_N-Sp-4R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(148619,'s^-1'), n=1.59852, w0=(299552,'J/mol'), E0=(53820.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1973822163864999, var=1.3898836254575293, Tref=1000.0, N=29, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 29 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 2.8593840721135186"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.8593840721135186""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.8593840721135186
""",
)

entry(
    index = 96,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.36909e+07,'s^-1'), n=1.14583, w0=(301000,'J/mol'), E0=(48785.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.044648981822552565, var=0.3649961171896117, Tref=1000.0, N=12, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 12 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.3233422345585109"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.3233422345585109""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.3233422345585109
""",
)

entry(
    index = 97,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2980.82,'s^-1'), n=2.00426, w0=(301000,'J/mol'), E0=(37890.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3563565371368287, var=4.180143749525445, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 7.506692022533614"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 7.506692022533614""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 7.506692022533614
""",
)

entry(
    index = 98,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.12951e+06,'s^-1'), n=1.40297, w0=(259000,'J/mol'), E0=(49301.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.28005e+07,'s^-1'), n=0.952261, w0=(301000,'J/mol'), E0=(51290.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0021744045974044, var=0.2676317379339218, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 1.0425756558328738"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 1.0425756558328738""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 1.0425756558328738
""",
)

entry(
    index = 100,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(96935.7,'s^-1'), n=1.57359, w0=(301000,'J/mol'), E0=(40218.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01241216377452139, var=0.00035005677044125264, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 0.06869454176500601"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.06869454176500601""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.06869454176500601
""",
)

entry(
    index = 101,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_1R!H-inRing_Sp-6R!H=3R!H",
    kinetics = ArrheniusBM(A=(6.311e+09,'s^-1'), n=0.537, w0=(301000,'J/mol'), E0=(30100,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_1R!H-inRing_Sp-6R!H=3R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_1R!H-inRing_Sp-6R!H=3R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_1R!H-inRing_Sp-6R!H=3R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_1R!H-inRing_Sp-6R!H=3R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 102,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_1R!H-inRing_N-Sp-6R!H=3R!H",
    kinetics = ArrheniusBM(A=(1.42e+11,'s^-1'), n=0.258, w0=(289500,'J/mol'), E0=(28950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_1R!H-inRing_N-Sp-6R!H=3R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_1R!H-inRing_N-Sp-6R!H=3R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_1R!H-inRing_N-Sp-6R!H=3R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_1R!H-inRing_N-Sp-6R!H=3R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 103,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(184000,'s^-1'), n=1.4, w0=(301000,'J/mol'), E0=(52693.1,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 104,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(40683.2,'s^-1'), n=1.71232, w0=(301000,'J/mol'), E0=(41686.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0018539796123168343, var=0.015978837537474706, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-2R!H-R
    Total Standard Deviation in ln(k): 0.25807164268015687"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.25807164268015687""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.25807164268015687
""",
)

entry(
    index = 105,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(72220.9,'s^-1'), n=1.6363, w0=(301000,'J/mol'), E0=(39718.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0017952159058182732, var=0.0036340586183760135, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.12536234549921912"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.12536234549921912""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.12536234549921912
""",
)

entry(
    index = 106,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(60370.2,'s^-1'), n=1.63267, w0=(301000,'J/mol'), E0=(38671.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0013317020727281882, var=0.6679269765401225, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 1.6417518034055345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.6417518034055345""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.6417518034055345
""",
)

entry(
    index = 107,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(465716,'s^-1'), n=1.42934, w0=(301000,'J/mol'), E0=(44693.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3292219847419922, var=4.161322094198857, Tref=1000.0, N=9, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Sp-5R!H-4R!H',), comment="""BM rule fitted to 9 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 4.916713921181709"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 4.916713921181709""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 4.916713921181709
""",
)

entry(
    index = 108,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(2.46301e+08,'s^-1'), n=0.668371, w0=(301000,'J/mol'), E0=(56547.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.0128758627126295, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 5.057477041991532"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 5.057477041991532""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 5.057477041991532
""",
)

entry(
    index = 109,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_6R!H-inRing",
    kinetics = ArrheniusBM(A=(4.39374e+10,'s^-1'), n=0.57269, w0=(301000,'J/mol'), E0=(106019,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.9984014443252837e-15, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_6R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_6R!H-inRing
    Total Standard Deviation in ln(k): 5.02110915659619e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_6R!H-inRing
Total Standard Deviation in ln(k): 5.02110915659619e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_6R!H-inRing
Total Standard Deviation in ln(k): 5.02110915659619e-15
""",
)

entry(
    index = 110,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing",
    kinetics = ArrheniusBM(A=(1.74074e+08,'s^-1'), n=1.24149, w0=(301000,'J/mol'), E0=(101796,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04780213785451442, var=2.446304786959407, Tref=1000.0, N=42, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing',), comment="""BM rule fitted to 42 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing
    Total Standard Deviation in ln(k): 3.255645343749588"""),
    rank = 11,
    shortDesc = """BM rule fitted to 42 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing
Total Standard Deviation in ln(k): 3.255645343749588""",
    longDesc = 
"""
BM rule fitted to 42 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing
Total Standard Deviation in ln(k): 3.255645343749588
""",
)

entry(
    index = 111,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(5.78002e+09,'s^-1'), n=0.563241, w0=(301000,'J/mol'), E0=(109837,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0022305788678015645, var=4.7510345651965284, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 4.3752990639945875"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 4.3752990639945875""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 4.3752990639945875
""",
)

entry(
    index = 112,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.55e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(90392.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 113,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-4R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(284.136,'s^-1'), n=1.70342, w0=(259000,'J/mol'), E0=(46834.5,'J/mol'), Tmin=(500,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-4R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-4R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 114,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-4R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(231677,'s^-1'), n=1.30099, w0=(259000,'J/mol'), E0=(53318.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-4R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-4R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-4R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-4R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(6.36525e+07,'s^-1'), n=1.18471, w0=(301000,'J/mol'), E0=(81437.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.012158273096921657, var=1.5117593314730657, Tref=1000.0, N=28, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 28 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 2.4954428264035364"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.4954428264035364""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.4954428264035364
""",
)

entry(
    index = 116,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.27686e+07,'s^-1'), n=1.3722, w0=(301000,'J/mol'), E0=(65013.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04685112769922145, var=0.36304324842089486, Tref=1000.0, N=12, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 12 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 1.3256308373696248"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 1.3256308373696248""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 1.3256308373696248
""",
)

entry(
    index = 117,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(17.8177,'s^-1'), n=2.38355, w0=(301000,'J/mol'), E0=(40649.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2347748574941748, var=3.4643283087411767, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 6.833803884591368"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 6.833803884591368""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 6.833803884591368
""",
)

entry(
    index = 118,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.1092e+07,'s^-1'), n=1.17998, w0=(301000,'J/mol'), E0=(67186.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.005875890017772092, var=0.26669553130136714, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 1.050060312143832"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 1.050060312143832""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 1.050060312143832
""",
)

entry(
    index = 119,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(687,'s^-1'), n=1.97585, w0=(301000,'J/mol'), E0=(49493.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.9142202704983133, var=19.296930668970482, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 16.12861622846918"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 16.12861622846918""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 16.12861622846918
""",
)

entry(
    index = 120,
    label = "Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C",
    kinetics = ArrheniusBM(A=(1.19472e+06,'s^-1'), n=1.60657, w0=(301000,'J/mol'), E0=(98149.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4926581779073288, var=4.6460874949433775, Tref=1000.0, N=5, data_mean=0.0, correlation='Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C',), comment="""BM rule fitted to 5 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C
    Total Standard Deviation in ln(k): 5.558997943280484"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C
Total Standard Deviation in ln(k): 5.558997943280484""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C
Total Standard Deviation in ln(k): 5.558997943280484
""",
)

entry(
    index = 121,
    label = "Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_N-6R!H->C",
    kinetics = ArrheniusBM(A=(9.291e+11,'s^-1'), n=0.234, w0=(307000,'J/mol'), E0=(90907.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 122,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(2.32098e+12,'s^-1'), n=0.205007, w0=(301000,'J/mol'), E0=(31996.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.029746988802869318, var=0.9410888741353161, Tref=1000.0, N=16, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 16 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 2.0195293697752668"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.0195293697752668""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.0195293697752668
""",
)

entry(
    index = 123,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.12473e+10,'s^-1'), n=0.616823, w0=(301000,'J/mol'), E0=(27026.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.013526110093322479, var=0.2726630257431694, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.0808006283595655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.0808006283595655""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.0808006283595655
""",
)

entry(
    index = 124,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(6.51216e+10,'s^-1'), n=0.655902, w0=(301000,'J/mol'), E0=(29465,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0035059095196261596, var=0.23862443778973919, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 0.9881058729600023"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.9881058729600023""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.9881058729600023
""",
)

entry(
    index = 125,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(5.57365e+10,'s^-1'), n=0.750742, w0=(301000,'J/mol'), E0=(30079.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.327358272776636e-05, var=0.8958621509142529, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 1.8975652477858749"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.8975652477858749""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.8975652477858749
""",
)

entry(
    index = 126,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.8e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(34655,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 127,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.95e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(32974.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 128,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.3603e+21,'s^-1'), n=-2.33324, w0=(301000,'J/mol'), E0=(8898.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1338627564997327, var=3.0510111120420698, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 3.8380381643374464"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.8380381643374464""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.8380381643374464
""",
)

entry(
    index = 129,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.28449e+16,'s^-1'), n=-0.867374, w0=(301000,'J/mol'), E0=(5403.85,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7041072017956109, var=1.101546839783793, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 3.8731752860438666"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.8731752860438666""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.8731752860438666
""",
)

entry(
    index = 130,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(5.72e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(18364.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.97e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(17058.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 132,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.42e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(11360.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.98e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(22004,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 134,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_1R!H-inRing",
    kinetics = ArrheniusBM(A=(8.15385e+14,'s^-1'), n=-0.537569, w0=(301000,'J/mol'), E0=(46122.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 135,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.32535e+20,'s^-1'), n=-2.47702, w0=(301000,'J/mol'), E0=(83357.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.18445624920335998, var=84.02295460920683, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-1R!H-inRing',), comment="""BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-1R!H-inRing
    Total Standard Deviation in ln(k): 18.83966870489162"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-1R!H-inRing
Total Standard Deviation in ln(k): 18.83966870489162""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-1R!H-inRing
Total Standard Deviation in ln(k): 18.83966870489162
""",
)

entry(
    index = 136,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_Sp-3R!H-2R!H_N-1R!H-inRing_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.85e+09,'s^-1'), n=0.75, w0=(301000,'J/mol'), E0=(14686.4,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_Sp-3R!H-2R!H_N-1R!H-inRing_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_Sp-3R!H-2R!H_N-1R!H-inRing_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_Sp-3R!H-2R!H_N-1R!H-inRing_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-2R!H-R_Sp-3R!H-2R!H_N-1R!H-inRing_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 137,
    label = "Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_Sp-5R!H-2R!H_1R!H-inRing",
    kinetics = ArrheniusBM(A=(5.59243e+10,'s^-1'), n=0.569544, w0=(259000,'J/mol'), E0=(42921.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.009572082996390356, var=18.110427446516322, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_Sp-5R!H-2R!H_1R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_Sp-5R!H-2R!H_1R!H-inRing
    Total Standard Deviation in ln(k): 8.555470795325947"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_Sp-5R!H-2R!H_1R!H-inRing
Total Standard Deviation in ln(k): 8.555470795325947""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_Sp-5R!H-2R!H_1R!H-inRing
Total Standard Deviation in ln(k): 8.555470795325947
""",
)

entry(
    index = 138,
    label = "Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_Sp-5R!H-2R!H_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.881e+08,'s^-1'), n=1.062, w0=(289500,'J/mol'), E0=(53416.1,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_Sp-5R!H-2R!H_N-1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_Sp-5R!H-2R!H_N-1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_Sp-5R!H-2R!H_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_Sp-5R!H-2R!H_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 139,
    label = "Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_2R!H->C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.46139e+07,'s^-1'), n=1.30419, w0=(259000,'J/mol'), E0=(29342.8,'J/mol'), Tmin=(500,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_2R!H->C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_2R!H->C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_2R!H->C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_2R!H->C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 140,
    label = "Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_2R!H->C_Ext-4R!H-R_Ext-5R!H-R_Sp-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(2.597e+08,'s^-1'), n=0.953, w0=(259000,'J/mol'), E0=(40543.1,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_2R!H->C_Ext-4R!H-R_Ext-5R!H-R_Sp-5R!H-3R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_2R!H->C_Ext-4R!H-R_Ext-5R!H-R_Sp-5R!H-3R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_2R!H->C_Ext-4R!H-R_Ext-5R!H-R_Sp-5R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_2R!H->C_Ext-4R!H-R_Ext-5R!H-R_Sp-5R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 141,
    label = "Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_2R!H->C_Ext-4R!H-R_Ext-5R!H-R_N-Sp-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(1.241e+10,'s^-1'), n=0.754, w0=(259000,'J/mol'), E0=(64365.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_2R!H->C_Ext-4R!H-R_Ext-5R!H-R_N-Sp-5R!H-3R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_2R!H->C_Ext-4R!H-R_Ext-5R!H-R_N-Sp-5R!H-3R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_2R!H->C_Ext-4R!H-R_Ext-5R!H-R_N-Sp-5R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_1R!H-inRing_2R!H->C_Ext-4R!H-R_Ext-5R!H-R_N-Sp-5R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 142,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(2.2923e+07,'s^-1'), n=1.49645, w0=(298529,'J/mol'), E0=(53694.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3099600476653369, var=1.0526550451750634, Tref=1000.0, N=17, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 17 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 2.8356318067557664"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.8356318067557664""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.8356318067557664
""",
)

entry(
    index = 143,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.9276e+09,'s^-1'), n=0.929295, w0=(301000,'J/mol'), E0=(64356.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.013750472370697034, var=0.276395061932914, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 1.0885040729930324"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.0885040729930324""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.0885040729930324
""",
)

entry(
    index = 144,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.29622e+09,'s^-1'), n=0.979983, w0=(301000,'J/mol'), E0=(65373.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0011442113882921582, var=0.26227892729126606, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.029563382412674"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.029563382412674""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.029563382412674
""",
)

entry(
    index = 145,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.60156e+09,'s^-1'), n=1.10104, w0=(301000,'J/mol'), E0=(65830.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0204473452911974e-05, var=0.8862713147752092, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.8873230147889108"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8873230147889108""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8873230147889108
""",
)

entry(
    index = 146,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.11e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(72264.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 147,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.17e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(70529.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.74981e+12,'s^-1'), n=0.0349271, w0=(301000,'J/mol'), E0=(55017.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.014070005972656065, var=2.899767145285883, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 3.449155529749758"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.449155529749758""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.449155529749758
""",
)

entry(
    index = 149,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.45044e+09,'s^-1'), n=1.12351, w0=(301000,'J/mol'), E0=(52286.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.006570588214302285, var=0.1492437062799305, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.7909797337858375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.7909797337858375""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.7909797337858375
""",
)

entry(
    index = 150,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(2.26e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(62960.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 151,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(7.81e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(55842.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 152,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.62e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(55941,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 153,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.27613e+11,'s^-1'), n=0.171892, w0=(301000,'J/mol'), E0=(56095.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0057002559890122805, var=9.688856635096064, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 6.254446746616778"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 6.254446746616778""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 6.254446746616778
""",
)

entry(
    index = 154,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.15e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(63700.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 155,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(7.43e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(56583.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 156,
    label = "Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-1R!H-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2.6e+07,'s^-1'), n=1.13, w0=(301000,'J/mol'), E0=(47188.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-1R!H-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-1R!H-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-1R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-1R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 157,
    label = "Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(6.2e+06,'s^-1'), n=1.3, w0=(301000,'J/mol'), E0=(39773.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_N-1R!H-inRing_4R!H->C_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 158,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(40105.2,'s^-1'), n=1.77115, w0=(299320,'J/mol'), E0=(52159,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.28604654148162134, var=1.5622817120166927, Tref=1000.0, N=25, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 25 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 3.2244537000179565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.2244537000179565""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.2244537000179565
""",
)

entry(
    index = 159,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(4.12116e+07,'s^-1'), n=0.718327, w0=(301000,'J/mol'), E0=(61505,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.179172750003073e-05, var=9.257702235323421, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 6.099806657220733"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.099806657220733""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.099806657220733
""",
)

entry(
    index = 160,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(7.08e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(72248.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 161,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(2.45e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(64277.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 162,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(920462,'s^-1'), n=1.41567, w0=(301000,'J/mol'), E0=(44271.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07418063236321441, var=0.2383333972106166, Tref=1000.0, N=6, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 6 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.1650831667514334"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.1650831667514334""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.1650831667514334
""",
)

entry(
    index = 163,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.88659e+08,'s^-1'), n=0.866151, w0=(301000,'J/mol'), E0=(53057.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004517307917863608, var=0.265921720982306, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 1.0451437545759918"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 1.0451437545759918""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 1.0451437545759918
""",
)

entry(
    index = 164,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5.89e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(58432.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 165,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(9.19391e+06,'s^-1'), n=0.961477, w0=(301000,'J/mol'), E0=(50887.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.006168232368378478, var=0.05077367337677354, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 0.46722531308767895"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 0.46722531308767895""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 0.46722531308767895
""",
)

entry(
    index = 166,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.53278e+07,'s^-1'), n=0.961764, w0=(301000,'J/mol'), E0=(51469.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.882097112640929e-05, var=0.9103453622999381, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 1.9129814078275085"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 1.9129814078275085""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 1.9129814078275085
""",
)

entry(
    index = 167,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.18e+07,'s^-1'), n=0.99, w0=(301000,'J/mol'), E0=(48077.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 168,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-1R!H-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.37e+07,'s^-1'), n=0.85, w0=(301000,'J/mol'), E0=(46777.4,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-1R!H-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-1R!H-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-1R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-1R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 169,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(7.05e+06,'s^-1'), n=1.03, w0=(301000,'J/mol'), E0=(41988,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_N-1R!H-inRing_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 170,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(4.30994e+08,'s^-1'), n=1.15743, w0=(301000,'J/mol'), E0=(103676,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.045344937561504435, var=2.7467287212737412, Tref=1000.0, N=36, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R',), comment="""BM rule fitted to 36 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R
    Total Standard Deviation in ln(k): 3.4364311177965106"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.4364311177965106""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.4364311177965106
""",
)

entry(
    index = 171,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(5.0863e+07,'s^-1'), n=1.21134, w0=(301000,'J/mol'), E0=(97597.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0028957901692660904, var=0.2707133857695818, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R
    Total Standard Deviation in ln(k): 1.0503420117858087"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R
Total Standard Deviation in ln(k): 1.0503420117858087""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R
Total Standard Deviation in ln(k): 1.0503420117858087
""",
)

entry(
    index = 172,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.98e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(100889,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 173,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.29367e+09,'s^-1'), n=0.587068, w0=(301000,'J/mol'), E0=(104418,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0006217986866287186, var=2.3471659617000005, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 3.0729093291025245"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.0729093291025245""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.0729093291025245
""",
)

entry(
    index = 174,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(2.4e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(107043,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 175,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(8.27e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(129794,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 176,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(3.44515e+06,'s^-1'), n=1.58413, w0=(301000,'J/mol'), E0=(78034.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.050765017599162875, var=1.076633620996986, Tref=1000.0, N=24, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 24 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 2.207682598293365"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.207682598293365""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.207682598293365
""",
)

entry(
    index = 177,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5.57618e+07,'s^-1'), n=0.932716, w0=(301000,'J/mol'), E0=(81061.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00039431836321757326, var=9.201227445488232, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 6.082058927089304"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 6.082058927089304""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 6.082058927089304
""",
)

entry(
    index = 178,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(2.42e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(86735.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 179,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(8.36e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(78507.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 180,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.3051e+06,'s^-1'), n=1.59128, w0=(301000,'J/mol'), E0=(61276.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07189859466960004, var=0.2426852982292884, Tref=1000.0, N=6, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 6 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.16824437326256"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.16824437326256""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.16824437326256
""",
)

entry(
    index = 181,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.79505e+08,'s^-1'), n=1.08586, w0=(301000,'J/mol'), E0=(69093.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00823901800207117, var=0.2661398938419471, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 1.0549187809395035"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 1.0549187809395035""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 1.0549187809395035
""",
)

entry(
    index = 182,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(2.01e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(71755.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 183,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(8.95438e+06,'s^-1'), n=1.17401, w0=(301000,'J/mol'), E0=(66906.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.858281319607548, var=0.030521375809949132, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 7.531845951268982"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 7.531845951268982""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 7.531845951268982
""",
)

entry(
    index = 184,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.19475e+07,'s^-1'), n=1.20316, w0=(301000,'J/mol'), E0=(67261.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.7828044883667897, var=0.7583875753606412, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 8.73780365723938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 8.73780365723938""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 8.73780365723938
""",
)

entry(
    index = 185,
    label = "Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_Sp-3R!H-1R!H",
    kinetics = ArrheniusBM(A=(52.2809,'s^-1'), n=2.74082, w0=(301000,'J/mol'), E0=(76039.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.974351130927458, var=0.1777718349317127, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_Sp-3R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_Sp-3R!H-1R!H
    Total Standard Deviation in ln(k): 23.393877330433632"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_Sp-3R!H-1R!H
Total Standard Deviation in ln(k): 23.393877330433632""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_Sp-3R!H-1R!H
Total Standard Deviation in ln(k): 23.393877330433632
""",
)

entry(
    index = 186,
    label = "Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_N-Sp-3R!H-1R!H",
    kinetics = ArrheniusBM(A=(5.0997e+08,'s^-1'), n=1.01017, w0=(301000,'J/mol'), E0=(119913,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06784010510212969, var=7.244758647748412, Tref=1000.0, N=3, data_mean=0.0, correlation='Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_N-Sp-3R!H-1R!H',), comment="""BM rule fitted to 3 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_N-Sp-3R!H-1R!H
    Total Standard Deviation in ln(k): 5.566415367824549"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_N-Sp-3R!H-1R!H
Total Standard Deviation in ln(k): 5.566415367824549""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_N-Sp-3R!H-1R!H
Total Standard Deviation in ln(k): 5.566415367824549
""",
)

entry(
    index = 187,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.73157e+13,'s^-1'), n=-0.235574, w0=(301000,'J/mol'), E0=(32686.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.025352896649199735, var=2.00747871541133, Tref=1000.0, N=8, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 8 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.9041201051590244"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.9041201051590244""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.9041201051590244
""",
)

entry(
    index = 188,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(4.3656e+10,'s^-1'), n=0.699341, w0=(301000,'J/mol'), E0=(29667.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01710712230809341, var=0.19609613958439448, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 0.9307344169668906"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.9307344169668906""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.9307344169668906
""",
)

entry(
    index = 189,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(5.21569e+09,'s^-1'), n=1.04737, w0=(301000,'J/mol'), E0=(28844.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00912178862021713, var=0.286009487861094, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 1.0950484771209643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.0950484771209643""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.0950484771209643
""",
)

entry(
    index = 190,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(7.51765e+10,'s^-1'), n=0.530146, w0=(301000,'J/mol'), E0=(26955.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.001624556954861856, var=0.28702562969298234, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 1.0781140674105063"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.0781140674105063""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.0781140674105063
""",
)

entry(
    index = 191,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(3.12987e+10,'s^-1'), n=0.717174, w0=(301000,'J/mol'), E0=(26979.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.7523741974937174e-05, var=0.8797090670508095, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 1.8803413342365833"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.8803413342365833""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.8803413342365833
""",
)

entry(
    index = 192,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.87e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(33146.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 193,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.97e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(31429.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 194,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(4.94336e+18,'s^-1'), n=-1.68867, w0=(301000,'J/mol'), E0=(4848.34,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.1213909113843856, var=0.1735893407736615, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 6.1653818261458735"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 6.1653818261458735""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 6.1653818261458735
""",
)

entry(
    index = 195,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.74322e+23,'s^-1'), n=-2.9778, w0=(301000,'J/mol'), E0=(-6854.73,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.46653426644048, var=0.16836183030057061, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 9.532466346647245"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 9.532466346647245""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 9.532466346647245
""",
)

entry(
    index = 196,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(9.58e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(17329.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 197,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.31e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(15951.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 198,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-1R!H-inRing_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.99e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(21615.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-1R!H-inRing_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-1R!H-inRing_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-1R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-1R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 199,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-1R!H-inRing_Sp-3R!H-2R!H",
    kinetics = ArrheniusBM(A=(3.46436e+07,'s^-1'), n=0.742146, w0=(301000,'J/mol'), E0=(54264.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.483316948192838, var=178.1611382516698, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-1R!H-inRing_Sp-3R!H-2R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-1R!H-inRing_Sp-3R!H-2R!H
    Total Standard Deviation in ln(k): 48.07347232281302"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-1R!H-inRing_Sp-3R!H-2R!H
Total Standard Deviation in ln(k): 48.07347232281302""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-1R!H-inRing_Sp-3R!H-2R!H
Total Standard Deviation in ln(k): 48.07347232281302
""",
)

entry(
    index = 200,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-1R!H-inRing_N-Sp-3R!H-2R!H",
    kinetics = ArrheniusBM(A=(1.126e+14,'s^-1'), n=-0.355, w0=(301000,'J/mol'), E0=(61561.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-1R!H-inRing_N-Sp-3R!H-2R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-1R!H-inRing_N-Sp-3R!H-2R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-1R!H-inRing_N-Sp-3R!H-2R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-1R!H-inRing_N-Sp-3R!H-2R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 201,
    label = "Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_Sp-5R!H-2R!H_1R!H-inRing_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.93867e+07,'s^-1'), n=1.59576, w0=(259000,'J/mol'), E0=(25609.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_Sp-5R!H-2R!H_1R!H-inRing_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_Sp-5R!H-2R!H_1R!H-inRing_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_Sp-5R!H-2R!H_1R!H-inRing_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_N-Sp-4R!H=1R!H_Sp-3R!H-2R!H_Ext-2R!H-R_Sp-5R!H-2R!H_1R!H-inRing_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 202,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.13845e+10,'s^-1'), n=0.568467, w0=(301000,'J/mol'), E0=(67440.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.005941575271063513, var=1.9456384455724038, Tref=1000.0, N=8, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 8 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 2.8112562442603526"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.8112562442603526""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.8112562442603526
""",
)

entry(
    index = 203,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H",
    kinetics = ArrheniusBM(A=(1.10988e+08,'s^-1'), n=1.43139, w0=(301000,'J/mol'), E0=(65458.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0012836583595059962, var=0.28542522155841993, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H',), comment="""BM rule fitted to 4 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H
    Total Standard Deviation in ln(k): 1.0742590382067005"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H
Total Standard Deviation in ln(k): 1.0742590382067005""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H
Total Standard Deviation in ln(k): 1.0742590382067005
""",
)

entry(
    index = 204,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H",
    kinetics = ArrheniusBM(A=(4.55674e+06,'s^-1'), n=1.68069, w0=(292600,'J/mol'), E0=(49444.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6872906345504638, var=1.4659403441090564, Tref=1000.0, N=5, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H',), comment="""BM rule fitted to 5 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H
    Total Standard Deviation in ln(k): 4.154114402139166"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H
Total Standard Deviation in ln(k): 4.154114402139166""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H
Total Standard Deviation in ln(k): 4.154114402139166
""",
)

entry(
    index = 205,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.50086e+09,'s^-1'), n=0.858133, w0=(301000,'J/mol'), E0=(64184,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0009099447885058024, var=0.27849951000157613, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.0602461939868872"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.0602461939868872""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.0602461939868872
""",
)

entry(
    index = 206,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.43917e+09,'s^-1'), n=1.00442, w0=(301000,'J/mol'), E0=(64494.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.17168491536089e-06, var=0.8893913685504728, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.890637035307336"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.890637035307336""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.890637035307336
""",
)

entry(
    index = 207,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(7.41e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(70621.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 208,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(7.81e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(68863.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 209,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(2.84411e+11,'s^-1'), n=0.30016, w0=(301000,'J/mol'), E0=(58502,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.002538541922622623, var=0.11550273728440234, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 0.6877013679258529"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 0.6877013679258529""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 0.6877013679258529
""",
)

entry(
    index = 210,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(4.61649e+12,'s^-1'), n=0.0654112, w0=(301000,'J/mol'), E0=(48388.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005313620952029403, var=0.0852679768198797, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 0.5987471003423"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 0.5987471003423""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 0.5987471003423
""",
)

entry(
    index = 211,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-5R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(3.79e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(65186.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-5R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-5R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-5R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-5R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 212,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-5R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.31e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(58117.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-5R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-5R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-5R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-5R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 213,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_Ext-4R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.16e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(55728.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_Ext-4R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_Ext-4R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_Ext-4R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_Ext-4R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 214,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_Ext-4R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(7.82e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(42274.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_Ext-4R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_Ext-4R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_Ext-4R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-4R!H-R_Ext-6R!H-R_N-3R!H-inRing_Ext-4R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 215,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H",
    kinetics = ArrheniusBM(A=(17015.3,'s^-1'), n=1.99916, w0=(301000,'J/mol'), E0=(49608.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11374458513228063, var=0.5556155968396796, Tref=1000.0, N=12, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H',), comment="""BM rule fitted to 12 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H
    Total Standard Deviation in ln(k): 1.7801124605842489"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H
Total Standard Deviation in ln(k): 1.7801124605842489""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H
Total Standard Deviation in ln(k): 1.7801124605842489
""",
)

entry(
    index = 216,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H",
    kinetics = ArrheniusBM(A=(5959.46,'s^-1'), n=1.97469, w0=(297769,'J/mol'), E0=(50486.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22886448915297658, var=0.8976856510574576, Tref=1000.0, N=13, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H',), comment="""BM rule fitted to 13 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H
    Total Standard Deviation in ln(k): 2.4744482021051213"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H
Total Standard Deviation in ln(k): 2.4744482021051213""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H
Total Standard Deviation in ln(k): 2.4744482021051213
""",
)

entry(
    index = 217,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.04e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(68008,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 218,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(2.57e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(57641.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 219,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(9.50689e+07,'s^-1'), n=0.824298, w0=(301000,'J/mol'), E0=(50919.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.007199520277616862, var=0.26525797984840893, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 1.0505919999456534"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 1.0505919999456534""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 1.0505919999456534
""",
)

entry(
    index = 220,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.85e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(54245.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 221,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.39707e+08,'s^-1'), n=0.871081, w0=(301000,'J/mol'), E0=(52662.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.006076656226940492, var=0.059162380386821777, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 0.5028860706020695"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 0.5028860706020695""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 0.5028860706020695
""",
)

entry(
    index = 222,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(2.21125e+08,'s^-1'), n=0.878781, w0=(301000,'J/mol'), E0=(53251.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.505122006297413e-05, var=0.9050939833988869, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 1.9074470296389483"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 1.9074470296389483""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 1.9074470296389483
""",
)

entry(
    index = 223,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(3.65e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(60423.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 224,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(3.84e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(58905.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 225,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.43504e+08,'s^-1'), n=1.29878, w0=(301000,'J/mol'), E0=(108235,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05769530058750815, var=2.5860788294641344, Tref=1000.0, N=24, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 24 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 3.368835650178335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 3.368835650178335""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 3.368835650178335
""",
)

entry(
    index = 226,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(9.3079e+09,'s^-1'), n=0.700553, w0=(301000,'J/mol'), E0=(93180.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03082119755829786, var=0.7930055447838621, Tref=1000.0, N=6, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 6 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.8626739973714708"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.8626739973714708""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.8626739973714708
""",
)

entry(
    index = 227,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.02838e+09,'s^-1'), n=1.09383, w0=(301000,'J/mol'), E0=(98048.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0043798771231796565, var=0.2697470048713491, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 1.0522074628572957"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 1.0522074628572957""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 1.0522074628572957
""",
)

entry(
    index = 228,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.99e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(98457,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 229,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(5.24776e+07,'s^-1'), n=1.17062, w0=(301000,'J/mol'), E0=(97304,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0015495595210675802, var=0.21284924432544747, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 0.9287896734223493"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 0.9287896734223493""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 0.9287896734223493
""",
)

entry(
    index = 230,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(4.88511e+07,'s^-1'), n=1.25321, w0=(301000,'J/mol'), E0=(97882.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.4402099292645639e-05, var=0.8893022089370891, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 1.8905579220764255"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 1.8905579220764255""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 1.8905579220764255
""",
)

entry(
    index = 231,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(3.52e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(106809,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 232,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(8.7e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(105313,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 233,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(6.50717e+06,'s^-1'), n=1.46029, w0=(301000,'J/mol'), E0=(78265.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06455769306516719, var=1.9544163491935767, Tref=1000.0, N=12, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 12 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 2.964833751526106"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.964833751526106""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.964833751526106
""",
)

entry(
    index = 234,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(9.3589e+06,'s^-1'), n=1.48843, w0=(301000,'J/mol'), E0=(81410.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.008428242825661465, var=0.16690778623452038, Tref=1000.0, N=8, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 8 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 0.8401979619485163"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.8401979619485163""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.8401979619485163
""",
)

entry(
    index = 235,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(3.44661e+07,'s^-1'), n=1.40448, w0=(301000,'J/mol'), E0=(77662.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.002861795074378164, var=0.014501203085819047, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 0.24860252481447878"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 0.24860252481447878""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 0.24860252481447878
""",
)

entry(
    index = 236,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(2.54e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(86097.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 237,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(8.78e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(77867.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 238,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(3.56e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(82883.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 239,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(8.8e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(72540.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 240,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(7.92793e+07,'s^-1'), n=1.06329, w0=(301000,'J/mol'), E0=(66904.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0906552764315988, var=0.3918379920356758, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 1.4826803740897867"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 1.4826803740897867""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 1.4826803740897867
""",
)

entry(
    index = 241,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(6.32e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(67583,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 242,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(1.50896e+08,'s^-1'), n=1.07425, w0=(301000,'J/mol'), E0=(68837.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.617130642308806, var=4.172426419855754, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 8.158118053220699"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 8.158118053220699""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 8.158118053220699
""",
)

entry(
    index = 243,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(1.87143e+08,'s^-1'), n=1.11371, w0=(301000,'J/mol'), E0=(69162.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.8935090526494047, var=0.7479513311358108, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 9.003901931573196"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 9.003901931573196""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 9.003901931573196
""",
)

entry(
    index = 244,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.25e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 245,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.31e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-7R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 246,
    label = "Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_Sp-3R!H-1R!H_2R!H-inRing",
    kinetics = ArrheniusBM(A=(1e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_Sp-3R!H-1R!H_2R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_Sp-3R!H-1R!H_2R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_Sp-3R!H-1R!H_2R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_Sp-3R!H-1R!H_2R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 247,
    label = "Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_Sp-3R!H-1R!H_N-2R!H-inRing",
    kinetics = ArrheniusBM(A=(2.5578e+10,'s^-1'), n=0.210583, w0=(301000,'J/mol'), E0=(95259.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_Sp-3R!H-1R!H_N-2R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_Sp-3R!H-1R!H_N-2R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_Sp-3R!H-1R!H_N-2R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_Sp-3R!H-1R!H_N-2R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 248,
    label = "Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_N-Sp-3R!H-1R!H_4R!H-inRing",
    kinetics = ArrheniusBM(A=(4.36e+10,'s^-1'), n=0.44, w0=(301000,'J/mol'), E0=(131415,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_N-Sp-3R!H-1R!H_4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_N-Sp-3R!H-1R!H_4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_N-Sp-3R!H-1R!H_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_N-Sp-3R!H-1R!H_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 249,
    label = "Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_N-Sp-3R!H-1R!H_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(2.27101e+07,'s^-1'), n=1.42496, w0=(301000,'J/mol'), E0=(110897,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.215402716989285, var=61.8043701559801, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_N-Sp-3R!H-1R!H_N-4R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_N-Sp-3R!H-1R!H_N-4R!H-inRing
    Total Standard Deviation in ln(k): 28.86440319929974"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_N-Sp-3R!H-1R!H_N-4R!H-inRing
Total Standard Deviation in ln(k): 28.86440319929974""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone4_N-Sp-5R!H-2R!H_Sp-2R!H-1R!H_N-3R!H-inRing_6R!H->C_N-Sp-3R!H-1R!H_N-4R!H-inRing
Total Standard Deviation in ln(k): 28.86440319929974
""",
)

entry(
    index = 250,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.45779e+12,'s^-1'), n=0.165319, w0=(301000,'J/mol'), E0=(34792.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.002824999359713774, var=0.3054684672867636, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 1.1150990647750283"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 1.1150990647750283""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 1.1150990647750283
""",
)

entry(
    index = 251,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.05736e+14,'s^-1'), n=-0.253437, w0=(301000,'J/mol'), E0=(26567.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.009383546652767203, var=0.32125941092383564, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 1.159855589109769"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 1.159855589109769""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 1.159855589109769
""",
)

entry(
    index = 252,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.05731e+10,'s^-1'), n=0.94173, w0=(301000,'J/mol'), E0=(31241.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.008711706330767403, var=0.5260663532288169, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H_Sp-8R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 1.475931716789591"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 1.475931716789591""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 1.475931716789591
""",
)

entry(
    index = 253,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(5.34661e+10,'s^-1'), n=0.608246, w0=(301000,'J/mol'), E0=(26719.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.011819111914780243, var=0.5425275801653988, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 1.506313383088425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 1.506313383088425""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 1.506313383088425
""",
)

entry(
    index = 254,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(9.49154e+09,'s^-1'), n=0.958426, w0=(301000,'J/mol'), E0=(31729.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00935209196786196, var=0.053141540759598455, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.48563825098692154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.48563825098692154""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.48563825098692154
""",
)

entry(
    index = 255,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(7.17e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(38069.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 256,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(2.48e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(30177.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 257,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(5.88e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(27110.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 258,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(6.19e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(25322.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 259,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.41e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(20651.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 260,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.48e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(20956.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 261,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(7.76234e+09,'s^-1'), n=0.720911, w0=(301000,'J/mol'), E0=(71440.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.007859345131137351, var=0.29201132213759073, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 4 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 1.1030672820901808"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 1.1030672820901808""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 1.1030672820901808
""",
)

entry(
    index = 262,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(9.83334e+10,'s^-1'), n=0.516815, w0=(301000,'J/mol'), E0=(62536.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.014136938914754524, var=0.29156076050454716, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 4 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 1.1180040485930356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 1.1180040485930356""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 1.1180040485930356
""",
)

entry(
    index = 263,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.93409e+08,'s^-1'), n=1.34583, w0=(301000,'J/mol'), E0=(67977.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.002103544109509488, var=0.07140553614019061, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.5409868720150801"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.5409868720150801""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.5409868720150801
""",
)

entry(
    index = 264,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(2.84e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(76269.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 265,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(9.8e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(68951.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 266,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_Sp-9R!H#8R!H",
    kinetics = ArrheniusBM(A=(2.6145e+08,'s^-1'), n=1.18012, w0=(301000,'J/mol'), E0=(62325,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.001630461308314668, var=0.39541936686895485, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_Sp-9R!H#8R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_Sp-9R!H#8R!H
    Total Standard Deviation in ln(k): 1.264721758516651"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_Sp-9R!H#8R!H
Total Standard Deviation in ln(k): 1.264721758516651""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_Sp-9R!H#8R!H
Total Standard Deviation in ln(k): 1.264721758516651
""",
)

entry(
    index = 267,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_N-Sp-9R!H#8R!H",
    kinetics = ArrheniusBM(A=(1.60193e+06,'s^-1'), n=1.81052, w0=(287000,'J/mol'), E0=(47735.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6861034150008943, var=1.2475211295547142, Tref=1000.0, N=3, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_N-Sp-9R!H#8R!H',), comment="""BM rule fitted to 3 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_N-Sp-9R!H#8R!H
    Total Standard Deviation in ln(k): 3.963016360829476"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_N-Sp-9R!H#8R!H
Total Standard Deviation in ln(k): 3.963016360829476""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_N-Sp-9R!H#8R!H
Total Standard Deviation in ln(k): 3.963016360829476
""",
)

entry(
    index = 268,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.32e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(66041.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 269,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.45e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(64261.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-4R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 270,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R_Sp-8R!H=7R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.57e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(57603.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R_Sp-8R!H=7R!H_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R_Sp-8R!H=7R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R_Sp-8R!H=7R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R_Sp-8R!H=7R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 271,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R_N-Sp-8R!H=7R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.38e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(44740.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R_N-Sp-8R!H=7R!H_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R_N-Sp-8R!H=7R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R_N-Sp-8R!H=7R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-4R!H-R_Ext-7R!H-R_Ext-4R!H-R_N-Sp-8R!H=7R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 272,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(3.81255e+06,'s^-1'), n=1.31385, w0=(301000,'J/mol'), E0=(58008.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.037457304726456704, var=0.2884091770286139, Tref=1000.0, N=8, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R',), comment="""BM rule fitted to 8 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R
    Total Standard Deviation in ln(k): 1.1707315596110726"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R
Total Standard Deviation in ln(k): 1.1707315596110726""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R
Total Standard Deviation in ln(k): 1.1707315596110726
""",
)

entry(
    index = 273,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(7.6404e+07,'s^-1'), n=1.00724, w0=(301000,'J/mol'), E0=(54520.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004335350325531904, var=1.3453127771217215, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 2.336137324399147"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.336137324399147""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.336137324399147
""",
)

entry(
    index = 274,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.7e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(56996.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 275,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.31807e+06,'s^-1'), n=1.24678, w0=(301000,'J/mol'), E0=(65266.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04639569926383342, var=0.7250907798709153, Tref=1000.0, N=6, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R',), comment="""BM rule fitted to 6 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.8236493830393776"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.8236493830393776""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.8236493830393776
""",
)

entry(
    index = 276,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_3R!H-inRing",
    kinetics = ArrheniusBM(A=(905.58,'s^-1'), n=2.15236, w0=(259000,'J/mol'), E0=(45992.7,'J/mol'), Tmin=(500,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_3R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_3R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 277,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(35855.9,'s^-1'), n=2.02638, w0=(301000,'J/mol'), E0=(59722.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06702113713073807, var=0.5738314479334877, Tref=1000.0, N=6, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing',), comment="""BM rule fitted to 6 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing
    Total Standard Deviation in ln(k): 1.687014981025298"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing
Total Standard Deviation in ln(k): 1.687014981025298""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing
Total Standard Deviation in ln(k): 1.687014981025298
""",
)

entry(
    index = 278,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_Sp-10R!H=8R!H",
    kinetics = ArrheniusBM(A=(7.10982e+07,'s^-1'), n=0.827664, w0=(301000,'J/mol'), E0=(50519.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.006628096165220685, var=0.055879889834976666, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_Sp-10R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_Sp-10R!H=8R!H
    Total Standard Deviation in ln(k): 0.49055138158503936"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_Sp-10R!H=8R!H
Total Standard Deviation in ln(k): 0.49055138158503936""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_Sp-10R!H=8R!H
Total Standard Deviation in ln(k): 0.49055138158503936
""",
)

entry(
    index = 279,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-Sp-10R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.07733e+08,'s^-1'), n=0.84137, w0=(301000,'J/mol'), E0=(51078.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=9.37264270386929e-05, var=0.8994028476387768, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-Sp-10R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-Sp-10R!H=8R!H
    Total Standard Deviation in ln(k): 1.9014631296685192"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-Sp-10R!H=8R!H
Total Standard Deviation in ln(k): 1.9014631296685192""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-Sp-10R!H=8R!H
Total Standard Deviation in ln(k): 1.9014631296685192
""",
)

entry(
    index = 280,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.44e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(59817.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 281,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.57e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(58299.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 282,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.89295e+10,'s^-1'), n=0.502775, w0=(301000,'J/mol'), E0=(110451,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.001646225347934208, var=1.2381673593032931, Tref=1000.0, N=12, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 12 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 2.2348644824568855"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.2348644824568855""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.2348644824568855
""",
)

entry(
    index = 283,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(3.46293e-31,'s^-1'), n=12.3908, w0=(301000,'J/mol'), E0=(7780.12,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0880277491929553, var=0.2896956848542018, Tref=1000.0, N=8, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 8 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 3.812754356329574"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 3.812754356329574""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 3.812754356329574
""",
)

entry(
    index = 284,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.65829e+10,'s^-1'), n=0.74359, w0=(301000,'J/mol'), E0=(111961,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0006744569604873945, var=27.78777288760903, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 10.569476956152398"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 10.569476956152398""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 10.569476956152398
""",
)

entry(
    index = 285,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(2.52e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(106383,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 286,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(8.69e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(129154,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 287,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.81201e+10,'s^-1'), n=0.606214, w0=(301000,'J/mol'), E0=(96764.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.008639217752073316, var=0.2712907275995352, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 1.065884398981816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 1.065884398981816""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 1.065884398981816
""",
)

entry(
    index = 288,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(6.25e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(91018.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 289,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R_Sp-9R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.11616e+09,'s^-1'), n=1.04653, w0=(301000,'J/mol'), E0=(97785.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0014286204878767815, var=0.21735111994079787, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R_Sp-9R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R_Sp-9R!H=7R!H
    Total Standard Deviation in ln(k): 0.9382156541797062"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R_Sp-9R!H=7R!H
Total Standard Deviation in ln(k): 0.9382156541797062""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R_Sp-9R!H=7R!H
Total Standard Deviation in ln(k): 0.9382156541797062
""",
)

entry(
    index = 290,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R_N-Sp-9R!H=7R!H",
    kinetics = ArrheniusBM(A=(9.38343e+08,'s^-1'), n=1.14235, w0=(301000,'J/mol'), E0=(98301.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3090081934027647e-05, var=0.8874136788859341, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R_N-Sp-9R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R_N-Sp-9R!H=7R!H
    Total Standard Deviation in ln(k): 1.8885461943478408"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R_N-Sp-9R!H=7R!H
Total Standard Deviation in ln(k): 1.8885461943478408""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R_N-Sp-9R!H=7R!H
Total Standard Deviation in ln(k): 1.8885461943478408
""",
)

entry(
    index = 291,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.23e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(108227,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 292,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.3e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(106544,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 293,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(4.23775e+06,'s^-1'), n=1.45945, w0=(301000,'J/mol'), E0=(83591.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05489579616661873, var=0.6358345826629968, Tref=1000.0, N=6, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 6 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 1.7364895792794346"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 1.7364895792794346""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 1.7364895792794346
""",
)

entry(
    index = 294,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.79815e+07,'s^-1'), n=1.38809, w0=(301000,'J/mol'), E0=(73579.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06697024731674808, var=0.6116208133908813, Tref=1000.0, N=6, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 6 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 1.7360938740650607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 1.7360938740650607""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 1.7360938740650607
""",
)

entry(
    index = 295,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(8.37988e+06,'s^-1'), n=1.46712, w0=(301000,'J/mol'), E0=(81071.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.012254835381840924, var=0.043829812330994616, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H',), comment="""BM rule fitted to 4 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 0.4504937744772678"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 0.4504937744772678""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 0.4504937744772678
""",
)

entry(
    index = 296,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(9.7958e+06,'s^-1'), n=1.51781, w0=(301000,'J/mol'), E0=(81675.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00394350533801648, var=0.26588919391311044, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H',), comment="""BM rule fitted to 4 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 1.0436388117175908"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 1.0436388117175908""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 1.0436388117175908
""",
)

entry(
    index = 297,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(4.26e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(87106.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 298,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.47e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(78833.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-7R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 299,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H",
    kinetics = ArrheniusBM(A=(6.92367e+07,'s^-1'), n=1.04664, w0=(301000,'J/mol'), E0=(66680.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.4925162221107378, var=3.5077320291177814, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H
    Total Standard Deviation in ln(k): 7.504697107358476"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H
Total Standard Deviation in ln(k): 7.504697107358476""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H
Total Standard Deviation in ln(k): 7.504697107358476
""",
)

entry(
    index = 300,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H",
    kinetics = ArrheniusBM(A=(7.86506e+07,'s^-1'), n=1.09755, w0=(301000,'J/mol'), E0=(66921.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.009100361533732e-05, var=0.9010269015666957, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H
    Total Standard Deviation in ln(k): 1.903119495700503"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H
Total Standard Deviation in ln(k): 1.903119495700503""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H
Total Standard Deviation in ln(k): 1.903119495700503
""",
)

entry(
    index = 301,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(8.34e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 302,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(8.79e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 303,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(6.54886e+12,'s^-1'), n=-0.0661714, w0=(301000,'J/mol'), E0=(35581.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02642234269757725, var=0.7420036436692553, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 1.7932592413801394"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.7932592413801394""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.7932592413801394
""",
)

entry(
    index = 304,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(2.53072e+11,'s^-1'), n=0.428141, w0=(301000,'J/mol'), E0=(33722.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00013200834821081278, var=0.8720616725206921, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 1.8724383430518639"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.8724383430518639""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.8724383430518639
""",
)

entry(
    index = 305,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(9.15065e+14,'s^-1'), n=-0.568565, w0=(301000,'J/mol'), E0=(28183.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2684916712269394, var=0.3767678850193292, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 1.9051370678171433"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.9051370678171433""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.9051370678171433
""",
)

entry(
    index = 306,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(4.88921e+12,'s^-1'), n=0.177787, w0=(301000,'J/mol'), E0=(23733.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06085811911567928, var=0.7130579319742886, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 1.8457634299772712"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.8457634299772712""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 1.8457634299772712
""",
)

entry(
    index = 307,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H_Sp-8R!H=7R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.97e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(41400.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H_Sp-8R!H=7R!H_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H_Sp-8R!H=7R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H_Sp-8R!H=7R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H_Sp-8R!H=7R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 308,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H_N-Sp-8R!H=7R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.37e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(33518.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H_N-Sp-8R!H=7R!H_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H_N-Sp-8R!H=7R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H_N-Sp-8R!H=7R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-6R!H=5R!H_N-Sp-8R!H=7R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 309,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(4.18e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(39168.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 310,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.44e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(31236,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-6R!H=5R!H_Ext-4R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 311,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.37067e+10,'s^-1'), n=0.608329, w0=(301000,'J/mol'), E0=(71355.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0030876277936222954, var=0.4586707173014343, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.3654693592160811"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.3654693592160811""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.3654693592160811
""",
)

entry(
    index = 312,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(4.31333e+09,'s^-1'), n=0.835853, w0=(301000,'J/mol'), E0=(71505,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.0552258378830456e-05, var=0.8884441047129247, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.8896610548317974"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8896610548317974""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8896610548317974
""",
)

entry(
    index = 313,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.86114e+11,'s^-1'), n=0.395679, w0=(301000,'J/mol'), E0=(62519.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.004503469261866359, var=0.49343132701207126, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.4195347327705414"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.4195347327705414""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.4195347327705414
""",
)

entry(
    index = 314,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(5.10234e+10,'s^-1'), n=0.640204, w0=(301000,'J/mol'), E0=(62533.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.785108394242037e-05, var=0.8700046154270793, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.8699673343515257"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8699673343515257""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.8699673343515257
""",
)

entry(
    index = 315,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_Ext-5R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.65e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(77298.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_Ext-5R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_Ext-5R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_Ext-5R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_Ext-5R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 316,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_Ext-5R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(5.71e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(69980.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_Ext-5R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_Ext-5R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_Ext-5R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Sp-7R!H#6R!H_Ext-5R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 317,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_Sp-9R!H#8R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.42e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(71976.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_Sp-9R!H#8R!H_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_Sp-9R!H#8R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_Sp-9R!H#8R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_Sp-9R!H#8R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 318,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_N-Sp-9R!H#8R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.57e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(79326.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_N-Sp-9R!H#8R!H_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_N-Sp-9R!H#8R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_N-Sp-9R!H#8R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_N-Sp-9R!H#8R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 319,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_N-Sp-9R!H#8R!H_2R!H-inRing",
    kinetics = ArrheniusBM(A=(966131,'s^-1'), n=1.86605, w0=(259000,'J/mol'), E0=(46209.4,'J/mol'), Tmin=(500,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_N-Sp-9R!H#8R!H_2R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_N-Sp-9R!H#8R!H_2R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_N-Sp-9R!H#8R!H_2R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_N-Sp-9R!H#8R!H_2R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 320,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_N-Sp-9R!H#8R!H_N-2R!H-inRing",
    kinetics = ArrheniusBM(A=(1.31e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(73987.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_N-Sp-9R!H#8R!H_N-2R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_N-Sp-9R!H#8R!H_N-2R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_N-Sp-9R!H#8R!H_N-2R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_N-Sp-7R!H#6R!H_N-Sp-9R!H#8R!H_N-2R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 321,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(3.26151e+06,'s^-1'), n=1.29785, w0=(301000,'J/mol'), E0=(57585.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.038981653018100214, var=0.2427754571706571, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_Sp-10R!H=9R!H',), comment="""BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 1.0857219211383389"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 1.0857219211383389""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 1.0857219211383389
""",
)

entry(
    index = 322,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_N-Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(4.22676e+06,'s^-1'), n=1.33647, w0=(301000,'J/mol'), E0=(58373.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03040356423953785, var=0.459863304797006, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_N-Sp-10R!H=9R!H',), comment="""BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_N-Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 1.4358663090266564"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 1.4358663090266564""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 1.4358663090266564
""",
)

entry(
    index = 323,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-6R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(4.53e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(58275,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-6R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-6R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 324,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(3.01001e+07,'s^-1'), n=0.960546, w0=(301000,'J/mol'), E0=(70385.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.007515431790619958, var=0.2706683011681045, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 1.0618622918136504"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 1.0618622918136504""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 1.0618622918136504
""",
)

entry(
    index = 325,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.83e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(68626,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 326,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(2.78095e+06,'s^-1'), n=1.47367, w0=(301000,'J/mol'), E0=(66943.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.003466253385273873, var=0.26959123603956786, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R
    Total Standard Deviation in ln(k): 1.0496112545436895"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R
Total Standard Deviation in ln(k): 1.0496112545436895""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R
Total Standard Deviation in ln(k): 1.0496112545436895
""",
)

entry(
    index = 327,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.25e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(72736.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 328,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_Sp-10R!H=8R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(7.65e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(55650.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_Sp-10R!H=8R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_Sp-10R!H=8R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_Sp-10R!H=8R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_Sp-10R!H=8R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 329,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-Sp-10R!H=8R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(8.06e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(54131.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-Sp-10R!H=8R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-Sp-10R!H=8R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-Sp-10R!H=8R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-Sp-10R!H=8R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 330,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(3.12461e+10,'s^-1'), n=0.507267, w0=(301000,'J/mol'), E0=(110151,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.008683364703926014, var=1.1337785468287422, Tref=1000.0, N=6, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 6 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 2.156440117983874"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 2.156440117983874""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 2.156440117983874
""",
)

entry(
    index = 331,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.52268e+11,'s^-1'), n=0.459106, w0=(301000,'J/mol'), E0=(111088,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.008839361369264435, var=1.0158248423153633, Tref=1000.0, N=6, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 6 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 2.0427445733647125"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 2.0427445733647125""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 2.0427445733647125
""",
)

entry(
    index = 332,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H",
    kinetics = ArrheniusBM(A=(2.89438e-31,'s^-1'), n=12.3812, w0=(301000,'J/mol'), E0=(7454.94,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.257987016416666, var=3.075482062543156, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H',), comment="""BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H
    Total Standard Deviation in ln(k): 4.163922990421162"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H
Total Standard Deviation in ln(k): 4.163922990421162""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H
Total Standard Deviation in ln(k): 4.163922990421162
""",
)

entry(
    index = 333,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H",
    kinetics = ArrheniusBM(A=(4.17241e-31,'s^-1'), n=12.3996, w0=(301000,'J/mol'), E0=(8122.16,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5786360701422935, var=5.022146569663627, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H',), comment="""BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H
    Total Standard Deviation in ln(k): 5.946500109445089"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H
Total Standard Deviation in ln(k): 5.946500109445089""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H
Total Standard Deviation in ln(k): 5.946500109445089
""",
)

entry(
    index = 334,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(4.22e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(107958,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 335,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.46e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(130267,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 336,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H",
    kinetics = ArrheniusBM(A=(2.06032e+10,'s^-1'), n=0.552706, w0=(301000,'J/mol'), E0=(96525,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0012691947758164508, var=0.2324833106962551, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H
    Total Standard Deviation in ln(k): 0.969802484761105"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H
Total Standard Deviation in ln(k): 0.969802484761105""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H
Total Standard Deviation in ln(k): 0.969802484761105
""",
)

entry(
    index = 337,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.58218e+10,'s^-1'), n=0.660626, w0=(301000,'J/mol'), E0=(96996.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1417269561725212e-05, var=0.8858049272061354, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H
    Total Standard Deviation in ln(k): 1.8868294150796763"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H
Total Standard Deviation in ln(k): 1.8868294150796763""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H
Total Standard Deviation in ln(k): 1.8868294150796763
""",
)

entry(
    index = 338,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R_Sp-9R!H=7R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(8.25e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(106134,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R_Sp-9R!H=7R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R_Sp-9R!H=7R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R_Sp-9R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R_Sp-9R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 339,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R_N-Sp-9R!H=7R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(8.69e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(104437,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R_N-Sp-9R!H=7R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R_N-Sp-9R!H=7R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R_N-Sp-9R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-7R!H-R_N-Sp-9R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 340,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(4.76006e+07,'s^-1'), n=1.1429, w0=(301000,'J/mol'), E0=(88475.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.013339900589089359, var=0.27095436672861695, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R
    Total Standard Deviation in ln(k): 1.0770476451301758"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R
Total Standard Deviation in ln(k): 1.0770476451301758""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R
Total Standard Deviation in ln(k): 1.0770476451301758
""",
)

entry(
    index = 341,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(6.26e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(83355.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 342,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(3.71471e+08,'s^-1'), n=0.995327, w0=(301000,'J/mol'), E0=(79063.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01743622032923233, var=0.2700782456349628, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R
    Total Standard Deviation in ln(k): 1.085651431119483"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R
Total Standard Deviation in ln(k): 1.085651431119483""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R
Total Standard Deviation in ln(k): 1.085651431119483
""",
)

entry(
    index = 343,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.55e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(73006,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 344,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(5.6373e+06,'s^-1'), n=1.58478, w0=(301000,'J/mol'), E0=(84603.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.002302280790385527, var=0.16352594002320128, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 0.8164662262426715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 0.8164662262426715""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 0.8164662262426715
""",
)

entry(
    index = 345,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.09592e+07,'s^-1'), n=1.36506, w0=(301000,'J/mol'), E0=(77311.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0029027673037737623, var=0.14365025671620152, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 0.7671124610015203"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 0.7671124610015203""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 0.7671124610015203
""",
)

entry(
    index = 346,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.08325e+07,'s^-1'), n=1.48446, w0=(301000,'J/mol'), E0=(83501,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005469175823717591, var=0.0022147313604411367, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 0.1080863497998224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 0.1080863497998224""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 0.1080863497998224
""",
)

entry(
    index = 347,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(3.19e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(90487.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 348,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.1e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(81381.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 349,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(2.62e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 350,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(2.76e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(67511.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 351,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Sp-6R!H=5R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(5.82e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(33559.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Sp-6R!H=5R!H_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Sp-6R!H=5R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 352,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_N-Sp-6R!H=5R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(6.13e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(30801.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_N-Sp-6R!H=5R!H_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_N-Sp-6R!H=5R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_N-Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_N-Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 353,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Sp-6R!H=5R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.44e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(19820.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Sp-6R!H=5R!H_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Sp-6R!H=5R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 354,
    label = "Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_N-Sp-6R!H=5R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.52e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(12471.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_N-Sp-6R!H=5R!H_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_N-Sp-6R!H=5R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_N-Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone1_Sp-4R!H=1R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_N-Sp-6R!H=5R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 355,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H_Sp-7R!H=6R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.3e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(73899.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H_Sp-7R!H=6R!H_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H_Sp-7R!H=6R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H_Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H_Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 356,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H_N-Sp-7R!H=6R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.43e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(71800.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H_N-Sp-7R!H=6R!H_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H_N-Sp-7R!H=6R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H_N-Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_Sp-9R!H=8R!H_N-Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 357,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H_Sp-7R!H=6R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.7e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(63112.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H_Sp-7R!H=6R!H_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H_Sp-7R!H=6R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H_Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H_Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 358,
    label = "Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H_N-Sp-7R!H=6R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(6.01e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(60899.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H_N-Sp-7R!H=6R!H_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H_N-Sp-7R!H=6R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H_N-Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone2_N-Sp-3R!H=1R!H_Ext-5R!H-R_Ext-6R!H-R_Ext-4R!H-R_Ext-8R!H-R_Ext-4R!H-R_N-Sp-9R!H=8R!H_N-Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 359,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.42547e+08,'s^-1'), n=0.774458, w0=(301000,'J/mol'), E0=(60866.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.002453640201206386, var=0.19510916919030544, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.891679735485539"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.891679735485539""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.891679735485539
""",
)

entry(
    index = 360,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.78e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(70652,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 361,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5.65297e+06,'s^-1'), n=1.2792, w0=(301000,'J/mol'), E0=(60396.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.009941611089130628, var=0.7189757867974458, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.7248427084349112"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.7248427084349112""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.7248427084349112
""",
)

entry(
    index = 362,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.39e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(63160.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 363,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H",
    kinetics = ArrheniusBM(A=(3.22094e+07,'s^-1'), n=0.91507, w0=(301000,'J/mol'), E0=(70114.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.001958562972609079, var=0.2048680495255573, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H
    Total Standard Deviation in ln(k): 0.9123112569426003"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H
Total Standard Deviation in ln(k): 0.9123112569426003""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H
Total Standard Deviation in ln(k): 0.9123112569426003
""",
)

entry(
    index = 364,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H",
    kinetics = ArrheniusBM(A=(2.76348e+07,'s^-1'), n=1.00824, w0=(301000,'J/mol'), E0=(70638,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.9237866958175902e-05, var=0.9015424868757916, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H
    Total Standard Deviation in ln(k): 1.9035360969473443"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H
Total Standard Deviation in ln(k): 1.9035360969473443""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H
Total Standard Deviation in ln(k): 1.9035360969473443
""",
)

entry(
    index = 365,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R_Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(2.70902e+06,'s^-1'), n=1.4406, w0=(301000,'J/mol'), E0=(66622.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0023353600125229266, var=0.1792391491342366, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R_Sp-10R!H=9R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R_Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 0.8546053072484454"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 0.8546053072484454""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 0.8546053072484454
""",
)

entry(
    index = 366,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R_N-Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(2.78519e+06,'s^-1'), n=1.50985, w0=(301000,'J/mol'), E0=(67238.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.390690160553946e-05, var=0.907081489862618, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R_N-Sp-10R!H=9R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R_N-Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 1.9093863103581328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 1.9093863103581328""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 1.9093863103581328
""",
)

entry(
    index = 367,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.98707e+09,'s^-1'), n=0.841553, w0=(301000,'J/mol'), E0=(111012,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.008643128607831852, var=0.2796782061625515, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 1.081912747197264"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 1.081912747197264""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 1.081912747197264
""",
)

entry(
    index = 368,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(6.19e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(107760,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 369,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(3.14797e+10,'s^-1'), n=0.64509, w0=(301000,'J/mol'), E0=(112851,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.012026013089026101, var=0.27806838538294565, Tref=1000.0, N=4, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R',), comment="""BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 1.0873568217067464"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 1.0873568217067464""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 1.0873568217067464
""",
)

entry(
    index = 370,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.53e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(106163,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 371,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(4.15903e+09,'s^-1'), n=0.931907, w0=(301000,'J/mol'), E0=(107967,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00010568628826577421, var=0.3096862221937616, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 1.1158897566730914"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 1.1158897566730914""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 1.1158897566730914
""",
)

entry(
    index = 372,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.31015e+09,'s^-1'), n=0.971716, w0=(301000,'J/mol'), E0=(128869,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0013158293062599836, var=0.21638386491865935, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 0.935850305738076"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 0.935850305738076""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 0.935850305738076
""",
)

entry(
    index = 373,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.26184e-31,'s^-1'), n=12.5219, w0=(301000,'J/mol'), E0=(8164.21,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.031394714063420245, var=22.77648537480469, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 9.64642245592732"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 9.64642245592732""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 9.64642245592732
""",
)

entry(
    index = 374,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(3.16e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(115473,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 375,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.09e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(134903,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 376,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.59e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(99243.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 377,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.73e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(97525.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 378,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R_Sp-12R!H=10R!H",
    kinetics = ArrheniusBM(A=(5.3888e+07,'s^-1'), n=1.09049, w0=(301000,'J/mol'), E0=(88290.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.002018200306894346, var=0.18289294178347487, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R_Sp-12R!H=10R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R_Sp-12R!H=10R!H
    Total Standard Deviation in ln(k): 0.8624155445959527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R_Sp-12R!H=10R!H
Total Standard Deviation in ln(k): 0.8624155445959527""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R_Sp-12R!H=10R!H
Total Standard Deviation in ln(k): 0.8624155445959527
""",
)

entry(
    index = 379,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R_N-Sp-12R!H=10R!H",
    kinetics = ArrheniusBM(A=(4.04643e+07,'s^-1'), n=1.20007, w0=(301000,'J/mol'), E0=(88618.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.039451428145079e-05, var=0.9082383871948089, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R_N-Sp-12R!H=10R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R_N-Sp-12R!H=10R!H
    Total Standard Deviation in ln(k): 1.9105946805222214"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R_N-Sp-12R!H=10R!H
Total Standard Deviation in ln(k): 1.9105946805222214""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R_N-Sp-12R!H=10R!H
Total Standard Deviation in ln(k): 1.9105946805222214
""",
)

entry(
    index = 380,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R_Sp-12R!H=10R!H",
    kinetics = ArrheniusBM(A=(3.88014e+08,'s^-1'), n=0.953541, w0=(301000,'J/mol'), E0=(78823,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0024160280265359537, var=0.17348811084398766, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R_Sp-12R!H=10R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R_Sp-12R!H=10R!H
    Total Standard Deviation in ln(k): 0.8410807524563301"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R_Sp-12R!H=10R!H
Total Standard Deviation in ln(k): 0.8410807524563301""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R_Sp-12R!H=10R!H
Total Standard Deviation in ln(k): 0.8410807524563301
""",
)

entry(
    index = 381,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R_N-Sp-12R!H=10R!H",
    kinetics = ArrheniusBM(A=(3.38245e+08,'s^-1'), n=1.04334, w0=(301000,'J/mol'), E0=(79248,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.495444613003688e-05, var=0.906041652794281, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R_N-Sp-12R!H=10R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R_N-Sp-12R!H=10R!H
    Total Standard Deviation in ln(k): 1.90829424606997"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R_N-Sp-12R!H=10R!H
Total Standard Deviation in ln(k): 1.90829424606997""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R_N-Sp-12R!H=10R!H
Total Standard Deviation in ln(k): 1.90829424606997
""",
)

entry(
    index = 382,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Sp-9R!H=8R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.77e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(93233.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Sp-9R!H=8R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Sp-9R!H=8R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Sp-9R!H=8R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_Sp-9R!H=8R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 383,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_N-Sp-9R!H=8R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(6.09e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(84125,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_N-Sp-9R!H=8R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_N-Sp-9R!H=8R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_N-Sp-9R!H=8R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H_N-Sp-9R!H=8R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 384,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-7R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.86e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(91607.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-7R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-7R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-7R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-7R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 385,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-7R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(6.42e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(82532.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-7R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-7R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-7R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H_Ext-7R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 386,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-5R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.88e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(65914.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-5R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-5R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 387,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-6R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.98e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(64292.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-6R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-6R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-8R!H#7R!H_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 388,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(7.58e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(76401,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 389,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(7.99e+09,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(74763,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_Ext-5R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 390,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5.16e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(79568.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 391,
    label = "Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5.44e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(77967.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_Sp-4R!H-1R!H_Ext-5R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-8R!H#7R!H_N-3R!H-inRing_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 392,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R_Sp-11R!H=7R!H",
    kinetics = ArrheniusBM(A=(2.48742e+09,'s^-1'), n=0.774406, w0=(301000,'J/mol'), E0=(110749,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.3550410155276123e-05, var=0.3223210820729283, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R_Sp-11R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R_Sp-11R!H=7R!H
    Total Standard Deviation in ln(k): 1.1382140014737567"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R_Sp-11R!H=7R!H
Total Standard Deviation in ln(k): 1.1382140014737567""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R_Sp-11R!H=7R!H
Total Standard Deviation in ln(k): 1.1382140014737567
""",
)

entry(
    index = 393,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R_N-Sp-11R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.59265e+09,'s^-1'), n=0.908286, w0=(301000,'J/mol'), E0=(111278,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.049473537862893e-08, var=0.8869413213547774, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R_N-Sp-11R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R_N-Sp-11R!H=7R!H
    Total Standard Deviation in ln(k): 1.8880108258134873"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R_N-Sp-11R!H=7R!H
Total Standard Deviation in ln(k): 1.8880108258134873""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R_N-Sp-11R!H=7R!H
Total Standard Deviation in ln(k): 1.8880108258134873
""",
)

entry(
    index = 394,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R_Sp-11R!H=7R!H",
    kinetics = ArrheniusBM(A=(3.87983e+10,'s^-1'), n=0.58032, w0=(301000,'J/mol'), E0=(112613,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0003577090102497314, var=0.29186446398988997, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R_Sp-11R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R_Sp-11R!H=7R!H
    Total Standard Deviation in ln(k): 1.0839465045217023"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R_Sp-11R!H=7R!H
Total Standard Deviation in ln(k): 1.0839465045217023""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R_Sp-11R!H=7R!H
Total Standard Deviation in ln(k): 1.0839465045217023
""",
)

entry(
    index = 395,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R_N-Sp-11R!H=7R!H",
    kinetics = ArrheniusBM(A=(2.55039e+10,'s^-1'), n=0.710046, w0=(301000,'J/mol'), E0=(113089,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.126559315319288e-06, var=0.8930120563683793, Tref=1000.0, N=2, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R_N-Sp-11R!H=7R!H',), comment="""BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R_N-Sp-11R!H=7R!H
    Total Standard Deviation in ln(k): 1.894468774371607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R_N-Sp-11R!H=7R!H
Total Standard Deviation in ln(k): 1.894468774371607""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R_N-Sp-11R!H=7R!H
Total Standard Deviation in ln(k): 1.894468774371607
""",
)

entry(
    index = 396,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_Sp-9R!H=8R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.75e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(118353,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_Sp-9R!H=8R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_Sp-9R!H=8R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_Sp-9R!H=8R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_Sp-9R!H=8R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 397,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_N-Sp-9R!H=8R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(6.03e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(137689,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_N-Sp-9R!H=8R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_N-Sp-9R!H=8R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_N-Sp-9R!H=8R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_Sp-10R!H=7R!H_N-Sp-9R!H=8R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 398,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Ext-6R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.84e+12,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(116509,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Ext-6R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Ext-6R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Ext-6R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Ext-6R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 399,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Ext-6R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(6.35e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(135986,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Ext-6R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Ext-6R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Ext-6R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-7R!H-R_N-Sp-10R!H=7R!H_Ext-6R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 400,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R_Sp-12R!H=10R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(2.59e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(90244.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R_Sp-12R!H=10R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R_Sp-12R!H=10R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R_Sp-12R!H=10R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R_Sp-12R!H=10R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 401,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R_N-Sp-12R!H=10R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(2.73e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(88634.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R_N-Sp-12R!H=10R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R_N-Sp-12R!H=10R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R_N-Sp-12R!H=10R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_Sp-9R!H=8R!H_Ext-10R!H-R_N-Sp-12R!H=10R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 402,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R_Sp-12R!H=10R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(6.41e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(79663.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R_Sp-12R!H=10R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R_Sp-12R!H=10R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R_Sp-12R!H=10R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R_Sp-12R!H=10R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 403,
    label = "Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R_N-Sp-12R!H=10R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(6.76e+10,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(78069.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R_N-Sp-12R!H=10R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R_N-Sp-12R!H=10R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R_N-Sp-12R!H=10R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone4_Sp-5R!H-2R!H_Sp-2R!H-1R!H_Ext-6R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-Sp-9R!H=8R!H_Ext-10R!H-R_N-Sp-12R!H=10R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 404,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R_Sp-11R!H=7R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.56e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(118434,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R_Sp-11R!H=7R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R_Sp-11R!H=7R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R_Sp-11R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R_Sp-11R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 405,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R_N-Sp-11R!H=7R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.7e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(116573,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R_N-Sp-11R!H=7R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R_N-Sp-11R!H=7R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R_N-Sp-11R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_Sp-9R!H=8R!H_Ext-7R!H-R_N-Sp-11R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 406,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R_Sp-11R!H=7R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(6.34e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(116038,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R_Sp-11R!H=7R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R_Sp-11R!H=7R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R_Sp-11R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R_Sp-11R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 407,
    label = "Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R_N-Sp-11R!H=7R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(6.68e+11,'s^-1'), n=0.21, w0=(301000,'J/mol'), E0=(114225,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R_N-Sp-11R!H=7R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R_N-Sp-11R!H=7R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R_N-Sp-11R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone3_N-Sp-2R!H=1R!H_N-Sp-4R!H-1R!H_Ext-6R!H-R_N-6R!H-inRing_Ext-5R!H-R_Ext-8R!H-R_Ext-5R!H-R_N-Sp-9R!H=8R!H_Ext-7R!H-R_N-Sp-11R!H=7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 408,
    label = "Backbone1",
    kinetics = ArrheniusBM(A=(3.36539e+09,'s^-1'), n=0.84129, w0=(294298,'J/mol'), E0=(36905.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.031430614527560546, var=6.099077214950256, Tref=1000.0, N=84, data_mean=0.0, correlation='Backbone1',), comment="""BM rule fitted to 84 training reactions at node Backbone1
    Total Standard Deviation in ln(k): 5.02992726236122"""),
    rank = 11,
    shortDesc = """BM rule fitted to 84 training reactions at node Backbone1
Total Standard Deviation in ln(k): 5.02992726236122""",
    longDesc = 
"""
BM rule fitted to 84 training reactions at node Backbone1
Total Standard Deviation in ln(k): 5.02992726236122
""",
)

entry(
    index = 409,
    label = "Backbone2",
    kinetics = ArrheniusBM(A=(2.29992e-11,'s^-1'), n=6.41391, w0=(299946,'J/mol'), E0=(-2602.48,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.060263897582951434, var=9.993740724871635, Tref=1000.0, N=74, data_mean=0.0, correlation='Backbone2',), comment="""BM rule fitted to 74 training reactions at node Backbone2
    Total Standard Deviation in ln(k): 6.488961424539268"""),
    rank = 11,
    shortDesc = """BM rule fitted to 74 training reactions at node Backbone2
Total Standard Deviation in ln(k): 6.488961424539268""",
    longDesc = 
"""
BM rule fitted to 74 training reactions at node Backbone2
Total Standard Deviation in ln(k): 6.488961424539268
""",
)

entry(
    index = 410,
    label = "Backbone3",
    kinetics = ArrheniusBM(A=(0.234039,'s^-1'), n=3.38729, w0=(299636,'J/mol'), E0=(58338.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23174178600410858, var=45.068923389250436, Tref=1000.0, N=140, data_mean=0.0, correlation='Backbone3',), comment="""BM rule fitted to 140 training reactions at node Backbone3
    Total Standard Deviation in ln(k): 14.040732400793539"""),
    rank = 11,
    shortDesc = """BM rule fitted to 140 training reactions at node Backbone3
Total Standard Deviation in ln(k): 14.040732400793539""",
    longDesc = 
"""
BM rule fitted to 140 training reactions at node Backbone3
Total Standard Deviation in ln(k): 14.040732400793539
""",
)

entry(
    index = 411,
    label = "Backbone4",
    kinetics = ArrheniusBM(A=(1.87342e+07,'s^-1'), n=1.00417, w0=(299807,'J/mol'), E0=(83382,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0654062900291529, var=6.730759255238982, Tref=1000.0, N=75, data_mean=0.0, correlation='Backbone4',), comment="""BM rule fitted to 75 training reactions at node Backbone4
    Total Standard Deviation in ln(k): 5.3653633296814895"""),
    rank = 11,
    shortDesc = """BM rule fitted to 75 training reactions at node Backbone4
Total Standard Deviation in ln(k): 5.3653633296814895""",
    longDesc = 
"""
BM rule fitted to 75 training reactions at node Backbone4
Total Standard Deviation in ln(k): 5.3653633296814895
""",
)

entry(
    index = 412,
    label = "Backbone5",
    kinetics = ArrheniusBM(A=(1.19e+11,'s^-1'), n=0.08, w0=(301000,'J/mol'), E0=(87554.3,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Backbone5',), comment="""BM rule fitted to 1 training reactions at node Backbone5
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Backbone5
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Backbone5
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 413,
    label = "Backbone6",
    kinetics = ArrheniusBM(A=(0.0020548,'s^-1'), n=4.08615, w0=(298536,'J/mol'), E0=(33139.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2567177210013423, var=31.29233349131318, Tref=1000.0, N=374, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 374 training reactions at node Root
    Total Standard Deviation in ln(k): 11.85941737946586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 374 training reactions at node Root
Total Standard Deviation in ln(k): 11.85941737946586""",
    longDesc = 
"""
BM rule fitted to 374 training reactions at node Root
Total Standard Deviation in ln(k): 11.85941737946586
""",
)

entry(
    index = 414,
    label = "Backbone7",
    kinetics = ArrheniusBM(A=(0.0020548,'s^-1'), n=4.08615, w0=(298536,'J/mol'), E0=(33139.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2567177210013423, var=31.29233349131318, Tref=1000.0, N=374, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 374 training reactions at node Root
    Total Standard Deviation in ln(k): 11.85941737946586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 374 training reactions at node Root
Total Standard Deviation in ln(k): 11.85941737946586""",
    longDesc = 
"""
BM rule fitted to 374 training reactions at node Root
Total Standard Deviation in ln(k): 11.85941737946586
""",
)

entry(
    index = 415,
    label = "Backbone8",
    kinetics = ArrheniusBM(A=(0.0020548,'s^-1'), n=4.08615, w0=(298536,'J/mol'), E0=(33139.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2567177210013423, var=31.29233349131318, Tref=1000.0, N=374, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 374 training reactions at node Root
    Total Standard Deviation in ln(k): 11.85941737946586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 374 training reactions at node Root
Total Standard Deviation in ln(k): 11.85941737946586""",
    longDesc = 
"""
BM rule fitted to 374 training reactions at node Root
Total Standard Deviation in ln(k): 11.85941737946586
""",
)

entry(
    index = 416,
    label = "Backbone9",
    kinetics = ArrheniusBM(A=(0.0020548,'s^-1'), n=4.08615, w0=(298536,'J/mol'), E0=(33139.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2567177210013423, var=31.29233349131318, Tref=1000.0, N=374, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 374 training reactions at node Root
    Total Standard Deviation in ln(k): 11.85941737946586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 374 training reactions at node Root
Total Standard Deviation in ln(k): 11.85941737946586""",
    longDesc = 
"""
BM rule fitted to 374 training reactions at node Root
Total Standard Deviation in ln(k): 11.85941737946586
""",
)

entry(
    index = 417,
    label = "Backbone10",
    kinetics = ArrheniusBM(A=(0.0020548,'s^-1'), n=4.08615, w0=(298536,'J/mol'), E0=(33139.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2567177210013423, var=31.29233349131318, Tref=1000.0, N=374, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 374 training reactions at node Root
    Total Standard Deviation in ln(k): 11.85941737946586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 374 training reactions at node Root
Total Standard Deviation in ln(k): 11.85941737946586""",
    longDesc = 
"""
BM rule fitted to 374 training reactions at node Root
Total Standard Deviation in ln(k): 11.85941737946586
""",
)

