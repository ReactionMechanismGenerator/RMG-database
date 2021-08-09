#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.25145e-05,'s^-1'), n=4.97977, w0=(415622,'J/mol'), E0=(106413,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21432815102021585, var=39.56664122544905, Tref=1000.0, N=862, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 862 training reactions at node Root
    Total Standard Deviation in ln(k): 13.148701539483868"""),
    rank = 11,
    shortDesc = """BM rule fitted to 862 training reactions at node Root
Total Standard Deviation in ln(k): 13.148701539483868""",
    longDesc = 
"""
BM rule fitted to 862 training reactions at node Root
Total Standard Deviation in ln(k): 13.148701539483868
""",
)

entry(
    index = 2,
    label = "Root_1R!H->C",
    kinetics = ArrheniusBM(A=(0.00544243,'s^-1'), n=4.41428, w0=(413604,'J/mol'), E0=(121129,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.19181177833768806, var=41.20334165758929, Tref=1000.0, N=765, data_mean=0.0, correlation='Root_1R!H->C',), comment="""BM rule fitted to 765 training reactions at node Root_1R!H->C
    Total Standard Deviation in ln(k): 13.350299351591545"""),
    rank = 11,
    shortDesc = """BM rule fitted to 765 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 13.350299351591545""",
    longDesc = 
"""
BM rule fitted to 765 training reactions at node Root_1R!H->C
Total Standard Deviation in ln(k): 13.350299351591545
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H->C",
    kinetics = ArrheniusBM(A=(1.55802e-19,'s^-1'), n=8.98724, w0=(431536,'J/mol'), E0=(21750.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.787917064006013, var=19.679491407441827, Tref=1000.0, N=97, data_mean=0.0, correlation='Root_N-1R!H->C',), comment="""BM rule fitted to 97 training reactions at node Root_N-1R!H->C
    Total Standard Deviation in ln(k): 10.87301122241373"""),
    rank = 11,
    shortDesc = """BM rule fitted to 97 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 10.87301122241373""",
    longDesc = 
"""
BM rule fitted to 97 training reactions at node Root_N-1R!H->C
Total Standard Deviation in ln(k): 10.87301122241373
""",
)

entry(
    index = 4,
    label = "Root_1R!H->C_3R!H->C",
    kinetics = ArrheniusBM(A=(0.143167,'s^-1'), n=3.9709, w0=(411000,'J/mol'), E0=(140281,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13512712213405362, var=26.648423274605882, Tref=1000.0, N=670, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C',), comment="""BM rule fitted to 670 training reactions at node Root_1R!H->C_3R!H->C
    Total Standard Deviation in ln(k): 10.688381019027446"""),
    rank = 11,
    shortDesc = """BM rule fitted to 670 training reactions at node Root_1R!H->C_3R!H->C
Total Standard Deviation in ln(k): 10.688381019027446""",
    longDesc = 
"""
BM rule fitted to 670 training reactions at node Root_1R!H->C_3R!H->C
Total Standard Deviation in ln(k): 10.688381019027446
""",
)

entry(
    index = 5,
    label = "Root_1R!H->C_N-3R!H->C",
    kinetics = ArrheniusBM(A=(3.01707e-18,'s^-1'), n=9.01743, w0=(431968,'J/mol'), E0=(23905.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12286491620956684, var=25.12180889800668, Tref=1000.0, N=95, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C',), comment="""BM rule fitted to 95 training reactions at node Root_1R!H->C_N-3R!H->C
    Total Standard Deviation in ln(k): 10.356770990822797"""),
    rank = 11,
    shortDesc = """BM rule fitted to 95 training reactions at node Root_1R!H->C_N-3R!H->C
Total Standard Deviation in ln(k): 10.356770990822797""",
    longDesc = 
"""
BM rule fitted to 95 training reactions at node Root_1R!H->C_N-3R!H->C
Total Standard Deviation in ln(k): 10.356770990822797
""",
)

entry(
    index = 6,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(10959.3,'s^-1'), n=1.97729, w0=(435000,'J/mol'), E0=(75472.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04174250582034565, var=8.597875713059503, Tref=1000.0, N=89, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O',), comment="""BM rule fitted to 89 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 5.983191824383614"""),
    rank = 11,
    shortDesc = """BM rule fitted to 89 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 5.983191824383614""",
    longDesc = 
"""
BM rule fitted to 89 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 5.983191824383614
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.09287e-41,'s^-1'), n=15.6473, w0=(393000,'J/mol'), E0=(-24447.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.9257407284152066, var=38.61636083817381, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 22.321507664716677"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 22.321507664716677""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O
Total Standard Deviation in ln(k): 22.321507664716677
""",
)

entry(
    index = 8,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00686643,'s^-1'), n=4.33388, w0=(411000,'J/mol'), E0=(136428,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15528758359569905, var=28.51235521514562, Tref=1000.0, N=603, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R',), comment="""BM rule fitted to 603 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.094846027767675"""),
    rank = 11,
    shortDesc = """BM rule fitted to 603 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.094846027767675""",
    longDesc = 
"""
BM rule fitted to 603 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.094846027767675
""",
)

entry(
    index = 9,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.7867e+06,'s^-1'), n=1.99263, w0=(411000,'J/mol'), E0=(164407,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.005353748031173918, var=18.08530830259281, Tref=1000.0, N=43, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R',), comment="""BM rule fitted to 43 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 8.538953375233456"""),
    rank = 11,
    shortDesc = """BM rule fitted to 43 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 8.538953375233456""",
    longDesc = 
"""
BM rule fitted to 43 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 8.538953375233456
""",
)

entry(
    index = 10,
    label = "Root_1R!H->C_3R!H->C_Int-3C-1C_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(8.3788e+10,'s^-1'), n=0.684982, w0=(411000,'J/mol'), E0=(171129,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0015738850846012977, var=1.3108540684772003, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Int-3C-1C_Sp-3C-1C',), comment="""BM rule fitted to 22 training reactions at node Root_1R!H->C_3R!H->C_Int-3C-1C_Sp-3C-1C
    Total Standard Deviation in ln(k): 2.2992265052645076"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_1R!H->C_3R!H->C_Int-3C-1C_Sp-3C-1C
Total Standard Deviation in ln(k): 2.2992265052645076""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_1R!H->C_3R!H->C_Int-3C-1C_Sp-3C-1C
Total Standard Deviation in ln(k): 2.2992265052645076
""",
)

entry(
    index = 11,
    label = "Root_1R!H->C_3R!H->C_Int-3C-1C_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(7.28e+10,'s^-1'), n=0.86, w0=(411000,'J/mol'), E0=(191198,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.551115123126669e-17, var=3.654028364887016e-29, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Int-3C-1C_N-Sp-3C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Int-3C-1C_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 1.2257810047050068e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Int-3C-1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 1.2257810047050068e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Int-3C-1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 1.2257810047050068e-14
""",
)

entry(
    index = 12,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R",
    kinetics = ArrheniusBM(A=(7.03796e-17,'s^-1'), n=8.56155, w0=(432333,'J/mol'), E0=(-7166.74,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.129752256494507, var=29.32236087340685, Tref=1000.0, N=90, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R',), comment="""BM rule fitted to 90 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R
    Total Standard Deviation in ln(k): 11.18167629021819"""),
    rank = 11,
    shortDesc = """BM rule fitted to 90 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R
Total Standard Deviation in ln(k): 11.18167629021819""",
    longDesc = 
"""
BM rule fitted to 90 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R
Total Standard Deviation in ln(k): 11.18167629021819
""",
)

entry(
    index = 13,
    label = "Root_1R!H->C_N-3R!H->C_3OS->O",
    kinetics = ArrheniusBM(A=(1.46272e+08,'s^-1'), n=1.39547, w0=(435000,'J/mol'), E0=(116040,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02715714579105423, var=1.8575455551106437, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_3OS->O',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_3OS->O
    Total Standard Deviation in ln(k): 2.8005236159836646"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_3OS->O
Total Standard Deviation in ln(k): 2.8005236159836646""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_3OS->O
Total Standard Deviation in ln(k): 2.8005236159836646
""",
)

entry(
    index = 14,
    label = "Root_1R!H->C_N-3R!H->C_N-3OS->O",
    kinetics = ArrheniusBM(A=(0.04604,'s^-1'), n=4.54588, w0=(387000,'J/mol'), E0=(101154,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_N-3OS->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_N-3OS->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_N-3OS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_N-3OS->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R",
    kinetics = ArrheniusBM(A=(4344.72,'s^-1'), n=2.06621, w0=(435000,'J/mol'), E0=(72457.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05044019530503273, var=9.046636804175513, Tref=1000.0, N=85, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R',), comment="""BM rule fitted to 85 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R
    Total Standard Deviation in ln(k): 6.15650166308842"""),
    rank = 11,
    shortDesc = """BM rule fitted to 85 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R
Total Standard Deviation in ln(k): 6.15650166308842""",
    longDesc = 
"""
BM rule fitted to 85 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R
Total Standard Deviation in ln(k): 6.15650166308842
""",
)

entry(
    index = 16,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(50615.2,'s^-1'), n=2.28121, w0=(435000,'J/mol'), E0=(111596,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006932387477473163, var=1.9398429045608188, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-3R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.809577856801361"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.809577856801361""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.809577856801361
""",
)

entry(
    index = 17,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R",
    kinetics = ArrheniusBM(A=(3.52977e-49,'s^-1'), n=17.7948, w0=(393857,'J/mol'), E0=(-101564,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-7.559649300485118, var=84.51634761779366, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R
    Total Standard Deviation in ln(k): 37.42417921057418"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R
Total Standard Deviation in ln(k): 37.42417921057418""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R
Total Standard Deviation in ln(k): 37.42417921057418
""",
)

entry(
    index = 18,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C",
    kinetics = ArrheniusBM(A=(1.19057e+14,'s^-1'), n=-0.2672, w0=(411000,'J/mol'), E0=(200499,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09094965678133479, var=68.11160492995258, Tref=1000.0, N=81, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C',), comment="""BM rule fitted to 81 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C
    Total Standard Deviation in ln(k): 16.77354624294285"""),
    rank = 11,
    shortDesc = """BM rule fitted to 81 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C
Total Standard Deviation in ln(k): 16.77354624294285""",
    longDesc = 
"""
BM rule fitted to 81 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C
Total Standard Deviation in ln(k): 16.77354624294285
""",
)

entry(
    index = 19,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C",
    kinetics = ArrheniusBM(A=(0.00862346,'s^-1'), n=4.26778, w0=(411000,'J/mol'), E0=(131109,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15019366064049383, var=20.499502769028407, Tref=1000.0, N=522, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C',), comment="""BM rule fitted to 522 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C
    Total Standard Deviation in ln(k): 9.454085038882708"""),
    rank = 11,
    shortDesc = """BM rule fitted to 522 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C
Total Standard Deviation in ln(k): 9.454085038882708""",
    longDesc = 
"""
BM rule fitted to 522 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C
Total Standard Deviation in ln(k): 9.454085038882708
""",
)

entry(
    index = 20,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.26954e+07,'s^-1'), n=1.82965, w0=(411000,'J/mol'), E0=(163716,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.032840065764219266, var=20.66058973659783, Tref=1000.0, N=32, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R',), comment="""BM rule fitted to 32 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 9.194819798285515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 32 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 9.194819798285515""",
    longDesc = 
"""
BM rule fitted to 32 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 9.194819798285515
""",
)

entry(
    index = 21,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.59662e+09,'s^-1'), n=1.17902, w0=(411000,'J/mol'), E0=(157736,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.3933273817247035e-17, var=1.0687721058500719, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 2.0725238866768882"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 2.0725238866768882""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 2.0725238866768882
""",
)

entry(
    index = 22,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(1.79996e-71,'s^-1'), n=24.8066, w0=(411000,'J/mol'), E0=(-9454.93,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.7441027904703117, var=4.602190881577467, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C
    Total Standard Deviation in ln(k): 6.1703065290565755"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C
Total Standard Deviation in ln(k): 6.1703065290565755""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C
Total Standard Deviation in ln(k): 6.1703065290565755
""",
)

entry(
    index = 23,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(2.3886e+11,'s^-1'), n=0.75539, w0=(411000,'J/mol'), E0=(188292,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.602528453014257e-15, var=1.218978277340342, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_N-Sp-3C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 2.213374858889017"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 2.213374858889017""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 2.213374858889017
""",
)

entry(
    index = 24,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.47208e+19,'s^-1'), n=-2.14564, w0=(433105,'J/mol'), E0=(74584,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4992250364654204, var=25.11672755685504, Tref=1000.0, N=76, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R',), comment="""BM rule fitted to 76 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.301383180640325"""),
    rank = 11,
    shortDesc = """BM rule fitted to 76 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.301383180640325""",
    longDesc = 
"""
BM rule fitted to 76 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.301383180640325
""",
)

entry(
    index = 25,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_4R!H->C",
    kinetics = ArrheniusBM(A=(6.22169e+07,'s^-1'), n=1.76577, w0=(423000,'J/mol'), E0=(87360,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.6998460535639754, var=83.34093790109623, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_4R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_4R!H->C
    Total Standard Deviation in ln(k): 32.62269996048423"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_4R!H->C
Total Standard Deviation in ln(k): 32.62269996048423""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_4R!H->C
Total Standard Deviation in ln(k): 32.62269996048423
""",
)

entry(
    index = 26,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(13101,'s^-1'), n=2.87145, w0=(430200,'J/mol'), E0=(130341,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9341603390832344, var=4.142281564393902, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C',), comment="""BM rule fitted to 10 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C
    Total Standard Deviation in ln(k): 6.427292805146317"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C
Total Standard Deviation in ln(k): 6.427292805146317""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C
Total Standard Deviation in ln(k): 6.427292805146317
""",
)

entry(
    index = 27,
    label = "Root_1R!H->C_N-3R!H->C_3OS->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.5014e+08,'s^-1'), n=1.3956, w0=(435000,'J/mol'), E0=(114482,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.015297806311563496, var=2.3143208481388196, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_3OS->O_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_3OS->O_Ext-1C-R
    Total Standard Deviation in ln(k): 3.0882185333035532"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_3OS->O_Ext-1C-R
Total Standard Deviation in ln(k): 3.0882185333035532""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_3OS->O_Ext-1C-R
Total Standard Deviation in ln(k): 3.0882185333035532
""",
)

entry(
    index = 28,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(41.8354,'s^-1'), n=2.73124, w0=(435000,'J/mol'), E0=(74012.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02338346427812497, var=10.463304155975436, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C',), comment="""BM rule fitted to 26 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C
    Total Standard Deviation in ln(k): 6.543475195689604"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 6.543475195689604""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 6.543475195689604
""",
)

entry(
    index = 29,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(3477.18,'s^-1'), n=2.08279, w0=(435000,'J/mol'), E0=(71241.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06265474991964914, var=9.148080459448344, Tref=1000.0, N=59, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C',), comment="""BM rule fitted to 59 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 6.220904383333134"""),
    rank = 11,
    shortDesc = """BM rule fitted to 59 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 6.220904383333134""",
    longDesc = 
"""
BM rule fitted to 59 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 6.220904383333134
""",
)

entry(
    index = 30,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-3R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2968.69,'s^-1'), n=2.48894, w0=(435000,'J/mol'), E0=(106342,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-3R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-3R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.47046e-07,'s^-1'), n=5.47513, w0=(395000,'J/mol'), E0=(14372,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0885066496339222, var=14.957632269250416, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C
    Total Standard Deviation in ln(k): 7.975711130915847"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C
Total Standard Deviation in ln(k): 7.975711130915847""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C
Total Standard Deviation in ln(k): 7.975711130915847
""",
)

entry(
    index = 32,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.000821,'s^-1'), n=4.56, w0=(387000,'J/mol'), E0=(114695,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing",
    kinetics = ArrheniusBM(A=(6.12789e+13,'s^-1'), n=-0.0233004, w0=(411000,'J/mol'), E0=(218999,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06613308070251134, var=109.63801272433597, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing',), comment="""BM rule fitted to 26 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing
    Total Standard Deviation in ln(k): 21.157378038502948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing
Total Standard Deviation in ln(k): 21.157378038502948""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing
Total Standard Deviation in ln(k): 21.157378038502948
""",
)

entry(
    index = 34,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(1.52414e+17,'s^-1'), n=-1.25999, w0=(411000,'J/mol'), E0=(198067,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1787936828372538, var=53.959512629471064, Tref=1000.0, N=55, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing',), comment="""BM rule fitted to 55 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing
    Total Standard Deviation in ln(k): 15.175440673006"""),
    rank = 11,
    shortDesc = """BM rule fitted to 55 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing
Total Standard Deviation in ln(k): 15.175440673006""",
    longDesc = 
"""
BM rule fitted to 55 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing
Total Standard Deviation in ln(k): 15.175440673006
""",
)

entry(
    index = 35,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.83482e-15,'s^-1'), n=7.90899, w0=(411000,'J/mol'), E0=(99058.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3325463704723599, var=25.381276256894505, Tref=1000.0, N=314, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R',), comment="""BM rule fitted to 314 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 10.935365589856127"""),
    rank = 11,
    shortDesc = """BM rule fitted to 314 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 10.935365589856127""",
    longDesc = 
"""
BM rule fitted to 314 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 10.935365589856127
""",
)

entry(
    index = 36,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.62793e-58,'s^-1'), n=20.5689, w0=(411000,'J/mol'), E0=(15016.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0663388962484346, var=8.80857322127193, Tref=1000.0, N=58, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R',), comment="""BM rule fitted to 58 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 8.629144926462518"""),
    rank = 11,
    shortDesc = """BM rule fitted to 58 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R
Total Standard Deviation in ln(k): 8.629144926462518""",
    longDesc = 
"""
BM rule fitted to 58 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R
Total Standard Deviation in ln(k): 8.629144926462518
""",
)

entry(
    index = 37,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(18219,'s^-1'), n=2.54712, w0=(411000,'J/mol'), E0=(156173,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05166323954251763, var=10.800499646654425, Tref=1000.0, N=47, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R',), comment="""BM rule fitted to 47 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R
    Total Standard Deviation in ln(k): 6.718191272620372"""),
    rank = 11,
    shortDesc = """BM rule fitted to 47 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R
Total Standard Deviation in ln(k): 6.718191272620372""",
    longDesc = 
"""
BM rule fitted to 47 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R
Total Standard Deviation in ln(k): 6.718191272620372
""",
)

entry(
    index = 38,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C",
    kinetics = ArrheniusBM(A=(8.62172e+09,'s^-1'), n=0.964164, w0=(411000,'J/mol'), E0=(173100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.003575086783767702, var=0.7720476219031678, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C
    Total Standard Deviation in ln(k): 1.7704679745356886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C
Total Standard Deviation in ln(k): 1.7704679745356886""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C
Total Standard Deviation in ln(k): 1.7704679745356886
""",
)

entry(
    index = 39,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-4R!H-3C_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(7.80277e+09,'s^-1'), n=0.776445, w0=(411000,'J/mol'), E0=(164615,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0011423590601642357, var=15.397173566340884, Tref=1000.0, N=94, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-4R!H-3C_Sp-4R!H-3C',), comment="""BM rule fitted to 94 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-4R!H-3C_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 7.869296802209575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 94 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-4R!H-3C_Sp-4R!H-3C
Total Standard Deviation in ln(k): 7.869296802209575""",
    longDesc = 
"""
BM rule fitted to 94 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-4R!H-3C_Sp-4R!H-3C
Total Standard Deviation in ln(k): 7.869296802209575
""",
)

entry(
    index = 40,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-4R!H-3C_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(337487,'s^-1'), n=2.17101, w0=(411000,'J/mol'), E0=(194138,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.0182159112448714e-14, var=0.8208346155989246, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-4R!H-3C_N-Sp-4R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-4R!H-3C_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 1.816288448464323"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-4R!H-3C_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 1.816288448464323""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-4R!H-3C_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 1.816288448464323
""",
)

entry(
    index = 41,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(7.95615e+15,'s^-1'), n=-0.647981, w0=(411000,'J/mol'), E0=(194197,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1958115700760942, var=37.72424393781524, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 13 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 12.80508476064793"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 12.80508476064793""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 12.80508476064793
""",
)

entry(
    index = 42,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(0.0923158,'s^-1'), n=4.1167, w0=(411000,'J/mol'), E0=(135308,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0912666761443932, var=10.576813379525337, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 19 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 6.749115307330298"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 6.749115307330298""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 6.749115307330298
""",
)

entry(
    index = 43,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C_4R!H->C",
    kinetics = ArrheniusBM(A=(5.48449e-73,'s^-1'), n=25.2307, w0=(411000,'J/mol'), E0=(-13672.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.0901372678008014, var=10.773821069160885, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C_4R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C_4R!H->C
    Total Standard Deviation in ln(k): 11.831843218222351"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C_4R!H->C
Total Standard Deviation in ln(k): 11.831843218222351""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C_4R!H->C
Total Standard Deviation in ln(k): 11.831843218222351
""",
)

entry(
    index = 44,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(2.12549e+13,'s^-1'), n=0.0400144, w0=(411000,'J/mol'), E0=(173575,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.262406225749307e-14, var=1.5220551232684387, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 2.4732737038660777"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C_N-4R!H->C
Total Standard Deviation in ln(k): 2.4732737038660777""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C_N-4R!H->C
Total Standard Deviation in ln(k): 2.4732737038660777
""",
)

entry(
    index = 45,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O",
    kinetics = ArrheniusBM(A=(4.44628e+07,'s^-1'), n=1.10889, w0=(435000,'J/mol'), E0=(70199.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0016081837802506874, var=7.799555716157679, Tref=1000.0, N=73, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O',), comment="""BM rule fitted to 73 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O
    Total Standard Deviation in ln(k): 5.602801573712938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 73 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O
Total Standard Deviation in ln(k): 5.602801573712938""",
    longDesc = 
"""
BM rule fitted to 73 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O
Total Standard Deviation in ln(k): 5.602801573712938
""",
)

entry(
    index = 46,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_N-3OS->O",
    kinetics = ArrheniusBM(A=(2.74749e+14,'s^-1'), n=-0.505079, w0=(387000,'J/mol'), E0=(46307.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.017457238679144456, var=3.030893134222422, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_N-3OS->O',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_N-3OS->O
    Total Standard Deviation in ln(k): 3.533998014512884"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_N-3OS->O
Total Standard Deviation in ln(k): 3.533998014512884""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_N-3OS->O
Total Standard Deviation in ln(k): 3.533998014512884
""",
)

entry(
    index = 47,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.463797,'s^-1'), n=3.74479, w0=(435000,'J/mol'), E0=(97605.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0722299650169795, var=0.07646985824375013, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.7358554027762921"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.7358554027762921""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.7358554027762921
""",
)

entry(
    index = 48,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.03263e+10,'s^-1'), n=0.912963, w0=(435000,'J/mol'), E0=(141237,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00639357383853101, var=0.40695750592651153, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.2949493364165294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.2949493364165294""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.2949493364165294
""",
)

entry(
    index = 49,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_3OS->O",
    kinetics = ArrheniusBM(A=(1.57e+08,'s^-1'), n=1.45, w0=(435000,'J/mol'), E0=(143229,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_3OS->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_3OS->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_3OS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_3OS->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_N-3OS->O",
    kinetics = ArrheniusBM(A=(3.33142e-06,'s^-1'), n=5.68654, w0=(387000,'J/mol'), E0=(104258,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_N-3OS->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_N-3OS->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_N-3OS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_N-3OS->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_1R!H->C_N-3R!H->C_3OS->O_Ext-1C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(76500,'s^-1'), n=2.26, w0=(435000,'J/mol'), E0=(108183,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_3OS->O_Ext-1C-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_3OS->O_Ext-1C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_3OS->O_Ext-1C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_3OS->O_Ext-1C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(999.461,'s^-1'), n=2.19619, w0=(435000,'J/mol'), E0=(62047.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.061306918556804126, var=12.438436001237765, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R',), comment="""BM rule fitted to 21 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R
    Total Standard Deviation in ln(k): 7.22437062413145"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R
Total Standard Deviation in ln(k): 7.22437062413145""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R
Total Standard Deviation in ln(k): 7.22437062413145
""",
)

entry(
    index = 53,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(5.5163e-09,'s^-1'), n=5.61347, w0=(435000,'J/mol'), E0=(77704.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.594956598695091, var=17.29838335549451, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 14.857950317196655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 14.857950317196655""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 14.857950317196655
""",
)

entry(
    index = 54,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Int-4C-3R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.58064e-06,'s^-1'), n=6.01842, w0=(435000,'J/mol'), E0=(117763,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Int-4C-3R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Int-4C-3R!H_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Int-4C-3R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Int-4C-3R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Int-4C-3R!H_Ext-3R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(4266.79,'s^-1'), n=2.19581, w0=(435000,'J/mol'), E0=(97614.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Int-4C-3R!H_Ext-3R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Int-4C-3R!H_Ext-3R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Int-4C-3R!H_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Int-4C-3R!H_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(2.22215,'s^-1'), n=2.93973, w0=(435000,'J/mol'), E0=(53503.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07613581250996147, var=8.62618784679819, Tref=1000.0, N=50, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R',), comment="""BM rule fitted to 50 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R
    Total Standard Deviation in ln(k): 6.07927762329939"""),
    rank = 11,
    shortDesc = """BM rule fitted to 50 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R
Total Standard Deviation in ln(k): 6.07927762329939""",
    longDesc = 
"""
BM rule fitted to 50 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R
Total Standard Deviation in ln(k): 6.07927762329939
""",
)

entry(
    index = 57,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.77055e+10,'s^-1'), n=0.476066, w0=(435000,'J/mol'), E0=(139999,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004172231286660466, var=0.43184102064981666, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.327886867287835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.327886867287835""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.327886867287835
""",
)

entry(
    index = 58,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(9.80429e+10,'s^-1'), n=0.108634, w0=(387000,'J/mol'), E0=(43374.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.018470885893508295, var=2.7818207229665397, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_Ext-3R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_Ext-3R!H-R
    Total Standard Deviation in ln(k): 3.390065016141599"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.390065016141599""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.390065016141599
""",
)

entry(
    index = 59,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_3R!H->C",
    kinetics = ArrheniusBM(A=(85.5,'s^-1'), n=3.04, w0=(387000,'J/mol'), E0=(76806.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_3R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_3R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_3R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_3R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_N-3R!H->C",
    kinetics = ArrheniusBM(A=(4.99e+11,'s^-1'), n=0.26, w0=(411000,'J/mol'), E0=(66898.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.273559366969508e-15, var=4.9920104158517705e-31, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_N-3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_N-3R!H->C
    Total Standard Deviation in ln(k): 1.466657790524389e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_N-3R!H->C
Total Standard Deviation in ln(k): 1.466657790524389e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_N-3R!H->C
Total Standard Deviation in ln(k): 1.466657790524389e-14
""",
)

entry(
    index = 61,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-3C-R_Ext-5R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.15163e+12,'s^-1'), n=0.130764, w0=(411000,'J/mol'), E0=(161167,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.4012784201783086, var=404.7957144276851, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-3C-R_Ext-5R!H-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-3C-R_Ext-5R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 46.367701706071315"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-3C-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 46.367701706071315""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-3C-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 46.367701706071315
""",
)

entry(
    index = 62,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(4.23573e+34,'s^-1'), n=-6.17638, w0=(411000,'J/mol'), E0=(290023,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.405485738748155, var=74.62892277225738, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 19 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 18.33732042771772"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 18.33732042771772""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 18.33732042771772
""",
)

entry(
    index = 63,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.85466e+11,'s^-1'), n=0.614175, w0=(411000,'J/mol'), E0=(181341,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.846876143357608e-14, var=51.66010811322203, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 14.409026655621904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 14.409026655621904""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 14.409026655621904
""",
)

entry(
    index = 64,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.25026e+12,'s^-1'), n=1.02883, w0=(411000,'J/mol'), E0=(177699,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing",
    kinetics = ArrheniusBM(A=(5.14706e+06,'s^-1'), n=1.81984, w0=(411000,'J/mol'), E0=(132413,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00040305967008980726, var=104.52120025227144, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing',), comment="""BM rule fitted to 13 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing
    Total Standard Deviation in ln(k): 20.496544137042324"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing
Total Standard Deviation in ln(k): 20.496544137042324""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing
Total Standard Deviation in ln(k): 20.496544137042324
""",
)

entry(
    index = 66,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing",
    kinetics = ArrheniusBM(A=(2.90335e+16,'s^-1'), n=-1.04208, w0=(411000,'J/mol'), E0=(212007,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.19609127893114922, var=31.230027769296825, Tref=1000.0, N=42, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing',), comment="""BM rule fitted to 42 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing
    Total Standard Deviation in ln(k): 11.695919658211238"""),
    rank = 11,
    shortDesc = """BM rule fitted to 42 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing
Total Standard Deviation in ln(k): 11.695919658211238""",
    longDesc = 
"""
BM rule fitted to 42 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing
Total Standard Deviation in ln(k): 11.695919658211238
""",
)

entry(
    index = 67,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C",
    kinetics = ArrheniusBM(A=(35.6955,'s^-1'), n=3.05054, w0=(411000,'J/mol'), E0=(119275,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.029519733018033307, var=54.327104489154955, Tref=1000.0, N=60, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C',), comment="""BM rule fitted to 60 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C
    Total Standard Deviation in ln(k): 14.850455515025446"""),
    rank = 11,
    shortDesc = """BM rule fitted to 60 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C
Total Standard Deviation in ln(k): 14.850455515025446""",
    longDesc = 
"""
BM rule fitted to 60 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C
Total Standard Deviation in ln(k): 14.850455515025446
""",
)

entry(
    index = 68,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C",
    kinetics = ArrheniusBM(A=(7.28308e+07,'s^-1'), n=1.52949, w0=(411000,'J/mol'), E0=(191286,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.023338530353951906, var=11.09507406981275, Tref=1000.0, N=44, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C',), comment="""BM rule fitted to 44 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C
    Total Standard Deviation in ln(k): 6.7362655372213975"""),
    rank = 11,
    shortDesc = """BM rule fitted to 44 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C
Total Standard Deviation in ln(k): 6.7362655372213975""",
    longDesc = 
"""
BM rule fitted to 44 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C
Total Standard Deviation in ln(k): 6.7362655372213975
""",
)

entry(
    index = 69,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(6.42071e-43,'s^-1'), n=16.0789, w0=(411000,'J/mol'), E0=(31342.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8028001537995771, var=16.573963061237375, Tref=1000.0, N=94, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 94 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 10.178589341739016"""),
    rank = 11,
    shortDesc = """BM rule fitted to 94 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 10.178589341739016""",
    longDesc = 
"""
BM rule fitted to 94 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 10.178589341739016
""",
)

entry(
    index = 70,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(2.04248e-13,'s^-1'), n=7.30196, w0=(411000,'J/mol'), E0=(91721.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5478812111633, var=21.111047473655944, Tref=1000.0, N=116, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 116 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 10.587694088598628"""),
    rank = 11,
    shortDesc = """BM rule fitted to 116 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 10.587694088598628""",
    longDesc = 
"""
BM rule fitted to 116 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 10.587694088598628
""",
)

entry(
    index = 71,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing",
    kinetics = ArrheniusBM(A=(7.75885e+08,'s^-1'), n=1.07655, w0=(411000,'J/mol'), E0=(146545,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0006180785112759613, var=24.36658409978534, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing',), comment="""BM rule fitted to 18 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing
    Total Standard Deviation in ln(k): 9.897430555691928"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing
Total Standard Deviation in ln(k): 9.897430555691928""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing
Total Standard Deviation in ln(k): 9.897430555691928
""",
)

entry(
    index = 72,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing",
    kinetics = ArrheniusBM(A=(1.78783e-58,'s^-1'), n=20.7504, w0=(411000,'J/mol'), E0=(15417.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0746401386147237, var=2.504653986688776, Tref=1000.0, N=40, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing',), comment="""BM rule fitted to 40 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing
    Total Standard Deviation in ln(k): 5.872814362185505"""),
    rank = 11,
    shortDesc = """BM rule fitted to 40 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing
Total Standard Deviation in ln(k): 5.872814362185505""",
    longDesc = 
"""
BM rule fitted to 40 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing
Total Standard Deviation in ln(k): 5.872814362185505
""",
)

entry(
    index = 73,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.17143e+12,'s^-1'), n=0.111482, w0=(411000,'J/mol'), E0=(163846,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04547843829105656, var=9.0428169505719, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 19 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 6.142761797440665"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.142761797440665""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.142761797440665
""",
)

entry(
    index = 74,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(0.0356626,'s^-1'), n=4.17807, w0=(411000,'J/mol'), E0=(153413,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12385969514673958, var=9.652388289183877, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C',), comment="""BM rule fitted to 26 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C
    Total Standard Deviation in ln(k): 6.539574938097432"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C
Total Standard Deviation in ln(k): 6.539574938097432""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C
Total Standard Deviation in ln(k): 6.539574938097432
""",
)

entry(
    index = 75,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_N-Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(4.34618e+08,'s^-1'), n=1.25262, w0=(411000,'J/mol'), E0=(162215,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.841571355720966e-15, var=0.04221798089308098, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_N-Sp-5R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_N-Sp-5R!H-3C
    Total Standard Deviation in ln(k): 0.41191320902312284"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 0.41191320902312284""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 0.41191320902312284
""",
)

entry(
    index = 76,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C_4R!H->C",
    kinetics = ArrheniusBM(A=(1.41767e+09,'s^-1'), n=1.23749, w0=(411000,'J/mol'), E0=(173333,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.003279317834917039, var=1.0836760921377713, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C_4R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C_4R!H->C
    Total Standard Deviation in ln(k): 2.095163981882497"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C_4R!H->C
Total Standard Deviation in ln(k): 2.095163981882497""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C_4R!H->C
Total Standard Deviation in ln(k): 2.095163981882497
""",
)

entry(
    index = 77,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.4046e+13,'s^-1'), n=-0.149533, w0=(411000,'J/mol'), E0=(172414,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.1074096357220593e-14, var=1.522055123268426, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 2.4732737038660635"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C_N-4R!H->C
Total Standard Deviation in ln(k): 2.4732737038660635""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C_N-4R!H->C
Total Standard Deviation in ln(k): 2.4732737038660635
""",
)

entry(
    index = 78,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(2.27217e+15,'s^-1'), n=-0.487395, w0=(411000,'J/mol'), E0=(185138,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.23030650122290006, var=61.00934009161797, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C',), comment="""BM rule fitted to 10 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C
    Total Standard Deviation in ln(k): 16.237339700897863"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C
Total Standard Deviation in ln(k): 16.237339700897863""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C
Total Standard Deviation in ln(k): 16.237339700897863
""",
)

entry(
    index = 79,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(3.1808e+06,'s^-1'), n=2.12891, w0=(411000,'J/mol'), E0=(192015,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07546773553777619, var=0.45866568958178827, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 1.547321485113894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 1.547321485113894""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 1.547321485113894
""",
)

entry(
    index = 80,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(0.0369317,'s^-1'), n=4.24425, w0=(411000,'J/mol'), E0=(140907,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11688620586780968, var=5.8739139771627755, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C',), comment="""BM rule fitted to 16 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C
    Total Standard Deviation in ln(k): 5.152391721045702"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C
Total Standard Deviation in ln(k): 5.152391721045702""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C
Total Standard Deviation in ln(k): 5.152391721045702
""",
)

entry(
    index = 81,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(1.00563e+12,'s^-1'), n=0.202776, w0=(411000,'J/mol'), E0=(122408,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08478286697937305, var=44.47596133538591, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 13.58266068126804"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 13.58266068126804""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 13.58266068126804
""",
)

entry(
    index = 82,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C_4R!H->C_Sp-4C-3C",
    kinetics = ArrheniusBM(A=(3.45914e+07,'s^-1'), n=1.6656, w0=(411000,'J/mol'), E0=(161529,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.011564135360099946, var=5.507604855606712, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C_4R!H->C_Sp-4C-3C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C_4R!H->C_Sp-4C-3C
    Total Standard Deviation in ln(k): 4.733825392911052"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C_4R!H->C_Sp-4C-3C
Total Standard Deviation in ln(k): 4.733825392911052""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C_4R!H->C_Sp-4C-3C
Total Standard Deviation in ln(k): 4.733825392911052
""",
)

entry(
    index = 83,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C_4R!H->C_N-Sp-4C-3C",
    kinetics = ArrheniusBM(A=(1.67497e+09,'s^-1'), n=1.15284, w0=(411000,'J/mol'), E0=(213898,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.786654763449407e-17, var=1.8876904843797733, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C_4R!H->C_N-Sp-4C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C_4R!H->C_N-Sp-4C-3C
    Total Standard Deviation in ln(k): 2.754370654706236"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C_4R!H->C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 2.754370654706236""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Int-3C-1C_Sp-3C-1C_4R!H->C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 2.754370654706236
""",
)

entry(
    index = 84,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C",
    kinetics = ArrheniusBM(A=(2.9481e+06,'s^-1'), n=1.62388, w0=(435000,'J/mol'), E0=(87926.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03651774628918092, var=2.271984393352723, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C',), comment="""BM rule fitted to 26 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C
    Total Standard Deviation in ln(k): 3.1135109974638544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C
Total Standard Deviation in ln(k): 3.1135109974638544""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C
Total Standard Deviation in ln(k): 3.1135109974638544
""",
)

entry(
    index = 85,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C",
    kinetics = ArrheniusBM(A=(7.93848e+13,'s^-1'), n=-0.655242, w0=(435000,'J/mol'), E0=(73630.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10597898732000431, var=12.10052616679662, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C',), comment="""BM rule fitted to 28 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C
    Total Standard Deviation in ln(k): 7.2399123261823135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C
Total Standard Deviation in ln(k): 7.2399123261823135""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C
Total Standard Deviation in ln(k): 7.2399123261823135
""",
)

entry(
    index = 86,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C",
    kinetics = ArrheniusBM(A=(9.16726e+09,'s^-1'), n=-0.379008, w0=(435000,'J/mol'), E0=(110182,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004197331293287508, var=11.939634157642326, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C
    Total Standard Deviation in ln(k): 6.937662680597455"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C
Total Standard Deviation in ln(k): 6.937662680597455""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C
Total Standard Deviation in ln(k): 6.937662680597455
""",
)

entry(
    index = 87,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1086.5,'s^-1'), n=2.06842, w0=(435000,'J/mol'), E0=(41155.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1547225040194285, var=3.049977083736834, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C',), comment="""BM rule fitted to 13 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C
    Total Standard Deviation in ln(k): 3.8898561536660576"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C
Total Standard Deviation in ln(k): 3.8898561536660576""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C
Total Standard Deviation in ln(k): 3.8898561536660576
""",
)

entry(
    index = 88,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_N-3OS->O_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(2.02789e+12,'s^-1'), n=0.121694, w0=(387000,'J/mol'), E0=(40750.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.911976076526591e-15, var=2.5675081511571354, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_N-3OS->O_Sp-5R!H-4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_N-3OS->O_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 3.212276384410907"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_N-3OS->O_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 3.212276384410907""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_N-3OS->O_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 3.212276384410907
""",
)

entry(
    index = 89,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_N-3OS->O_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(3.60682e+10,'s^-1'), n=0.84551, w0=(387000,'J/mol'), E0=(91070.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_N-3OS->O_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_N-3OS->O_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_N-3OS->O_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_N-3OS->O_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_4R!H->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7e-08,'s^-1'), n=6.3, w0=(435000,'J/mol'), E0=(115186,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_4R!H->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_4R!H->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_4R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_4R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_4R!H->C_Ext-1C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(9000,'s^-1'), n=2.287, w0=(435000,'J/mol'), E0=(96609.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_4R!H->C_Ext-1C-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_4R!H->C_Ext-1C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_4R!H->C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_4R!H->C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.3736e+10,'s^-1'), n=0.851945, w0=(435000,'J/mol'), E0=(134125,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06195011163934345, var=0.065460773370415, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.6685710923382886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.6685710923382886""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.6685710923382886
""",
)

entry(
    index = 93,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.23502e+10,'s^-1'), n=0.797019, w0=(435000,'J/mol'), E0=(146705,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.018318661209691247, var=0.3299656003782434, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.1975993857466936"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.1975993857466936""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.1975993857466936
""",
)

entry(
    index = 94,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(3.33e+08,'s^-1'), n=1.28, w0=(435000,'J/mol'), E0=(133422,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3e+08,'s^-1'), n=1.23, w0=(435000,'J/mol'), E0=(132997,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(525.502,'s^-1'), n=2.17188, w0=(435000,'J/mol'), E0=(42105.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.39067615368682723, var=17.632706598620903, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H
    Total Standard Deviation in ln(k): 9.399744885769772"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H
Total Standard Deviation in ln(k): 9.399744885769772""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H
Total Standard Deviation in ln(k): 9.399744885769772
""",
)

entry(
    index = 97,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.42137e+06,'s^-1'), n=0.500473, w0=(435000,'J/mol'), E0=(106272,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0020874052896491155, var=12.10771869251732, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 6.980950448664473"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.980950448664473""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.980950448664473
""",
)

entry(
    index = 98,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Sp-6R!H-4C",
    kinetics = ArrheniusBM(A=(226.401,'s^-1'), n=2.39564, w0=(435000,'J/mol'), E0=(67640.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15350872443349559, var=3.5220941756746353, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Sp-6R!H-4C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Sp-6R!H-4C
    Total Standard Deviation in ln(k): 4.148035388828901"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Sp-6R!H-4C
Total Standard Deviation in ln(k): 4.148035388828901""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Sp-6R!H-4C
Total Standard Deviation in ln(k): 4.148035388828901
""",
)

entry(
    index = 99,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_N-Sp-6R!H-4C",
    kinetics = ArrheniusBM(A=(1.46865e+08,'s^-1'), n=1.37918, w0=(435000,'J/mol'), E0=(115752,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_N-Sp-6R!H-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_N-Sp-6R!H-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_N-Sp-6R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_N-Sp-6R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 100,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(32.0094,'s^-1'), n=2.77578, w0=(435000,'J/mol'), E0=(78230.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.22125587862965218, var=5.7836130810940904, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H
    Total Standard Deviation in ln(k): 5.377135469560429"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 5.377135469560429""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H
Total Standard Deviation in ln(k): 5.377135469560429
""",
)

entry(
    index = 101,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(20.1156,'s^-1'), n=2.54836, w0=(435000,'J/mol'), E0=(38759.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.18395584635402756, var=5.632698499604569, Tref=1000.0, N=30, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H',), comment="""BM rule fitted to 30 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 5.220099876241324"""),
    rank = 11,
    shortDesc = """BM rule fitted to 30 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 5.220099876241324""",
    longDesc = 
"""
BM rule fitted to 30 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 5.220099876241324
""",
)

entry(
    index = 102,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(306.116,'s^-1'), n=2.45324, w0=(435000,'J/mol'), E0=(131639,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 103,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(6.84247e+10,'s^-1'), n=0.438383, w0=(435000,'J/mol'), E0=(144395,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.011381620299470143, var=0.2513185128827167, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.0336043676274367"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.0336043676274367""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.0336043676274367
""",
)

entry(
    index = 104,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.90638e+10,'s^-1'), n=0.543862, w0=(435000,'J/mol'), E0=(134803,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.046878711381011705, var=0.5795860572362846, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 1.644001538110327"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_5R!H->C
Total Standard Deviation in ln(k): 1.644001538110327""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_5R!H->C
Total Standard Deviation in ln(k): 1.644001538110327
""",
)

entry(
    index = 105,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.35932e+07,'s^-1'), n=1.35012, w0=(435000,'J/mol'), E0=(131893,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 106,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.61e+11,'s^-1'), n=0.22, w0=(387000,'J/mol'), E0=(96324.3,'J/mol'), Tmin=(300,'K'), Tmax=(1550,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 107,
    label = "Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_Ext-3R!H-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.21e+10,'s^-1'), n=0.214, w0=(387000,'J/mol'), E0=(30194,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_Ext-3R!H-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_Ext-3R!H-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_Ext-3R!H-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_N-1BrClFINOPSSi->O_Ext-1S-R_4R!H->C_Ext-3R!H-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 108,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_3C-inRing",
    kinetics = ArrheniusBM(A=(642906,'s^-1'), n=2.00533, w0=(411000,'J/mol'), E0=(91355.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.4795152863259646e-15, var=0.09444486157929466, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_3C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_3C-inRing
    Total Standard Deviation in ln(k): 0.6160928329218596"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_3C-inRing
Total Standard Deviation in ln(k): 0.6160928329218596""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_3C-inRing
Total Standard Deviation in ln(k): 0.6160928329218596
""",
)

entry(
    index = 109,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_N-3C-inRing",
    kinetics = ArrheniusBM(A=(5.87108e+13,'s^-1'), n=0.892442, w0=(411000,'J/mol'), E0=(470065,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_N-3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_N-3C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_N-3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_N-3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 110,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3C",
    kinetics = ArrheniusBM(A=(2.90781e+124,'s^-1'), n=-32.3206, w0=(411000,'J/mol'), E0=(616547,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=15.19752359565196, var=1766.4846266639338, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3C
    Total Standard Deviation in ln(k): 122.44288287315351"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3C
Total Standard Deviation in ln(k): 122.44288287315351""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3C
Total Standard Deviation in ln(k): 122.44288287315351
""",
)

entry(
    index = 111,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing",
    kinetics = ArrheniusBM(A=(3.81466e+34,'s^-1'), n=-6.16993, w0=(411000,'J/mol'), E0=(277438,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.39231147193805793, var=55.73177412416543, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing',), comment="""BM rule fitted to 15 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing
    Total Standard Deviation in ln(k): 15.95179966223773"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing
Total Standard Deviation in ln(k): 15.95179966223773""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing
Total Standard Deviation in ln(k): 15.95179966223773
""",
)

entry(
    index = 112,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-1C-inRing",
    kinetics = ArrheniusBM(A=(121.196,'s^-1'), n=3.09435, w0=(411000,'J/mol'), E0=(182570,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0051595538305861015, var=65.70968870587475, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-1C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-1C-inRing
    Total Standard Deviation in ln(k): 16.263649533047904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-1C-inRing
Total Standard Deviation in ln(k): 16.263649533047904""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-1C-inRing
Total Standard Deviation in ln(k): 16.263649533047904
""",
)

entry(
    index = 113,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(2.14912e+48,'s^-1'), n=-10.3886, w0=(411000,'J/mol'), E0=(257839,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.322875795063743, var=168.0037558103258, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C
    Total Standard Deviation in ln(k): 26.795872578897495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C
Total Standard Deviation in ln(k): 26.795872578897495""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C
Total Standard Deviation in ln(k): 26.795872578897495
""",
)

entry(
    index = 114,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(8.57158e+10,'s^-1'), n=0.45187, w0=(411000,'J/mol'), E0=(92653.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.055486650770905324, var=3.006889275381358, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C
    Total Standard Deviation in ln(k): 3.6157013608027424"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 3.6157013608027424""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 3.6157013608027424
""",
)

entry(
    index = 115,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C",
    kinetics = ArrheniusBM(A=(1.03012e+12,'s^-1'), n=0.396357, w0=(411000,'J/mol'), E0=(204248,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.025956212070301493, var=5.156259575325087, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C',), comment="""BM rule fitted to 17 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C
    Total Standard Deviation in ln(k): 4.617448490265912"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C
Total Standard Deviation in ln(k): 4.617448490265912""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C
Total Standard Deviation in ln(k): 4.617448490265912
""",
)

entry(
    index = 116,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C",
    kinetics = ArrheniusBM(A=(1.81825e+17,'s^-1'), n=-1.14844, w0=(411000,'J/mol'), E0=(225336,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.13561535659980692, var=29.000037949604785, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C',), comment="""BM rule fitted to 11 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C
    Total Standard Deviation in ln(k): 11.136577952167103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C
Total Standard Deviation in ln(k): 11.136577952167103""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C
Total Standard Deviation in ln(k): 11.136577952167103
""",
)

entry(
    index = 117,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Int-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(22332.9,'s^-1'), n=2.22523, w0=(411000,'J/mol'), E0=(211529,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.6916240297166782, var=168.76549956740908, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Int-5R!H-4R!H',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Int-5R!H-4R!H
    Total Standard Deviation in ln(k): 30.293780160310373"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Int-5R!H-4R!H
Total Standard Deviation in ln(k): 30.293780160310373""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Int-5R!H-4R!H
Total Standard Deviation in ln(k): 30.293780160310373
""",
)

entry(
    index = 118,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.43003e+09,'s^-1'), n=0.827234, w0=(411000,'J/mol'), E0=(157144,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04402684544958665, var=1.3024600599526792, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 2.3985315851310864"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.3985315851310864""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.3985315851310864
""",
)

entry(
    index = 119,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.36439e+08,'s^-1'), n=1.13431, w0=(411000,'J/mol'), E0=(161578,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0543985716139288e-14, var=0.04221798089311289, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-1C-R
    Total Standard Deviation in ln(k): 0.4119132090232828"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 0.4119132090232828""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 0.4119132090232828
""",
)

entry(
    index = 120,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(2.71959e+12,'s^-1'), n=-0.202525, w0=(411000,'J/mol'), E0=(110171,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.13517391880197865, var=6.196099136077553, Tref=1000.0, N=44, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H',), comment="""BM rule fitted to 44 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 5.32981246786312"""),
    rank = 11,
    shortDesc = """BM rule fitted to 44 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 5.32981246786312""",
    longDesc = 
"""
BM rule fitted to 44 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 5.32981246786312
""",
)

entry(
    index = 121,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(4.25485e+16,'s^-1'), n=-1.31642, w0=(411000,'J/mol'), E0=(224850,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6797189906281119, var=74.64043367772497, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 16 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 19.027684267216124"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 19.027684267216124""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 19.027684267216124
""",
)

entry(
    index = 122,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(3.83143e+07,'s^-1'), n=1.70485, w0=(411000,'J/mol'), E0=(209329,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0110469340196304, var=6.562243420427611, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H',), comment="""BM rule fitted to 24 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 5.163261128320081"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 5.163261128320081""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 5.163261128320081
""",
)

entry(
    index = 123,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(6.05137e-55,'s^-1'), n=19.7476, w0=(411000,'J/mol'), E0=(22871.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9249325383225004, var=7.487664887979259, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 20 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 7.809627552172833"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 7.809627552172833""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 7.809627552172833
""",
)

entry(
    index = 124,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(7.08692e-47,'s^-1'), n=17.343, w0=(411000,'J/mol'), E0=(3409.72,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8809656261896871, var=23.205736023802064, Tref=1000.0, N=55, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R',), comment="""BM rule fitted to 55 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.87075791158042"""),
    rank = 11,
    shortDesc = """BM rule fitted to 55 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.87075791158042""",
    longDesc = 
"""
BM rule fitted to 55 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.87075791158042
""",
)

entry(
    index = 125,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C",
    kinetics = ArrheniusBM(A=(7.31275e-55,'s^-1'), n=19.7355, w0=(411000,'J/mol'), E0=(28396.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9424438051420054, var=10.962274006786556, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C',), comment="""BM rule fitted to 17 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C
    Total Standard Deviation in ln(k): 9.005491776919063"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C
Total Standard Deviation in ln(k): 9.005491776919063""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C
Total Standard Deviation in ln(k): 9.005491776919063
""",
)

entry(
    index = 126,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.23363e+08,'s^-1'), n=0.485828, w0=(411000,'J/mol'), E0=(88240.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08494393259284662, var=4.0220881507951525, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R',), comment="""BM rule fitted to 15 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 4.233952103279004"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 4.233952103279004""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 4.233952103279004
""",
)

entry(
    index = 127,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.52228e+07,'s^-1'), n=1.35733, w0=(411000,'J/mol'), E0=(155894,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.010491566587114328, var=3.904693905277638, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 3.9877770424780676"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 3.9877770424780676""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 3.9877770424780676
""",
)

entry(
    index = 128,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing",
    kinetics = ArrheniusBM(A=(4.73205e-06,'s^-1'), n=5.32757, w0=(411000,'J/mol'), E0=(129353,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21149648266373136, var=21.902450636367156, Tref=1000.0, N=68, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing',), comment="""BM rule fitted to 68 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing
    Total Standard Deviation in ln(k): 9.913569205198561"""),
    rank = 11,
    shortDesc = """BM rule fitted to 68 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing
Total Standard Deviation in ln(k): 9.913569205198561""",
    longDesc = 
"""
BM rule fitted to 68 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing
Total Standard Deviation in ln(k): 9.913569205198561
""",
)

entry(
    index = 129,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(6468.8,'s^-1'), n=2.02468, w0=(411000,'J/mol'), E0=(81511.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03924868513024682, var=10.025565104204752, Tref=1000.0, N=48, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing',), comment="""BM rule fitted to 48 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing
    Total Standard Deviation in ln(k): 6.446242099885617"""),
    rank = 11,
    shortDesc = """BM rule fitted to 48 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing
Total Standard Deviation in ln(k): 6.446242099885617""",
    longDesc = 
"""
BM rule fitted to 48 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing
Total Standard Deviation in ln(k): 6.446242099885617
""",
)

entry(
    index = 130,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(7.79935e+08,'s^-1'), n=1.08582, w0=(411000,'J/mol'), E0=(154208,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.816088082991524e-05, var=5.051334381781329, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 12 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 4.505823065342426"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 4.505823065342426""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 4.505823065342426
""",
)

entry(
    index = 131,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.92019e+08,'s^-1'), n=1.005, w0=(411000,'J/mol'), E0=(66521.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=440.9022129426109, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-1C-R
    Total Standard Deviation in ln(k): 42.09476881545405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 42.09476881545405""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 42.09476881545405
""",
)

entry(
    index = 132,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Int-3C-1C",
    kinetics = ArrheniusBM(A=(9.21744e+09,'s^-1'), n=0.874999, w0=(411000,'J/mol'), E0=(173626,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.4058647621519051e-15, var=96.32222815302124, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Int-3C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Int-3C-1C
    Total Standard Deviation in ln(k): 19.675249555444783"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Int-3C-1C
Total Standard Deviation in ln(k): 19.675249555444783""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Int-3C-1C
Total Standard Deviation in ln(k): 19.675249555444783
""",
)

entry(
    index = 133,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_4R!H->O",
    kinetics = ArrheniusBM(A=(1.52689e-15,'s^-1'), n=8.20959, w0=(411000,'J/mol'), E0=(128987,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.381826042612762e-15, var=0.3371579086880763, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_4R!H->O
    Total Standard Deviation in ln(k): 1.1640554408284651"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_4R!H->O
Total Standard Deviation in ln(k): 1.1640554408284651""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_4R!H->O
Total Standard Deviation in ln(k): 1.1640554408284651
""",
)

entry(
    index = 134,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O",
    kinetics = ArrheniusBM(A=(2.91628e-58,'s^-1'), n=20.6836, w0=(411000,'J/mol'), E0=(15041.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.081274898874226, var=2.4151405704107067, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O',), comment="""BM rule fitted to 38 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O
    Total Standard Deviation in ln(k): 5.83227426294178"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O
Total Standard Deviation in ln(k): 5.83227426294178""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O
Total Standard Deviation in ln(k): 5.83227426294178
""",
)

entry(
    index = 135,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C",
    kinetics = ArrheniusBM(A=(5.37399e+13,'s^-1'), n=-0.16686, w0=(411000,'J/mol'), E0=(168165,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04884875546316626, var=15.29826428786176, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C',), comment="""BM rule fitted to 10 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C
    Total Standard Deviation in ln(k): 7.963855002819774"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C
Total Standard Deviation in ln(k): 7.963855002819774""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C
Total Standard Deviation in ln(k): 7.963855002819774
""",
)

entry(
    index = 136,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.0195e+09,'s^-1'), n=1.16268, w0=(411000,'J/mol'), E0=(158466,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7573309526898815e-15, var=29.802682500890867, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-6R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-6R!H-5R!H
    Total Standard Deviation in ln(k): 10.944216291769465"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-6R!H-5R!H
Total Standard Deviation in ln(k): 10.944216291769465""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-6R!H-5R!H
Total Standard Deviation in ln(k): 10.944216291769465
""",
)

entry(
    index = 137,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_3C-inRing",
    kinetics = ArrheniusBM(A=(3.29027e+13,'s^-1'), n=-0.121471, w0=(411000,'J/mol'), E0=(162344,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06280074175211896, var=10.02126258745812, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_3C-inRing',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_3C-inRing
    Total Standard Deviation in ln(k): 6.504055918854967"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_3C-inRing
Total Standard Deviation in ln(k): 6.504055918854967""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_3C-inRing
Total Standard Deviation in ln(k): 6.504055918854967
""",
)

entry(
    index = 138,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_N-3C-inRing",
    kinetics = ArrheniusBM(A=(7.26571e+07,'s^-1'), n=1.46755, w0=(411000,'J/mol'), E0=(148417,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.514661905379763e-15, var=3.1712869946232227, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_N-3C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_N-3C-inRing
    Total Standard Deviation in ln(k): 3.570053814611125"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_N-3C-inRing
Total Standard Deviation in ln(k): 3.570053814611125""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_N-3C-inRing
Total Standard Deviation in ln(k): 3.570053814611125
""",
)

entry(
    index = 139,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.37778e-64,'s^-1'), n=22.42, w0=(411000,'J/mol'), E0=(16359.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6435632529358146, var=20.739148544088028, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R',), comment="""BM rule fitted to 11 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 10.746607824732981"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R
Total Standard Deviation in ln(k): 10.746607824732981""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R
Total Standard Deviation in ln(k): 10.746607824732981
""",
)

entry(
    index = 140,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C",
    kinetics = ArrheniusBM(A=(0.961235,'s^-1'), n=3.80935, w0=(411000,'J/mol'), E0=(156151,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2188067779908578, var=6.8056841287503635, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C',), comment="""BM rule fitted to 11 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C
    Total Standard Deviation in ln(k): 5.779659737325716"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C
Total Standard Deviation in ln(k): 5.779659737325716""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C
Total Standard Deviation in ln(k): 5.779659737325716
""",
)

entry(
    index = 141,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.45705e-16,'s^-1'), n=8.33892, w0=(411000,'J/mol'), E0=(124578,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0107486433859309, var=5.628881922382919, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_N-5R!H->C
    Total Standard Deviation in ln(k): 4.783293708349904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_N-5R!H->C
Total Standard Deviation in ln(k): 4.783293708349904""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_N-5R!H->C
Total Standard Deviation in ln(k): 4.783293708349904
""",
)

entry(
    index = 142,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C_4R!H->C_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(1.00154e+07,'s^-1'), n=1.69143, w0=(411000,'J/mol'), E0=(159245,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.012913991447379116, var=5.5076049414940735, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C_4R!H->C_Sp-3C-1C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C_4R!H->C_Sp-3C-1C
    Total Standard Deviation in ln(k): 4.7372170278041414"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C_4R!H->C_Sp-3C-1C
Total Standard Deviation in ln(k): 4.7372170278041414""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C_4R!H->C_Sp-3C-1C
Total Standard Deviation in ln(k): 4.7372170278041414
""",
)

entry(
    index = 143,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C_4R!H->C_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(2.24791e+11,'s^-1'), n=0.77192, w0=(411000,'J/mol'), E0=(187678,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.470728631562516e-15, var=1.2189782773399884, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C_4R!H->C_N-Sp-3C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C_4R!H->C_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 2.213374858888696"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C_4R!H->C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 2.213374858888696""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Int-3C-1C_4R!H->C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 2.213374858888696
""",
)

entry(
    index = 144,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(1.3474e+10,'s^-1'), n=1.05059, w0=(411000,'J/mol'), E0=(146086,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3158716493814431, var=11.648436646490637, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 7.635769308250088"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C
Total Standard Deviation in ln(k): 7.635769308250088""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C
Total Standard Deviation in ln(k): 7.635769308250088
""",
)

entry(
    index = 145,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(302097,'s^-1'), n=2.44153, w0=(411000,'J/mol'), E0=(208599,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.024445257498743e-15, var=298.7983478449616, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_N-Sp-4R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 34.653418647143226"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 34.653418647143226""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 34.653418647143226
""",
)

entry(
    index = 146,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.96004e+09,'s^-1'), n=1.32678, w0=(411000,'J/mol'), E0=(205564,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 147,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C",
    kinetics = ArrheniusBM(A=(0.0618821,'s^-1'), n=4.19262, w0=(411000,'J/mol'), E0=(141370,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11735646744327279, var=5.569284440820117, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C',), comment="""BM rule fitted to 15 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C
    Total Standard Deviation in ln(k): 5.025906248756216"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C
Total Standard Deviation in ln(k): 5.025906248756216""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C
Total Standard Deviation in ln(k): 5.025906248756216
""",
)

entry(
    index = 148,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.99526e-18,'s^-1'), n=8.39274, w0=(411000,'J/mol'), E0=(107025,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_4R!H-inRing",
    kinetics = ArrheniusBM(A=(6.7494e+12,'s^-1'), n=-0.226785, w0=(411000,'J/mol'), E0=(94514,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07670168124186505, var=36.010141538052935, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_4R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_4R!H-inRing
    Total Standard Deviation in ln(k): 12.222822395213946"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_4R!H-inRing
Total Standard Deviation in ln(k): 12.222822395213946""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_4R!H-inRing
Total Standard Deviation in ln(k): 12.222822395213946
""",
)

entry(
    index = 150,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(1.37e+08,'s^-1'), n=1.713, w0=(411000,'J/mol'), E0=(173240,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_N-4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_N-4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 151,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.8241e+09,'s^-1'), n=0.820956, w0=(435000,'J/mol'), E0=(91777.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0047781624164764565, var=1.9913715293370595, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 20 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.8410066631562465"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 2.8410066631562465""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 2.8410066631562465
""",
)

entry(
    index = 152,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_4R!H->C",
    kinetics = ArrheniusBM(A=(2.36054e-05,'s^-1'), n=4.77057, w0=(435000,'J/mol'), E0=(81804.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.5949565986951457, var=17.298383355495293, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_4R!H->C
    Total Standard Deviation in ln(k): 14.85795031719698"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 14.85795031719698""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 14.85795031719698
""",
)

entry(
    index = 153,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.29921e+10,'s^-1'), n=0.47801, w0=(435000,'J/mol'), E0=(100900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0003521444255434044, var=0.11607121681501201, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 0.6838825115350323"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 0.6838825115350323""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 0.6838825115350323
""",
)

entry(
    index = 154,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C",
    kinetics = ArrheniusBM(A=(20904,'s^-1'), n=2.18215, w0=(435000,'J/mol'), E0=(45877.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07259063542812937, var=2.7414174013319452, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C',), comment="""BM rule fitted to 26 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C
    Total Standard Deviation in ln(k): 3.5016737501842554"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C
Total Standard Deviation in ln(k): 3.5016737501842554""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C
Total Standard Deviation in ln(k): 3.5016737501842554
""",
)

entry(
    index = 155,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_N-Sp-6R!H-1C",
    kinetics = ArrheniusBM(A=(27903,'s^-1'), n=2.09711, w0=(435000,'J/mol'), E0=(122470,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.4776254631265133, var=41.20630143800507, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_N-Sp-6R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_N-Sp-6R!H-1C
    Total Standard Deviation in ln(k): 16.581449183218403"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_N-Sp-6R!H-1C
Total Standard Deviation in ln(k): 16.581449183218403""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_N-Sp-6R!H-1C
Total Standard Deviation in ln(k): 16.581449183218403
""",
)

entry(
    index = 156,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(8.72348e+08,'s^-1'), n=-0.210791, w0=(435000,'J/mol'), E0=(121760,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0038813368189617903, var=0.9782291639087144, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.9925447169480572"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.9925447169480572""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.9925447169480572
""",
)

entry(
    index = 157,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.33469e+10,'s^-1'), n=-0.375791, w0=(435000,'J/mol'), E0=(93561.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0013363296483071166, var=0.6069419382836586, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 1.5651761130198412"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.5651761130198412""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.5651761130198412
""",
)

entry(
    index = 158,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2973.9,'s^-1'), n=1.83364, w0=(435000,'J/mol'), E0=(43695.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.23492139077814683, var=2.646147921934718, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 3.85135423978791"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.85135423978791""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.85135423978791
""",
)

entry(
    index = 159,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7876.03,'s^-1'), n=1.92358, w0=(435000,'J/mol'), E0=(37931.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03176186382984914, var=0.7362995872465017, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 1.8000247683047534"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.8000247683047534""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.8000247683047534
""",
)

entry(
    index = 160,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_N-3OS->O_Sp-5R!H-4R!H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.68473e+12,'s^-1'), n=0.0353599, w0=(387000,'J/mol'), E0=(32080,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_N-3OS->O_Sp-5R!H-4R!H_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_N-3OS->O_Sp-5R!H-4R!H_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_N-3OS->O_Sp-5R!H-4R!H_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_N-3OS->O_Sp-5R!H-4R!H_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 161,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->O",
    kinetics = ArrheniusBM(A=(3e+08,'s^-1'), n=1.23, w0=(435000,'J/mol'), E0=(122916,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 162,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(4.97e+09,'s^-1'), n=1.01, w0=(435000,'J/mol'), E0=(135279,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-1C-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 163,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.11885e+10,'s^-1'), n=0.861884, w0=(435000,'J/mol'), E0=(147582,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.5421202015155422e-15, var=0.006065465625170296, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.15613097159404382"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.15613097159404382""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.15613097159404382
""",
)

entry(
    index = 164,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.22e+09,'s^-1'), n=1.17, w0=(435000,'J/mol'), E0=(138561,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 165,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.66e+07,'s^-1'), n=1.69, w0=(435000,'J/mol'), E0=(167013,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 166,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.30377e-08,'s^-1'), n=5.06892, w0=(435000,'J/mol'), E0=(-60692.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-6.3036212068362785, var=115.6804405539103, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 37.40014070491911"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 37.40014070491911""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 37.40014070491911
""",
)

entry(
    index = 167,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(15585.1,'s^-1'), n=1.88918, w0=(435000,'J/mol'), E0=(66491.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 168,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-4C-R",
    kinetics = ArrheniusBM(A=(4.12607e+08,'s^-1'), n=0.414008, w0=(435000,'J/mol'), E0=(39030.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 169,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(55300.9,'s^-1'), n=1.82899, w0=(435000,'J/mol'), E0=(46831.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 170,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Sp-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(5.14508e+08,'s^-1'), n=0.32093, w0=(435000,'J/mol'), E0=(34870.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.27140784399567536, var=9.290993833061181, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Sp-5R!H-3R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Sp-5R!H-3R!H
    Total Standard Deviation in ln(k): 6.792588626968472"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Sp-5R!H-3R!H
Total Standard Deviation in ln(k): 6.792588626968472""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Sp-5R!H-3R!H
Total Standard Deviation in ln(k): 6.792588626968472
""",
)

entry(
    index = 171,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_N-Sp-5R!H-3R!H",
    kinetics = ArrheniusBM(A=(1.65024e+07,'s^-1'), n=1.0892, w0=(435000,'J/mol'), E0=(102026,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_N-Sp-5R!H-3R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_N-Sp-5R!H-3R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_N-Sp-5R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_N-Sp-5R!H-3R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(193447,'s^-1'), n=0.691119, w0=(435000,'J/mol'), E0=(117697,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.008003090800926675, var=0.5466031047245785, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.5022612652652414"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.5022612652652414""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.5022612652652414
""",
)

entry(
    index = 173,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.51658e+06,'s^-1'), n=0.572814, w0=(435000,'J/mol'), E0=(90415.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0017901988934959567, var=2.927815489525202, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 3.434772223186776"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.434772223186776""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.434772223186776
""",
)

entry(
    index = 174,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Sp-6R!H-4C_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(8.67363e+08,'s^-1'), n=0.437108, w0=(435000,'J/mol'), E0=(116527,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Sp-6R!H-4C_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Sp-6R!H-4C_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Sp-6R!H-4C_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Sp-6R!H-4C_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 175,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.09777e+07,'s^-1'), n=1.05721, w0=(435000,'J/mol'), E0=(89728.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0020103166367771937, var=4.338097876834202, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 4.180533496604463"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.180533496604463""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.180533496604463
""",
)

entry(
    index = 176,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.81983e+06,'s^-1'), n=1.01662, w0=(435000,'J/mol'), E0=(94703.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.028451313715313755, var=0.5164236946833786, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.5121409742171135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.5121409742171135""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.5121409742171135
""",
)

entry(
    index = 177,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H",
    kinetics = ArrheniusBM(A=(3.96742e-10,'s^-1'), n=5.94672, w0=(435000,'J/mol'), E0=(153.043,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.274276038358179, var=2.8196023378001835, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H
    Total Standard Deviation in ln(k): 4.055421073217241"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H
Total Standard Deviation in ln(k): 4.055421073217241""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H
Total Standard Deviation in ln(k): 4.055421073217241
""",
)

entry(
    index = 178,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.19424e-09,'s^-1'), n=5.21276, w0=(435000,'J/mol'), E0=(6539.06,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2653913465325213, var=2.5334135624235667, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 3.8576892183875136"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 3.8576892183875136""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 3.8576892183875136
""",
)

entry(
    index = 179,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_7R!H->O",
    kinetics = ArrheniusBM(A=(1.42736e-08,'s^-1'), n=5.17746, w0=(435000,'J/mol'), E0=(6105.09,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.007180247125480332, var=10.037331972870637, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_7R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_7R!H->O
    Total Standard Deviation in ln(k): 6.369392104364643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_7R!H->O
Total Standard Deviation in ln(k): 6.369392104364643""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_7R!H->O
Total Standard Deviation in ln(k): 6.369392104364643
""",
)

entry(
    index = 180,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_N-7R!H->O",
    kinetics = ArrheniusBM(A=(4.19612e-08,'s^-1'), n=4.96903, w0=(435000,'J/mol'), E0=(4004.65,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.37878839529388325, var=0.9040310782446457, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_N-7R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_N-7R!H->O
    Total Standard Deviation in ln(k): 2.8578427523441015"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_N-7R!H->O
Total Standard Deviation in ln(k): 2.8578427523441015""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_N-7R!H->O
Total Standard Deviation in ln(k): 2.8578427523441015
""",
)

entry(
    index = 181,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(5.70543e+10,'s^-1'), n=0.462073, w0=(435000,'J/mol'), E0=(143923,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.005215631086792439, var=0.023172268843031377, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 0.31827420088099984"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 0.31827420088099984""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 0.31827420088099984
""",
)

entry(
    index = 182,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(2.91097e+10,'s^-1'), n=0.578253, w0=(435000,'J/mol'), E0=(176588,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 183,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_5R!H->C_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.08135e+09,'s^-1'), n=0.863772, w0=(435000,'J/mol'), E0=(132138,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.13316136928054825, var=0.32770335321869787, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_5R!H->C_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_5R!H->C_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.4821945179200973"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_5R!H->C_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.4821945179200973""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_5R!H->C_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.4821945179200973
""",
)

entry(
    index = 184,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_3C-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(127974,'s^-1'), n=2.20069, w0=(411000,'J/mol'), E0=(90045.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_3C-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_3C-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_3C-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-3C-R_Ext-5R!H-R_Ext-1C-R_3C-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 185,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3C_1C-inRing",
    kinetics = ArrheniusBM(A=(1.28069e+11,'s^-1'), n=0.735165, w0=(411000,'J/mol'), E0=(41100,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3C_1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3C_1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3C_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3C_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 186,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3C_N-1C-inRing",
    kinetics = ArrheniusBM(A=(4.604e+12,'s^-1'), n=1.135, w0=(411000,'J/mol'), E0=(467967,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3C_N-1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3C_N-1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3C_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Int-7R!H-3C_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 187,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.4536e+70,'s^-1'), n=-16.7257, w0=(411000,'J/mol'), E0=(386202,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9881800129114333, var=74.97907115941527, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_Sp-7R!H=6R!H',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 19.841956857972573"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 19.841956857972573""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 19.841956857972573
""",
)

entry(
    index = 188,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.29626e+21,'s^-1'), n=-2.15948, w0=(411000,'J/mol'), E0=(227222,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.16911766919861554, var=36.25530649848308, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 12.495905702516916"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 12.495905702516916""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 12.495905702516916
""",
)

entry(
    index = 189,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-1C-inRing_Ext-3C-R",
    kinetics = ArrheniusBM(A=(12019.1,'s^-1'), n=2.46128, w0=(411000,'J/mol'), E0=(160453,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-1C-inRing_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-1C-inRing_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-1C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-1C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 190,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(9.57112e+15,'s^-1'), n=-0.769258, w0=(411000,'J/mol'), E0=(326542,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=7.029323810759526e-15, var=178.93539779568087, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_Sp-6R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 26.816686874299016"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 26.816686874299016""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 26.816686874299016
""",
)

entry(
    index = 191,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.17396e-28,'s^-1'), n=12.1236, w0=(411000,'J/mol'), E0=(-97336.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.76184491619675, var=108.32528282567527, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 32.82960339217223"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 32.82960339217223""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 32.82960339217223
""",
)

entry(
    index = 192,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(9.80562e+08,'s^-1'), n=0.838826, w0=(411000,'J/mol'), E0=(66266,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.028156058672020402, var=1.4602566787289715, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 2.4932873989163267"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.4932873989163267""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.4932873989163267
""",
)

entry(
    index = 193,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-6R!H-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4570.73,'s^-1'), n=2.68412, w0=(411000,'J/mol'), E0=(86416.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013904837512974368, var=4.431102125626661, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-6R!H-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-6R!H-R_Ext-3C-R
    Total Standard Deviation in ln(k): 4.254940841423051"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-6R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 4.254940841423051""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-6R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 4.254940841423051
""",
)

entry(
    index = 194,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.69839e+09,'s^-1'), n=1.13858, w0=(411000,'J/mol'), E0=(122139,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 195,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.67923e+13,'s^-1'), n=-0.103215, w0=(411000,'J/mol'), E0=(211649,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.001354918620300302, var=9.601706638493173, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R
    Total Standard Deviation in ln(k): 6.215400867531148"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R
Total Standard Deviation in ln(k): 6.215400867531148""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R
Total Standard Deviation in ln(k): 6.215400867531148
""",
)

entry(
    index = 196,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(9.15238e+10,'s^-1'), n=0.681486, w0=(411000,'J/mol'), E0=(198530,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.010526094533705076, var=5.115144610455085, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-3C-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 4.560493740638439"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 4.560493740638439""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 4.560493740638439
""",
)

entry(
    index = 197,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3602.64,'s^-1'), n=2.77186, w0=(411000,'J/mol'), E0=(176069,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 198,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.57228e+08,'s^-1'), n=1.47755, w0=(411000,'J/mol'), E0=(214183,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12433088873133252, var=99.82287437203006, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-4R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 20.34197757472118"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 20.34197757472118""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 20.34197757472118
""",
)

entry(
    index = 199,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.02776e+26,'s^-1'), n=-4.01649, w0=(411000,'J/mol'), E0=(234113,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2698390467681817, var=16.59832032279773, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R
    Total Standard Deviation in ln(k): 8.845485994656851"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R
Total Standard Deviation in ln(k): 8.845485994656851""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R
Total Standard Deviation in ln(k): 8.845485994656851
""",
)

entry(
    index = 200,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Int-5R!H-4R!H_Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(0.00329684,'s^-1'), n=4.19487, w0=(411000,'J/mol'), E0=(236926,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.377432715231036e-15, var=0.6373200583295843, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Int-5R!H-4R!H_Sp-5R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Int-5R!H-4R!H_Sp-5R!H-3C
    Total Standard Deviation in ln(k): 1.6004266811849561"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Int-5R!H-4R!H_Sp-5R!H-3C
Total Standard Deviation in ln(k): 1.6004266811849561""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Int-5R!H-4R!H_Sp-5R!H-3C
Total Standard Deviation in ln(k): 1.6004266811849561
""",
)

entry(
    index = 201,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Int-5R!H-4R!H_N-Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(1.40126e+09,'s^-1'), n=0.942538, w0=(411000,'J/mol'), E0=(111673,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-9.665320239794348e-16, var=1.5157062300993762, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Int-5R!H-4R!H_N-Sp-5R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Int-5R!H-4R!H_N-Sp-5R!H-3C
    Total Standard Deviation in ln(k): 2.468109975104088"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Int-5R!H-4R!H_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 2.468109975104088""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Int-5R!H-4R!H_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 2.468109975104088
""",
)

entry(
    index = 202,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Ext-1C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.88794e+07,'s^-1'), n=1.40387, w0=(411000,'J/mol'), E0=(154352,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.55859517919701e-15, var=0.04740494784925479, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 0.43648449989557786"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.43648449989557786""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.43648449989557786
""",
)

entry(
    index = 203,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Ext-1C-R_Int-6R!H-3C",
    kinetics = ArrheniusBM(A=(3.10465e+08,'s^-1'), n=1.12904, w0=(411000,'J/mol'), E0=(160553,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.3598594057041384e-15, var=3.23231579872649, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Ext-1C-R_Int-6R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Ext-1C-R_Int-6R!H-3C
    Total Standard Deviation in ln(k): 3.6042414914097525"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Ext-1C-R_Int-6R!H-3C
Total Standard Deviation in ln(k): 3.6042414914097525""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Ext-1C-R_Int-6R!H-3C
Total Standard Deviation in ln(k): 3.6042414914097525
""",
)

entry(
    index = 204,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_Sp-5R!H-=3C",
    kinetics = ArrheniusBM(A=(8.48474e-16,'s^-1'), n=8.14723, w0=(411000,'J/mol'), E0=(2868.48,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6911024478693569, var=4.994044956579098, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_Sp-5R!H-=3C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_Sp-5R!H-=3C
    Total Standard Deviation in ln(k): 6.216491944290756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_Sp-5R!H-=3C
Total Standard Deviation in ln(k): 6.216491944290756""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_Sp-5R!H-=3C
Total Standard Deviation in ln(k): 6.216491944290756
""",
)

entry(
    index = 205,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C",
    kinetics = ArrheniusBM(A=(3.22308e+10,'s^-1'), n=0.34395, w0=(411000,'J/mol'), E0=(107503,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09919317119830902, var=5.427908245123952, Tref=1000.0, N=41, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C',), comment="""BM rule fitted to 41 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C
    Total Standard Deviation in ln(k): 4.919835130601185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 41 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C
Total Standard Deviation in ln(k): 4.919835130601185""",
    longDesc = 
"""
BM rule fitted to 41 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C
Total Standard Deviation in ln(k): 4.919835130601185
""",
)

entry(
    index = 206,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(2.58602e-39,'s^-1'), n=15.1033, w0=(411000,'J/mol'), E0=(70135.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6604452127175902, var=27.950524211402385, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C',), comment="""BM rule fitted to 14 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C
    Total Standard Deviation in ln(k): 12.25809467532916"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C
Total Standard Deviation in ln(k): 12.25809467532916""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C
Total Standard Deviation in ln(k): 12.25809467532916
""",
)

entry(
    index = 207,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_N-Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(1.18269e-05,'s^-1'), n=4.88266, w0=(411000,'J/mol'), E0=(235631,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.282536843785783e-15, var=0.6373200583298498, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_N-Sp-5R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_N-Sp-5R!H-3C
    Total Standard Deviation in ln(k): 1.6004266811852894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 1.6004266811852894""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 1.6004266811852894
""",
)

entry(
    index = 208,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.22832e+08,'s^-1'), n=1.54357, w0=(411000,'J/mol'), E0=(203739,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013819779037492213, var=6.331042946083522, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R',), comment="""BM rule fitted to 14 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R
    Total Standard Deviation in ln(k): 5.078950025062412"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R
Total Standard Deviation in ln(k): 5.078950025062412""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R
Total Standard Deviation in ln(k): 5.078950025062412
""",
)

entry(
    index = 209,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_3C-inRing",
    kinetics = ArrheniusBM(A=(68.8,'s^-1'), n=3.351, w0=(411000,'J/mol'), E0=(248981,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_3C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 210,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_N-3C-inRing",
    kinetics = ArrheniusBM(A=(1.93195e+07,'s^-1'), n=1.81636, w0=(411000,'J/mol'), E0=(213290,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.010012616455701177, var=2.361751059865273, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_N-3C-inRing',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_N-3C-inRing
    Total Standard Deviation in ln(k): 3.106032120495109"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_N-3C-inRing
Total Standard Deviation in ln(k): 3.106032120495109""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_N-3C-inRing
Total Standard Deviation in ln(k): 3.106032120495109
""",
)

entry(
    index = 211,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(5.41807e-55,'s^-1'), n=19.7622, w0=(411000,'J/mol'), E0=(27446.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8741056623815299, var=6.852222922852382, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C',), comment="""BM rule fitted to 17 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 7.4439904746440275"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C
Total Standard Deviation in ln(k): 7.4439904746440275""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C
Total Standard Deviation in ln(k): 7.4439904746440275
""",
)

entry(
    index = 212,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(4.11757e-51,'s^-1'), n=18.62, w0=(411000,'J/mol'), E0=(-3661.21,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.0764429706497602, var=41.42278151462463, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_N-Sp-4R!H-1C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 18.119775115958948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 18.119775115958948""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 18.119775115958948
""",
)

entry(
    index = 213,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.36708e-49,'s^-1'), n=18.1257, w0=(411000,'J/mol'), E0=(960.095,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9603187865348412, var=25.14377761763613, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R',), comment="""BM rule fitted to 36 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R
    Total Standard Deviation in ln(k): 12.465318939864703"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 12.465318939864703""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 12.465318939864703
""",
)

entry(
    index = 214,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.94832e+10,'s^-1'), n=1.06135, w0=(411000,'J/mol'), E0=(41100,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 215,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.16107e+07,'s^-1'), n=1.51084, w0=(411000,'J/mol'), E0=(132492,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07031731301834021, var=0.6253172834482212, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 1.7619611378036741"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.7619611378036741""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.7619611378036741
""",
)

entry(
    index = 216,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C",
    kinetics = ArrheniusBM(A=(1.03216e-41,'s^-1'), n=15.8181, w0=(411000,'J/mol'), E0=(1420.92,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9915970831343481, var=14.246497831223486, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C',), comment="""BM rule fitted to 13 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C
    Total Standard Deviation in ln(k): 10.058228917282271"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C
Total Standard Deviation in ln(k): 10.058228917282271""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C
Total Standard Deviation in ln(k): 10.058228917282271
""",
)

entry(
    index = 217,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(2.83862e-53,'s^-1'), n=19.1539, w0=(411000,'J/mol'), E0=(-6987.87,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1248737333354304, var=6.546793963987591, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C',), comment="""BM rule fitted to 15 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C
    Total Standard Deviation in ln(k): 7.9557721166106665"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C
Total Standard Deviation in ln(k): 7.9557721166106665""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C
Total Standard Deviation in ln(k): 7.9557721166106665
""",
)

entry(
    index = 218,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(2.52014e+06,'s^-1'), n=2.14922, w0=(411000,'J/mol'), E0=(188540,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=9.489587144525358e-17, var=0.39131910560159616, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 1.2540721275743656"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 1.2540721275743656""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 1.2540721275743656
""",
)

entry(
    index = 219,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(343.168,'s^-1'), n=2.22949, w0=(411000,'J/mol'), E0=(83163.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01506054755439508, var=3.4270086969065363, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 3.749042564372551"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 3.749042564372551""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 3.749042564372551
""",
)

entry(
    index = 220,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.77905e+06,'s^-1'), n=0.956373, w0=(411000,'J/mol'), E0=(70489,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0869405042475439, var=5.059198939430216, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 4.727626550798202"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 4.727626550798202""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 4.727626550798202
""",
)

entry(
    index = 221,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-1C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(7.4029e+06,'s^-1'), n=1.55542, w0=(411000,'J/mol'), E0=(153021,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-7.907989287104467e-16, var=1.8491915360385638, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 2.72613863641576"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 2.72613863641576""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 2.72613863641576
""",
)

entry(
    index = 222,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing",
    kinetics = ArrheniusBM(A=(2.60131,'s^-1'), n=3.89201, w0=(411000,'J/mol'), E0=(174308,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13716601479964888, var=28.962668340871275, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing',), comment="""BM rule fitted to 17 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing
    Total Standard Deviation in ln(k): 11.133516049247637"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing
Total Standard Deviation in ln(k): 11.133516049247637""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing
Total Standard Deviation in ln(k): 11.133516049247637
""",
)

entry(
    index = 223,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing",
    kinetics = ArrheniusBM(A=(26050.2,'s^-1'), n=2.36316, w0=(411000,'J/mol'), E0=(138672,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04941074076598725, var=19.25901819364284, Tref=1000.0, N=51, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing',), comment="""BM rule fitted to 51 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing
    Total Standard Deviation in ln(k): 8.921947107183138"""),
    rank = 11,
    shortDesc = """BM rule fitted to 51 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing
Total Standard Deviation in ln(k): 8.921947107183138""",
    longDesc = 
"""
BM rule fitted to 51 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing
Total Standard Deviation in ln(k): 8.921947107183138
""",
)

entry(
    index = 224,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_3C-inRing",
    kinetics = ArrheniusBM(A=(721.5,'s^-1'), n=2.46, w0=(411000,'J/mol'), E0=(36632.9,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_3C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 225,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing",
    kinetics = ArrheniusBM(A=(391.337,'s^-1'), n=2.37942, w0=(411000,'J/mol'), E0=(80196.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02018788146056969, var=9.133220911344527, Tref=1000.0, N=47, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing',), comment="""BM rule fitted to 47 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing
    Total Standard Deviation in ln(k): 6.109277145418531"""),
    rank = 11,
    shortDesc = """BM rule fitted to 47 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing
Total Standard Deviation in ln(k): 6.109277145418531""",
    longDesc = 
"""
BM rule fitted to 47 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing
Total Standard Deviation in ln(k): 6.109277145418531
""",
)

entry(
    index = 226,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Int-3C-1C",
    kinetics = ArrheniusBM(A=(4.52616e+09,'s^-1'), n=1.1775, w0=(411000,'J/mol'), E0=(161389,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0011019876843434524, var=17.56557112726679, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Int-3C-1C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Int-3C-1C
    Total Standard Deviation in ln(k): 8.404874245907658"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Int-3C-1C
Total Standard Deviation in ln(k): 8.404874245907658""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Int-3C-1C
Total Standard Deviation in ln(k): 8.404874245907658
""",
)

entry(
    index = 227,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.05651e+09,'s^-1'), n=0.855, w0=(411000,'J/mol'), E0=(148942,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0010169852271363175, var=0.42329395449151763, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 1.3068568252334345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.3068568252334345""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.3068568252334345
""",
)

entry(
    index = 228,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.3681e+08,'s^-1'), n=1.19074, w0=(411000,'J/mol'), E0=(152339,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.690395000648751e-15, var=7.242330208232984, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Ext-3C-R
    Total Standard Deviation in ln(k): 5.3950584046062335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 5.3950584046062335""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 5.3950584046062335
""",
)

entry(
    index = 229,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.63017e-57,'s^-1'), n=20.4563, w0=(411000,'J/mol'), E0=(15798.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.06296223118798, var=2.7458467633136903, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R',), comment="""BM rule fitted to 31 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R
    Total Standard Deviation in ln(k): 5.992725028717855"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 5.992725028717855""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 5.992725028717855
""",
)

entry(
    index = 230,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Int-3C-1C",
    kinetics = ArrheniusBM(A=(1.16503e+09,'s^-1'), n=1.09347, w0=(411000,'J/mol'), E0=(153801,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.3933273817247035e-17, var=1.0687721058499329, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Int-3C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Int-3C-1C
    Total Standard Deviation in ln(k): 2.0725238866767532"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Int-3C-1C
Total Standard Deviation in ln(k): 2.0725238866767532""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Int-3C-1C
Total Standard Deviation in ln(k): 2.0725238866767532
""",
)

entry(
    index = 231,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Int-5R!H-3C_Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(7.15013e+08,'s^-1'), n=1.04319, w0=(411000,'J/mol'), E0=(152973,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.012346294545952211, var=1.4775853058817954, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Int-5R!H-3C_Sp-5R!H-3C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Int-5R!H-3C_Sp-5R!H-3C
    Total Standard Deviation in ln(k): 2.4678959451892717"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Int-5R!H-3C_Sp-5R!H-3C
Total Standard Deviation in ln(k): 2.4678959451892717""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Int-5R!H-3C_Sp-5R!H-3C
Total Standard Deviation in ln(k): 2.4678959451892717
""",
)

entry(
    index = 232,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Int-5R!H-3C_N-Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(1.84573e+09,'s^-1'), n=0.979515, w0=(411000,'J/mol'), E0=(201281,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.4267953577452687e-15, var=2.6324616864486563, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Int-5R!H-3C_N-Sp-5R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Int-5R!H-3C_N-Sp-5R!H-3C
    Total Standard Deviation in ln(k): 3.252655131949452"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Int-5R!H-3C_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 3.252655131949452""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Int-5R!H-3C_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 3.252655131949452
""",
)

entry(
    index = 233,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Int-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(6.45294e+09,'s^-1'), n=0.956272, w0=(411000,'J/mol'), E0=(178397,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7573309526898815e-15, var=59.80441251619811, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Int-6R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Int-6R!H-5R!H
    Total Standard Deviation in ln(k): 15.503280460086799"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Int-6R!H-5R!H
Total Standard Deviation in ln(k): 15.503280460086799""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Int-6R!H-5R!H
Total Standard Deviation in ln(k): 15.503280460086799
""",
)

entry(
    index = 234,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.42465e+15,'s^-1'), n=-0.642642, w0=(411000,'J/mol'), E0=(165819,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0698137615439801, var=23.36463248890884, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 9.865694593539121"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R
Total Standard Deviation in ln(k): 9.865694593539121""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R
Total Standard Deviation in ln(k): 9.865694593539121
""",
)

entry(
    index = 235,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_3C-inRing_Ext-6R!H-R_Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(2.5621e+08,'s^-1'), n=1.29514, w0=(411000,'J/mol'), E0=(155221,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00781824116197305, var=1.8966282897672235, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_3C-inRing_Ext-6R!H-R_Sp-7R!H-6R!H',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_3C-inRing_Ext-6R!H-R_Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 2.7805274505389974"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_3C-inRing_Ext-6R!H-R_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 2.7805274505389974""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_3C-inRing_Ext-6R!H-R_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 2.7805274505389974
""",
)

entry(
    index = 236,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_3C-inRing_Ext-6R!H-R_N-Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(4.16964e+08,'s^-1'), n=1.69974, w0=(411000,'J/mol'), E0=(138633,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_3C-inRing_Ext-6R!H-R_N-Sp-7R!H-6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_3C-inRing_Ext-6R!H-R_N-Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_3C-inRing_Ext-6R!H-R_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_3C-inRing_Ext-6R!H-R_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 237,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(3528.82,'s^-1'), n=2.67643, w0=(411000,'J/mol'), E0=(142710,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 238,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(99.8918,'s^-1'), n=3.12429, w0=(411000,'J/mol'), E0=(162664,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4126475029112614, var=21.84390991255983, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 10 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 10.4064270873874"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 10.4064270873874""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 10.4064270873874
""",
)

entry(
    index = 239,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C",
    kinetics = ArrheniusBM(A=(6.71658e-69,'s^-1'), n=23.9969, w0=(411000,'J/mol'), E0=(8907.41,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1906793402144049, var=6.35263829731135, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C
    Total Standard Deviation in ln(k): 5.5319164523277395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C
Total Standard Deviation in ln(k): 5.5319164523277395""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C
Total Standard Deviation in ln(k): 5.5319164523277395
""",
)

entry(
    index = 240,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(4.66488e-20,'s^-1'), n=9.0801, w0=(411000,'J/mol'), E0=(117239,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.8890209409570795e-15, var=0.0030553665687993894, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_N-4R!H->C
    Total Standard Deviation in ln(k): 0.11081247388325362"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_N-4R!H->C
Total Standard Deviation in ln(k): 0.11081247388325362""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_N-4R!H->C
Total Standard Deviation in ln(k): 0.11081247388325362
""",
)

entry(
    index = 241,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_N-5R!H->C_Int-3C-1C",
    kinetics = ArrheniusBM(A=(2.58303e-19,'s^-1'), n=8.89528, w0=(411000,'J/mol'), E0=(116678,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.6845115513377943e-15, var=0.003055366568775093, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_N-5R!H->C_Int-3C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_N-5R!H->C_Int-3C-1C
    Total Standard Deviation in ln(k): 0.11081247388281251"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_N-5R!H->C_Int-3C-1C
Total Standard Deviation in ln(k): 0.11081247388281251""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_N-5R!H->C_Int-3C-1C
Total Standard Deviation in ln(k): 0.11081247388281251
""",
)

entry(
    index = 242,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_3C-inRing",
    kinetics = ArrheniusBM(A=(2.22347e-22,'s^-1'), n=10.5306, w0=(411000,'J/mol'), E0=(63585.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.181334768897018, var=8.587462185886405, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_3C-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_3C-inRing
    Total Standard Deviation in ln(k): 11.355490873248147"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_3C-inRing
Total Standard Deviation in ln(k): 11.355490873248147""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_3C-inRing
Total Standard Deviation in ln(k): 11.355490873248147
""",
)

entry(
    index = 243,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_N-3C-inRing",
    kinetics = ArrheniusBM(A=(5.18059e+09,'s^-1'), n=1.06978, w0=(411000,'J/mol'), E0=(157353,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01419339638653076, var=1.2315485230572414, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_N-3C-inRing',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_N-3C-inRing
    Total Standard Deviation in ln(k): 2.2604196778063095"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_N-3C-inRing
Total Standard Deviation in ln(k): 2.2604196778063095""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_N-3C-inRing
Total Standard Deviation in ln(k): 2.2604196778063095
""",
)

entry(
    index = 244,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H",
    kinetics = ArrheniusBM(A=(2.69419e-66,'s^-1'), n=23.2581, w0=(411000,'J/mol'), E0=(9504.64,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6557188644036495, var=9.979494917520894, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H',), comment="""BM rule fitted to 12 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H
    Total Standard Deviation in ln(k): 7.980560821479008"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H
Total Standard Deviation in ln(k): 7.980560821479008""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H
Total Standard Deviation in ln(k): 7.980560821479008
""",
)

entry(
    index = 245,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_N-Sp-5C-4R!H",
    kinetics = ArrheniusBM(A=(56703.2,'s^-1'), n=2.37205, w0=(411000,'J/mol'), E0=(146043,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008796437834352683, var=0.1371532335660861, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_N-Sp-5C-4R!H',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_N-Sp-5C-4R!H
    Total Standard Deviation in ln(k): 0.7645392996983624"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_N-Sp-5C-4R!H
Total Standard Deviation in ln(k): 0.7645392996983624""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_N-Sp-5C-4R!H
Total Standard Deviation in ln(k): 0.7645392996983624
""",
)

entry(
    index = 246,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_4R!H-inRing_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(169384,'s^-1'), n=2.23256, w0=(411000,'J/mol'), E0=(108593,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_4R!H-inRing_Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_4R!H-inRing_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_4R!H-inRing_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_4R!H-inRing_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 247,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_4R!H-inRing_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(6.64783e+06,'s^-1'), n=1.32428, w0=(411000,'J/mol'), E0=(50944.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_4R!H-inRing_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_4R!H-inRing_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_4R!H-inRing_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_N-Sp-3C-1C_4R!H-inRing_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 248,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C",
    kinetics = ArrheniusBM(A=(1.73399e+09,'s^-1'), n=0.826793, w0=(435000,'J/mol'), E0=(91709.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004089795312932947, var=1.9963927670720945, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C',), comment="""BM rule fitted to 19 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C
    Total Standard Deviation in ln(k): 2.842841511408998"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C
Total Standard Deviation in ln(k): 2.842841511408998""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C
Total Standard Deviation in ln(k): 2.842841511408998
""",
)

entry(
    index = 249,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_N-Sp-6R!H-1C",
    kinetics = ArrheniusBM(A=(274,'s^-1'), n=3.09, w0=(435000,'J/mol'), E0=(85396.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_N-Sp-6R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_N-Sp-6R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_N-Sp-6R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_N-Sp-6R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 250,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.73902e+09,'s^-1'), n=0.713983, w0=(435000,'J/mol'), E0=(100785,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0020429727599893606, var=0.19928188772676808, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.9000668824483696"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.9000668824483696""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.9000668824483696
""",
)

entry(
    index = 251,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C",
    kinetics = ArrheniusBM(A=(3.14788e-05,'s^-1'), n=4.46373, w0=(435000,'J/mol'), E0=(2453.77,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4771892801720955, var=7.120007485590531, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C
    Total Standard Deviation in ln(k): 6.548271240650651"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 6.548271240650651""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 6.548271240650651
""",
)

entry(
    index = 252,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(32012.9,'s^-1'), n=2.17201, w0=(435000,'J/mol'), E0=(48782.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05824000524434272, var=2.4367220769922477, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C',), comment="""BM rule fitted to 17 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 3.2757238188511963"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 3.2757238188511963""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 3.2757238188511963
""",
)

entry(
    index = 253,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_N-Sp-6R!H-1C_4R!H->C",
    kinetics = ArrheniusBM(A=(1.234e+06,'s^-1'), n=1.554, w0=(435000,'J/mol'), E0=(97863.6,'J/mol'), Tmin=(600,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_N-Sp-6R!H-1C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_N-Sp-6R!H-1C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_N-Sp-6R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_N-Sp-6R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 254,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_N-Sp-6R!H-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.7135,'s^-1'), n=3.311, w0=(435000,'J/mol'), E0=(124433,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_N-Sp-6R!H-1C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_N-Sp-6R!H-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_N-Sp-6R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_N-Sp-6R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 255,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.24429e+09,'s^-1'), n=-0.26729, w0=(435000,'J/mol'), E0=(124380,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0006694375883480343, var=0.4409491011586226, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 1.3329062539273913"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.3329062539273913""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.3329062539273913
""",
)

entry(
    index = 256,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.56e+09,'s^-1'), n=0, w0=(435000,'J/mol'), E0=(90400.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 257,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_6R!H->O",
    kinetics = ArrheniusBM(A=(5510.54,'s^-1'), n=1.73997, w0=(435000,'J/mol'), E0=(52117.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.007424362249889667, var=3.633003105012246, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_6R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_6R!H->O
    Total Standard Deviation in ln(k): 3.8397671137233544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_6R!H->O
Total Standard Deviation in ln(k): 3.8397671137233544""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_6R!H->O
Total Standard Deviation in ln(k): 3.8397671137233544
""",
)

entry(
    index = 258,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(51.3281,'s^-1'), n=2.36038, w0=(435000,'J/mol'), E0=(36770.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.30560139929271085, var=2.398019621922024, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O
    Total Standard Deviation in ln(k): 3.872283319628955"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O
Total Standard Deviation in ln(k): 3.872283319628955""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O
Total Standard Deviation in ln(k): 3.872283319628955
""",
)

entry(
    index = 259,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.10248e+06,'s^-1'), n=1.28767, w0=(435000,'J/mol'), E0=(37994.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.19194503318271833, var=0.7301438167238283, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 2.1952890686324706"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.1952890686324706""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.1952890686324706
""",
)

entry(
    index = 260,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(549,'s^-1'), n=2.21, w0=(435000,'J/mol'), E0=(39169.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 261,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(1.62e+06,'s^-1'), n=1.22, w0=(435000,'J/mol'), E0=(44760.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_N-6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 262,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.31e+09,'s^-1'), n=1.04, w0=(435000,'J/mol'), E0=(142062,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 263,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.0842e+08,'s^-1'), n=0.437108, w0=(435000,'J/mol'), E0=(95393.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Int-6R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 264,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(171026,'s^-1'), n=0.72513, w0=(435000,'J/mol'), E0=(120941,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0004903675179796251, var=0.07120806802292765, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 0.5361924249152471"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.5361924249152471""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 0.5361924249152471
""",
)

entry(
    index = 265,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.35309e+07,'s^-1'), n=0.437108, w0=(435000,'J/mol'), E0=(86700.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 266,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(216815,'s^-1'), n=1.72227, w0=(435000,'J/mol'), E0=(84587.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.005837283917104243, var=4.486832425502775, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 4.261125337342369"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C
Total Standard Deviation in ln(k): 4.261125337342369""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C
Total Standard Deviation in ln(k): 4.261125337342369
""",
)

entry(
    index = 267,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(8.34091e+10,'s^-1'), n=-0.0685761, w0=(435000,'J/mol'), E0=(99361,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.014255303752605506, var=6.460596688148609, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_N-6R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 5.131393594848193"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 5.131393594848193""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 5.131393594848193
""",
)

entry(
    index = 268,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-5R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(2.24722e+07,'s^-1'), n=0.746413, w0=(435000,'J/mol'), E0=(96920.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.6373631156125286e-05, var=0.0426232168393348, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-5R!H-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-5R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 0.4140270369733915"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 0.4140270369733915""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 0.4140270369733915
""",
)

entry(
    index = 269,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-5R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(4.53671e+14,'s^-1'), n=-1.07459, w0=(435000,'J/mol'), E0=(99737.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-5R!H-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-5R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 270,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(22.2059,'s^-1'), n=2.82818, w0=(435000,'J/mol'), E0=(40279.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10115238616451377, var=5.301382529514583, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 4.870000379092137"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.870000379092137""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.870000379092137
""",
)

entry(
    index = 271,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(4.09598e+07,'s^-1'), n=0.797425, w0=(435000,'J/mol'), E0=(59737.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.100003639688035e-05, var=1.8266917802100315, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 2.7095305788303143"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.7095305788303143""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.7095305788303143
""",
)

entry(
    index = 272,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(7.99029e+09,'s^-1'), n=0.110041, w0=(435000,'J/mol'), E0=(59324.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006608144100340599, var=0.974892103708406, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.9960111246954912"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.9960111246954912""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.9960111246954912
""",
)

entry(
    index = 273,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(195814,'s^-1'), n=1.30023, w0=(435000,'J/mol'), E0=(56688.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 274,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(100546,'s^-1'), n=0.97162, w0=(435000,'J/mol'), E0=(49380.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.2055290335452586e-14, var=1.159810186916584, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 2.1589890957835087"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.1589890957835087""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 2.1589890957835087
""",
)

entry(
    index = 275,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.43509e-08,'s^-1'), n=4.73237, w0=(435000,'J/mol'), E0=(6493.67,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11177503525780397, var=4.7438623689633195, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 4.647236884573407"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.647236884573407""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.647236884573407
""",
)

entry(
    index = 276,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_7R!H->O_Ext-6R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.91926e+06,'s^-1'), n=0.880434, w0=(435000,'J/mol'), E0=(39445.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_7R!H->O_Ext-6R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_7R!H->O_Ext-6R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_7R!H->O_Ext-6R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_7R!H->O_Ext-6R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 277,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_N-7R!H->O_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.66737e-07,'s^-1'), n=4.75865, w0=(435000,'J/mol'), E0=(6023.63,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.011120979836584215, var=3.4380002900502005, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_N-7R!H->O_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_N-7R!H->O_Ext-3R!H-R
    Total Standard Deviation in ln(k): 3.7450909377869865"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_N-7R!H->O_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.7450909377869865""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_N-7R!H->O_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.7450909377869865
""",
)

entry(
    index = 278,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.13261e+11,'s^-1'), n=0.244037, w0=(435000,'J/mol'), E0=(146034,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.006065465625166089, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.1561309715939808"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.1561309715939808""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.1561309715939808
""",
)

entry(
    index = 279,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_5R!H->C_Ext-3R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.23428e+09,'s^-1'), n=0.855988, w0=(435000,'J/mol'), E0=(136566,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_5R!H->C_Ext-3R!H-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_5R!H->C_Ext-3R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_5R!H->C_Ext-3R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_5R!H->C_Ext-3R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 280,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_5R!H->C_Ext-3R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.88498e+10,'s^-1'), n=0.531138, w0=(435000,'J/mol'), E0=(129111,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_5R!H->C_Ext-3R!H-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_5R!H->C_Ext-3R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_5R!H->C_Ext-3R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_5R!H->C_Ext-3R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 281,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_Sp-7R!H=6R!H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.19262e+06,'s^-1'), n=1.85331, w0=(411000,'J/mol'), E0=(313583,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.514661905379763e-15, var=178.93539779568823, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_Sp-7R!H=6R!H_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_Sp-7R!H=6R!H_Ext-1C-R
    Total Standard Deviation in ln(k): 26.81668687429956"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_Sp-7R!H=6R!H_Ext-1C-R
Total Standard Deviation in ln(k): 26.81668687429956""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_Sp-7R!H=6R!H_Ext-1C-R
Total Standard Deviation in ln(k): 26.81668687429956
""",
)

entry(
    index = 282,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_Sp-7R!H=6R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.72654e+11,'s^-1'), n=0.708549, w0=(411000,'J/mol'), E0=(41100,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_Sp-7R!H=6R!H_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_Sp-7R!H=6R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_Sp-7R!H=6R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_Sp-7R!H=6R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 283,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_Sp-7R!H=6R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.43408e-65,'s^-1'), n=23.3003, w0=(411000,'J/mol'), E0=(41100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=19.991320955161427, var=13.422233267770059, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_Sp-7R!H=6R!H_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_Sp-7R!H=6R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 57.57407047474596"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 57.57407047474596""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 57.57407047474596
""",
)

entry(
    index = 284,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_7R!H-inRing",
    kinetics = ArrheniusBM(A=(2.32515e+07,'s^-1'), n=1.70321, w0=(411000,'J/mol'), E0=(229888,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.014597942516685414, var=0.22330122559168278, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_7R!H-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_7R!H-inRing
    Total Standard Deviation in ln(k): 0.9840109785883276"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_7R!H-inRing
Total Standard Deviation in ln(k): 0.9840109785883276""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_7R!H-inRing
Total Standard Deviation in ln(k): 0.9840109785883276
""",
)

entry(
    index = 285,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_N-7R!H-inRing",
    kinetics = ArrheniusBM(A=(9.29973e+10,'s^-1'), n=0.99796, w0=(411000,'J/mol'), E0=(180036,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04956759818558802, var=15.581763694207444, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_N-7R!H-inRing',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_N-7R!H-inRing
    Total Standard Deviation in ln(k): 8.037981383605812"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_N-7R!H-inRing
Total Standard Deviation in ln(k): 8.037981383605812""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_N-7R!H-inRing
Total Standard Deviation in ln(k): 8.037981383605812
""",
)

entry(
    index = 286,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_Int-4R!H-3C",
    kinetics = ArrheniusBM(A=(6.75073e+06,'s^-1'), n=1.96509, w0=(411000,'J/mol'), E0=(173341,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_Int-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_Int-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_Int-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_Int-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 287,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_Int-3C-1C",
    kinetics = ArrheniusBM(A=(4.18415e+06,'s^-1'), n=1.93358, w0=(411000,'J/mol'), E0=(139159,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.8955863034014815, var=482.4080649455928, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_Int-3C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_Int-3C-1C
    Total Standard Deviation in ln(k): 56.33204806072147"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_Int-3C-1C
Total Standard Deviation in ln(k): 56.33204806072147""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_Int-3C-1C
Total Standard Deviation in ln(k): 56.33204806072147
""",
)

entry(
    index = 288,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.658e+09,'s^-1'), n=0.699, w0=(411000,'J/mol'), E0=(59612,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 289,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-5R!H-R_Int-6R!H-1C",
    kinetics = ArrheniusBM(A=(3.39093e+07,'s^-1'), n=1.46345, w0=(411000,'J/mol'), E0=(81970.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-5R!H-R_Int-6R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-5R!H-R_Int-6R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-5R!H-R_Int-6R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-5R!H-R_Int-6R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 290,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-6R!H-R_Ext-3C-R_Int-5R!H-1C",
    kinetics = ArrheniusBM(A=(78891.1,'s^-1'), n=2.3929, w0=(411000,'J/mol'), E0=(99392.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-6R!H-R_Ext-3C-R_Int-5R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-6R!H-R_Ext-3C-R_Int-5R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-6R!H-R_Ext-3C-R_Int-5R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_3C-inRing_Ext-3C-R_N-Sp-5R!H-3C_Ext-5R!H-R_Ext-6R!H-R_Ext-3C-R_Int-5R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 291,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.04073e+08,'s^-1'), n=1.3511, w0=(411000,'J/mol'), E0=(219994,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.7843446624655664, var=29.910434381504363, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 12.934698132410837"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 12.934698132410837""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 12.934698132410837
""",
)

entry(
    index = 292,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.90325e+12,'s^-1'), n=0.273498, w0=(411000,'J/mol'), E0=(199859,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.010752214530844321, var=5.117207707567967, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 4.561976150183224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 4.561976150183224""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 4.561976150183224
""",
)

entry(
    index = 293,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(8.94266e+11,'s^-1'), n=0.519524, w0=(411000,'J/mol'), E0=(199958,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.786654763449407e-15, var=35.965867722369566, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 12.02270693095096"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 12.02270693095096""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 12.02270693095096
""",
)

entry(
    index = 294,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-3C-R_5R!H-inRing",
    kinetics = ArrheniusBM(A=(420000,'s^-1'), n=2.094, w0=(411000,'J/mol'), E0=(179990,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-3C-R_5R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-3C-R_5R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-3C-R_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-3C-R_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 295,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-3C-R_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(3.5087e+11,'s^-1'), n=0.460473, w0=(411000,'J/mol'), E0=(203907,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.602528453014257e-15, var=2.632461686448911, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-3C-R_N-5R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-3C-R_N-5R!H-inRing
    Total Standard Deviation in ln(k): 3.2526551319496098"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-3C-R_N-5R!H-inRing
Total Standard Deviation in ln(k): 3.2526551319496098""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-3C-R_N-5R!H-inRing
Total Standard Deviation in ln(k): 3.2526551319496098
""",
)

entry(
    index = 296,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-4R!H-R_5R!H-inRing",
    kinetics = ArrheniusBM(A=(6.32736e+11,'s^-1'), n=0.52899, w0=(411000,'J/mol'), E0=(232064,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0395184756449857, var=5.03368028861736, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-4R!H-R_5R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-4R!H-R_5R!H-inRing
    Total Standard Deviation in ln(k): 4.597089165932851"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-4R!H-R_5R!H-inRing
Total Standard Deviation in ln(k): 4.597089165932851""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-4R!H-R_5R!H-inRing
Total Standard Deviation in ln(k): 4.597089165932851
""",
)

entry(
    index = 297,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-4R!H-R_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(1.01577e+08,'s^-1'), n=1.63477, w0=(411000,'J/mol'), E0=(209048,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.048890514997486e-15, var=298.7983478449594, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-4R!H-R_N-5R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-4R!H-R_N-5R!H-inRing
    Total Standard Deviation in ln(k): 34.6534186471431"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-4R!H-R_N-5R!H-inRing
Total Standard Deviation in ln(k): 34.6534186471431""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-4R!H-R_N-5R!H-inRing
Total Standard Deviation in ln(k): 34.6534186471431
""",
)

entry(
    index = 298,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(4.57049e+14,'s^-1'), n=-0.506823, w0=(411000,'J/mol'), E0=(197080,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.16524201304746614, var=9.021391732077245, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_Sp-5R!H-3C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_Sp-5R!H-3C
    Total Standard Deviation in ln(k): 6.436529386678488"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_Sp-5R!H-3C
Total Standard Deviation in ln(k): 6.436529386678488""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_Sp-5R!H-3C
Total Standard Deviation in ln(k): 6.436529386678488
""",
)

entry(
    index = 299,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_N-Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(1.806e+09,'s^-1'), n=1.172, w0=(411000,'J/mol'), E0=(242271,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_N-Sp-5R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_N-Sp-5R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 300,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Int-5R!H-4R!H_N-Sp-5R!H-3C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.02078e+09,'s^-1'), n=0.95143, w0=(411000,'J/mol'), E0=(111614,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Int-5R!H-4R!H_N-Sp-5R!H-3C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Int-5R!H-4R!H_N-Sp-5R!H-3C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Int-5R!H-4R!H_N-Sp-5R!H-3C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Ext-3C-R_Int-5R!H-4R!H_N-Sp-5R!H-3C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 301,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_Sp-5R!H-=3C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.76188e-12,'s^-1'), n=7.0527, w0=(411000,'J/mol'), E0=(28820.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08213083017003764, var=3.0473446538828086, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_Sp-5R!H-=3C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_Sp-5R!H-=3C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.705953787910698"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_Sp-5R!H-=3C_Ext-1C-R
Total Standard Deviation in ln(k): 3.705953787910698""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_Sp-5R!H-=3C_Ext-1C-R
Total Standard Deviation in ln(k): 3.705953787910698
""",
)

entry(
    index = 302,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.07051e+11,'s^-1'), n=0.11345, w0=(411000,'J/mol'), E0=(111549,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12081868008693555, var=6.507923994543385, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R',), comment="""BM rule fitted to 27 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R
    Total Standard Deviation in ln(k): 5.417770618328708"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R
Total Standard Deviation in ln(k): 5.417770618328708""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R
Total Standard Deviation in ln(k): 5.417770618328708
""",
)

entry(
    index = 303,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(9.37184e+06,'s^-1'), n=1.43598, w0=(411000,'J/mol'), E0=(111176,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 304,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.36207e+07,'s^-1'), n=1.2663, w0=(411000,'J/mol'), E0=(92958.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03702794547819634, var=6.045852238067892, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 5.022340752589715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R
Total Standard Deviation in ln(k): 5.022340752589715""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R
Total Standard Deviation in ln(k): 5.022340752589715
""",
)

entry(
    index = 305,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(10800,'s^-1'), n=2.04, w0=(411000,'J/mol'), E0=(105994,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 306,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.9e+10,'s^-1'), n=0.87, w0=(411000,'J/mol'), E0=(41100,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 307,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_1C-inRing",
    kinetics = ArrheniusBM(A=(2.62799e+09,'s^-1'), n=1.7149, w0=(411000,'J/mol'), E0=(41100,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 308,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing",
    kinetics = ArrheniusBM(A=(6.9569e+11,'s^-1'), n=0.0572376, w0=(411000,'J/mol'), E0=(164756,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.009825825314485018, var=27.653328754391445, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing',), comment="""BM rule fitted to 12 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing
    Total Standard Deviation in ln(k): 10.56687457152074"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing
Total Standard Deviation in ln(k): 10.56687457152074""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing
Total Standard Deviation in ln(k): 10.56687457152074
""",
)

entry(
    index = 309,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_1C-inRing",
    kinetics = ArrheniusBM(A=(875.817,'s^-1'), n=3.31778, w0=(411000,'J/mol'), E0=(249335,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 310,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing",
    kinetics = ArrheniusBM(A=(2.10332e+08,'s^-1'), n=1.45533, w0=(411000,'J/mol'), E0=(199915,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.017683731196587723, var=4.212949108200346, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing',), comment="""BM rule fitted to 13 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing
    Total Standard Deviation in ln(k): 4.159244415734544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing
Total Standard Deviation in ln(k): 4.159244415734544""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing
Total Standard Deviation in ln(k): 4.159244415734544
""",
)

entry(
    index = 311,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_N-3C-inRing_Ext-3C-R",
    kinetics = ArrheniusBM(A=(7.36091e+06,'s^-1'), n=1.92305, w0=(411000,'J/mol'), E0=(208105,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.025213978439405343, var=3.526143596673675, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_N-3C-inRing_Ext-3C-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_N-3C-inRing_Ext-3C-R
    Total Standard Deviation in ln(k): 3.8278489748483184"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 3.8278489748483184""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 3.8278489748483184
""",
)

entry(
    index = 312,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.55667e-52,'s^-1'), n=18.9464, w0=(411000,'J/mol'), E0=(28918,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6340134285826801, var=6.190045831817436, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 6.5807398865976925"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 6.5807398865976925""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 6.5807398865976925
""",
)

entry(
    index = 313,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(9.32291e-54,'s^-1'), n=19.4486, w0=(411000,'J/mol'), E0=(-600.132,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.5507332151459265, var=32.48343149829907, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 15.322149396681601"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 15.322149396681601""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 15.322149396681601
""",
)

entry(
    index = 314,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(1.32458e-62,'s^-1'), n=22.1531, w0=(411000,'J/mol'), E0=(21885.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4291539058615245, var=38.652692035380625, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 13.541972576416779"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 13.541972576416779""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 13.541972576416779
""",
)

entry(
    index = 315,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_N-Sp-4R!H-1C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.04374e-39,'s^-1'), n=14.9813, w0=(411000,'J/mol'), E0=(-17128.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3581248204562306, var=126.17473897971041, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_N-Sp-4R!H-1C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_N-Sp-4R!H-1C_Ext-3C-R
    Total Standard Deviation in ln(k): 23.418504974089313"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_N-Sp-4R!H-1C_Ext-3C-R
Total Standard Deviation in ln(k): 23.418504974089313""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_N-Sp-4R!H-1C_Ext-3C-R
Total Standard Deviation in ln(k): 23.418504974089313
""",
)

entry(
    index = 316,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(4.21582e-59,'s^-1'), n=20.9228, w0=(411000,'J/mol'), E0=(-18473.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1808435655799019, var=29.15978123452567, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R',), comment="""BM rule fitted to 26 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 13.79247244192357"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 13.79247244192357""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 13.79247244192357
""",
)

entry(
    index = 317,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.57811e-36,'s^-1'), n=14.2472, w0=(411000,'J/mol'), E0=(32507.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9085309355333664, var=104.53105457977136, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 22.77923861167643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 22.77923861167643""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 22.77923861167643
""",
)

entry(
    index = 318,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_6R!H-inRing",
    kinetics = ArrheniusBM(A=(3.239e-08,'s^-1'), n=6.224, w0=(411000,'J/mol'), E0=(128219,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_6R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_6R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_6R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_6R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 319,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_N-6R!H-inRing",
    kinetics = ArrheniusBM(A=(2.18962e-42,'s^-1'), n=15.9377, w0=(411000,'J/mol'), E0=(9475.46,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.627618578106151, var=11.688908483902742, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_N-6R!H-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_N-6R!H-inRing
    Total Standard Deviation in ln(k): 10.94349183995111"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_N-6R!H-inRing
Total Standard Deviation in ln(k): 10.94349183995111""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_N-6R!H-inRing
Total Standard Deviation in ln(k): 10.94349183995111
""",
)

entry(
    index = 320,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(4.5106e+08,'s^-1'), n=1.31916, w0=(411000,'J/mol'), E0=(142162,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 321,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_1C-inRing",
    kinetics = ArrheniusBM(A=(1.21942e+06,'s^-1'), n=1.83, w0=(411000,'J/mol'), E0=(128236,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4342055346384141, var=1.558861193133268, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_1C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_1C-inRing
    Total Standard Deviation in ln(k): 3.5939678884016217"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_1C-inRing
Total Standard Deviation in ln(k): 3.5939678884016217""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_1C-inRing
Total Standard Deviation in ln(k): 3.5939678884016217
""",
)

entry(
    index = 322,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_N-1C-inRing",
    kinetics = ArrheniusBM(A=(4.52e+08,'s^-1'), n=1.11, w0=(411000,'J/mol'), E0=(139668,'J/mol'), Tmin=(600,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_N-1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_N-1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 323,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing",
    kinetics = ArrheniusBM(A=(2.20909e-51,'s^-1'), n=18.7777, w0=(411000,'J/mol'), E0=(-12507.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.306583788314028, var=15.88714800028161, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing',), comment="""BM rule fitted to 9 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing
    Total Standard Deviation in ln(k): 13.786047125578591"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing
Total Standard Deviation in ln(k): 13.786047125578591""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing
Total Standard Deviation in ln(k): 13.786047125578591
""",
)

entry(
    index = 324,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_N-1C-inRing",
    kinetics = ArrheniusBM(A=(1.32824e+15,'s^-1'), n=-1.12142, w0=(411000,'J/mol'), E0=(115493,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2773706537692505, var=6.584938480479951, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_N-1C-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_N-1C-inRing
    Total Standard Deviation in ln(k): 5.8412889307738505"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_N-1C-inRing
Total Standard Deviation in ln(k): 5.8412889307738505""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_N-1C-inRing
Total Standard Deviation in ln(k): 5.8412889307738505
""",
)

entry(
    index = 325,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(18926.7,'s^-1'), n=2.14067, w0=(411000,'J/mol'), E0=(155806,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.042293669451274794, var=1.7264826442619996, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.740400919483408"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R
Total Standard Deviation in ln(k): 2.740400919483408""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R
Total Standard Deviation in ln(k): 2.740400919483408
""",
)

entry(
    index = 326,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.09465e-53,'s^-1'), n=19.3499, w0=(411000,'J/mol'), E0=(-3984.24,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.5791015332331935, var=9.729536015429858, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R
    Total Standard Deviation in ln(k): 10.220802377926693"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R
Total Standard Deviation in ln(k): 10.220802377926693""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R
Total Standard Deviation in ln(k): 10.220802377926693
""",
)

entry(
    index = 327,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Int-7R!H-4R!H",
    kinetics = ArrheniusBM(A=(69064.5,'s^-1'), n=1.88101, w0=(411000,'J/mol'), E0=(116215,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Int-7R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Int-7R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Int-7R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Int-7R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 328,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3C-R",
    kinetics = ArrheniusBM(A=(98.2877,'s^-1'), n=2.17851, w0=(411000,'J/mol'), E0=(71449.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7573309526898815e-15, var=25.78233841156295, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3C-R
    Total Standard Deviation in ln(k): 10.17930533887744"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3C-R
Total Standard Deviation in ln(k): 10.17930533887744""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3C-R
Total Standard Deviation in ln(k): 10.17930533887744
""",
)

entry(
    index = 329,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1826.68,'s^-1'), n=2.00376, w0=(411000,'J/mol'), E0=(82076.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.182896165358259e-05, var=6.008614819005408, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1C-R
    Total Standard Deviation in ln(k): 4.914182028564233"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1C-R
Total Standard Deviation in ln(k): 4.914182028564233""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1C-R
Total Standard Deviation in ln(k): 4.914182028564233
""",
)

entry(
    index = 330,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1199.16,'s^-1'), n=2.02105, w0=(411000,'J/mol'), E0=(56792.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.14802029964777058, var=7.0678697389567215, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1C-R
    Total Standard Deviation in ln(k): 5.701591816917807"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1C-R
Total Standard Deviation in ln(k): 5.701591816917807""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1C-R
Total Standard Deviation in ln(k): 5.701591816917807
""",
)

entry(
    index = 331,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(104,'s^-1'), n=2.1, w0=(411000,'J/mol'), E0=(67426.9,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 332,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(2.25777e-57,'s^-1'), n=20.7154, w0=(411000,'J/mol'), E0=(10643.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1051052497558502, var=19.953738426901058, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C',), comment="""BM rule fitted to 13 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C
    Total Standard Deviation in ln(k): 11.73171928008063"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C
Total Standard Deviation in ln(k): 11.73171928008063""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C
Total Standard Deviation in ln(k): 11.73171928008063
""",
)

entry(
    index = 333,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(6.17364e+09,'s^-1'), n=1.18155, w0=(411000,'J/mol'), E0=(236276,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0016113701993376941, var=0.5132728471492656, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 1.440302282689433"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 1.440302282689433""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 1.440302282689433
""",
)

entry(
    index = 334,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1040.17,'s^-1'), n=2.79966, w0=(411000,'J/mol'), E0=(141584,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07407798987715528, var=15.399759999710335, Tref=1000.0, N=48, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C',), comment="""BM rule fitted to 48 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 8.05321283356965"""),
    rank = 11,
    shortDesc = """BM rule fitted to 48 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C
Total Standard Deviation in ln(k): 8.05321283356965""",
    longDesc = 
"""
BM rule fitted to 48 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C
Total Standard Deviation in ln(k): 8.05321283356965
""",
)

entry(
    index = 335,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(3.47666e-05,'s^-1'), n=4.60587, w0=(411000,'J/mol'), E0=(21197.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6458162484521329, var=2.5267578073656294, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_N-Sp-4R!H-1C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 4.809336406443504"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 4.809336406443504""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 4.809336406443504
""",
)

entry(
    index = 336,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.19114e+07,'s^-1'), n=0.825772, w0=(411000,'J/mol'), E0=(64126.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06217134588593297, var=4.497382805125185, Tref=1000.0, N=40, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R',), comment="""BM rule fitted to 40 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R
    Total Standard Deviation in ln(k): 4.407657856568094"""),
    rank = 11,
    shortDesc = """BM rule fitted to 40 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.407657856568094""",
    longDesc = 
"""
BM rule fitted to 40 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.407657856568094
""",
)

entry(
    index = 337,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C",
    kinetics = ArrheniusBM(A=(706297,'s^-1'), n=2.00342, w0=(411000,'J/mol'), E0=(148524,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.000966495745609887, var=0.2833861409529628, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C
    Total Standard Deviation in ln(k): 1.0696295520155852"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C
Total Standard Deviation in ln(k): 1.0696295520155852""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C
Total Standard Deviation in ln(k): 1.0696295520155852
""",
)

entry(
    index = 338,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.2e-16,'s^-1'), n=7.98, w0=(411000,'J/mol'), E0=(110572,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 339,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Int-3C-1C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.04555e+09,'s^-1'), n=1.46, w0=(411000,'J/mol'), E0=(161493,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.514661905379763e-15, var=80.48558491555974, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Int-3C-1C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Int-3C-1C_Ext-3C-R
    Total Standard Deviation in ln(k): 17.98523188955043"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Int-3C-1C_Ext-3C-R
Total Standard Deviation in ln(k): 17.98523188955043""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Int-3C-1C_Ext-3C-R
Total Standard Deviation in ln(k): 17.98523188955043
""",
)

entry(
    index = 340,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Ext-1C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.08655e+09,'s^-1'), n=0.75, w0=(411000,'J/mol'), E0=(149570,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.6694644050553874e-15, var=2.316488358032995, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 3.0512096579310324"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.0512096579310324""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_3C-inRing_Ext-3C-R_Ext-6R!H-R_Ext-7R!H-R_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.0512096579310324
""",
)

entry(
    index = 341,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(3.38897e+11,'s^-1'), n=0.320153, w0=(411000,'J/mol'), E0=(153770,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00886095701538189, var=2.7569053964794508, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-6R!H-R',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 3.3509120914519723"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.3509120914519723""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.3509120914519723
""",
)

entry(
    index = 342,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Sp-6R!H=3C",
    kinetics = ArrheniusBM(A=(4.28238e-59,'s^-1'), n=20.9359, w0=(411000,'J/mol'), E0=(2615.85,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1035140128347498, var=3.4445245071834267, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Sp-6R!H=3C',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Sp-6R!H=3C
    Total Standard Deviation in ln(k): 6.4933223546903385"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Sp-6R!H=3C
Total Standard Deviation in ln(k): 6.4933223546903385""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Sp-6R!H=3C
Total Standard Deviation in ln(k): 6.4933223546903385
""",
)

entry(
    index = 343,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C",
    kinetics = ArrheniusBM(A=(3.86363e-62,'s^-1'), n=21.816, w0=(411000,'J/mol'), E0=(8869.23,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.536996122552561, var=6.44458552862221, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C',), comment="""BM rule fitted to 16 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C
    Total Standard Deviation in ln(k): 6.438494691478881"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C
Total Standard Deviation in ln(k): 6.438494691478881""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C
Total Standard Deviation in ln(k): 6.438494691478881
""",
)

entry(
    index = 344,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_Sp-7R!H-5R!H",
    kinetics = ArrheniusBM(A=(2.95072e+09,'s^-1'), n=1.01879, w0=(411000,'J/mol'), E0=(163229,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.009670969358962802, var=0.6931422212179202, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_Sp-7R!H-5R!H',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_Sp-7R!H-5R!H
    Total Standard Deviation in ln(k): 1.6933443799309953"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_Sp-7R!H-5R!H
Total Standard Deviation in ln(k): 1.6933443799309953""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_Sp-7R!H-5R!H
Total Standard Deviation in ln(k): 1.6933443799309953
""",
)

entry(
    index = 345,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_N-Sp-7R!H-5R!H",
    kinetics = ArrheniusBM(A=(2.74742e+12,'s^-1'), n=0.39923, w0=(411000,'J/mol'), E0=(140504,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.108797143227858e-15, var=168.46068539082947, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_N-Sp-7R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_N-Sp-7R!H-5R!H
    Total Standard Deviation in ln(k): 26.01993881902945"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_N-Sp-7R!H-5R!H
Total Standard Deviation in ln(k): 26.01993881902945""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_N-Sp-7R!H-5R!H
Total Standard Deviation in ln(k): 26.01993881902945
""",
)

entry(
    index = 346,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_3C-inRing_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.61006e+08,'s^-1'), n=1.29264, w0=(411000,'J/mol'), E0=(155117,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.690395000648751e-15, var=7.408525637180125, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_3C-inRing_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_3C-inRing_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 5.456609608908824"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_3C-inRing_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 5.456609608908824""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_3C-inRing_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 5.456609608908824
""",
)

entry(
    index = 347,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_5R!H-inRing",
    kinetics = ArrheniusBM(A=(0.0075412,'s^-1'), n=4.37441, w0=(411000,'J/mol'), E0=(170816,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3926778182630178, var=15.598952574552035, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_5R!H-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_5R!H-inRing
    Total Standard Deviation in ln(k): 8.904430979973789"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_5R!H-inRing
Total Standard Deviation in ln(k): 8.904430979973789""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_5R!H-inRing
Total Standard Deviation in ln(k): 8.904430979973789
""",
)

entry(
    index = 348,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(4.19465e-59,'s^-1'), n=20.916, w0=(411000,'J/mol'), E0=(8149.94,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.41262461527702676, var=31.23520010963428, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-5R!H-inRing',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-5R!H-inRing
    Total Standard Deviation in ln(k): 12.240900972171396"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-5R!H-inRing
Total Standard Deviation in ln(k): 12.240900972171396""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-5R!H-inRing
Total Standard Deviation in ln(k): 12.240900972171396
""",
)

entry(
    index = 349,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-3C-1C",
    kinetics = ArrheniusBM(A=(3.64927e+10,'s^-1'), n=0.785, w0=(411000,'J/mol'), E0=(172789,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0011798131909388663, var=0.009237312667628667, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-3C-1C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-3C-1C
    Total Standard Deviation in ln(k): 0.19564132623833957"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-3C-1C
Total Standard Deviation in ln(k): 0.19564132623833957""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-3C-1C
Total Standard Deviation in ln(k): 0.19564132623833957
""",
)

entry(
    index = 350,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-4C-3C_Sp-4C-3C",
    kinetics = ArrheniusBM(A=(1.03223e+09,'s^-1'), n=1.08556, w0=(411000,'J/mol'), E0=(155199,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01453158003255348, var=1.477585361723857, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-4C-3C_Sp-4C-3C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-4C-3C_Sp-4C-3C
    Total Standard Deviation in ln(k): 2.4733866582891797"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-4C-3C_Sp-4C-3C
Total Standard Deviation in ln(k): 2.4733866582891797""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-4C-3C_Sp-4C-3C
Total Standard Deviation in ln(k): 2.4733866582891797
""",
)

entry(
    index = 351,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-4C-3C_N-Sp-4C-3C",
    kinetics = ArrheniusBM(A=(1.73339e+09,'s^-1'), n=1.15206, w0=(411000,'J/mol'), E0=(205359,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.514661905379763e-15, var=0.6799256397610199, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-4C-3C_N-Sp-4C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-4C-3C_N-Sp-4C-3C
    Total Standard Deviation in ln(k): 1.6530565040960854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-4C-3C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 1.6530565040960854""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-4C-3C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 1.6530565040960854
""",
)

entry(
    index = 352,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_3C-inRing_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(7.423e+08,'s^-1'), n=1.522, w0=(411000,'J/mol'), E0=(41100,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_3C-inRing_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_3C-inRing_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_3C-inRing_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_3C-inRing_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 353,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_3C-inRing_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(8.964e+07,'s^-1'), n=1.633, w0=(411000,'J/mol'), E0=(139333,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_3C-inRing_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_3C-inRing_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_3C-inRing_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_3C-inRing_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 354,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_N-3C-inRing_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.61982e+11,'s^-1'), n=0.625535, w0=(411000,'J/mol'), E0=(167204,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.5302300558753372, var=27.86480318540388, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_N-3C-inRing_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_N-3C-inRing_Ext-3C-R
    Total Standard Deviation in ln(k): 19.4523444062821"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 19.4523444062821""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 19.4523444062821
""",
)

entry(
    index = 355,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_Int-5C-3C",
    kinetics = ArrheniusBM(A=(8.29281e+08,'s^-1'), n=1.30976, w0=(411000,'J/mol'), E0=(180720,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.1631957148417866e-15, var=69.73498940962418, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_Int-5C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_Int-5C-3C
    Total Standard Deviation in ln(k): 16.741037108001866"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_Int-5C-3C
Total Standard Deviation in ln(k): 16.741037108001866""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_Int-5C-3C
Total Standard Deviation in ln(k): 16.741037108001866
""",
)

entry(
    index = 356,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_3C-inRing",
    kinetics = ArrheniusBM(A=(116313,'s^-1'), n=2.43845, w0=(411000,'J/mol'), E0=(151525,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0013719289980274043, var=2.172824079862177, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_3C-inRing',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_3C-inRing
    Total Standard Deviation in ln(k): 2.9585272592292773"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_3C-inRing
Total Standard Deviation in ln(k): 2.9585272592292773""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_3C-inRing
Total Standard Deviation in ln(k): 2.9585272592292773
""",
)

entry(
    index = 357,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing",
    kinetics = ArrheniusBM(A=(1.45582e-66,'s^-1'), n=23.2264, w0=(411000,'J/mol'), E0=(-18782,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.4955488072615695, var=11.265911309567263, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing
    Total Standard Deviation in ln(k): 10.486499571708224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing
Total Standard Deviation in ln(k): 10.486499571708224""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing
Total Standard Deviation in ln(k): 10.486499571708224
""",
)

entry(
    index = 358,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_N-Sp-5C-4R!H_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.55379e-06,'s^-1'), n=5.43883, w0=(411000,'J/mol'), E0=(118995,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_N-Sp-5C-4R!H_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_N-Sp-5C-4R!H_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_N-Sp-5C-4R!H_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_N-Sp-5C-4R!H_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 359,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C",
    kinetics = ArrheniusBM(A=(6.28339e+08,'s^-1'), n=0.952519, w0=(435000,'J/mol'), E0=(89508.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.005531443939448918, var=2.337033605188413, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C',), comment="""BM rule fitted to 15 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C
    Total Standard Deviation in ln(k): 3.0786086836288065"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C
Total Standard Deviation in ln(k): 3.0786086836288065""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C
Total Standard Deviation in ln(k): 3.0786086836288065
""",
)

entry(
    index = 360,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.03876e+10,'s^-1'), n=0.620438, w0=(435000,'J/mol'), E0=(99953.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0013235937995983926, var=0.279855497232683, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_N-6R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_N-6R!H->C
    Total Standard Deviation in ln(k): 1.0638579380065998"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_N-6R!H->C
Total Standard Deviation in ln(k): 1.0638579380065998""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_N-6R!H->C
Total Standard Deviation in ln(k): 1.0638579380065998
""",
)

entry(
    index = 361,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C_Ext-5R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(4.6871e+09,'s^-1'), n=0.645198, w0=(435000,'J/mol'), E0=(101424,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.580117586697306e-06, var=0.18398009708210997, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C_Ext-5R!H-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C_Ext-5R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 0.8599005433098691"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 0.8599005433098691""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 0.8599005433098691
""",
)

entry(
    index = 362,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C_Ext-5R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(7.66667e+08,'s^-1'), n=0.75, w0=(435000,'J/mol'), E0=(83876,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C_Ext-5R!H-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C_Ext-5R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 363,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(5.91667e+08,'s^-1'), n=0.686, w0=(435000,'J/mol'), E0=(36490.3,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 364,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5133.33,'s^-1'), n=2.338, w0=(435000,'J/mol'), E0=(42219.3,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 365,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(21.1933,'s^-1'), n=2.81162, w0=(435000,'J/mol'), E0=(58082.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 366,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.95845e+06,'s^-1'), n=1.14601, w0=(435000,'J/mol'), E0=(37400.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-6.556264522968056, var=125.22118874967111, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 38.90646778636996"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 38.90646778636996""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 38.90646778636996
""",
)

entry(
    index = 367,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8848.43,'s^-1'), n=2.35115, w0=(435000,'J/mol'), E0=(47223.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05983542338355077, var=4.147096627310405, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 12 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.23286726947673"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.23286726947673""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.23286726947673
""",
)

entry(
    index = 368,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.21799e+08,'s^-1'), n=1.09942, w0=(435000,'J/mol'), E0=(61718.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.745805162314537e-05, var=3.511614508295888, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-6R!H-R
    Total Standard Deviation in ln(k): 3.756878032376596"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.756878032376596""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.756878032376596
""",
)

entry(
    index = 369,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.26811e+10,'s^-1'), n=0.439003, w0=(435000,'J/mol'), E0=(61396.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.009062957198920285, var=1.0485638081992423, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 2.075608034216947"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.075608034216947""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.075608034216947
""",
)

entry(
    index = 370,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.95e+08,'s^-1'), n=0, w0=(435000,'J/mol'), E0=(126320,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 371,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_6R!H->O_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(628,'s^-1'), n=2.2, w0=(435000,'J/mol'), E0=(48618.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_6R!H->O_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_6R!H->O_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_6R!H->O_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_6R!H->O_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 372,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_6R!H->O_Ext-8R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(557,'s^-1'), n=1.8, w0=(435000,'J/mol'), E0=(45083.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_6R!H->O_Ext-8R!H-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_6R!H->O_Ext-8R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_6R!H->O_Ext-8R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_6R!H->O_Ext-8R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 373,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.24399e-08,'s^-1'), n=5.03824, w0=(435000,'J/mol'), E0=(5164.86,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.017863011894803615, var=3.337092796022325, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 3.707074121112904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 3.707074121112904""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 3.707074121112904
""",
)

entry(
    index = 374,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_Ext-1C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(72300,'s^-1'), n=1.65, w0=(435000,'J/mol'), E0=(32457.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_Ext-1C-R_6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_Ext-1C-R_6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_Ext-1C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_Ext-1C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 375,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_Ext-1C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(1.48e+06,'s^-1'), n=1.22, w0=(435000,'J/mol'), E0=(38207.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_Ext-1C-R_N-6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_Ext-1C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_Ext-1C-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-1C-R_Ext-1C-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 376,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.69136e+06,'s^-1'), n=0.437108, w0=(435000,'J/mol'), E0=(122643,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_4R!H->C_Ext-3R!H-R_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 377,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H",
    kinetics = ArrheniusBM(A=(221338,'s^-1'), n=1.71888, w0=(435000,'J/mol'), E0=(84569.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.005660858420503035, var=4.513159609029384, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H
    Total Standard Deviation in ln(k): 4.273122212284589"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H
Total Standard Deviation in ln(k): 4.273122212284589""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H
Total Standard Deviation in ln(k): 4.273122212284589
""",
)

entry(
    index = 378,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_N-Sp-6C-3R!H",
    kinetics = ArrheniusBM(A=(300.781,'s^-1'), n=2.76092, w0=(435000,'J/mol'), E0=(88466.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_N-Sp-6C-3R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_N-Sp-6C-3R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_N-Sp-6C-3R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_N-Sp-6C-3R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 379,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_N-6R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.30387e+10,'s^-1'), n=0.259039, w0=(435000,'J/mol'), E0=(97923.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-9.053131366243684e-05, var=0.6921867645320384, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_N-6R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_N-6R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.6681221892754037"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_N-6R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.6681221892754037""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_N-6R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.6681221892754037
""",
)

entry(
    index = 380,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(3.01549e+14,'s^-1'), n=-1.05193, w0=(435000,'J/mol'), E0=(107107,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_N-6R!H->C_Ext-6BrClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 381,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-5R!H-R_6R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(7.14711e+08,'s^-1'), n=0.332878, w0=(435000,'J/mol'), E0=(102830,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-5R!H-R_6R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-5R!H-R_6R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-5R!H-R_6R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-5R!H-R_6R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 382,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(750011,'s^-1'), n=1.64735, w0=(435000,'J/mol'), E0=(47136.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10025873825017419, var=4.664288215499689, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 4.5815253564260825"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.5815253564260825""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.5815253564260825
""",
)

entry(
    index = 383,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2026.74,'s^-1'), n=2.70023, w0=(435000,'J/mol'), E0=(57989.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 384,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(605046,'s^-1'), n=1.43896, w0=(435000,'J/mol'), E0=(48244.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.18347928702532493, var=6.057244153423674, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 5.394950791454645"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 5.394950791454645""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 5.394950791454645
""",
)

entry(
    index = 385,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(4.706e+06,'s^-1'), n=0.937076, w0=(435000,'J/mol'), E0=(64628,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 386,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.86198e+06,'s^-1'), n=1.12731, w0=(435000,'J/mol'), E0=(52842.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 387,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(9.53732e+06,'s^-1'), n=1.02876, w0=(435000,'J/mol'), E0=(53673.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 388,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-6R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.62975e+08,'s^-1'), n=0.649005, w0=(435000,'J/mol'), E0=(62880.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-6R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-6R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 389,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(9.11076e+08,'s^-1'), n=0.421138, w0=(435000,'J/mol'), E0=(56278.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 390,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(173676,'s^-1'), n=0.900233, w0=(435000,'J/mol'), E0=(53205.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-6R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 391,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.93409e-07,'s^-1'), n=4.53645, w0=(435000,'J/mol'), E0=(3620.86,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.9686968826674995, var=17.81434365448546, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 10.89530545780899"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 10.89530545780899""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 10.89530545780899
""",
)

entry(
    index = 392,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_9R!H->C",
    kinetics = ArrheniusBM(A=(285336,'s^-1'), n=0.857309, w0=(435000,'J/mol'), E0=(52842.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 393,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(7.73767e+08,'s^-1'), n=-0.331238, w0=(435000,'J/mol'), E0=(42141.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 394,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_N-7R!H->O_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(192770,'s^-1'), n=1.23024, w0=(435000,'J/mol'), E0=(38151.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_N-7R!H->O_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_N-7R!H->O_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_N-7R!H->O_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Int-7R!H-3R!H_N-7R!H->O_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 395,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.03208e+12,'s^-1'), n=0.140233, w0=(435000,'J/mol'), E0=(149838,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 396,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_7R!H-inRing_3C-inRing",
    kinetics = ArrheniusBM(A=(8.35153e+10,'s^-1'), n=0.707499, w0=(411000,'J/mol'), E0=(241277,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.024718216590170053, var=0.3636836520014926, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_7R!H-inRing_3C-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_7R!H-inRing_3C-inRing
    Total Standard Deviation in ln(k): 1.271085411235675"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_7R!H-inRing_3C-inRing
Total Standard Deviation in ln(k): 1.271085411235675""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_7R!H-inRing_3C-inRing
Total Standard Deviation in ln(k): 1.271085411235675
""",
)

entry(
    index = 397,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_7R!H-inRing_N-3C-inRing",
    kinetics = ArrheniusBM(A=(191.5,'s^-1'), n=3.05, w0=(411000,'J/mol'), E0=(208747,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_7R!H-inRing_N-3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_7R!H-inRing_N-3C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_7R!H-inRing_N-3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_7R!H-inRing_N-3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 398,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_N-7R!H-inRing_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.65505e+11,'s^-1'), n=0.822983, w0=(411000,'J/mol'), E0=(182392,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.846876143357608e-14, var=42.12869312856673, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_N-7R!H-inRing_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_N-7R!H-inRing_Ext-7R!H-R
    Total Standard Deviation in ln(k): 13.012057776148819"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_N-7R!H-inRing_Ext-7R!H-R
Total Standard Deviation in ln(k): 13.012057776148819""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_N-7R!H-inRing_Ext-7R!H-R
Total Standard Deviation in ln(k): 13.012057776148819
""",
)

entry(
    index = 399,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_N-7R!H-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.1342e+11,'s^-1'), n=0.790506, w0=(411000,'J/mol'), E0=(182304,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7221843336360837e-14, var=54.64854356810548, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_N-7R!H-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_N-7R!H-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 14.819934543654572"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_N-7R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 14.819934543654572""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_N-7R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 14.819934543654572
""",
)

entry(
    index = 400,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-5R!H-R_5R!H-inRing",
    kinetics = ArrheniusBM(A=(375845,'s^-1'), n=2.35203, w0=(411000,'J/mol'), E0=(200736,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-5R!H-R_5R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-5R!H-R_5R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-5R!H-R_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-5R!H-R_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 401,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-5R!H-R_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(4.76029e+09,'s^-1'), n=0.859089, w0=(411000,'J/mol'), E0=(235406,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=14.14617574107582, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-5R!H-R_N-5R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-5R!H-R_N-5R!H-inRing
    Total Standard Deviation in ln(k): 7.5400897264538225"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-5R!H-R_N-5R!H-inRing
Total Standard Deviation in ln(k): 7.5400897264538225""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-5R!H-R_N-5R!H-inRing
Total Standard Deviation in ln(k): 7.5400897264538225
""",
)

entry(
    index = 402,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.76675e+12,'s^-1'), n=0.355429, w0=(411000,'J/mol'), E0=(196036,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7573309526898815e-15, var=11.898357620908873, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 6.915132380005717"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.915132380005717""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-4R!H-3C_Ext-1C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.915132380005717
""",
)

entry(
    index = 403,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-4R!H-R_5R!H-inRing_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.54098e+10,'s^-1'), n=1.02289, w0=(411000,'J/mol'), E0=(243584,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-4R!H-R_5R!H-inRing_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-4R!H-R_5R!H-inRing_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-4R!H-R_5R!H-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-4R!H-R_5R!H-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 404,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.03e+09,'s^-1'), n=1.31, w0=(411000,'J/mol'), E0=(177464,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_Sp-5R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 405,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_Sp-5R!H-3C_5R!H-inRing",
    kinetics = ArrheniusBM(A=(7.5e+08,'s^-1'), n=0.835, w0=(411000,'J/mol'), E0=(178125,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_Sp-5R!H-3C_5R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_Sp-5R!H-3C_5R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_Sp-5R!H-3C_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_Sp-5R!H-3C_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 406,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_Sp-5R!H-3C_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(2.31128e-53,'s^-1'), n=19.4746, w0=(411000,'J/mol'), E0=(33421.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-7.029323810759526e-15, var=29.110037171839704, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_Sp-5R!H-3C_N-5R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_Sp-5R!H-3C_N-5R!H-inRing
    Total Standard Deviation in ln(k): 10.816291160933911"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_Sp-5R!H-3C_N-5R!H-inRing
Total Standard Deviation in ln(k): 10.816291160933911""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_N-4R!H-inRing_N-3C-inRing_Int-3C-1C_Ext-3C-R_Sp-5R!H-3C_N-5R!H-inRing
Total Standard Deviation in ln(k): 10.816291160933911
""",
)

entry(
    index = 407,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_Sp-5R!H-=3C_Ext-1C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(135526,'s^-1'), n=2.09917, w0=(411000,'J/mol'), E0=(72645.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_Sp-5R!H-=3C_Ext-1C-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_Sp-5R!H-=3C_Ext-1C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_Sp-5R!H-=3C_Ext-1C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_Sp-5R!H-=3C_Ext-1C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 408,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing",
    kinetics = ArrheniusBM(A=(384933,'s^-1'), n=2.03445, w0=(411000,'J/mol'), E0=(133381,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0039511199329899304, var=8.964536629858936, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing
    Total Standard Deviation in ln(k): 6.012271863315848"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing
Total Standard Deviation in ln(k): 6.012271863315848""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing
Total Standard Deviation in ln(k): 6.012271863315848
""",
)

entry(
    index = 409,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(715246,'s^-1'), n=1.72555, w0=(411000,'J/mol'), E0=(89363.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06638675968171073, var=3.5551353037787297, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing',), comment="""BM rule fitted to 22 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing
    Total Standard Deviation in ln(k): 3.9467422111897195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing
Total Standard Deviation in ln(k): 3.9467422111897195""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing
Total Standard Deviation in ln(k): 3.9467422111897195
""",
)

entry(
    index = 410,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.71095e+10,'s^-1'), n=0.35101, w0=(411000,'J/mol'), E0=(104106,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.059123513100317, var=10.714913874004335, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C
    Total Standard Deviation in ln(k): 6.7107797840079915"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 6.7107797840079915""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 6.7107797840079915
""",
)

entry(
    index = 411,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1655.27,'s^-1'), n=2.42251, w0=(411000,'J/mol'), E0=(77613.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=12.821237199397752, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 7.1783058212729856"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 7.1783058212729856""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 7.1783058212729856
""",
)

entry(
    index = 412,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.34654e+13,'s^-1'), n=-0.297776, w0=(411000,'J/mol'), E0=(172437,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.804498668245169, var=79.58786606104867, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R
    Total Standard Deviation in ln(k): 19.906002372073004"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 19.906002372073004""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 19.906002372073004
""",
)

entry(
    index = 413,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.5242e+06,'s^-1'), n=1.7546, w0=(411000,'J/mol'), E0=(145723,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07764089534213643, var=1.3478400397824717, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-3C-R
    Total Standard Deviation in ln(k): 2.522505152020604"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 2.522505152020604""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 2.522505152020604
""",
)

entry(
    index = 414,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.04149e+10,'s^-1'), n=0.999348, w0=(411000,'J/mol'), E0=(197062,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0010417285039057264, var=2.279717561882543, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-1C-R
    Total Standard Deviation in ln(k): 3.0295134946165634"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 3.0295134946165634""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 3.0295134946165634
""",
)

entry(
    index = 415,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5200,'s^-1'), n=2.49, w0=(411000,'J/mol'), E0=(210988,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 416,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.43267e+10,'s^-1'), n=0.89195, w0=(411000,'J/mol'), E0=(202385,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00018314710545991875, var=2.0502310118016003, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-3C-R
    Total Standard Deviation in ln(k): 2.8709657034239555"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 2.8709657034239555""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 2.8709657034239555
""",
)

entry(
    index = 417,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_N-3C-inRing_Ext-3C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(55151.7,'s^-1'), n=2.33227, w0=(411000,'J/mol'), E0=(212072,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_N-3C-inRing_Ext-3C-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_N-3C-inRing_Ext-3C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_N-3C-inRing_Ext-3C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_N-3C-inRing_Ext-3C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 418,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_N-3C-inRing_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.06827e+08,'s^-1'), n=1.41461, w0=(411000,'J/mol'), E0=(206909,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.602528453014257e-15, var=1.792278026969943, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_N-3C-inRing_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_N-3C-inRing_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 2.683858899634646"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_N-3C-inRing_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 2.683858899634646""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_N-3C-inRing_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 2.683858899634646
""",
)

entry(
    index = 419,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing",
    kinetics = ArrheniusBM(A=(1.10981e-58,'s^-1'), n=20.7861, w0=(411000,'J/mol'), E0=(20409.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8298591631807296, var=6.5817626352075465, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing
    Total Standard Deviation in ln(k): 7.228210325980089"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing
Total Standard Deviation in ln(k): 7.228210325980089""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing
Total Standard Deviation in ln(k): 7.228210325980089
""",
)

entry(
    index = 420,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_N-3C-inRing",
    kinetics = ArrheniusBM(A=(2.48808,'s^-1'), n=3.50854, w0=(411000,'J/mol'), E0=(139526,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.014556055480879267, var=1.6681099751382131, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_N-3C-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_N-3C-inRing
    Total Standard Deviation in ln(k): 2.6257952461158522"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_N-3C-inRing
Total Standard Deviation in ln(k): 2.6257952461158522""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_N-3C-inRing
Total Standard Deviation in ln(k): 2.6257952461158522
""",
)

entry(
    index = 421,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H_1C-inRing",
    kinetics = ArrheniusBM(A=(2.21729e+09,'s^-1'), n=1.2167, w0=(411000,'J/mol'), E0=(222065,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H_1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H_1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 422,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H_N-1C-inRing",
    kinetics = ArrheniusBM(A=(537046,'s^-1'), n=2.06148, w0=(411000,'J/mol'), E0=(149768,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008107878889372994, var=0.18888398391553898, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H_N-1C-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H_N-1C-inRing
    Total Standard Deviation in ln(k): 0.8916451582663203"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H_N-1C-inRing
Total Standard Deviation in ln(k): 0.8916451582663203""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H_N-1C-inRing
Total Standard Deviation in ln(k): 0.8916451582663203
""",
)

entry(
    index = 423,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing",
    kinetics = ArrheniusBM(A=(2.4403e-06,'s^-1'), n=5.61728, w0=(411000,'J/mol'), E0=(150266,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.23234970758858214, var=76.651170471253, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing
    Total Standard Deviation in ln(k): 18.135379983239506"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing
Total Standard Deviation in ln(k): 18.135379983239506""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing
Total Standard Deviation in ln(k): 18.135379983239506
""",
)

entry(
    index = 424,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3C-inRing",
    kinetics = ArrheniusBM(A=(240,'s^-1'), n=2.932, w0=(411000,'J/mol'), E0=(174552,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 425,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_N-Sp-4R!H-1C_Ext-3C-R_Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(3.45e+06,'s^-1'), n=1.572, w0=(411000,'J/mol'), E0=(166835,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_N-Sp-4R!H-1C_Ext-3C-R_Sp-6R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_N-Sp-4R!H-1C_Ext-3C-R_Sp-6R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_N-Sp-4R!H-1C_Ext-3C-R_Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_N-Sp-4R!H-1C_Ext-3C-R_Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 426,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_N-Sp-4R!H-1C_Ext-3C-R_N-Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(65110,'s^-1'), n=2.209, w0=(411000,'J/mol'), E0=(100963,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_N-Sp-4R!H-1C_Ext-3C-R_N-Sp-6R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_N-Sp-4R!H-1C_Ext-3C-R_N-Sp-6R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_N-Sp-4R!H-1C_Ext-3C-R_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_N-Sp-4R!H-1C_Ext-3C-R_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 427,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Int-8R!H-4R!H",
    kinetics = ArrheniusBM(A=(6.9946e+07,'s^-1'), n=1.62993, w0=(411000,'J/mol'), E0=(87055.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.005185499231412631, var=60.67524021007497, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Int-8R!H-4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Int-8R!H-4R!H
    Total Standard Deviation in ln(k): 15.628775082541813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Int-8R!H-4R!H
Total Standard Deviation in ln(k): 15.628775082541813""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Int-8R!H-4R!H
Total Standard Deviation in ln(k): 15.628775082541813
""",
)

entry(
    index = 428,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(6.65027e-54,'s^-1'), n=19.2199, w0=(411000,'J/mol'), E0=(-993.887,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.7121442869669025, var=13.671573365525829, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 16 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 9.201833396898667"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 9.201833396898667""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 9.201833396898667
""",
)

entry(
    index = 429,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(5.13234e-76,'s^-1'), n=26.1817, w0=(411000,'J/mol'), E0=(-43549.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.527743566977079, var=38.39743024830779, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 23.798713346671583"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 23.798713346671583""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 23.798713346671583
""",
)

entry(
    index = 430,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Int-3C-1C",
    kinetics = ArrheniusBM(A=(7.07809e-34,'s^-1'), n=13.5311, w0=(411000,'J/mol'), E0=(16576.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.8017570734031807, var=300.358454164588, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Int-3C-1C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Int-3C-1C
    Total Standard Deviation in ln(k): 44.29592171340741"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Int-3C-1C
Total Standard Deviation in ln(k): 44.29592171340741""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Int-3C-1C
Total Standard Deviation in ln(k): 44.29592171340741
""",
)

entry(
    index = 431,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Sp-7R!H-3C",
    kinetics = ArrheniusBM(A=(9.37e+06,'s^-1'), n=1.6, w0=(411000,'J/mol'), E0=(139726,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Sp-7R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Sp-7R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Sp-7R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Sp-7R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 432,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_N-Sp-7R!H-3C",
    kinetics = ArrheniusBM(A=(1.08e+06,'s^-1'), n=1.99, w0=(411000,'J/mol'), E0=(173335,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_N-Sp-7R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_N-Sp-7R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_N-Sp-7R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_N-Sp-7R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 433,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_N-6R!H-inRing_1C-inRing",
    kinetics = ArrheniusBM(A=(7.85841e+10,'s^-1'), n=0.620824, w0=(411000,'J/mol'), E0=(180240,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.013569789216041206, var=15.919304697354198, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_N-6R!H-inRing_1C-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_N-6R!H-inRing_1C-inRing
    Total Standard Deviation in ln(k): 8.032788108207692"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_N-6R!H-inRing_1C-inRing
Total Standard Deviation in ln(k): 8.032788108207692""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_N-6R!H-inRing_1C-inRing
Total Standard Deviation in ln(k): 8.032788108207692
""",
)

entry(
    index = 434,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_N-6R!H-inRing_N-1C-inRing",
    kinetics = ArrheniusBM(A=(2670,'s^-1'), n=1.94, w0=(411000,'J/mol'), E0=(78656.5,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_N-6R!H-inRing_N-1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_N-6R!H-inRing_N-1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_N-6R!H-inRing_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_N-6R!H-inRing_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 435,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_1C-inRing_3C-inRing",
    kinetics = ArrheniusBM(A=(1.36e+08,'s^-1'), n=1.39, w0=(411000,'J/mol'), E0=(147916,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_1C-inRing_3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_1C-inRing_3C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_1C-inRing_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_1C-inRing_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 436,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_1C-inRing_N-3C-inRing",
    kinetics = ArrheniusBM(A=(1.107e+09,'s^-1'), n=0.879, w0=(411000,'J/mol'), E0=(128066,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_1C-inRing_N-3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_1C-inRing_N-3C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_1C-inRing_N-3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-1C-R_1C-inRing_N-3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 437,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(1.80655e-61,'s^-1'), n=21.7603, w0=(411000,'J/mol'), E0=(-16586.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.28415298096258196, var=55.709797472318215, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_Sp-6R!H-3C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_Sp-6R!H-3C
    Total Standard Deviation in ln(k): 15.677093587091532"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_Sp-6R!H-3C
Total Standard Deviation in ln(k): 15.677093587091532""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_Sp-6R!H-3C
Total Standard Deviation in ln(k): 15.677093587091532
""",
)

entry(
    index = 438,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_N-Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(9.54886e+11,'s^-1'), n=0.269652, w0=(411000,'J/mol'), E0=(182745,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.027217561771662614, var=9.458697983435117, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_N-Sp-6R!H-3C',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_N-Sp-6R!H-3C
    Total Standard Deviation in ln(k): 6.233947825403504"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 6.233947825403504""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 6.233947825403504
""",
)

entry(
    index = 439,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_N-1C-inRing_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.11e+06,'s^-1'), n=1.64, w0=(411000,'J/mol'), E0=(118531,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_N-1C-inRing_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_N-1C-inRing_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_N-1C-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_N-1C-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 440,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_N-1C-inRing_Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(40333.3,'s^-1'), n=1.9, w0=(411000,'J/mol'), E0=(78656.5,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_N-1C-inRing_Sp-6R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_N-1C-inRing_Sp-6R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_N-1C-inRing_Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_N-1C-inRing_Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 441,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_N-1C-inRing_N-Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(4522.73,'s^-1'), n=2.241, w0=(411000,'J/mol'), E0=(79402.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=9.618399503357528e-14, var=4.112370340645024, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_N-1C-inRing_N-Sp-6R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_N-1C-inRing_N-Sp-6R!H-3C
    Total Standard Deviation in ln(k): 4.065398274856922"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_N-1C-inRing_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 4.065398274856922""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_N-1C-inRing_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 4.065398274856922
""",
)

entry(
    index = 442,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(175.851,'s^-1'), n=2.76726, w0=(411000,'J/mol'), E0=(150797,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0591143599406187, var=2.3148986794803834, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 3.1986910821342045"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.1986910821342045""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.1986910821342045
""",
)

entry(
    index = 443,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.21703e+08,'s^-1'), n=1.35316, w0=(411000,'J/mol'), E0=(150102,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-6.194591608231832e-15, var=0.3386105707970163, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 1.1665604417252655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.1665604417252655""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.1665604417252655
""",
)

entry(
    index = 444,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_1C-inRing",
    kinetics = ArrheniusBM(A=(1.01255e+11,'s^-1'), n=0.635492, w0=(411000,'J/mol'), E0=(135508,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09902827688777566, var=0.08652270454441036, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_1C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_1C-inRing
    Total Standard Deviation in ln(k): 0.8385024163434938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_1C-inRing
Total Standard Deviation in ln(k): 0.8385024163434938""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_1C-inRing
Total Standard Deviation in ln(k): 0.8385024163434938
""",
)

entry(
    index = 445,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_N-1C-inRing",
    kinetics = ArrheniusBM(A=(1.33475e-54,'s^-1'), n=19.4696, w0=(411000,'J/mol'), E0=(29347,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.44928989990144425, var=14.296940605416598, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_N-1C-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_N-1C-inRing
    Total Standard Deviation in ln(k): 8.709032118135939"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_N-1C-inRing
Total Standard Deviation in ln(k): 8.709032118135939""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_N-1C-inRing
Total Standard Deviation in ln(k): 8.709032118135939
""",
)

entry(
    index = 446,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3C-R_Ext-8R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.66898,'s^-1'), n=2.29768, w0=(411000,'J/mol'), E0=(67867,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3C-R_Ext-8R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3C-R_Ext-8R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3C-R_Ext-8R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3C-R_Ext-8R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 447,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1C-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(5470,'s^-1'), n=1.94, w0=(411000,'J/mol'), E0=(94139.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1C-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1C-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 448,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(233.246,'s^-1'), n=2.04524, w0=(411000,'J/mol'), E0=(70972.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.108797143227858e-15, var=25.78233841156287, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1C-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 10.179305338877423"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 10.179305338877423""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 10.179305338877423
""",
)

entry(
    index = 449,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1C-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(344.078,'s^-1'), n=2.05418, w0=(411000,'J/mol'), E0=(55236.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.887984046863765, var=78.77288225900668, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1C-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1C-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 32.586773214289785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 32.586773214289785""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 32.586773214289785
""",
)

entry(
    index = 450,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.51882e+13,'s^-1'), n=-0.0209574, w0=(411000,'J/mol'), E0=(155857,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.009029934674495876, var=3.1124017860049142, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 3.559441984571133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.559441984571133""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.559441984571133
""",
)

entry(
    index = 451,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(4.33698e-71,'s^-1'), n=24.7531, w0=(411000,'J/mol'), E0=(-20602.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8656698587367897, var=6.878747640803367, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 7.4329420976853315"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 7.4329420976853315""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 7.4329420976853315
""",
)

entry(
    index = 452,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(2.27469e+08,'s^-1'), n=1.59713, w0=(411000,'J/mol'), E0=(153543,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.040609914000723536, var=5.722135725524844, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Sp-6R!H-3C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Sp-6R!H-3C
    Total Standard Deviation in ln(k): 4.897558937422459"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Sp-6R!H-3C
Total Standard Deviation in ln(k): 4.897558937422459""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Sp-6R!H-3C
Total Standard Deviation in ln(k): 4.897558937422459
""",
)

entry(
    index = 453,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_N-Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(1.09e+11,'s^-1'), n=0.703, w0=(411000,'J/mol'), E0=(41100,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_N-Sp-6R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_N-Sp-6R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 454,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C_Sp-3C-=1C",
    kinetics = ArrheniusBM(A=(3.10894e+08,'s^-1'), n=1.59264, w0=(411000,'J/mol'), E0=(238900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.8767745408805217e-15, var=0.0005885213501385992, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C_Sp-3C-=1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C_Sp-3C-=1C
    Total Standard Deviation in ln(k): 0.04863378838144642"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C_Sp-3C-=1C
Total Standard Deviation in ln(k): 0.04863378838144642""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C_Sp-3C-=1C
Total Standard Deviation in ln(k): 0.04863378838144642
""",
)

entry(
    index = 455,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C_N-Sp-3C-=1C",
    kinetics = ArrheniusBM(A=(1.22664e+11,'s^-1'), n=0.770379, w0=(411000,'J/mol'), E0=(233652,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7847892488256607e-15, var=0.01218497527050402, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C_N-Sp-3C-=1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C_N-Sp-3C-=1C
    Total Standard Deviation in ln(k): 0.22129383517089163"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C_N-Sp-3C-=1C
Total Standard Deviation in ln(k): 0.22129383517089163""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C_N-Sp-3C-=1C
Total Standard Deviation in ln(k): 0.22129383517089163
""",
)

entry(
    index = 456,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(8.48559,'s^-1'), n=3.41616, w0=(411000,'J/mol'), E0=(138488,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0960940443586556, var=8.871690520261525, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R',), comment="""BM rule fitted to 36 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 6.212622570815795"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.212622570815795""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.212622570815795
""",
)

entry(
    index = 457,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.30201e+08,'s^-1'), n=1.13171, w0=(411000,'J/mol'), E0=(124400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.015770342243151336, var=79.0640628867512, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 17.865322336741343"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 17.865322336741343""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 17.865322336741343
""",
)

entry(
    index = 458,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.50161e+10,'s^-1'), n=0.780693, w0=(411000,'J/mol'), E0=(175989,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006098182399097379, var=23.609251502800483, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-3C-R
    Total Standard Deviation in ln(k): 9.756199946970844"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-3C-R
Total Standard Deviation in ln(k): 9.756199946970844""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-3C-R
Total Standard Deviation in ln(k): 9.756199946970844
""",
)

entry(
    index = 459,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_N-Sp-4R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(4.8432e+08,'s^-1'), n=0.666516, w0=(411000,'J/mol'), E0=(53921.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0748182869102846, var=1.5063702844306015, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_N-Sp-4R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_N-Sp-4R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H-3C
    Total Standard Deviation in ln(k): 2.648482756152047"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_N-Sp-4R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H-3C
Total Standard Deviation in ln(k): 2.648482756152047""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_N-Sp-4R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H-3C
Total Standard Deviation in ln(k): 2.648482756152047
""",
)

entry(
    index = 460,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_N-Sp-4R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(403802,'s^-1'), n=1.7686, w0=(411000,'J/mol'), E0=(45742.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_N-Sp-4R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_N-Sp-4R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_N-Sp-4R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_N-Sp-4R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 461,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C",
    kinetics = ArrheniusBM(A=(4.30404e+07,'s^-1'), n=0.656601, w0=(411000,'J/mol'), E0=(65416.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06755490520885192, var=4.895633934409995, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C',), comment="""BM rule fitted to 36 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C
    Total Standard Deviation in ln(k): 4.60542870990686"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C
Total Standard Deviation in ln(k): 4.60542870990686""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C
Total Standard Deviation in ln(k): 4.60542870990686
""",
)

entry(
    index = 462,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(16.2379,'s^-1'), n=2.60422, w0=(411000,'J/mol'), E0=(50682.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0018544902149090715, var=1.4905945717675486, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_N-4R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_N-4R!H->C
    Total Standard Deviation in ln(k): 2.4522387415381663"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_N-4R!H->C
Total Standard Deviation in ln(k): 2.4522387415381663""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_N-4R!H->C
Total Standard Deviation in ln(k): 2.4522387415381663
""",
)

entry(
    index = 463,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C_Sp-5C-4R!H",
    kinetics = ArrheniusBM(A=(264618,'s^-1'), n=2.06864, w0=(411000,'J/mol'), E0=(146387,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04231211104410312, var=0.9373253728937793, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C_Sp-5C-4R!H',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C_Sp-5C-4R!H
    Total Standard Deviation in ln(k): 2.047207439356206"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C_Sp-5C-4R!H
Total Standard Deviation in ln(k): 2.047207439356206""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C_Sp-5C-4R!H
Total Standard Deviation in ln(k): 2.047207439356206
""",
)

entry(
    index = 464,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C_N-Sp-5C-4R!H",
    kinetics = ArrheniusBM(A=(619277,'s^-1'), n=2.04356, w0=(411000,'J/mol'), E0=(148895,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.043753626584753985, var=0.2978860801850417, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C_N-Sp-5C-4R!H',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C_N-Sp-5C-4R!H
    Total Standard Deviation in ln(k): 1.204096910449502"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C_N-Sp-5C-4R!H
Total Standard Deviation in ln(k): 1.204096910449502""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C_N-Sp-5C-4R!H
Total Standard Deviation in ln(k): 1.204096910449502
""",
)

entry(
    index = 465,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-6R!H-R_Int-3C-1C",
    kinetics = ArrheniusBM(A=(6.64662e+12,'s^-1'), n=0.0217215, w0=(411000,'J/mol'), E0=(152222,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.011065965414880325, var=0.09785938614189518, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-6R!H-R_Int-3C-1C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-6R!H-R_Int-3C-1C
    Total Standard Deviation in ln(k): 0.6549348810420694"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-6R!H-R_Int-3C-1C
Total Standard Deviation in ln(k): 0.6549348810420694""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-6R!H-R_Int-3C-1C
Total Standard Deviation in ln(k): 0.6549348810420694
""",
)

entry(
    index = 466,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-6R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.52411e+10,'s^-1'), n=0.456173, w0=(411000,'J/mol'), E0=(153392,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7573309526898814e-16, var=1.8491915360388114, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-6R!H-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-6R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 2.7261386364159406"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-6R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.7261386364159406""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-6R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.7261386364159406
""",
)

entry(
    index = 467,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Sp-6R!H=3C_Int-4C-3C",
    kinetics = ArrheniusBM(A=(6.12521e+08,'s^-1'), n=1.09546, w0=(411000,'J/mol'), E0=(155285,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00708960926879331, var=0.5447437968554663, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Sp-6R!H=3C_Int-4C-3C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Sp-6R!H=3C_Int-4C-3C
    Total Standard Deviation in ln(k): 1.4974431157677779"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Sp-6R!H=3C_Int-4C-3C
Total Standard Deviation in ln(k): 1.4974431157677779""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Sp-6R!H=3C_Int-4C-3C
Total Standard Deviation in ln(k): 1.4974431157677779
""",
)

entry(
    index = 468,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Sp-6R!H=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.65529e+08,'s^-1'), n=1.15905, w0=(411000,'J/mol'), E0=(191115,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.514661905379763e-15, var=11.898357620908772, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Sp-6R!H=3C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Sp-6R!H=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 6.9151323800056925"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Sp-6R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 6.9151323800056925""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Sp-6R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 6.9151323800056925
""",
)

entry(
    index = 469,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C",
    kinetics = ArrheniusBM(A=(1.69166e-63,'s^-1'), n=22.1373, w0=(411000,'J/mol'), E0=(4688.21,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6625970117912926, var=6.864603590178566, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C',), comment="""BM rule fitted to 10 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C
    Total Standard Deviation in ln(k): 6.917300404883445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C
Total Standard Deviation in ln(k): 6.917300404883445""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C
Total Standard Deviation in ln(k): 6.917300404883445
""",
)

entry(
    index = 470,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-3C-1C",
    kinetics = ArrheniusBM(A=(1.46366e+10,'s^-1'), n=0.868215, w0=(411000,'J/mol'), E0=(159880,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0060176690117007626, var=0.5158063569021745, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-3C-1C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-3C-1C
    Total Standard Deviation in ln(k): 1.4549136887794316"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-3C-1C
Total Standard Deviation in ln(k): 1.4549136887794316""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-3C-1C
Total Standard Deviation in ln(k): 1.4549136887794316
""",
)

entry(
    index = 471,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_Sp-7R!H-5R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.92106e+09,'s^-1'), n=0.991289, w0=(411000,'J/mol'), E0=(162288,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.690395000648751e-15, var=2.6304091267166116, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_Sp-7R!H-5R!H_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_Sp-7R!H-5R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 3.251386818933089"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_Sp-7R!H-5R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.251386818933089""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_Sp-7R!H-5R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.251386818933089
""",
)

entry(
    index = 472,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_N-Sp-7R!H-5R!H_3C-inRing",
    kinetics = ArrheniusBM(A=(3.21781e+12,'s^-1'), n=0.690459, w0=(411000,'J/mol'), E0=(120023,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_N-Sp-7R!H-5R!H_3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_N-Sp-7R!H-5R!H_3C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_N-Sp-7R!H-5R!H_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_N-Sp-7R!H-5R!H_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 473,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_N-Sp-7R!H-5R!H_N-3C-inRing",
    kinetics = ArrheniusBM(A=(2.13e+10,'s^-1'), n=0.77, w0=(411000,'J/mol'), E0=(159767,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_N-Sp-7R!H-5R!H_N-3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_N-Sp-7R!H-5R!H_N-3C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_N-Sp-7R!H-5R!H_N-3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Ext-3C-R_Int-3C-1C_Ext-5R!H-R_N-Sp-7R!H-5R!H_N-3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 474,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_5R!H-inRing_Int-3C-1C",
    kinetics = ArrheniusBM(A=(228.553,'s^-1'), n=3.07318, w0=(411000,'J/mol'), E0=(172151,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.020643327652459437, var=21.25892052423337, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_5R!H-inRing_Int-3C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_5R!H-inRing_Int-3C-1C
    Total Standard Deviation in ln(k): 9.295179254367037"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_5R!H-inRing_Int-3C-1C
Total Standard Deviation in ln(k): 9.295179254367037""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_5R!H-inRing_Int-3C-1C
Total Standard Deviation in ln(k): 9.295179254367037
""",
)

entry(
    index = 475,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-5R!H-inRing_Int-3C-1C",
    kinetics = ArrheniusBM(A=(3.25992e+11,'s^-1'), n=0.252711, w0=(411000,'J/mol'), E0=(155506,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.613511771468569e-15, var=0.04652630173414255, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-5R!H-inRing_Int-3C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-5R!H-inRing_Int-3C-1C
    Total Standard Deviation in ln(k): 0.4324204813131864"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-5R!H-inRing_Int-3C-1C
Total Standard Deviation in ln(k): 0.4324204813131864""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-5R!H-inRing_Int-3C-1C
Total Standard Deviation in ln(k): 0.4324204813131864
""",
)

entry(
    index = 476,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-5R!H-inRing_Int-4R!H-3C_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(1.08913e+09,'s^-1'), n=1.087, w0=(411000,'J/mol'), E0=(158499,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004191729052989848, var=1.4144626816979218, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-5R!H-inRing_Int-4R!H-3C_Sp-4R!H-3C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-5R!H-inRing_Int-4R!H-3C_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 2.394787170539091"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-5R!H-inRing_Int-4R!H-3C_Sp-4R!H-3C
Total Standard Deviation in ln(k): 2.394787170539091""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-5R!H-inRing_Int-4R!H-3C_Sp-4R!H-3C
Total Standard Deviation in ln(k): 2.394787170539091
""",
)

entry(
    index = 477,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-5R!H-inRing_Int-4R!H-3C_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(6.91564e+06,'s^-1'), n=1.59524, w0=(411000,'J/mol'), E0=(231480,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.4443686672721673e-15, var=14.146175741074925, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-5R!H-inRing_Int-4R!H-3C_N-Sp-4R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-5R!H-inRing_Int-4R!H-3C_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 7.540089726453592"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-5R!H-inRing_Int-4R!H-3C_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 7.540089726453592""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-5R!H-inRing_Int-4R!H-3C_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 7.540089726453592
""",
)

entry(
    index = 478,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-3C-1C_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(3.38e+09,'s^-1'), n=0.88, w0=(411000,'J/mol'), E0=(158983,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7208456881684118e-15, var=2.315855261671823e-27, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-3C-1C_Sp-3C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-3C-1C_Sp-3C-1C
    Total Standard Deviation in ln(k): 1.0079826831244498e-13"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-3C-1C_Sp-3C-1C
Total Standard Deviation in ln(k): 1.0079826831244498e-13""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-3C-1C_Sp-3C-1C
Total Standard Deviation in ln(k): 1.0079826831244498e-13
""",
)

entry(
    index = 479,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-3C-1C_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(3.94e+11,'s^-1'), n=0.69, w0=(411000,'J/mol'), E0=(186595,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7208456881694482e-15, var=1.817147258152429e-27, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-3C-1C_N-Sp-3C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-3C-1C_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 8.978160031908413e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-3C-1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 8.978160031908413e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_5R!H->C_4R!H->C_Int-3C-1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 8.978160031908413e-14
""",
)

entry(
    index = 480,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_N-3C-inRing_Ext-3C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.28587e+12,'s^-1'), n=0.404023, w0=(411000,'J/mol'), E0=(145985,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_N-3C-inRing_Ext-3C-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_N-3C-inRing_Ext-3C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_N-3C-inRing_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Sp-4R!H-3C_N-3C-inRing_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 481,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_3C-inRing_Ext-5C-R_Sp-6R!H-5C",
    kinetics = ArrheniusBM(A=(2.58962e+08,'s^-1'), n=1.45508, w0=(411000,'J/mol'), E0=(161666,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.001297720149276119, var=2.2126810094368476, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_3C-inRing_Ext-5C-R_Sp-6R!H-5C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_3C-inRing_Ext-5C-R_Sp-6R!H-5C
    Total Standard Deviation in ln(k): 2.9853207153744834"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_3C-inRing_Ext-5C-R_Sp-6R!H-5C
Total Standard Deviation in ln(k): 2.9853207153744834""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_3C-inRing_Ext-5C-R_Sp-6R!H-5C
Total Standard Deviation in ln(k): 2.9853207153744834
""",
)

entry(
    index = 482,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_3C-inRing_Ext-5C-R_N-Sp-6R!H-5C",
    kinetics = ArrheniusBM(A=(3.25145e-09,'s^-1'), n=6.37271, w0=(411000,'J/mol'), E0=(107834,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_3C-inRing_Ext-5C-R_N-Sp-6R!H-5C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_3C-inRing_Ext-5C-R_N-Sp-6R!H-5C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_3C-inRing_Ext-5C-R_N-Sp-6R!H-5C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_3C-inRing_Ext-5C-R_N-Sp-6R!H-5C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 483,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing",
    kinetics = ArrheniusBM(A=(3.35254e-67,'s^-1'), n=23.3815, w0=(411000,'J/mol'), E0=(-27214,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.9306193967260232, var=17.642413064894647, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing
    Total Standard Deviation in ln(k): 13.271265709202963"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing
Total Standard Deviation in ln(k): 13.271265709202963""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing
Total Standard Deviation in ln(k): 13.271265709202963
""",
)

entry(
    index = 484,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_N-5C-inRing",
    kinetics = ArrheniusBM(A=(1.33035e+06,'s^-1'), n=2.00913, w0=(411000,'J/mol'), E0=(149864,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03263007960912512, var=0.020244507617540326, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_N-5C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_N-5C-inRing
    Total Standard Deviation in ln(k): 0.36722523685489"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_N-5C-inRing
Total Standard Deviation in ln(k): 0.36722523685489""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_N-5C-inRing
Total Standard Deviation in ln(k): 0.36722523685489
""",
)

entry(
    index = 485,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.89182e+09,'s^-1'), n=0.851578, w0=(435000,'J/mol'), E0=(90815.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05162258252714722, var=3.073155100171579, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.6440891111593436"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.6440891111593436""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.6440891111593436
""",
)

entry(
    index = 486,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_4R!H->C",
    kinetics = ArrheniusBM(A=(2.09575e+08,'s^-1'), n=0.892458, w0=(435000,'J/mol'), E0=(83819.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.19990112223702483, var=6.014203472047712, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_4R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_4R!H->C
    Total Standard Deviation in ln(k): 5.418650971052994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_4R!H->C
Total Standard Deviation in ln(k): 5.418650971052994""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_4R!H->C
Total Standard Deviation in ln(k): 5.418650971052994
""",
)

entry(
    index = 487,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(2.12119e+10,'s^-1'), n=0.510507, w0=(435000,'J/mol'), E0=(96880.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0013942797843650562, var=0.15272136300835765, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_N-4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_N-4R!H->C
    Total Standard Deviation in ln(k): 0.7869452785445528"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_N-4R!H->C
Total Standard Deviation in ln(k): 0.7869452785445528""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_N-4R!H->C
Total Standard Deviation in ln(k): 0.7869452785445528
""",
)

entry(
    index = 488,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_N-6R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(8.91132e+07,'s^-1'), n=1.29797, w0=(435000,'J/mol'), E0=(97020.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0002633686412902341, var=0.2217599814183539, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_N-6R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_N-6R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.944719514738255"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_N-6R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.944719514738255""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_N-6R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.944719514738255
""",
)

entry(
    index = 489,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_N-6R!H->C_Ext-6O-R",
    kinetics = ArrheniusBM(A=(2.47e+12,'s^-1'), n=-0.24, w0=(435000,'J/mol'), E0=(100282,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_N-6R!H->C_Ext-6O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_N-6R!H->C_Ext-6O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_N-6R!H->C_Ext-6O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_N-6R!H->C_Ext-6O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 490,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C_Ext-5R!H-R_6R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.62e+07,'s^-1'), n=1.2, w0=(435000,'J/mol'), E0=(94919.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C_Ext-5R!H-R_6R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C_Ext-5R!H-R_6R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C_Ext-5R!H-R_6R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_N-4R!H->C_Ext-5R!H-R_6R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 491,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.25e+10,'s^-1'), n=0, w0=(435000,'J/mol'), E0=(99085.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_4R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 492,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.17707e+06,'s^-1'), n=1.80857, w0=(435000,'J/mol'), E0=(48438.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15977815089226846, var=6.648386088689768, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 5.570554681275905"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.570554681275905""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.570554681275905
""",
)

entry(
    index = 493,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(6.5,'s^-1'), n=3.6, w0=(435000,'J/mol'), E0=(49937.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 494,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(20753.2,'s^-1'), n=2.15247, w0=(435000,'J/mol'), E0=(62835.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0007691219014401321, var=4.7133517178175355, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 4.35426343908661"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 4.35426343908661""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 4.35426343908661
""",
)

entry(
    index = 495,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.70094e+07,'s^-1'), n=1.30807, w0=(435000,'J/mol'), E0=(46470.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.7669268262994082, var=11.417499319059575, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 8.700909622143477"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 8.700909622143477""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 8.700909622143477
""",
)

entry(
    index = 496,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(8.94e+06,'s^-1'), n=1.26, w0=(435000,'J/mol'), E0=(51686.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 497,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(11500,'s^-1'), n=2.11, w0=(435000,'J/mol'), E0=(43971.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 498,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-6R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.09e+08,'s^-1'), n=1.23, w0=(435000,'J/mol'), E0=(57505.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-6R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-6R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 499,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(4.35e+07,'s^-1'), n=1.12, w0=(435000,'J/mol'), E0=(49413.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 500,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(22479.4,'s^-1'), n=1.59681, w0=(435000,'J/mol'), E0=(35748.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.7873620788870184, var=11.8917690567062, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 8.891514212206443"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 8.891514212206443""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 8.891514212206443
""",
)

entry(
    index = 501,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(1.37e+06,'s^-1'), n=0.99, w0=(435000,'J/mol'), E0=(51686.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 502,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(933000,'s^-1'), n=0.75, w0=(435000,'J/mol'), E0=(32161.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 503,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.3078e+09,'s^-1'), n=0.69951, w0=(435000,'J/mol'), E0=(91019.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10478915279499133, var=5.711145760429147, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 5.054205938196556"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 5.054205938196556""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 5.054205938196556
""",
)

entry(
    index = 504,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(9.93106e+09,'s^-1'), n=0.146064, w0=(435000,'J/mol'), E0=(95651.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0027614883126703305, var=0.5181940448683321, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.450060914060106"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.450060914060106""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.450060914060106
""",
)

entry(
    index = 505,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_N-6R!H->C_Ext-5R!H-R_Ext-6BrClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(5.10157e+08,'s^-1'), n=0.92435, w0=(435000,'J/mol'), E0=(102117,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_N-6R!H->C_Ext-5R!H-R_Ext-6BrClFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_N-6R!H->C_Ext-5R!H-R_Ext-6BrClFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_N-6R!H->C_Ext-5R!H-R_Ext-6BrClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_N-6R!H->C_Ext-5R!H-R_Ext-6BrClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 506,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(44508.2,'s^-1'), n=2.19368, w0=(435000,'J/mol'), E0=(45731,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0010284309826246016, var=7.516970129282439, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 5.49898489222274"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 5.49898489222274""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 5.49898489222274
""",
)

entry(
    index = 507,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_7R!H->O",
    kinetics = ArrheniusBM(A=(132961,'s^-1'), n=1.65696, w0=(435000,'J/mol'), E0=(50125.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00023367146018175242, var=0.011593116541485137, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_7R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_7R!H->O
    Total Standard Deviation in ln(k): 0.21643961782291352"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_7R!H->O
Total Standard Deviation in ln(k): 0.21643961782291352""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_7R!H->O
Total Standard Deviation in ln(k): 0.21643961782291352
""",
)

entry(
    index = 508,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(4.13413e+07,'s^-1'), n=1.16024, w0=(435000,'J/mol'), E0=(44855.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_N-7R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_N-7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_N-7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_N-7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 509,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.71181e+06,'s^-1'), n=1.50023, w0=(435000,'J/mol'), E0=(67482.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 510,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-5R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(7.03969e+09,'s^-1'), n=0.0773087, w0=(435000,'J/mol'), E0=(54283.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-5R!H-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-5R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-5R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-5R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 511,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-5R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.89917e+11,'s^-1'), n=0.0387625, w0=(435000,'J/mol'), E0=(53285.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-5R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-5R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-5R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-5R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 512,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_9R!H->O",
    kinetics = ArrheniusBM(A=(3.73509e+08,'s^-1'), n=0.320434, w0=(435000,'J/mol'), E0=(41533.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_9R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_9R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 513,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-9R!H->O",
    kinetics = ArrheniusBM(A=(73200.4,'s^-1'), n=1.10024, w0=(435000,'J/mol'), E0=(40090.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-9R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-9R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Ext-3R!H-R_N-9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 514,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_7R!H-inRing_3C-inRing_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.13932e+09,'s^-1'), n=1.20089, w0=(411000,'J/mol'), E0=(231781,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-7.018340492305214e-15, var=0.019046942239972563, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_7R!H-inRing_3C-inRing_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_7R!H-inRing_3C-inRing_Ext-6R!H-R
    Total Standard Deviation in ln(k): 0.2766748109118395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_7R!H-inRing_3C-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.2766748109118395""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_Sp-4R!H=1C_4R!H-inRing_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_1C-inRing_N-Sp-7R!H=6R!H_7R!H-inRing_3C-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.2766748109118395
""",
)

entry(
    index = 515,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing",
    kinetics = ArrheniusBM(A=(618577,'s^-1'), n=1.98573, w0=(411000,'J/mol'), E0=(126266,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0021115886394793746, var=1.8689466008317932, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing
    Total Standard Deviation in ln(k): 2.7459672319795048"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing
Total Standard Deviation in ln(k): 2.7459672319795048""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing
Total Standard Deviation in ln(k): 2.7459672319795048
""",
)

entry(
    index = 516,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_N-3C-inRing",
    kinetics = ArrheniusBM(A=(24735,'s^-1'), n=2.344, w0=(411000,'J/mol'), E0=(161467,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_N-3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_N-3C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_N-3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_N-3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 517,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(6.3014e+06,'s^-1'), n=1.32476, w0=(411000,'J/mol'), E0=(92394.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.047224414236382135, var=2.38878281659555, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C',), comment="""BM rule fitted to 15 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 3.217110230847089"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C
Total Standard Deviation in ln(k): 3.217110230847089""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C
Total Standard Deviation in ln(k): 3.217110230847089
""",
)

entry(
    index = 518,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1.85524e+09,'s^-1'), n=0.890233, w0=(411000,'J/mol'), E0=(95123.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0625607746517324, var=2.338047709925661, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 3.2225633193119902"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 3.2225633193119902""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 3.2225633193119902
""",
)

entry(
    index = 519,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3752.29,'s^-1'), n=2.28338, w0=(411000,'J/mol'), E0=(109908,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 520,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.15671e+08,'s^-1'), n=1.2891, w0=(411000,'J/mol'), E0=(114758,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 521,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C_Ext-6C-R",
    kinetics = ArrheniusBM(A=(1.46438e+07,'s^-1'), n=1.26829, w0=(411000,'J/mol'), E0=(87422.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006559368294255823, var=0.7767287925551758, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C_Ext-6C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C_Ext-6C-R
    Total Standard Deviation in ln(k): 1.7832983222297971"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C_Ext-6C-R
Total Standard Deviation in ln(k): 1.7832983222297971""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C_Ext-6C-R
Total Standard Deviation in ln(k): 1.7832983222297971
""",
)

entry(
    index = 522,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.57202e+10,'s^-1'), n=-0.0259023, w0=(411000,'J/mol'), E0=(418161,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.401314058931265e-15, var=0.48294555011136037, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 1.3931762870416098"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.3931762870416098""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.3931762870416098
""",
)

entry(
    index = 523,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R_Ext-6R!H-R_7R!H-inRing",
    kinetics = ArrheniusBM(A=(1.04e+07,'s^-1'), n=1.61, w0=(411000,'J/mol'), E0=(151400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R_Ext-6R!H-R_7R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R_Ext-6R!H-R_7R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R_Ext-6R!H-R_7R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R_Ext-6R!H-R_7R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 524,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R_Ext-6R!H-R_N-7R!H-inRing",
    kinetics = ArrheniusBM(A=(128000,'s^-1'), n=2, w0=(411000,'J/mol'), E0=(147528,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R_Ext-6R!H-R_N-7R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R_Ext-6R!H-R_N-7R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R_Ext-6R!H-R_N-7R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R_Ext-6R!H-R_N-7R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 525,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-3C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.54363e+07,'s^-1'), n=1.62399, w0=(411000,'J/mol'), E0=(150363,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0009818960175137581, var=0.0054867737739806, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-3C-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-3C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 0.15096333567178524"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-3C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.15096333567178524""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-3C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.15096333567178524
""",
)

entry(
    index = 526,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-1C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.40582e+10,'s^-1'), n=0.940067, w0=(411000,'J/mol'), E0=(192059,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0021644521473662337, var=2.712658968639844, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 3.3072674053219004"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.3072674053219004""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.3072674053219004
""",
)

entry(
    index = 527,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.56723e+10,'s^-1'), n=0.884056, w0=(411000,'J/mol'), E0=(199695,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7573309526898815e-15, var=11.75897897194934, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 6.8745107634945875"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.8745107634945875""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.8745107634945875
""",
)

entry(
    index = 528,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-6R!H-R_Int-7R!H-5R!H",
    kinetics = ArrheniusBM(A=(4.51075e+07,'s^-1'), n=1.46272, w0=(411000,'J/mol'), E0=(161609,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0033074109246061527, var=12.873581574538184, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-6R!H-R_Int-7R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-6R!H-R_Int-7R!H-5R!H
    Total Standard Deviation in ln(k): 7.2012541589899675"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-6R!H-R_Int-7R!H-5R!H
Total Standard Deviation in ln(k): 7.2012541589899675""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-6R!H-R_Int-7R!H-5R!H
Total Standard Deviation in ln(k): 7.2012541589899675
""",
)

entry(
    index = 529,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.23667e-49,'s^-1'), n=17.8443, w0=(411000,'J/mol'), E0=(18190.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09583294611784136, var=78.56329516354802, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-3C-R
    Total Standard Deviation in ln(k): 18.009943712094454"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 18.009943712094454""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 18.009943712094454
""",
)

entry(
    index = 530,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_N-3C-inRing_Ext-6R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(117.456,'s^-1'), n=2.87512, w0=(411000,'J/mol'), E0=(144934,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_N-3C-inRing_Ext-6R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_N-3C-inRing_Ext-6R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_N-3C-inRing_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_N-3C-inRing_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 531,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_N-3C-inRing_Ext-6R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(164917,'s^-1'), n=2.26924, w0=(411000,'J/mol'), E0=(153423,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_N-3C-inRing_Ext-6R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_N-3C-inRing_Ext-6R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_N-3C-inRing_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_N-3C-inRing_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 532,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_N-3C-inRing_Ext-6R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2222.25,'s^-1'), n=2.55411, w0=(411000,'J/mol'), E0=(145224,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_N-3C-inRing_Ext-6R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_N-3C-inRing_Ext-6R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_N-3C-inRing_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_N-3C-inRing_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 533,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H_N-1C-inRing_Ext-3C-R_Int-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(285000,'s^-1'), n=2.15, w0=(411000,'J/mol'), E0=(151392,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H_N-1C-inRing_Ext-3C-R_Int-7R!H-6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H_N-1C-inRing_Ext-3C-R_Int-7R!H-6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H_N-1C-inRing_Ext-3C-R_Int-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H_N-1C-inRing_Ext-3C-R_Int-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 534,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H_N-1C-inRing_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(671000,'s^-1'), n=2.07, w0=(411000,'J/mol'), E0=(149443,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H_N-1C-inRing_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H_N-1C-inRing_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H_N-1C-inRing_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_Sp-6R!H=5R!H_N-1C-inRing_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 535,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(9.80751e+07,'s^-1'), n=1.63474, w0=(411000,'J/mol'), E0=(159676,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1266693711798032, var=48.968538774594336, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing_Sp-4R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 14.346904468509761"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing_Sp-4R!H-3C
Total Standard Deviation in ln(k): 14.346904468509761""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing_Sp-4R!H-3C
Total Standard Deviation in ln(k): 14.346904468509761
""",
)

entry(
    index = 536,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(4.712e+10,'s^-1'), n=0.722, w0=(411000,'J/mol'), E0=(221506,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 537,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Int-8R!H-4R!H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.07e+06,'s^-1'), n=2, w0=(411000,'J/mol'), E0=(111008,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Int-8R!H-4R!H_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Int-8R!H-4R!H_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Int-8R!H-4R!H_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Int-8R!H-4R!H_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 538,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing",
    kinetics = ArrheniusBM(A=(22641.8,'s^-1'), n=2.33409, w0=(411000,'J/mol'), E0=(150962,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04213744117615937, var=9.096989882916835, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing
    Total Standard Deviation in ln(k): 6.152397862253132"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing
Total Standard Deviation in ln(k): 6.152397862253132""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing
Total Standard Deviation in ln(k): 6.152397862253132
""",
)

entry(
    index = 539,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing",
    kinetics = ArrheniusBM(A=(2.37238e-48,'s^-1'), n=17.4435, w0=(411000,'J/mol'), E0=(-3446.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2580245936116772, var=13.316090013866273, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing
    Total Standard Deviation in ln(k): 7.96382550135938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing
Total Standard Deviation in ln(k): 7.96382550135938""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing
Total Standard Deviation in ln(k): 7.96382550135938
""",
)

entry(
    index = 540,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C",
    kinetics = ArrheniusBM(A=(5.2838e+06,'s^-1'), n=2.09796, w0=(411000,'J/mol'), E0=(139966,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02035235708232669, var=22.253579863746697, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C
    Total Standard Deviation in ln(k): 9.508213718833135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C
Total Standard Deviation in ln(k): 9.508213718833135""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C
Total Standard Deviation in ln(k): 9.508213718833135
""",
)

entry(
    index = 541,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-7R!H-3C",
    kinetics = ArrheniusBM(A=(1.91935e-73,'s^-1'), n=25.1665, w0=(411000,'J/mol'), E0=(41100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.34272407984715, var=1.3709965656569216, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-7R!H-3C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-7R!H-3C
    Total Standard Deviation in ln(k): 5.721014124852617"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-7R!H-3C
Total Standard Deviation in ln(k): 5.721014124852617""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-7R!H-3C
Total Standard Deviation in ln(k): 5.721014124852617
""",
)

entry(
    index = 542,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Int-3C-1C_Sp-7R!H-3C",
    kinetics = ArrheniusBM(A=(2.88e+09,'s^-1'), n=1, w0=(411000,'J/mol'), E0=(117659,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Int-3C-1C_Sp-7R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Int-3C-1C_Sp-7R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Int-3C-1C_Sp-7R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Int-3C-1C_Sp-7R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 543,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Int-3C-1C_N-Sp-7R!H-3C",
    kinetics = ArrheniusBM(A=(82.632,'s^-1'), n=3.17395, w0=(411000,'J/mol'), E0=(133079,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.70965546825602, var=474.5856429269174, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Int-3C-1C_N-Sp-7R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Int-3C-1C_N-Sp-7R!H-3C
    Total Standard Deviation in ln(k): 55.50643207540319"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Int-3C-1C_N-Sp-7R!H-3C
Total Standard Deviation in ln(k): 55.50643207540319""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Int-3C-1C_N-Sp-7R!H-3C
Total Standard Deviation in ln(k): 55.50643207540319
""",
)

entry(
    index = 544,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_N-6R!H-inRing_1C-inRing_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(4.40375e+12,'s^-1'), n=0.00413218, w0=(411000,'J/mol'), E0=(184812,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.0385039051202625e-14, var=42.128693128565445, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_N-6R!H-inRing_1C-inRing_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_N-6R!H-inRing_1C-inRing_Ext-6R!H-R
    Total Standard Deviation in ln(k): 13.0120577761486"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_N-6R!H-inRing_1C-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 13.0120577761486""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_N-6R!H-inRing_1C-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 13.0120577761486
""",
)

entry(
    index = 545,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_Sp-6R!H-3C_Ext-6R!H-R_Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(23841.2,'s^-1'), n=2.22888, w0=(411000,'J/mol'), E0=(149786,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_Sp-6R!H-3C_Ext-6R!H-R_Sp-7R!H-6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_Sp-6R!H-3C_Ext-6R!H-R_Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_Sp-6R!H-3C_Ext-6R!H-R_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_Sp-6R!H-3C_Ext-6R!H-R_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 546,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_Sp-6R!H-3C_Ext-6R!H-R_N-Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(5789.48,'s^-1'), n=2.76434, w0=(411000,'J/mol'), E0=(101649,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.603505247954606, var=120.38251036030431, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_Sp-6R!H-3C_Ext-6R!H-R_N-Sp-7R!H-6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_Sp-6R!H-3C_Ext-6R!H-R_N-Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 31.04977884190776"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_Sp-6R!H-3C_Ext-6R!H-R_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 31.04977884190776""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_Sp-6R!H-3C_Ext-6R!H-R_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 31.04977884190776
""",
)

entry(
    index = 547,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_N-Sp-6R!H-3C_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5.67818e+12,'s^-1'), n=-0.028334, w0=(411000,'J/mol'), E0=(184724,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.511304619313298e-14, var=54.648543568104195, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_N-Sp-6R!H-3C_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_N-Sp-6R!H-3C_Ext-6R!H-R
    Total Standard Deviation in ln(k): 14.819934543654394"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_N-Sp-6R!H-3C_Ext-6R!H-R
Total Standard Deviation in ln(k): 14.819934543654394""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_N-Sp-6R!H-3C_Ext-6R!H-R
Total Standard Deviation in ln(k): 14.819934543654394
""",
)

entry(
    index = 548,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_N-Sp-6R!H-3C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.62317e+11,'s^-1'), n=0.503152, w0=(411000,'J/mol'), E0=(181761,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.020236161337455493, var=19.598041102897348, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_N-Sp-6R!H-3C_Ext-4R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_N-Sp-6R!H-3C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 8.925741627795357"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_N-Sp-6R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 8.925741627795357""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_N-Sp-6R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 8.925741627795357
""",
)

entry(
    index = 549,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R_Ext-3C-R_Sp-7R!H-3C",
    kinetics = ArrheniusBM(A=(1.0952e+07,'s^-1'), n=1.23522, w0=(411000,'J/mol'), E0=(153265,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0012541097291014006, var=8.41748768955221, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R_Ext-3C-R_Sp-7R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R_Ext-3C-R_Sp-7R!H-3C
    Total Standard Deviation in ln(k): 5.819470252917437"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R_Ext-3C-R_Sp-7R!H-3C
Total Standard Deviation in ln(k): 5.819470252917437""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R_Ext-3C-R_Sp-7R!H-3C
Total Standard Deviation in ln(k): 5.819470252917437
""",
)

entry(
    index = 550,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R_Ext-3C-R_N-Sp-7R!H-3C",
    kinetics = ArrheniusBM(A=(152073,'s^-1'), n=2.09033, w0=(411000,'J/mol'), E0=(170622,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R_Ext-3C-R_N-Sp-7R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R_Ext-3C-R_N-Sp-7R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R_Ext-3C-R_N-Sp-7R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R_Ext-3C-R_N-Sp-7R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 551,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_1C-inRing_Ext-6R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.181e+10,'s^-1'), n=0.964, w0=(411000,'J/mol'), E0=(135202,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_1C-inRing_Ext-6R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_1C-inRing_Ext-6R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_1C-inRing_Ext-6R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_1C-inRing_Ext-6R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 552,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_N-1C-inRing_Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(6.06221e+08,'s^-1'), n=0.885894, w0=(411000,'J/mol'), E0=(157062,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.5700965183089515e-15, var=0.046526301734191, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_N-1C-inRing_Sp-6R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_N-1C-inRing_Sp-6R!H-3C
    Total Standard Deviation in ln(k): 0.43242048131340893"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_N-1C-inRing_Sp-6R!H-3C
Total Standard Deviation in ln(k): 0.43242048131340893""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_N-1C-inRing_Sp-6R!H-3C
Total Standard Deviation in ln(k): 0.43242048131340893
""",
)

entry(
    index = 553,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_N-1C-inRing_N-Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(4.38577e+07,'s^-1'), n=1.43278, w0=(411000,'J/mol'), E0=(199892,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.441011381205703e-14, var=29.110037171840368, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_N-1C-inRing_N-Sp-6R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_N-1C-inRing_N-Sp-6R!H-3C
    Total Standard Deviation in ln(k): 10.816291160934052"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_N-1C-inRing_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 10.816291160934052""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-3C-R_N-1C-inRing_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 10.816291160934052
""",
)

entry(
    index = 554,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1C-R_Ext-6R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(28.4,'s^-1'), n=2.07, w0=(411000,'J/mol'), E0=(69827,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1C-R_Ext-6R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1C-R_Ext-6R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1C-R_Ext-6R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-3C-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1C-R_Ext-6R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 555,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Ext-3C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.30422e+09,'s^-1'), n=1.27157, w0=(411000,'J/mol'), E0=(147532,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Ext-3C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Ext-3C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 556,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.72106e-70,'s^-1'), n=24.4429, w0=(411000,'J/mol'), E0=(-28505,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.9988295955631914, var=26.39774699633116, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_Ext-3C-R
    Total Standard Deviation in ln(k): 17.834823520875243"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 17.834823520875243""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 17.834823520875243
""",
)

entry(
    index = 557,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(4.90973e+11,'s^-1'), n=0.582521, w0=(411000,'J/mol'), E0=(248014,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02185743445490992, var=0.7179884341357717, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 1.753614370503277"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 1.753614370503277""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 1.753614370503277
""",
)

entry(
    index = 558,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(2.02311e+10,'s^-1'), n=0.929813, w0=(411000,'J/mol'), E0=(135495,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 559,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Sp-6R!H-3C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.21315e+08,'s^-1'), n=1.47871, w0=(411000,'J/mol'), E0=(154609,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00020216210216620397, var=0.5537807581836116, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Sp-6R!H-3C_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Sp-6R!H-3C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 1.49236056103428"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Sp-6R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.49236056103428""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Sp-6R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 1.49236056103428
""",
)

entry(
    index = 560,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Sp-6R!H-3C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000554079,'s^-1'), n=5.38744, w0=(411000,'J/mol'), E0=(135491,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Sp-6R!H-3C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Sp-6R!H-3C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Sp-6R!H-3C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Sp-6R!H-3C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 561,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C_Sp-3C-=1C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.40059e+08,'s^-1'), n=1.58026, w0=(411000,'J/mol'), E0=(239019,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C_Sp-3C-=1C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C_Sp-3C-=1C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C_Sp-3C-=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C_Sp-3C-=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 562,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C_N-Sp-3C-=1C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.231e+11,'s^-1'), n=0.765, w0=(411000,'J/mol'), E0=(233711,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C_N-Sp-3C-=1C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C_N-Sp-3C-=1C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C_N-Sp-3C-=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C_N-Sp-3C-=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 563,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.91768e+09,'s^-1'), n=1.07853, w0=(411000,'J/mol'), E0=(127792,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11805573244850995, var=74.84630370870173, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 17.640339032452758"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 17.640339032452758""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 17.640339032452758
""",
)

entry(
    index = 564,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.849155,'s^-1'), n=3.67649, w0=(411000,'J/mol'), E0=(141349,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13050063136328505, var=5.768054059829054, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R',), comment="""BM rule fitted to 25 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R
    Total Standard Deviation in ln(k): 5.1426178476498645"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 5.1426178476498645""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 5.1426178476498645
""",
)

entry(
    index = 565,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(184613,'s^-1'), n=2.19389, w0=(411000,'J/mol'), E0=(147367,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.003506575944600556, var=1.291884532466765, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C',), comment="""BM rule fitted to 7 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C
    Total Standard Deviation in ln(k): 2.287414404401271"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C
Total Standard Deviation in ln(k): 2.287414404401271""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C
Total Standard Deviation in ln(k): 2.287414404401271
""",
)

entry(
    index = 566,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(1.08e+06,'s^-1'), n=1.99, w0=(411000,'J/mol'), E0=(110691,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 567,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-1C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.59487e+08,'s^-1'), n=1.00235, w0=(411000,'J/mol'), E0=(110372,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00654234359572215, var=142.9699562847935, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 23.98706436342942"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 23.98706436342942""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 23.98706436342942
""",
)

entry(
    index = 568,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(9.21713e+09,'s^-1'), n=0.875003, w0=(411000,'J/mol'), E0=(173626,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=96.32222815302424, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 19.675249555445085"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 19.675249555445085""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 19.675249555445085
""",
)

entry(
    index = 569,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_N-Sp-4R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.84076e+09,'s^-1'), n=0.461313, w0=(411000,'J/mol'), E0=(61840.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_N-Sp-4R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H-3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_N-Sp-4R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_N-Sp-4R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_N-Sp-4R!H-1C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 570,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(6.87616e+07,'s^-1'), n=0.504433, w0=(411000,'J/mol'), E0=(68179.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07973241677681306, var=4.775037228659855, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R',), comment="""BM rule fitted to 22 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R
    Total Standard Deviation in ln(k): 4.58105144317653"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R
Total Standard Deviation in ln(k): 4.58105144317653""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R
Total Standard Deviation in ln(k): 4.58105144317653
""",
)

entry(
    index = 571,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(8.38837e+07,'s^-1'), n=0.689149, w0=(411000,'J/mol'), E0=(58799.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03699656920643553, var=1.2806889016741412, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H',), comment="""BM rule fitted to 13 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 2.361665300689583"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 2.361665300689583""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 2.361665300689583
""",
)

entry(
    index = 572,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.74999e+07,'s^-1'), n=1.29598, w0=(411000,'J/mol'), E0=(83893.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 573,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_N-4R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(0.345261,'s^-1'), n=3.36394, w0=(411000,'J/mol'), E0=(53084.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_N-4R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_N-4R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_N-4R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_N-4R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 574,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_N-4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0282,'s^-1'), n=3.28, w0=(411000,'J/mol'), E0=(33221.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_N-4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_N-4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 575,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_N-4R!H->C_Ext-6R!H-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(409.402,'s^-1'), n=2.04131, w0=(411000,'J/mol'), E0=(52281.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_N-4R!H->C_Ext-6R!H-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_N-4R!H->C_Ext-6R!H-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_N-4R!H->C_Ext-6R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_N-4R!H->C_Ext-6R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 576,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C_Sp-5C-4R!H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(532000,'s^-1'), n=1.93, w0=(411000,'J/mol'), E0=(149234,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C_Sp-5C-4R!H_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C_Sp-5C-4R!H_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C_Sp-5C-4R!H_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C_Sp-5C-4R!H_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 577,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C_N-Sp-5C-4R!H_Ext-3C-R",
    kinetics = ArrheniusBM(A=(498215,'s^-1'), n=2.10017, w0=(411000,'J/mol'), E0=(145383,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C_N-Sp-5C-4R!H_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C_N-Sp-5C-4R!H_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C_N-Sp-5C-4R!H_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_5R!H->C_N-Sp-5C-4R!H_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 578,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.62e+13,'s^-1'), n=-0.14, w0=(411000,'J/mol'), E0=(156790,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 579,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Sp-6R!H=3C_Int-4C-3C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.5287e+08,'s^-1'), n=1.0301, w0=(411000,'J/mol'), E0=(152930,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-9.884986608880582e-16, var=0.04740494784920821, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Sp-6R!H=3C_Int-4C-3C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Sp-6R!H=3C_Int-4C-3C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.436484499895357"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Sp-6R!H=3C_Int-4C-3C_Ext-1C-R
Total Standard Deviation in ln(k): 0.436484499895357""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_Sp-6R!H=3C_Int-4C-3C_Ext-1C-R
Total Standard Deviation in ln(k): 0.436484499895357
""",
)

entry(
    index = 580,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_Sp-4C-3C",
    kinetics = ArrheniusBM(A=(4.57736e+08,'s^-1'), n=1.02185, w0=(411000,'J/mol'), E0=(148917,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0009856626350043158, var=0.46721747170259353, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_Sp-4C-3C',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_Sp-4C-3C
    Total Standard Deviation in ln(k): 1.3727792816833113"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_Sp-4C-3C
Total Standard Deviation in ln(k): 1.3727792816833113""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_Sp-4C-3C
Total Standard Deviation in ln(k): 1.3727792816833113
""",
)

entry(
    index = 581,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_N-Sp-4C-3C",
    kinetics = ArrheniusBM(A=(2.1555e+08,'s^-1'), n=1.1784, w0=(411000,'J/mol'), E0=(198647,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.54980852443356e-14, var=19.92934995607649, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_N-Sp-4C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_N-Sp-4C-3C
    Total Standard Deviation in ln(k): 8.949598578553772"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 8.949598578553772""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 8.949598578553772
""",
)

entry(
    index = 582,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-3C-1C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.28e+10,'s^-1'), n=0.97, w0=(411000,'J/mol'), E0=(161075,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.887379141862762e-15, var=8.899337087024507e-30, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-3C-1C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-3C-1C_Ext-3C-R
    Total Standard Deviation in ln(k): 1.0722635558579567e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-3C-1C_Ext-3C-R
Total Standard Deviation in ln(k): 1.0722635558579567e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-3C-1C_Ext-3C-R
Total Standard Deviation in ln(k): 1.0722635558579567e-14
""",
)

entry(
    index = 583,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_5R!H-inRing_Int-3C-1C_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(3.74786e-10,'s^-1'), n=6.48235, w0=(411000,'J/mol'), E0=(128712,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_5R!H-inRing_Int-3C-1C_Sp-3C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_5R!H-inRing_Int-3C-1C_Sp-3C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_5R!H-inRing_Int-3C-1C_Sp-3C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_5R!H-inRing_Int-3C-1C_Sp-3C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 584,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_5R!H-inRing_Int-3C-1C_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(1.90656e+11,'s^-1'), n=0.510047, w0=(411000,'J/mol'), E0=(209541,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_5R!H-inRing_Int-3C-1C_N-Sp-3C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_5R!H-inRing_Int-3C-1C_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_5R!H-inRing_Int-3C-1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-3C-R_Sp-5R!H-3C_Ext-5R!H-R_N-Sp-6R!H-5R!H_5R!H-inRing_Int-3C-1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 585,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_3C-inRing_Ext-5C-R_Sp-6R!H-5C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.17102e+08,'s^-1'), n=1.45512, w0=(411000,'J/mol'), E0=(159782,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7573309526898815e-15, var=10.175067115382197, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_3C-inRing_Ext-5C-R_Sp-6R!H-5C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_3C-inRing_Ext-5C-R_Sp-6R!H-5C_Ext-3C-R
    Total Standard Deviation in ln(k): 6.394780333788482"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_3C-inRing_Ext-5C-R_Sp-6R!H-5C_Ext-3C-R
Total Standard Deviation in ln(k): 6.394780333788482""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_3C-inRing_Ext-5C-R_Sp-6R!H-5C_Ext-3C-R
Total Standard Deviation in ln(k): 6.394780333788482
""",
)

entry(
    index = 586,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing_4R!H-inRing",
    kinetics = ArrheniusBM(A=(5.97e+06,'s^-1'), n=1.8, w0=(411000,'J/mol'), E0=(151703,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing_4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing_4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 587,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(1.27241e-67,'s^-1'), n=23.4525, w0=(411000,'J/mol'), E0=(-4569.17,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.23169192593954088, var=81.81379442177378, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing_N-4R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing_N-4R!H-inRing
    Total Standard Deviation in ln(k): 18.71516537885166"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing_N-4R!H-inRing
Total Standard Deviation in ln(k): 18.71516537885166""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing_N-4R!H-inRing
Total Standard Deviation in ln(k): 18.71516537885166
""",
)

entry(
    index = 588,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.38869e+10,'s^-1'), n=0.522397, w0=(435000,'J/mol'), E0=(91405.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01994993785409357, var=1.6829828977561325, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 2.6508648941997475"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 2.6508648941997475""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 2.6508648941997475
""",
)

entry(
    index = 589,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.52743e+10,'s^-1'), n=0.827913, w0=(435000,'J/mol'), E0=(93509.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.009162488781956971, var=4.1163174868604155, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 4.090370166199508"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 4.090370166199508""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 4.090370166199508
""",
)

entry(
    index = 590,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_4R!H->C_Sp-5R!H-4C",
    kinetics = ArrheniusBM(A=(878968,'s^-1'), n=1.53692, w0=(435000,'J/mol'), E0=(70236.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08310491961582676, var=3.1218143740247366, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_4R!H->C_Sp-5R!H-4C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_4R!H->C_Sp-5R!H-4C
    Total Standard Deviation in ln(k): 3.7509039607495773"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_4R!H->C_Sp-5R!H-4C
Total Standard Deviation in ln(k): 3.7509039607495773""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_4R!H->C_Sp-5R!H-4C
Total Standard Deviation in ln(k): 3.7509039607495773
""",
)

entry(
    index = 591,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_4R!H->C_N-Sp-5R!H-4C",
    kinetics = ArrheniusBM(A=(1.11e+06,'s^-1'), n=1.78, w0=(435000,'J/mol'), E0=(112292,'J/mol'), Tmin=(600,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_4R!H->C_N-Sp-5R!H-4C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_4R!H->C_N-Sp-5R!H-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_4R!H->C_N-Sp-5R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_4R!H->C_N-Sp-5R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 592,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_N-4R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(6.14522e+10,'s^-1'), n=0.379781, w0=(435000,'J/mol'), E0=(97999.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.003144416846615619, var=0.5334584934303138, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_N-4R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_N-4R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.4721238213199468"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_N-4R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.4721238213199468""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_N-4R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.4721238213199468
""",
)

entry(
    index = 593,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_N-6R!H->C_Ext-5R!H-R_Ext-6O-R",
    kinetics = ArrheniusBM(A=(1.22e+07,'s^-1'), n=1.6, w0=(435000,'J/mol'), E0=(96387.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_N-6R!H->C_Ext-5R!H-R_Ext-6O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_N-6R!H->C_Ext-5R!H-R_Ext-6O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_N-6R!H->C_Ext-5R!H-R_Ext-6O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_N-6R!H->C_Ext-5R!H-R_Ext-6O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 594,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(136.53,'s^-1'), n=2.99293, w0=(435000,'J/mol'), E0=(53344.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7221843336360837e-15, var=9.999482891834894, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 6.339365036571209"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 6.339365036571209""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 6.339365036571209
""",
)

entry(
    index = 595,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.17e+11,'s^-1'), n=0.43, w0=(435000,'J/mol'), E0=(47200.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 596,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_7R!H->O",
    kinetics = ArrheniusBM(A=(1.9e+07,'s^-1'), n=1.1, w0=(435000,'J/mol'), E0=(47200.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_7R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 597,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(3.174e+08,'s^-1'), n=1.15, w0=(435000,'J/mol'), E0=(44910.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_N-7R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_N-7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_N-7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_N-7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 598,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-7R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5490,'s^-1'), n=2.4, w0=(435000,'J/mol'), E0=(59521.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-7R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-7R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-7R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-7R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 599,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(3.38e+10,'s^-1'), n=0.21, w0=(435000,'J/mol'), E0=(53130.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 600,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2.29e+08,'s^-1'), n=1.12, w0=(435000,'J/mol'), E0=(43577.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-5R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 601,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_Ext-1C-R_9R!H->O",
    kinetics = ArrheniusBM(A=(3.41e+06,'s^-1'), n=1.09, w0=(435000,'J/mol'), E0=(34583.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_Ext-1C-R_9R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_Ext-1C-R_9R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_Ext-1C-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_Ext-1C-R_9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 602,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_Ext-1C-R_N-9R!H->O",
    kinetics = ArrheniusBM(A=(562000,'s^-1'), n=1.09, w0=(435000,'J/mol'), E0=(40146,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_Ext-1C-R_N-9R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_Ext-1C-R_N-9R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_Ext-1C-R_N-9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_N-4R!H->C_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R_N-6R!H->O_Ext-1C-R_Ext-1C-R_N-9R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 603,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(8.65699e+09,'s^-1'), n=0.281375, w0=(435000,'J/mol'), E0=(93532.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.019597732862741822, var=1.2997893561465588, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_7R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 2.334805012131619"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_7R!H->C
Total Standard Deviation in ln(k): 2.334805012131619""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_7R!H->C
Total Standard Deviation in ln(k): 2.334805012131619
""",
)

entry(
    index = 604,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(7.9067e+10,'s^-1'), n=0.431321, w0=(435000,'J/mol'), E0=(93487.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.012850765338135934, var=4.6243732321940945, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_N-7R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 4.343342016613604"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 4.343342016613604""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 4.343342016613604
""",
)

entry(
    index = 605,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.68355e+10,'s^-1'), n=0.0361976, w0=(435000,'J/mol'), E0=(95601.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 606,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1794.19,'s^-1'), n=2.69445, w0=(435000,'J/mol'), E0=(55788.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 607,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_7R!H->O_Ext-7O-R",
    kinetics = ArrheniusBM(A=(593.62,'s^-1'), n=2.49445, w0=(435000,'J/mol'), E0=(53629.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_7R!H->O_Ext-7O-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_7R!H->O_Ext-7O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_7R!H->O_Ext-7O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Ext-5R!H-R_Sp-6R!H-5R!H_Int-6R!H-3R!H_Ext-3R!H-R_Ext-3R!H-R_7R!H->O_Ext-7O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 608,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing_Ext-3C-R",
    kinetics = ArrheniusBM(A=(980323,'s^-1'), n=1.78107, w0=(411000,'J/mol'), E0=(111525,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7573309526898815e-15, var=0.9834797825310088, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing_Ext-3C-R
    Total Standard Deviation in ln(k): 1.98810678592129"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 1.98810678592129""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 1.98810678592129
""",
)

entry(
    index = 609,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(198803,'s^-1'), n=2.23529, w0=(411000,'J/mol'), E0=(140765,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 610,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_1C-inRing",
    kinetics = ArrheniusBM(A=(37100,'s^-1'), n=2.23, w0=(411000,'J/mol'), E0=(98732,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 611,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing",
    kinetics = ArrheniusBM(A=(99.3065,'s^-1'), n=2.65624, w0=(411000,'J/mol'), E0=(79145.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0146072473611479, var=2.890821745273478, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing',), comment="""BM rule fitted to 14 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing
    Total Standard Deviation in ln(k): 3.445235747660449"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing
Total Standard Deviation in ln(k): 3.445235747660449""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing
Total Standard Deviation in ln(k): 3.445235747660449
""",
)

entry(
    index = 612,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(2.37817e-09,'s^-1'), n=6.13848, w0=(411000,'J/mol'), E0=(46502.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24026273523958191, var=0.7084680003344632, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C
    Total Standard Deviation in ln(k): 2.2910715781342654"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C
Total Standard Deviation in ln(k): 2.2910715781342654""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C
Total Standard Deviation in ln(k): 2.2910715781342654
""",
)

entry(
    index = 613,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_N-Sp-5R!H-3C",
    kinetics = ArrheniusBM(A=(6.95093e+06,'s^-1'), n=1.6539, w0=(411000,'J/mol'), E0=(99911.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.004052550976213612, var=5.404542780111745, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_N-Sp-5R!H-3C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_N-Sp-5R!H-3C
    Total Standard Deviation in ln(k): 4.670724747531616"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 4.670724747531616""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_N-Sp-5R!H-3C
Total Standard Deviation in ln(k): 4.670724747531616
""",
)

entry(
    index = 614,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1250.34,'s^-1'), n=2.37643, w0=(411000,'J/mol'), E0=(76078.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-3C-R_6R!H->C_Ext-6C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 615,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R_Ext-3C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1e+10,'s^-1'), n=0, w0=(411000,'J/mol'), E0=(417954,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R_Ext-3C-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R_Ext-3C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R_Ext-3C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-1C-R_Ext-3C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 616,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-3C-R_Ext-6R!H-R_7R!H-inRing",
    kinetics = ArrheniusBM(A=(8.25242e+06,'s^-1'), n=1.71899, w0=(411000,'J/mol'), E0=(150378,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-3C-R_Ext-6R!H-R_7R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-3C-R_Ext-6R!H-R_7R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-3C-R_Ext-6R!H-R_7R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-3C-R_Ext-6R!H-R_7R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 617,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-3C-R_Ext-6R!H-R_N-7R!H-inRing",
    kinetics = ArrheniusBM(A=(2.71516e+06,'s^-1'), n=1.84227, w0=(411000,'J/mol'), E0=(148618,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-3C-R_Ext-6R!H-R_N-7R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-3C-R_Ext-6R!H-R_N-7R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-3C-R_Ext-6R!H-R_N-7R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_N-Sp-5R!H-4R!H_Sp-5R!H-3C_N-1C-inRing_Ext-3C-R_Ext-6R!H-R_N-7R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 618,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-1C-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.76e+09,'s^-1'), n=1.18, w0=(411000,'J/mol'), E0=(183249,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-7.804117142251072e-32, var=3.94430452610506e-31, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-1C-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-1C-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 1.259047770670146e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-1C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.259047770670146e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_Sp-5R!H=4R!H_Ext-1C-R_N-1C-inRing_Ext-1C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.259047770670146e-15
""",
)

entry(
    index = 619,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-6R!H-R_Int-7R!H-5R!H_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.49673e+06,'s^-1'), n=1.74115, w0=(411000,'J/mol'), E0=(143020,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-6R!H-R_Int-7R!H-5R!H_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-6R!H-R_Int-7R!H-5R!H_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-6R!H-R_Int-7R!H-5R!H_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-6R!H-R_Int-7R!H-5R!H_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 620,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-3C-R_1C-inRing",
    kinetics = ArrheniusBM(A=(6.36e+06,'s^-1'), n=1.7, w0=(411000,'J/mol'), E0=(143419,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-3C-R_1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-3C-R_1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-3C-R_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-3C-R_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 621,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-3C-R_N-1C-inRing",
    kinetics = ArrheniusBM(A=(117270,'s^-1'), n=1.73674, w0=(411000,'J/mol'), E0=(165270,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-3C-R_N-1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-3C-R_N-1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-3C-R_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-1C-R_3C-inRing_Ext-3C-R_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 622,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing_Sp-4R!H-3C_1C-inRing",
    kinetics = ArrheniusBM(A=(2.401e+08,'s^-1'), n=1.453, w0=(411000,'J/mol'), E0=(178311,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing_Sp-4R!H-3C_1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing_Sp-4R!H-3C_1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing_Sp-4R!H-3C_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing_Sp-4R!H-3C_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 623,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing_Sp-4R!H-3C_N-1C-inRing",
    kinetics = ArrheniusBM(A=(3.73658e-14,'s^-1'), n=8.03514, w0=(411000,'J/mol'), E0=(96650,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing_Sp-4R!H-3C_N-1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing_Sp-4R!H-3C_N-1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing_Sp-4R!H-3C_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-4R!H-3C_N-Sp-5R!H=4R!H_Sp-4R!H-1C_Ext-5R!H-R_N-Sp-6R!H=5R!H_3C-inRing_Sp-4R!H-3C_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 624,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.78401e+06,'s^-1'), n=1.9781, w0=(411000,'J/mol'), E0=(167594,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013635815293742637, var=40.65239927684252, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-1C-R
    Total Standard Deviation in ln(k): 12.816298144865806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 12.816298144865806""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 12.816298144865806
""",
)

entry(
    index = 625,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(3.50188e+07,'s^-1'), n=1.09175, w0=(411000,'J/mol'), E0=(112351,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 626,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-8R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(235191,'s^-1'), n=2.1702, w0=(411000,'J/mol'), E0=(143968,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01755630473557093, var=3.3424551085136254, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-8R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-8R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 3.7092446733856863"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-8R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 3.7092446733856863""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-8R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 3.7092446733856863
""",
)

entry(
    index = 627,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-8R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(302335,'s^-1'), n=1.6157, w0=(411000,'J/mol'), E0=(149148,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-8R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-8R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 628,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_1C-inRing",
    kinetics = ArrheniusBM(A=(2.65682e+10,'s^-1'), n=0.737307, w0=(411000,'J/mol'), E0=(191679,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 629,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_N-1C-inRing",
    kinetics = ArrheniusBM(A=(0.0487298,'s^-1'), n=3.78826, w0=(411000,'J/mol'), E0=(151865,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_N-1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_N-1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 630,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.27e+06,'s^-1'), n=1.5, w0=(411000,'J/mol'), E0=(150194,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 631,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.59e+08,'s^-1'), n=1.01, w0=(411000,'J/mol'), E0=(113112,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 632,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(4.36685e-05,'s^-1'), n=4.64006, w0=(411000,'J/mol'), E0=(112771,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.6551020510007493, var=45.220024858738874, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-6R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-6R!H-R
    Total Standard Deviation in ln(k): 20.15211934424883"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 20.15211934424883""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 20.15211934424883
""",
)

entry(
    index = 633,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Int-6R!H-3C",
    kinetics = ArrheniusBM(A=(49540.9,'s^-1'), n=2.06328, w0=(411000,'J/mol'), E0=(93722.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.243886914276945, var=11.440510890927648, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Int-6R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Int-6R!H-3C
    Total Standard Deviation in ln(k): 12.41868751886365"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Int-6R!H-3C
Total Standard Deviation in ln(k): 12.41868751886365""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Int-6R!H-3C
Total Standard Deviation in ln(k): 12.41868751886365
""",
)

entry(
    index = 634,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(14.1918,'s^-1'), n=3.54805, w0=(411000,'J/mol'), E0=(127588,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11670587349760464, var=13.728431257241946, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R
    Total Standard Deviation in ln(k): 7.721154745161041"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R
Total Standard Deviation in ln(k): 7.721154745161041""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R
Total Standard Deviation in ln(k): 7.721154745161041
""",
)

entry(
    index = 635,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-7R!H-3C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.677e+10,'s^-1'), n=0.839, w0=(411000,'J/mol'), E0=(41100,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-7R!H-3C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-7R!H-3C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-7R!H-3C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_N-Sp-7R!H-3C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 636,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_Sp-6R!H-3C_Ext-6R!H-R_N-Sp-7R!H-6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.1979e+07,'s^-1'), n=1.76606, w0=(411000,'J/mol'), E0=(59486.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_Sp-6R!H-3C_Ext-6R!H-R_N-Sp-7R!H-6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_Sp-6R!H-3C_Ext-6R!H-R_N-Sp-7R!H-6R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_Sp-6R!H-3C_Ext-6R!H-R_N-Sp-7R!H-6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_Sp-6R!H-3C_Ext-6R!H-R_N-Sp-7R!H-6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 637,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_N-Sp-6R!H-3C_Ext-4R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(7.15861e+11,'s^-1'), n=0.19723, w0=(411000,'J/mol'), E0=(183832,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.7765829052500127e-14, var=51.66010811322142, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_N-Sp-6R!H-3C_Ext-4R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_N-Sp-6R!H-3C_Ext-4R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 14.409026655621814"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_N-Sp-6R!H-3C_Ext-4R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 14.409026655621814""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Int-6R!H-3C_1C-inRing_N-Sp-6R!H-3C_Ext-4R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 14.409026655621814
""",
)

entry(
    index = 638,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R_Ext-3C-R_Sp-7R!H-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.05896e+09,'s^-1'), n=0.469359, w0=(411000,'J/mol'), E0=(151659,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R_Ext-3C-R_Sp-7R!H-3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R_Ext-3C-R_Sp-7R!H-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R_Ext-3C-R_Sp-7R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_Ext-1C-R_Ext-3C-R_Sp-7R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 639,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_Ext-3C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.41119e+07,'s^-1'), n=1.71363, w0=(411000,'J/mol'), E0=(150798,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_Ext-3C-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_Ext-3C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_Ext-3C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_Ext-3C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 640,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-4R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(9.527e+10,'s^-1'), n=0.853, w0=(411000,'J/mol'), E0=(252683,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-4R!H_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-4R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-4R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-4R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 641,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Sp-6R!H-3C_Ext-4R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.21535e+07,'s^-1'), n=1.63877, w0=(411000,'J/mol'), E0=(155050,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Sp-6R!H-3C_Ext-4R!H-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Sp-6R!H-3C_Ext-4R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Sp-6R!H-3C_Ext-4R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_3C-inRing_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Ext-3C-R_Sp-6R!H-3C_Ext-4R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 642,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R_4R!H-inRing",
    kinetics = ArrheniusBM(A=(1.193e+07,'s^-1'), n=1.425, w0=(411000,'J/mol'), E0=(50096.5,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R_4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R_4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 643,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(0.110248,'s^-1'), n=4.25478, w0=(411000,'J/mol'), E0=(142596,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0025146815002933106, var=0.0024821379191006998, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R_N-4R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R_N-4R!H-inRing
    Total Standard Deviation in ln(k): 0.10619631978138153"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R_N-4R!H-inRing
Total Standard Deviation in ln(k): 0.10619631978138153""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R_N-4R!H-inRing
Total Standard Deviation in ln(k): 0.10619631978138153
""",
)

entry(
    index = 644,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(7.36952e-58,'s^-1'), n=20.553, w0=(411000,'J/mol'), E0=(22949,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.455975311027981, var=10.12374494765533, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R',), comment="""BM rule fitted to 15 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 7.524299194340628"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 7.524299194340628""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 7.524299194340628
""",
)

entry(
    index = 645,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.85887e+08,'s^-1'), n=0.862516, w0=(411000,'J/mol'), E0=(151333,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0016939798665731656, var=0.9683014291617127, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 1.976961823584996"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.976961823584996""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.976961823584996
""",
)

entry(
    index = 646,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Int-3C-1C",
    kinetics = ArrheniusBM(A=(8.80437e+09,'s^-1'), n=0.834438, w0=(411000,'J/mol'), E0=(162713,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006080130825372302, var=0.5361559687594992, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Int-3C-1C',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Int-3C-1C
    Total Standard Deviation in ln(k): 1.4831972998167697"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Int-3C-1C
Total Standard Deviation in ln(k): 1.4831972998167697""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Int-3C-1C
Total Standard Deviation in ln(k): 1.4831972998167697
""",
)

entry(
    index = 647,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(1.17936e+07,'s^-1'), n=1.67829, w0=(411000,'J/mol'), E0=(151910,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.002412008211180112, var=1.6131431628505977, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 2.552265783312788"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 2.552265783312788""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 2.552265783312788
""",
)

entry(
    index = 648,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(6.414e-06,'s^-1'), n=5.188, w0=(411000,'J/mol'), E0=(121224,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 649,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-1C-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.92058e+08,'s^-1'), n=1.00499, w0=(411000,'J/mol'), E0=(66521.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=440.9022129426087, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-1C-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-1C-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 42.09476881545396"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-1C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 42.09476881545396""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-1C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 42.09476881545396
""",
)

entry(
    index = 650,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.02148e+06,'s^-1'), n=0.868591, w0=(411000,'J/mol'), E0=(69830.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08117179481274918, var=3.4157363281530118, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 3.909042619359619"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 3.909042619359619""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 3.909042619359619
""",
)

entry(
    index = 651,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(6.6582e+06,'s^-1'), n=0.858417, w0=(411000,'J/mol'), E0=(58241.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.060622389193913405, var=1.6399141886358217, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H',), comment="""BM rule fitted to 14 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 2.7195639465885075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 2.7195639465885075""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 2.7195639465885075
""",
)

entry(
    index = 652,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_N-Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(1.77463e+06,'s^-1'), n=1.28888, w0=(411000,'J/mol'), E0=(74540.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.635996429034822e-15, var=11.331340419642299, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_N-Sp-7R!H-6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_N-Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 6.748350526872567"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 6.748350526872567""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 6.748350526872567
""",
)

entry(
    index = 653,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C",
    kinetics = ArrheniusBM(A=(2.09154e+08,'s^-1'), n=0.585093, w0=(411000,'J/mol'), E0=(60282.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03435809518035862, var=1.4145414835799628, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C',), comment="""BM rule fitted to 12 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C
    Total Standard Deviation in ln(k): 2.470648474635182"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C
Total Standard Deviation in ln(k): 2.470648474635182""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C
Total Standard Deviation in ln(k): 2.470648474635182
""",
)

entry(
    index = 654,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_N-6R!H->C",
    kinetics = ArrheniusBM(A=(19.5507,'s^-1'), n=2.53147, w0=(411000,'J/mol'), E0=(39906.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 655,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_Sp-4C-3C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.33751e+08,'s^-1'), n=0.907767, w0=(411000,'J/mol'), E0=(148209,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0018005723720103954, var=0.8104051310048662, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_Sp-4C-3C_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_Sp-4C-3C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.8092367757331225"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_Sp-4C-3C_Ext-1C-R
Total Standard Deviation in ln(k): 1.8092367757331225""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_Sp-4C-3C_Ext-1C-R
Total Standard Deviation in ln(k): 1.8092367757331225
""",
)

entry(
    index = 656,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_Sp-4C-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(8.53716e+07,'s^-1'), n=1.27085, w0=(411000,'J/mol'), E0=(146898,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-7.11719035839402e-15, var=3.15280802852223, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_Sp-4C-3C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_Sp-4C-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 3.5596373359038713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_Sp-4C-3C_Ext-3C-R
Total Standard Deviation in ln(k): 3.5596373359038713""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_Sp-4C-3C_Ext-3C-R
Total Standard Deviation in ln(k): 3.5596373359038713
""",
)

entry(
    index = 657,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing_N-4R!H-inRing_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(1.68e-11,'s^-1'), n=6.833, w0=(411000,'J/mol'), E0=(111898,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing_N-4R!H-inRing_Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing_N-4R!H-inRing_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing_N-4R!H-inRing_Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing_N-4R!H-inRing_Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 658,
    label = "Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing_N-4R!H-inRing_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(401300,'s^-1'), n=2.064, w0=(411000,'J/mol'), E0=(206690,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing_N-4R!H-inRing_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing_N-4R!H-inRing_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing_N-4R!H-inRing_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Int-3C-1C_Sp-3C-1C_5R!H->C_Sp-5C-4R!H_N-3C-inRing_5C-inRing_N-4R!H-inRing_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 659,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C_4R!H->C",
    kinetics = ArrheniusBM(A=(1e+11,'s^-1'), n=0, w0=(435000,'J/mol'), E0=(120206,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 660,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.34072e+10,'s^-1'), n=0.530121, w0=(435000,'J/mol'), E0=(91105.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.005736965341721745, var=1.3055679397694133, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C_N-4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C_N-4R!H->C
    Total Standard Deviation in ln(k): 2.3050538926113524"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C_N-4R!H->C
Total Standard Deviation in ln(k): 2.3050538926113524""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C_N-4R!H->C
Total Standard Deviation in ln(k): 2.3050538926113524
""",
)

entry(
    index = 661,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_N-7R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.3292e+11,'s^-1'), n=0.709413, w0=(435000,'J/mol'), E0=(96108.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0010133927853504488, var=10.119431010112812, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_N-7R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_N-7R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 6.3798196181647695"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_N-7R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.3798196181647695""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_N-7R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.3798196181647695
""",
)

entry(
    index = 662,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_N-7R!H->C_Ext-7BrClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(2.76e+08,'s^-1'), n=1.2, w0=(435000,'J/mol'), E0=(91855.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_N-7R!H->C_Ext-7BrClFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_N-7R!H->C_Ext-7BrClFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_N-7R!H->C_Ext-7BrClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_N-7R!H->C_Ext-7BrClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 663,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_N-4R!H->C_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.53e+09,'s^-1'), n=0.69, w0=(435000,'J/mol'), E0=(89695.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_N-4R!H->C_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_N-4R!H->C_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_N-4R!H->C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_N-4R!H->C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 664,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_Ext-7R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(175,'s^-1'), n=3.1, w0=(435000,'J/mol'), E0=(52198.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_Ext-7R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_Ext-7R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_Ext-7R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Ext-5R!H-R_Int-6R!H-1C_Sp-6R!H-1C_N-4R!H->C_Ext-1C-R_Ext-1C-R_Ext-7R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 665,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_7R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.01629e+10,'s^-1'), n=0.103653, w0=(435000,'J/mol'), E0=(92500.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.005661087261641983, var=4.1149455482061645, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_7R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_7R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 4.080894809575874"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_7R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.080894809575874""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_7R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.080894809575874
""",
)

entry(
    index = 666,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_N-7R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.55059e+11,'s^-1'), n=0.420605, w0=(435000,'J/mol'), E0=(94457.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0015557729345091656, var=15.395935712287024, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_N-7R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_N-7R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 7.870019313938119"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_N-7R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 7.870019313938119""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_N-7R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 7.870019313938119
""",
)

entry(
    index = 667,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(6.42176e+06,'s^-1'), n=1.58785, w0=(435000,'J/mol'), E0=(88290.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_N-7R!H->C_Ext-7BrClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 668,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing_Ext-3C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Sp-8R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.78e+06,'s^-1'), n=1.75, w0=(411000,'J/mol'), E0=(111791,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing_Ext-3C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Sp-8R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing_Ext-3C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Sp-8R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing_Ext-3C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Sp-8R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing_Ext-3C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Sp-8R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 669,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing_Ext-3C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_N-Sp-8R!H-5R!H",
    kinetics = ArrheniusBM(A=(543980,'s^-1'), n=1.81089, w0=(411000,'J/mol'), E0=(111262,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing_Ext-3C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_N-Sp-8R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing_Ext-3C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_N-Sp-8R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing_Ext-3C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_N-Sp-8R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_5R!H-inRing_3C-inRing_Ext-3C-R_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_N-Sp-8R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 670,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.22831e+06,'s^-1'), n=1.4712, w0=(411000,'J/mol'), E0=(95122,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05055912861742147, var=6.398023677957131, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_Ext-6R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_Ext-6R!H-R
    Total Standard Deviation in ln(k): 5.197873026428559"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 5.197873026428559""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_Ext-6R!H-R
Total Standard Deviation in ln(k): 5.197873026428559
""",
)

entry(
    index = 671,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C",
    kinetics = ArrheniusBM(A=(17.3807,'s^-1'), n=2.87796, w0=(411000,'J/mol'), E0=(73361,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01563113912053406, var=2.8616386285779494, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C
    Total Standard Deviation in ln(k): 3.4305599627564725"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C
Total Standard Deviation in ln(k): 3.4305599627564725""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C
Total Standard Deviation in ln(k): 3.4305599627564725
""",
)

entry(
    index = 672,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.197332,'s^-1'), n=3.35836, w0=(411000,'J/mol'), E0=(61065.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 673,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.23105e-09,'s^-1'), n=5.97729, w0=(411000,'J/mol'), E0=(43279.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05974082031380661, var=1.331602198737592, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 2.4634679927174643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 2.4634679927174643""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 2.4634679927174643
""",
)

entry(
    index = 674,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_N-Sp-5R!H-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.62e+09,'s^-1'), n=1.05, w0=(411000,'J/mol'), E0=(122866,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_N-Sp-5R!H-3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_N-Sp-5R!H-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_N-Sp-5R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_N-Sp-5R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 675,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_N-Sp-5R!H-3C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.915e+06,'s^-1'), n=1.697, w0=(411000,'J/mol'), E0=(81746.1,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_N-Sp-5R!H-3C_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_N-Sp-5R!H-3C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_N-Sp-5R!H-3C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_N-Sp-5R!H-3C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 676,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-1C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.83e+08,'s^-1'), n=1.45, w0=(411000,'J/mol'), E0=(156568,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-1C-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-1C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-1C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-1C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 677,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-8R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-9R!H-R_1C-inRing",
    kinetics = ArrheniusBM(A=(1.0253e+08,'s^-1'), n=1.58427, w0=(411000,'J/mol'), E0=(155395,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-8R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-9R!H-R_1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-8R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-9R!H-R_1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-8R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-9R!H-R_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-8R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-9R!H-R_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 678,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-8R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-9R!H-R_N-1C-inRing",
    kinetics = ArrheniusBM(A=(53324.9,'s^-1'), n=2.14607, w0=(411000,'J/mol'), E0=(135224,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-8R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-9R!H-R_N-1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-8R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-9R!H-R_N-1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-8R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-9R!H-R_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_3C-inRing_Ext-8R!H-R_Ext-9R!H-R_Ext-8R!H-R_Ext-9R!H-R_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 679,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-6R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(250000,'s^-1'), n=1.95, w0=(411000,'J/mol'), E0=(136976,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-6R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-6R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-6R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-6R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 680,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-6R!H-R_1C-inRing",
    kinetics = ArrheniusBM(A=(0.107,'s^-1'), n=3.67, w0=(411000,'J/mol'), E0=(152988,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-6R!H-R_1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-6R!H-R_1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-6R!H-R_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-6R!H-R_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 681,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-6R!H-R_N-1C-inRing",
    kinetics = ArrheniusBM(A=(1798.54,'s^-1'), n=2.16768, w0=(411000,'J/mol'), E0=(92181.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-6R!H-R_N-1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-6R!H-R_N-1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-6R!H-R_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_Sp-8R!H=7R!H_N-3C-inRing_Ext-6R!H-R_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 682,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R_Sp-9R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.72084e-38,'s^-1'), n=15.0845, w0=(411000,'J/mol'), E0=(17985,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15182761116122837, var=42.20479858949331, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R_Sp-9R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R_Sp-9R!H=6R!H
    Total Standard Deviation in ln(k): 13.405282020483387"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R_Sp-9R!H=6R!H
Total Standard Deviation in ln(k): 13.405282020483387""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R_Sp-9R!H=6R!H
Total Standard Deviation in ln(k): 13.405282020483387
""",
)

entry(
    index = 683,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R_N-Sp-9R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.81124e+06,'s^-1'), n=1.94666, w0=(411000,'J/mol'), E0=(150997,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0013828052999337627, var=5.152630079601109, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R_N-Sp-9R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R_N-Sp-9R!H=6R!H
    Total Standard Deviation in ln(k): 4.554103820116301"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R_N-Sp-9R!H=6R!H
Total Standard Deviation in ln(k): 4.554103820116301""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R_N-Sp-9R!H=6R!H
Total Standard Deviation in ln(k): 4.554103820116301
""",
)

entry(
    index = 684,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R_N-4R!H-inRing_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(1.01286e-10,'s^-1'), n=6.74404, w0=(411000,'J/mol'), E0=(112702,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R_N-4R!H-inRing_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Sp-3C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R_N-4R!H-inRing_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Sp-3C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R_N-4R!H-inRing_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Sp-3C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R_N-4R!H-inRing_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_Sp-3C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 685,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R_N-4R!H-inRing_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(2.43199e+08,'s^-1'), n=1.68104, w0=(411000,'J/mol'), E0=(173555,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R_N-4R!H-inRing_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_N-Sp-3C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R_N-4R!H-inRing_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R_N-4R!H-inRing_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_N-Sp-3C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-5R!H-R_N-4R!H-inRing_Ext-7R!H-R_Ext-8R!H-R_Ext-8R!H-R_N-Sp-3C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 686,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.08089e+09,'s^-1'), n=0.742266, w0=(411000,'J/mol'), E0=(151874,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0018387564174322734, var=1.6806590502370513, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 2.6035632542573466"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.6035632542573466""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.6035632542573466
""",
)

entry(
    index = 687,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.04551e+09,'s^-1'), n=1.46, w0=(411000,'J/mol'), E0=(161493,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.514661905379763e-15, var=80.48558491556025, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Ext-3C-R
    Total Standard Deviation in ln(k): 17.985231889550487"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 17.985231889550487""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 17.985231889550487
""",
)

entry(
    index = 688,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C",
    kinetics = ArrheniusBM(A=(6.9728e-61,'s^-1'), n=21.3828, w0=(411000,'J/mol'), E0=(23780.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.32642214020757176, var=8.593533485355351, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C
    Total Standard Deviation in ln(k): 6.696982723923911"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C
Total Standard Deviation in ln(k): 6.696982723923911""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C
Total Standard Deviation in ln(k): 6.696982723923911
""",
)

entry(
    index = 689,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_1C-inRing",
    kinetics = ArrheniusBM(A=(6.35122e+09,'s^-1'), n=0.783709, w0=(411000,'J/mol'), E0=(154228,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7573309526898814e-16, var=7.408525637179385, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_1C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_1C-inRing
    Total Standard Deviation in ln(k): 5.456609608908543"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_1C-inRing
Total Standard Deviation in ln(k): 5.456609608908543""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_1C-inRing
Total Standard Deviation in ln(k): 5.456609608908543
""",
)

entry(
    index = 690,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_N-1C-inRing",
    kinetics = ArrheniusBM(A=(96112.2,'s^-1'), n=2.08634, w0=(411000,'J/mol'), E0=(180021,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_N-1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_N-1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 691,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.34958e+08,'s^-1'), n=0.96, w0=(411000,'J/mol'), E0=(148315,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.5366285422883864e-15, var=0.30950448886871756, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 1.115296824032291"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.115296824032291""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.115296824032291
""",
)

entry(
    index = 692,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Int-3C-1C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.72656e+09,'s^-1'), n=0.895, w0=(411000,'J/mol'), E0=(161284,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.782043419212083e-15, var=0.003958535609340644, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Int-3C-1C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Int-3C-1C_Ext-3C-R
    Total Standard Deviation in ln(k): 0.12613170529821086"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Int-3C-1C_Ext-3C-R
Total Standard Deviation in ln(k): 0.12613170529821086""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Int-3C-1C_Ext-3C-R
Total Standard Deviation in ln(k): 0.12613170529821086
""",
)

entry(
    index = 693,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_1C-inRing",
    kinetics = ArrheniusBM(A=(8.72575e+06,'s^-1'), n=1.71375, w0=(411000,'J/mol'), E0=(151725,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.003294223662091774, var=2.172823987507329, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_1C-inRing',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_1C-inRing
    Total Standard Deviation in ln(k): 2.963357082517756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_1C-inRing
Total Standard Deviation in ln(k): 2.963357082517756""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_1C-inRing
Total Standard Deviation in ln(k): 2.963357082517756
""",
)

entry(
    index = 694,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_N-1C-inRing",
    kinetics = ArrheniusBM(A=(1.49894e+08,'s^-1'), n=1.39072, w0=(411000,'J/mol'), E0=(155094,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_N-1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_N-1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 695,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_8R!H->C",
    kinetics = ArrheniusBM(A=(2.92655e+06,'s^-1'), n=0.710881, w0=(411000,'J/mol'), E0=(71940.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05497253040036928, var=2.549063386596073, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_8R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_8R!H->C
    Total Standard Deviation in ln(k): 3.338839159755758"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_8R!H->C
Total Standard Deviation in ln(k): 3.338839159755758""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_8R!H->C
Total Standard Deviation in ln(k): 3.338839159755758
""",
)

entry(
    index = 696,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(2000,'s^-1'), n=1.9, w0=(411000,'J/mol'), E0=(53308.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 697,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_Int-7R!H-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.45158e+07,'s^-1'), n=0.826543, w0=(411000,'J/mol'), E0=(59022.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07180797502318415, var=1.8911724717287335, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_Int-7R!H-3C_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_Int-7R!H-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 2.9373318542451945"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_Int-7R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 2.9373318542451945""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_Int-7R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 2.9373318542451945
""",
)

entry(
    index = 698,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3C-R",
    kinetics = ArrheniusBM(A=(254,'s^-1'), n=2.6, w0=(411000,'J/mol'), E0=(59673.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 699,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_7R!H->C",
    kinetics = ArrheniusBM(A=(8463.98,'s^-1'), n=1.59356, w0=(411000,'J/mol'), E0=(50234.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008462870638694987, var=1.7956361405058099, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_7R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_7R!H->C
    Total Standard Deviation in ln(k): 2.707635532019671"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_7R!H->C
Total Standard Deviation in ln(k): 2.707635532019671""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_7R!H->C
Total Standard Deviation in ln(k): 2.707635532019671
""",
)

entry(
    index = 700,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_N-7R!H->C",
    kinetics = ArrheniusBM(A=(377,'s^-1'), n=2.2, w0=(411000,'J/mol'), E0=(54993.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 701,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_N-Sp-7R!H-6R!H_Int-6R!H-3C",
    kinetics = ArrheniusBM(A=(1.99586e+06,'s^-1'), n=1.37598, w0=(411000,'J/mol'), E0=(70546.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_N-Sp-7R!H-6R!H_Int-6R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_N-Sp-7R!H-6R!H_Int-6R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_N-Sp-7R!H-6R!H_Int-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_N-Sp-7R!H-6R!H_Int-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 702,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.12847e+09,'s^-1'), n=0.419, w0=(411000,'J/mol'), E0=(62486.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04622755911655563, var=2.2177514806162852, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 3.101624574099854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 3.101624574099854""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 3.101624574099854
""",
)

entry(
    index = 703,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(22274.5,'s^-1'), n=1.79535, w0=(411000,'J/mol'), E0=(50329.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.441094538585411, var=67.26916404082088, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 30.11348406435247"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 30.11348406435247""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 30.11348406435247
""",
)

entry(
    index = 704,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_Sp-4C-3C_Ext-1C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.78e+08,'s^-1'), n=1, w0=(411000,'J/mol'), E0=(147687,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-9.240074696425269e-29, var=3.669189285409231e-28, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_Sp-4C-3C_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_Sp-4C-3C_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 3.8400957005439667e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_Sp-4C-3C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.8400957005439667e-14""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-1C-R_N-3C-inRing_N-4R!H->O_Ext-3C-R_N-Sp-6R!H=3C_Int-4C-3C_Sp-4C-3C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.8400957005439667e-14
""",
)

entry(
    index = 705,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C_N-4R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(4.81442e+10,'s^-1'), n=0.348527, w0=(435000,'J/mol'), E0=(90096.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.005484669336264653, var=4.106488125428435, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C_N-4R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C_N-4R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 4.076270296760054"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C_N-4R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.076270296760054""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C_N-4R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.076270296760054
""",
)

entry(
    index = 706,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_N-7R!H->C_Ext-5R!H-R_Ext-7BrClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.75e+08,'s^-1'), n=1.7, w0=(435000,'J/mol'), E0=(88497.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_N-7R!H->C_Ext-5R!H-R_Ext-7BrClFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_N-7R!H->C_Ext-5R!H-R_Ext-7BrClFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_N-7R!H->C_Ext-5R!H-R_Ext-7BrClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_N-7R!H->C_Ext-5R!H-R_Ext-7BrClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 707,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_7R!H->C_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(9.8388e+08,'s^-1'), n=0.534541, w0=(435000,'J/mol'), E0=(82869.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_7R!H->C_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_7R!H->C_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_7R!H->C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_7R!H->C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 708,
    label = "Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_N-7R!H->C_Ext-5R!H-R_Ext-7BrClFINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.79419e+09,'s^-1'), n=1.29445, w0=(435000,'J/mol'), E0=(92015.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_N-7R!H->C_Ext-5R!H-R_Ext-7BrClFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_N-7R!H->C_Ext-5R!H-R_Ext-7BrClFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_N-7R!H->C_Ext-5R!H-R_Ext-7BrClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->C_1BrClFINOPSSi->O_Ext-1O-R_N-4R!H->C_Ext-4BrClFINOPSSi-R_Int-5R!H-3R!H_Ext-3R!H-R_6R!H->C_Sp-6C-3R!H_Ext-3R!H-R_N-7R!H->C_Ext-5R!H-R_Ext-7BrClFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 709,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_Ext-6R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(25800,'s^-1'), n=2.04, w0=(411000,'J/mol'), E0=(112003,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_Ext-6R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_Ext-6R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 710,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_Ext-6R!H-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.251,'s^-1'), n=3.86, w0=(411000,'J/mol'), E0=(63700.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_Ext-6R!H-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_Ext-6R!H-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_Ext-6R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_Ext-6R!H-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 711,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_Ext-6R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(377000,'s^-1'), n=1.63, w0=(411000,'J/mol'), E0=(82613.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_Ext-6R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_Ext-6R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 712,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_6R!H->O",
    kinetics = ArrheniusBM(A=(1854.24,'s^-1'), n=2.35598, w0=(411000,'J/mol'), E0=(80117.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7573309526898815e-15, var=12.82123719939755, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_6R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_6R!H->O
    Total Standard Deviation in ln(k): 7.178305821272933"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_6R!H->O
Total Standard Deviation in ln(k): 7.178305821272933""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_6R!H->O
Total Standard Deviation in ln(k): 7.178305821272933
""",
)

entry(
    index = 713,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O",
    kinetics = ArrheniusBM(A=(0.0908716,'s^-1'), n=3.45696, w0=(411000,'J/mol'), E0=(65475.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06291432071007827, var=1.4927155370519378, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O
    Total Standard Deviation in ln(k): 2.607396110893502"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O
Total Standard Deviation in ln(k): 2.607396110893502""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O
Total Standard Deviation in ln(k): 2.607396110893502
""",
)

entry(
    index = 714,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C_Ext-3C-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(264300,'s^-1'), n=1.839, w0=(411000,'J/mol'), E0=(75210.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C_Ext-3C-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C_Ext-3C-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C_Ext-3C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C_Ext-3C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 715,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C_Ext-3C-R_Sp-7R!H-3C",
    kinetics = ArrheniusBM(A=(1.478,'s^-1'), n=3.436, w0=(411000,'J/mol'), E0=(63075.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C_Ext-3C-R_Sp-7R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C_Ext-3C-R_Sp-7R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C_Ext-3C-R_Sp-7R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C_Ext-3C-R_Sp-7R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 716,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C_Ext-3C-R_N-Sp-7R!H-3C",
    kinetics = ArrheniusBM(A=(1.286e+08,'s^-1'), n=1.323, w0=(411000,'J/mol'), E0=(83158,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C_Ext-3C-R_N-Sp-7R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C_Ext-3C-R_N-Sp-7R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C_Ext-3C-R_N-Sp-7R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_N-Sp-4R!H-1C_Sp-5R!H-3C_Ext-3C-R_N-Sp-7R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 717,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.67e+09,'s^-1'), n=1.14, w0=(411000,'J/mol'), E0=(148658,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 718,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R_N-Sp-9R!H=6R!H_Int-6R!H-3C",
    kinetics = ArrheniusBM(A=(1.46e+07,'s^-1'), n=1.66, w0=(411000,'J/mol'), E0=(154796,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R_N-Sp-9R!H=6R!H_Int-6R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R_N-Sp-9R!H=6R!H_Int-6R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R_N-Sp-9R!H=6R!H_Int-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-3C-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Sp-7R!H-3C_Ext-6R!H-R_N-Sp-9R!H=6R!H_Int-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 719,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Ext-1C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.08655e+09,'s^-1'), n=0.75, w0=(411000,'J/mol'), E0=(149570,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=2.3164883580329096, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 3.0512096579309724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.0512096579309724""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.0512096579309724
""",
)

entry(
    index = 720,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(7.80267e-62,'s^-1'), n=21.5956, w0=(411000,'J/mol'), E0=(10128.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.13783209761794926, var=8.12523421395439, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C
    Total Standard Deviation in ln(k): 6.060768337390117"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C
Total Standard Deviation in ln(k): 6.060768337390117""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C
Total Standard Deviation in ln(k): 6.060768337390117
""",
)

entry(
    index = 721,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(1.75e+11,'s^-1'), n=0.633, w0=(411000,'J/mol'), E0=(208478,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_N-Sp-3C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_N-Sp-3C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 722,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_1C-inRing_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.94274e+10,'s^-1'), n=0.730382, w0=(411000,'J/mol'), E0=(161866,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0033684910933067078, var=2.2126809857589755, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_1C-inRing_Sp-6R!H-5R!H',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_1C-inRing_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 2.990523641489417"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_1C-inRing_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 2.990523641489417""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_1C-inRing_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 2.990523641489417
""",
)

entry(
    index = 723,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_1C-inRing_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(5.265e-07,'s^-1'), n=5.639, w0=(411000,'J/mol'), E0=(113971,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_1C-inRing_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_1C-inRing_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_1C-inRing_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_1C-inRing_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 724,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_8R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(531,'s^-1'), n=1.81, w0=(411000,'J/mol'), E0=(62391.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_8R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_8R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_8R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_8R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 725,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_8R!H->C_Int-7R!H-3C",
    kinetics = ArrheniusBM(A=(90247.4,'s^-1'), n=1.49598, w0=(411000,'J/mol'), E0=(72708.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_8R!H->C_Int-7R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_8R!H->C_Int-7R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_8R!H->C_Int-7R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_8R!H->C_Int-7R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 726,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_8R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.28039,'s^-1'), n=2.37617, w0=(411000,'J/mol'), E0=(57374.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_8R!H->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_8R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_8R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Ext-7R!H-R_8R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 727,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_Int-7R!H-3C_Ext-3C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(171400,'s^-1'), n=1.46477, w0=(411000,'J/mol'), E0=(56612.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.887984046863722, var=78.77288225900539, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_Int-7R!H-3C_Ext-3C-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_Int-7R!H-3C_Ext-3C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 32.58677321428953"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_Int-7R!H-3C_Ext-3C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 32.58677321428953""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_Int-7R!H-3C_Ext-3C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 32.58677321428953
""",
)

entry(
    index = 728,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_7R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2379.98,'s^-1'), n=1.84268, w0=(411000,'J/mol'), E0=(46677.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.015333042059421, var=36.634193273202385, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_7R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_7R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 22.222673529682922"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_7R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 22.222673529682922""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Ext-6R!H-R_Sp-7R!H-6R!H_7R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 22.222673529682922
""",
)

entry(
    index = 729,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.816956,'s^-1'), n=2.92389, w0=(411000,'J/mol'), E0=(40162.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.1527304170451046e-16, var=0.6719547612573656, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 1.6433384137476181"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.6433384137476181""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.6433384137476181
""",
)

entry(
    index = 730,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(2.08308e+06,'s^-1'), n=1.3984, w0=(411000,'J/mol'), E0=(59703.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.246000262775281, var=40.96410970215077, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 23.49929050921465"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 23.49929050921465""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 23.49929050921465
""",
)

entry(
    index = 731,
    label = "Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C_N-4R!H->C_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(4.87e+10,'s^-1'), n=0.35, w0=(435000,'J/mol'), E0=(84310.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C_N-4R!H->C_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C_N-4R!H->C_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C_N-4R!H->C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_N-3R!H->C_Ext-3OS-R_Ext-4R!H-R_3OS->O_Int-5R!H-1C_Ext-1C-R_Sp-6R!H-1C_6R!H->C_Ext-1C-R_7R!H->C_N-4R!H->C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 732,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C",
    kinetics = ArrheniusBM(A=(0.237756,'s^-1'), n=3.35173, w0=(411000,'J/mol'), E0=(68046,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.138076153198593, var=2.7711574004402966, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C
    Total Standard Deviation in ln(k): 3.684166131002509"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C
Total Standard Deviation in ln(k): 3.684166131002509""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C
Total Standard Deviation in ln(k): 3.684166131002509
""",
)

entry(
    index = 733,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.00114,'s^-1'), n=3.95, w0=(411000,'J/mol'), E0=(56059.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 734,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(120000,'s^-1'), n=2.099, w0=(411000,'J/mol'), E0=(145365,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 735,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_Sp-7R!H-3C",
    kinetics = ArrheniusBM(A=(162.558,'s^-1'), n=2.97254, w0=(411000,'J/mol'), E0=(148773,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.003094228411961254, var=5.634946495075013, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_Sp-7R!H-3C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_Sp-7R!H-3C
    Total Standard Deviation in ln(k): 4.7666230384698025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_Sp-7R!H-3C
Total Standard Deviation in ln(k): 4.7666230384698025""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_Sp-7R!H-3C
Total Standard Deviation in ln(k): 4.7666230384698025
""",
)

entry(
    index = 736,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_N-Sp-7R!H-3C",
    kinetics = ArrheniusBM(A=(9.66829e+07,'s^-1'), n=0.859294, w0=(411000,'J/mol'), E0=(177828,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_N-Sp-7R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_N-Sp-7R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_N-Sp-7R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_N-Sp-7R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 737,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_1C-inRing_Sp-6R!H-5R!H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.6287e+10,'s^-1'), n=0.730417, w0=(411000,'J/mol'), E0=(159982,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7573309526898815e-15, var=10.17506711538144, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_1C-inRing_Sp-6R!H-5R!H_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_1C-inRing_Sp-6R!H-5R!H_Ext-1C-R
    Total Standard Deviation in ln(k): 6.394780333788244"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_1C-inRing_Sp-6R!H-5R!H_Ext-1C-R
Total Standard Deviation in ln(k): 6.394780333788244""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Int-3C-1C_Sp-3C-1C_Sp-5R!H-4R!H_1C-inRing_Sp-6R!H-5R!H_Ext-1C-R
Total Standard Deviation in ln(k): 6.394780333788244
""",
)

entry(
    index = 738,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(0.0508,'s^-1'), n=3.24, w0=(411000,'J/mol'), E0=(37605.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 739,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R_Ext-1C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(35.2189,'s^-1'), n=2.49147, w0=(411000,'J/mol'), E0=(44268.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-5R!H-inRing_N-3C-inRing_Ext-5R!H-R_4R!H->C_Sp-6R!H-5R!H_6R!H->C_Ext-3C-R_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 740,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.86e+10,'s^-1'), n=0.58, w0=(411000,'J/mol'), E0=(120929,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 741,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0638484,'s^-1'), n=3.5157, w0=(411000,'J/mol'), E0=(65910.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2256101082383283, var=3.132344963360579, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 4.114926319067642"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 4.114926319067642""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 4.114926319067642
""",
)

entry(
    index = 742,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_Sp-7R!H-3C_1C-inRing",
    kinetics = ArrheniusBM(A=(1.21898e+10,'s^-1'), n=0.709077, w0=(411000,'J/mol'), E0=(162327,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.8451975003243754e-15, var=2.630409126716088, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_Sp-7R!H-3C_1C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_Sp-7R!H-3C_1C-inRing
    Total Standard Deviation in ln(k): 3.2513868189327604"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_Sp-7R!H-3C_1C-inRing
Total Standard Deviation in ln(k): 3.2513868189327604""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_Sp-7R!H-3C_1C-inRing
Total Standard Deviation in ln(k): 3.2513868189327604
""",
)

entry(
    index = 743,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_Sp-7R!H-3C_N-1C-inRing",
    kinetics = ArrheniusBM(A=(1.842e-10,'s^-1'), n=6.38, w0=(411000,'J/mol'), E0=(129571,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_Sp-7R!H-3C_N-1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_Sp-7R!H-3C_N-1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_Sp-7R!H-3C_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_N-Sp-5R!H=4R!H_5R!H-inRing_N-3C-inRing_Sp-4R!H-1C_Ext-5R!H-R_Ext-3C-R_Ext-6R!H-R_Int-3C-1C_Sp-3C-1C_Sp-7R!H-3C_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 744,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-3C-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(3600.87,'s^-1'), n=2.91748, w0=(411000,'J/mol'), E0=(72135.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-3C-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-3C-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-3C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-3C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 745,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-3C-R_6CS->C",
    kinetics = ArrheniusBM(A=(0.0124098,'s^-1'), n=3.75147, w0=(411000,'J/mol'), E0=(65302.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-3C-R_6CS->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-3C-R_6CS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-3C-R_6CS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-3C-R_6CS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 746,
    label = "Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-3C-R_N-6CS->C",
    kinetics = ArrheniusBM(A=(1.79e-05,'s^-1'), n=4.5, w0=(411000,'J/mol'), E0=(58687.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-3C-R_N-6CS->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-3C-R_N-6CS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-3C-R_N-6CS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->C_3R!H->C_Ext-1C-R_N-Sp-4R!H=1C_Ext-4R!H-R_Int-5R!H-3C_Sp-5R!H-4R!H_N-Sp-5R!H-=3C_Ext-1C-R_N-5R!H-inRing_Sp-4R!H-1C_N-1C-inRing_5R!H->C_N-6R!H->O_4R!H->C_Ext-3C-R_N-6CS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

