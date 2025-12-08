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
    kinetics = ArrheniusBM(A=(1.33538e+06,'s^-1'), n=2.00179, w0=(548.25,'kJ/mol'), E0=(71.4091,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6196094538418404, var=78.13381220537823, Tref=1000.0, N=8, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 8 training reactions at node Root
    Total Standard Deviation in ln(k): 19.277329088774174"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root
Total Standard Deviation in ln(k): 19.277329088774174""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root
Total Standard Deviation in ln(k): 19.277329088774174
""",
)

entry(
    index = 2,
    label = "Root_2Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(2.21087e+06,'s^-1'), n=1.93893, w0=(539,'kJ/mol'), E0=(70.4285,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1467027819186768, var=92.22567695901714, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H',), comment="""BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 22.133475837375318"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 22.133475837375318""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 22.133475837375318
""",
)

entry(
    index = 3,
    label = "Root_N-2Br1sCl1sF1sH->H",
    kinetics = Arrhenius(A=(1.91033e+10,'s^-1'), n=0.827, Ea=(149.134,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_2Br1sCl1sF1sH->H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.55301e+06,'s^-1'), n=1.88257, w0=(539,'kJ/mol'), E0=(70.4124,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3606859402011853, var=99.56545527071377, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R
    Total Standard Deviation in ln(k): 23.422554893707563"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R
Total Standard Deviation in ln(k): 23.422554893707563""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R
Total Standard Deviation in ln(k): 23.422554893707563
""",
)

entry(
    index = 5,
    label = "Root_2Br1sCl1sF1sH->H_Ext-3C-R_4R!H->Cl",
    kinetics = Arrhenius(A=(3.33333e+12,'s^-1'), n=0, Ea=(41.84,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_Ext-3C-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Cl",
    kinetics = Arrhenius(A=(3.33333e+12,'s^-1'), n=0, Ea=(62.76,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_2Br1sCl1sF1sH->H_Ext-1C-R_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(3.20582e+20,'s^-1'), n=-2.15816, w0=(539,'kJ/mol'), E0=(176.432,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.47055052453932933, var=23.50376589543941, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_Ext-1C-R_Sp-4R!H-1C',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 10.901380257168498"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 10.901380257168498""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 10.901380257168498
""",
)

entry(
    index = 8,
    label = "Root_2Br1sCl1sF1sH->H_Ext-1C-R_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(4.9849e+44,'s^-1'), n=-9.00409, w0=(539,'kJ/mol'), E0=(165.134,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7922609571441235, var=199.2222972900656, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_Ext-1C-R_N-Sp-4R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 30.286665002527975"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 30.286665002527975""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 30.286665002527975
""",
)

entry(
    index = 9,
    label = "Root_2Br1sCl1sF1sH->H_Ext-1C-R_Sp-4R!H-1C_1C-inRing",
    kinetics = ArrheniusBM(A=(1.9802e+22,'s^-1'), n=-2.66998, w0=(539,'kJ/mol'), E0=(184.064,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.0720040911798128, var=5.164887496394842, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_Ext-1C-R_Sp-4R!H-1C_1C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R_Sp-4R!H-1C_1C-inRing
    Total Standard Deviation in ln(k): 9.762079318807452"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R_Sp-4R!H-1C_1C-inRing
Total Standard Deviation in ln(k): 9.762079318807452""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R_Sp-4R!H-1C_1C-inRing
Total Standard Deviation in ln(k): 9.762079318807452
""",
)

entry(
    index = 10,
    label = "Root_2Br1sCl1sF1sH->H_Ext-1C-R_Sp-4R!H-1C_N-1C-inRing",
    kinetics = Arrhenius(A=(5e+12,'s^-1'), n=0, Ea=(17.5728,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_Ext-1C-R_Sp-4R!H-1C_N-1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R_Sp-4R!H-1C_N-1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R_Sp-4R!H-1C_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R_Sp-4R!H-1C_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_2Br1sCl1sF1sH->H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    kinetics = Arrhenius(A=(8.17959e+16,'s^-1'), n=-1.28029, Ea=(-20.6713,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_2Br1sCl1sF1sH->H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    kinetics = Arrhenius(A=(2.5558e+16,'s^-1'), n=-0.661604, Ea=(142.748,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_2Br1sCl1sF1sH->H_Ext-1C-R_Sp-4R!H-1C_1C-inRing_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = Arrhenius(A=(8.067e+10,'s^-1'), n=0.649, Ea=(33.5975,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_Ext-1C-R_Sp-4R!H-1C_1C-inRing_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R_Sp-4R!H-1C_1C-inRing_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R_Sp-4R!H-1C_1C-inRing_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_Ext-1C-R_Sp-4R!H-1C_1C-inRing_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

