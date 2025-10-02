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
    kinetics = ArrheniusBM(A=(1.79864e+17,'s^-1'), n=-1.47793, w0=(548.25,'kJ/mol'), E0=(114.78,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5549334436695161, var=16.974171373432917, Tref=1000.0, N=8, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 8 training reactions at node Root
    Total Standard Deviation in ln(k): 9.653758030260164"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root
Total Standard Deviation in ln(k): 9.653758030260164""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root
Total Standard Deviation in ln(k): 9.653758030260164
""",
)

entry(
    index = 2,
    label = "CCH",
    kinetics = ArrheniusBM(A=(1.20443e+17,'s^-1'), n=-1.43042, w0=(539,'kJ/mol'), E0=(113.022,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.514991623114097, var=15.884634944160005, Tref=1000.0, N=7, data_mean=0.0, correlation='CCH',), comment="""BM rule fitted to 7 training reactions at node CCH
    Total Standard Deviation in ln(k): 9.28392726413843"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node CCH
Total Standard Deviation in ln(k): 9.28392726413843""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node CCH
Total Standard Deviation in ln(k): 9.28392726413843
""",
)

entry(
    index = 3,
    label = "CCH_Ext-3C-R_4R!H->Br",
    kinetics = ArrheniusBM(A=(5e+12,'s^-1'), n=4.22455e-09, w0=(539,'kJ/mol'), E0=(101.409,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CCH_Ext-3C-R_4R!H->Br',), comment="""BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_4R!H->Br
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
    index = 4,
    label = "CCH_Ext-3C-R_N-4R!H->Br",
    kinetics = ArrheniusBM(A=(1.18269e+17,'s^-1'), n=-1.42952, w0=(539,'kJ/mol'), E0=(112.965,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5517143818398826, var=16.398565006535087, Tref=1000.0, N=6, data_mean=0.0, correlation='CCH_Ext-3C-R_N-4R!H->Br',), comment="""BM rule fitted to 6 training reactions at node CCH_Ext-3C-R_N-4R!H->Br
    Total Standard Deviation in ln(k): 9.504420141194425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node CCH_Ext-3C-R_N-4R!H->Br
Total Standard Deviation in ln(k): 9.504420141194425""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node CCH_Ext-3C-R_N-4R!H->Br
Total Standard Deviation in ln(k): 9.504420141194425
""",
)

entry(
    index = 5,
    label = "CCH_Ext-3C-R_N-4R!H->Br_4CClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(3.33334e+12,'s^-1'), n=-1.40567e-07, w0=(539,'kJ/mol'), E0=(154.384,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CCH_Ext-3C-R_N-4R!H->Br_4CClFINOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_4CClFINOPSSi->F
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
    index = 6,
    label = "CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(1.74721e+17,'s^-1'), n=-1.47908, w0=(539,'kJ/mol'), E0=(113.052,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.51192054127672, var=16.166971379645908, Tref=1000.0, N=5, data_mean=0.0, correlation='CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F',), comment="""BM rule fitted to 5 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F
    Total Standard Deviation in ln(k): 9.346905902058813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F
Total Standard Deviation in ln(k): 9.346905902058813""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F
Total Standard Deviation in ln(k): 9.346905902058813
""",
)

entry(
    index = 7,
    label = "CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing",
    kinetics = ArrheniusBM(A=(2.22161e+17,'s^-1'), n=-1.50998, w0=(539,'kJ/mol'), E0=(113.127,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5018375041037424, var=16.310967916345923, Tref=1000.0, N=4, data_mean=0.0, correlation='CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing',), comment="""BM rule fitted to 4 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing
    Total Standard Deviation in ln(k): 9.357389599918276"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing
Total Standard Deviation in ln(k): 9.357389599918276""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing
Total Standard Deviation in ln(k): 9.357389599918276
""",
)

entry(
    index = 8,
    label = "CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(4.03468e+20,'s^-1'), n=-2.18552, w0=(539,'kJ/mol'), E0=(146.145,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5822770821690705, var=6.058307656543806, Tref=1000.0, N=2, data_mean=0.0, correlation='CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C',), comment="""BM rule fitted to 2 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C
    Total Standard Deviation in ln(k): 6.3973884227859665"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 6.3973884227859665""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 6.3973884227859665
""",
)

entry(
    index = 9,
    label = "CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(8.067e+10,'s^-1'), n=0.649, w0=(539,'kJ/mol'), E0=(123.553,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_Sp-5R!H-1C_Ext-5R!H-R_Ext-5R!H-R
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
    index = 10,
    label = "CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(7.26313e-09,'s^-1'), n=5.53373, w0=(539,'kJ/mol'), E0=(4.64464,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.525240051516825, var=52.082221049180056, Tref=1000.0, N=2, data_mean=0.0, correlation='CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C',), comment="""BM rule fitted to 2 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C
    Total Standard Deviation in ln(k): 15.787473340914588"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 15.787473340914588""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 15.787473340914588
""",
)

entry(
    index = 11,
    label = "CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-4CCl",
    kinetics = ArrheniusBM(A=(1.61832e+16,'s^-1'), n=-0.885455, w0=(539,'kJ/mol'), E0=(106.175,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-4CCl',), comment="""BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-4CCl
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
    index = 12,
    label = "CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-4CCl",
    kinetics = ArrheniusBM(A=(4.66894e+13,'s^-1'), n=-1.27142, w0=(539,'kJ/mol'), E0=(76.0866,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-4CCl',), comment="""BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_1C-inRing_Ext-4CCl-R_Ext-5R!H-R_N-Sp-5R!H-1C_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-4CCl
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

entry(
    index = 13,
    label = "CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_N-1C-inRing",
    kinetics = ArrheniusBM(A=(3.33333e+12,'s^-1'), n=8.2394e-08, w0=(539,'kJ/mol'), E0=(130.615,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_N-1C-inRing',), comment="""BM rule fitted to 1 training reactions at node CCH_Ext-3C-R_N-4R!H->Br_N-4CClFINOPSSi->F_N-1C-inRing
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
    index = 14,
    label = "CCY",
    kinetics = ArrheniusBM(A=(1.91033e+10,'s^-1'), n=0.827, w0=(613,'kJ/mol'), E0=(219.153,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CCY',), comment="""BM rule fitted to 1 training reactions at node CCY
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

