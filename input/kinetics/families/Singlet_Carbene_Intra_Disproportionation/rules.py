#!/usr/bin/env python
# encoding: utf-8

name = "Singlet_Carbene_Intra_Disproportionation/rules"
shortDesc = "Convert a singlet carbene to a closed-shell molecule through a concerted 1,2-H shift + 1,2-bond formation"
longDesc = """
Reaction site *1 should always be a singlet in this family.
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(7.2916e+18,'s^-1'), n=-1.99364, w0=(548250,'J/mol'), E0=(117960,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7325825992036357, var=16.609355364929396, Tref=1000.0, N=8, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 8 training reactions at node Root
    Total Standard Deviation in ln(k): 10.01087278013311"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root
Total Standard Deviation in ln(k): 10.01087278013311""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root
Total Standard Deviation in ln(k): 10.01087278013311
""",
)

entry(
    index = 2,
    label = "CCH",
    kinetics = ArrheniusBM(A=(4.61437e+18,'s^-1'), n=-1.93909, w0=(539000,'J/mol'), E0=(116153,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.70731621670093, var=15.46517233475561, Tref=1000.0, N=7, data_mean=0.0, correlation='CCH',), comment="""BM rule fitted to 7 training reactions at node CCH
    Total Standard Deviation in ln(k): 9.660954149979611"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node CCH
Total Standard Deviation in ln(k): 9.660954149979611""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node CCH
Total Standard Deviation in ln(k): 9.660954149979611
""",
)

entry(
    index = 3,
    label = "CCY",
    kinetics = ArrheniusBM(A=(1.91033e+10,'s^-1'), n=0.827, w0=(613000,'J/mol'), E0=(218621,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CCY',), comment="""BM rule fitted to 1 training reactions at node CCY
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CCY
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CCY
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "CCH_Ext-3C-R_4R!H->Br",
    kinetics = ArrheniusBM(A=(5e+12,'s^-1'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CCH_Ext-3C-R_4R!H->Br',), comment="""BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_4R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_4R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_4R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "CCH_Ext-3C-R_N-4R!H->Br",
    kinetics = ArrheniusBM(A=(4.63567e+18,'s^-1'), n=-1.94146, w0=(539000,'J/mol'), E0=(116108,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7487914615112697, var=15.996802296776211, Tref=1000.0, N=6, data_mean=0.0, correlation='CCH_Ext-3C-R_N-4R!H->Br',), comment="""BM rule fitted to 6 training reactions at node CCH_Ext-3C-R_N-4R!H->Br
    Total Standard Deviation in ln(k): 9.899524532744497"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node CCH_Ext-3C-R_N-4R!H->Br
Total Standard Deviation in ln(k): 9.899524532744497""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node CCH_Ext-3C-R_N-4R!H->Br
Total Standard Deviation in ln(k): 9.899524532744497
""",
)

entry(
    index = 6,
    label = "CCH_Ext-3C-R_N-4R!H->Br_4CClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(3.33333e+12,'s^-1'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CCH_Ext-3C-R_N-4R!H->Br_4CClFINOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_4CClFINOPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_4CClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_4CClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(6.72407e+18,'s^-1'), n=-1.98917, w0=(539000,'J/mol'), E0=(116152,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7069805602838418, var=15.821367274462165, Tref=1000.0, N=5, data_mean=0.0, correlation='CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F',), comment="""BM rule fitted to 5 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F
    Total Standard Deviation in ln(k): 9.750383819713313"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F
Total Standard Deviation in ln(k): 9.750383819713313""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F
Total Standard Deviation in ln(k): 9.750383819713313
""",
)

entry(
    index = 8,
    label = "CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing",
    kinetics = ArrheniusBM(A=(8.5826e+18,'s^-1'), n=-2.02101, w0=(539000,'J/mol'), E0=(116212,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6999071222609732, var=15.970463668735485, Tref=1000.0, N=4, data_mean=0.0, correlation='CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing',), comment="""BM rule fitted to 4 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing
    Total Standard Deviation in ln(k): 9.770095934337473"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing
Total Standard Deviation in ln(k): 9.770095934337473""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing
Total Standard Deviation in ln(k): 9.770095934337473
""",
)

entry(
    index = 9,
    label = "CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_N-1C-inRing",
    kinetics = ArrheniusBM(A=(3.33333e+12,'s^-1'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_N-1C-inRing',), comment="""BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_N-1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(34750.3,'s^-1'), n=2.41729, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.0720040911798123, var=5.164887496394838, Tref=1000.0, N=2, data_mean=0.0, correlation='CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C',), comment="""BM rule fitted to 2 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C
    Total Standard Deviation in ln(k): 9.762079318807448"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 9.762079318807448""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 9.762079318807448
""",
)

entry(
    index = 11,
    label = "CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(5.64592e-16,'s^-1'), n=7.76139, w0=(539000,'J/mol'), E0=(-10613.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2245170669211892, var=51.16218975222246, Tref=1000.0, N=2, data_mean=0.0, correlation='CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C',), comment="""BM rule fitted to 2 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C
    Total Standard Deviation in ln(k): 14.90353211384042"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 14.90353211384042""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 14.90353211384042
""",
)

entry(
    index = 12,
    label = "CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(8.067e+10,'s^-1'), n=0.649, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-4CCl",
    kinetics = ArrheniusBM(A=(1.61832e+16,'s^-1'), n=-0.885455, w0=(539000,'J/mol'), E0=(109382,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-4CCl',), comment="""BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-4CCl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-4CCl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-4CCl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-4CCl",
    kinetics = ArrheniusBM(A=(4.66894e+13,'s^-1'), n=-1.27142, w0=(539000,'J/mol'), E0=(78261.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-4CCl',), comment="""BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-4CCl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-4CCl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-4CCl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

