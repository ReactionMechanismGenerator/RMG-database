#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_COm/rules"
shortDesc = ""
longDesc = """
.. [MRHCBSQB31DHR] M.R. Harper (mrharper_at_mit_dot_edu or michael_dot_harper_dot_jr_at_gmail_dot_com)
The geometries of all reactants, products, and the transition state were optimized using the CBS-QB3 method.
The zero-point energy is that computed by the CBS-QB3 calculations.  The frequencies were computed with B3LYP/CBSB7.
In computing k(T), an asymmetric tunneling correction was employed, the calculated frequencies were scaled by 0.99, and the 
temperatures used were from 600 K to 2000 K (in 200 K increments).
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.46291e-07,'m^3/(mol*s)'), n=3.72352, w0=(309147,'J/mol'), E0=(728.641,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.34325964327833525, var=1.332195104688388, Tref=1000.0, N=17, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 17 training reactions at node Root
    Total Standard Deviation in ln(k): 3.176341808797994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root
Total Standard Deviation in ln(k): 3.176341808797994""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root
Total Standard Deviation in ln(k): 3.176341808797994
""",
)

entry(
    index = 2,
    label = "Root_3R->O",
    kinetics = ArrheniusBM(A=(34.1,'m^3/(mol*s)'), n=0, w0=(315500,'J/mol'), E0=(38037.3,'J/mol'), Tmin=(250,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_N-3R->O",
    kinetics = ArrheniusBM(A=(2.36023e-06,'m^3/(mol*s)'), n=3.53686, w0=(308750,'J/mol'), E0=(17579.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3220491474970854, var=0.9923725232954674, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-3R->O',), comment="""BM rule fitted to 16 training reactions at node Root_N-3R->O
    Total Standard Deviation in ln(k): 2.806243619745347"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-3R->O
Total Standard Deviation in ln(k): 2.806243619745347""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-3R->O
Total Standard Deviation in ln(k): 2.806243619745347
""",
)

entry(
    index = 4,
    label = "Root_N-3R->O_3BrCClFHINPSSi-inRing",
    kinetics = ArrheniusBM(A=(2.24597,'m^3/(mol*s)'), n=1.72812, w0=(309500,'J/mol'), E0=(37290,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.45664945129539924, var=0.9066904653816424, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing
    Total Standard Deviation in ln(k): 3.0562750928360427"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing
Total Standard Deviation in ln(k): 3.0562750928360427""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing
Total Standard Deviation in ln(k): 3.0562750928360427
""",
)

entry(
    index = 5,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing",
    kinetics = ArrheniusBM(A=(5.86939e-08,'m^3/(mol*s)'), n=3.99767, w0=(308643,'J/mol'), E0=(1970.45,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.30146310194536086, var=0.6440138394170295, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing',), comment="""BM rule fitted to 14 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing
    Total Standard Deviation in ln(k): 2.3662543589508878"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing
Total Standard Deviation in ln(k): 2.3662543589508878""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing
Total Standard Deviation in ln(k): 2.3662543589508878
""",
)

entry(
    index = 6,
    label = "Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_4R!H->O",
    kinetics = ArrheniusBM(A=(0.00721,'m^3/(mol*s)'), n=2.333, w0=(309500,'J/mol'), E0=(19464.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.48e+06,'m^3/(mol*s)'), n=0, w0=(309500,'J/mol'), E0=(53857.6,'J/mol'), Tmin=(295,'K'), Tmax=(500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C",
    kinetics = ArrheniusBM(A=(3.25841e-08,'m^3/(mol*s)'), n=4.07459, w0=(309500,'J/mol'), E0=(6461.64,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2908679106050406, var=0.5794274955291425, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C
    Total Standard Deviation in ln(k): 2.2568309436756833"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 2.2568309436756833""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 2.2568309436756833
""",
)

entry(
    index = 9,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C",
    kinetics = ArrheniusBM(A=(2.59363e-13,'m^3/(mol*s)'), n=5.36337, w0=(307100,'J/mol'), E0=(-53252.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.7258740605267215, var=26.998204933099615, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C
    Total Standard Deviation in ln(k): 22.29061817331208"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 22.29061817331208""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 22.29061817331208
""",
)

entry(
    index = 10,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0707843,'m^3/(mol*s)'), n=2.30417, w0=(309500,'J/mol'), E0=(33260.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.37531220468720855, var=0.6706108866911895, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R
    Total Standard Deviation in ln(k): 2.584689784793377"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 2.584689784793377""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 2.584689784793377
""",
)

entry(
    index = 11,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_3BrClHS->H",
    kinetics = ArrheniusBM(A=(11492.6,'m^3/(mol*s)'), n=0.258022, w0=(342000,'J/mol'), E0=(39622.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.498300370263393e-14, var=3.447156939379626, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_3BrClHS->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_3BrClHS->H
    Total Standard Deviation in ln(k): 3.72209554762774"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_3BrClHS->H
Total Standard Deviation in ln(k): 3.72209554762774""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_3BrClHS->H
Total Standard Deviation in ln(k): 3.72209554762774
""",
)

entry(
    index = 12,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H",
    kinetics = ArrheniusBM(A=(3.18793e+08,'m^3/(mol*s)'), n=-0.414732, w0=(283833,'J/mol'), E0=(16988.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4983492459945176, var=13.363940199711392, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H
    Total Standard Deviation in ln(k): 8.58078833953412"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H
Total Standard Deviation in ln(k): 8.58078833953412""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H
Total Standard Deviation in ln(k): 8.58078833953412
""",
)

entry(
    index = 13,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(4.93498,'m^3/(mol*s)'), n=1.78226, w0=(309500,'J/mol'), E0=(38303.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16003985906469037, var=0.32905128401744904, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 1.5520862187965685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 1.5520862187965685""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 1.5520862187965685
""",
)

entry(
    index = 14,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(151000,'m^3/(mol*s)'), n=0, w0=(309500,'J/mol'), E0=(54199.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_3BrClS->S",
    kinetics = ArrheniusBM(A=(0.0785,'m^3/(mol*s)'), n=2.33, w0=(272500,'J/mol'), E0=(17156.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_3BrClS->S',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_3BrClS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_3BrClS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_3BrClS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S",
    kinetics = ArrheniusBM(A=(32434.8,'m^3/(mol*s)'), n=0.691866, w0=(289500,'J/mol'), E0=(-27319.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3595377448742767, var=3.6966857594756677, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S
    Total Standard Deviation in ln(k): 7.270381439875438"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S
Total Standard Deviation in ln(k): 7.270381439875438""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S
Total Standard Deviation in ln(k): 7.270381439875438
""",
)

entry(
    index = 17,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(86.1,'m^3/(mol*s)'), n=1.36, w0=(309500,'J/mol'), E0=(35435.6,'J/mol'), Tmin=(600,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(65100,'m^3/(mol*s)'), n=0.45, w0=(309500,'J/mol'), E0=(45510.1,'J/mol'), Tmin=(600,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Cl",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(300000,'J/mol'), E0=(8765.12,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Cl",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(279000,'J/mol'), E0=(-5396.12,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

