#!/usr/bin/env python
# encoding: utf-8

name = "F_Abstraction/rules"
shortDesc = ""
longDesc = """
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')


.. [MRHCBSQB3RRHO] M.R. Harper (mrharper_at_mit_dot_edu or michael.harper.jr_at_gmail_dot_com)
The geometries of all reactants, products, and the transition state were optimized using the CBS-QB3 calculations.  The zero-point
energy is that computed by the CBS-QB3 calculations.  The frequencies were computed with B3LYP/CBSB7.
In computing k(T), an asymmetric tunneling correction was employed, the calculated frequencies were scaled by 0.99, and the
temperatures used were: 300, 331, 370, 419, 482, 568, 692, 885, 1227, 2000 (evenly spaced on inverse temperature scale).

.. [Tsang1990] W. Tsang; "Chemical kinetic database for combustion chemistry. Part IV. Isobutane" J. Phys. Chem. Ref. Data 19 (1990) 1-68

.. [Tsang1991] W. Tsang; "Chemical kinetic database for combustion chemistry. Part V. Propene" J. Phys. Chem. Ref. Data 20 (1991) 221-273
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.09594e+46,'m^3/(mol*s)'), n=-11.5781, w0=(417576,'J/mol'), E0=(266801,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.8715551744105312, var=12.831449264144078, Tref=1000.0, N=164, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 164 training reactions at node Root
    Total Standard Deviation in ln(k): 9.371001119994302"""),
    rank = 11,
    shortDesc = """BM rule fitted to 164 training reactions at node Root
Total Standard Deviation in ln(k): 9.371001119994302""",
    longDesc = 
"""
BM rule fitted to 164 training reactions at node Root
Total Standard Deviation in ln(k): 9.371001119994302
""",
)

entry(
    index = 2,
    label = "Root_1R->O",
    kinetics = ArrheniusBM(A=(2.55398e-08,'m^3/(mol*s)'), n=4.31901, w0=(328817,'J/mol'), E0=(92237.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.17005340775529246, var=4.6427461831213614, Tref=1000.0, N=41, data_mean=0.0, correlation='Root_1R->O',), comment="""BM rule fitted to 41 training reactions at node Root_1R->O
    Total Standard Deviation in ln(k): 4.746879096115299"""),
    rank = 11,
    shortDesc = """BM rule fitted to 41 training reactions at node Root_1R->O
Total Standard Deviation in ln(k): 4.746879096115299""",
    longDesc = 
"""
BM rule fitted to 41 training reactions at node Root_1R->O
Total Standard Deviation in ln(k): 4.746879096115299
""",
)

entry(
    index = 3,
    label = "Root_N-1R->O",
    kinetics = ArrheniusBM(A=(9.64369e+42,'m^3/(mol*s)'), n=-10.6838, w0=(447163,'J/mol'), E0=(264125,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.82807501852954, var=11.358535849176148, Tref=1000.0, N=123, data_mean=0.0, correlation='Root_N-1R->O',), comment="""BM rule fitted to 123 training reactions at node Root_N-1R->O
    Total Standard Deviation in ln(k): 8.837034256541271"""),
    rank = 11,
    shortDesc = """BM rule fitted to 123 training reactions at node Root_N-1R->O
Total Standard Deviation in ln(k): 8.837034256541271""",
    longDesc = 
"""
BM rule fitted to 123 training reactions at node Root_N-1R->O
Total Standard Deviation in ln(k): 8.837034256541271
""",
)

entry(
    index = 4,
    label = "Root_1R->O_3R->O",
    kinetics = ArrheniusBM(A=(0.228712,'m^3/(mol*s)'), n=2.60844, w0=(222000,'J/mol'), E0=(114917,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06962233810856709, var=4.343846871314699, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->O_3R->O',), comment="""BM rule fitted to 8 training reactions at node Root_1R->O_3R->O
    Total Standard Deviation in ln(k): 4.353178776999081"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->O_3R->O
Total Standard Deviation in ln(k): 4.353178776999081""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->O_3R->O
Total Standard Deviation in ln(k): 4.353178776999081
""",
)

entry(
    index = 5,
    label = "Root_1R->O_N-3R->O",
    kinetics = ArrheniusBM(A=(5.36369e-11,'m^3/(mol*s)'), n=5.03475, w0=(354712,'J/mol'), E0=(35471.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1066421358299803, var=5.7463302541322925, Tref=1000.0, N=33, data_mean=0.0, correlation='Root_1R->O_N-3R->O',), comment="""BM rule fitted to 33 training reactions at node Root_1R->O_N-3R->O
    Total Standard Deviation in ln(k): 5.073596647016104"""),
    rank = 11,
    shortDesc = """BM rule fitted to 33 training reactions at node Root_1R->O_N-3R->O
Total Standard Deviation in ln(k): 5.073596647016104""",
    longDesc = 
"""
BM rule fitted to 33 training reactions at node Root_1R->O_N-3R->O
Total Standard Deviation in ln(k): 5.073596647016104
""",
)

entry(
    index = 6,
    label = "Root_N-1R->O_3R->O",
    kinetics = ArrheniusBM(A=(9.91899e-10,'m^3/(mol*s)'), n=4.84263, w0=(354712,'J/mol'), E0=(35471.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11654889275285538, var=5.172356718991652, Tref=1000.0, N=33, data_mean=0.0, correlation='Root_N-1R->O_3R->O',), comment="""BM rule fitted to 33 training reactions at node Root_N-1R->O_3R->O
    Total Standard Deviation in ln(k): 4.852168479359832"""),
    rank = 11,
    shortDesc = """BM rule fitted to 33 training reactions at node Root_N-1R->O_3R->O
Total Standard Deviation in ln(k): 4.852168479359832""",
    longDesc = 
"""
BM rule fitted to 33 training reactions at node Root_N-1R->O_3R->O
Total Standard Deviation in ln(k): 4.852168479359832
""",
)

entry(
    index = 7,
    label = "Root_N-1R->O_N-3R->O",
    kinetics = ArrheniusBM(A=(1.1576e+27,'m^3/(mol*s)'), n=-6.00599, w0=(481062,'J/mol'), E0=(234920,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5780600725396313, var=8.92229117345638, Tref=1000.0, N=90, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O',), comment="""BM rule fitted to 90 training reactions at node Root_N-1R->O_N-3R->O
    Total Standard Deviation in ln(k): 7.4405969171605095"""),
    rank = 11,
    shortDesc = """BM rule fitted to 90 training reactions at node Root_N-1R->O_N-3R->O
Total Standard Deviation in ln(k): 7.4405969171605095""",
    longDesc = 
"""
BM rule fitted to 90 training reactions at node Root_N-1R->O_N-3R->O
Total Standard Deviation in ln(k): 7.4405969171605095
""",
)

entry(
    index = 8,
    label = "Root_1R->O_3R->O_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.063049,'m^3/(mol*s)'), n=2.86668, w0=(222000,'J/mol'), E0=(112973,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08667904085672841, var=4.540542309670579, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_3R->O_Ext-1O-R
    Total Standard Deviation in ln(k): 4.489585958826926"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_3R->O_Ext-1O-R
Total Standard Deviation in ln(k): 4.489585958826926""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_3R->O_Ext-1O-R
Total Standard Deviation in ln(k): 4.489585958826926
""",
)

entry(
    index = 9,
    label = "Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.99935e-05,'m^3/(mol*s)'), n=4.01289, w0=(222000,'J/mol'), E0=(22200,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_1R->O_3R->O_1O-u0",
    kinetics = ArrheniusBM(A=(0.000414801,'m^3/(mol*s)'), n=3.324, w0=(222000,'J/mol'), E0=(110012,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_1O-u0',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_1O-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_1O-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_1O-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_1R->O_3R->O_N-1O-u0",
    kinetics = ArrheniusBM(A=(3662.37,'m^3/(mol*s)'), n=0.997174, w0=(222000,'J/mol'), E0=(127070,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04425865729168887, var=3.064816837797954, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
    Total Standard Deviation in ln(k): 3.6208158327784288"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
Total Standard Deviation in ln(k): 3.6208158327784288""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
Total Standard Deviation in ln(k): 3.6208158327784288
""",
)

entry(
    index = 12,
    label = "Root_1R->O_N-3R->O_3CClFH->C",
    kinetics = ArrheniusBM(A=(1.67254e-11,'m^3/(mol*s)'), n=5.14934, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10780862743180514, var=4.628255933518876, Tref=1000.0, N=32, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C',), comment="""BM rule fitted to 32 training reactions at node Root_1R->O_N-3R->O_3CClFH->C
    Total Standard Deviation in ln(k): 4.583739046564252"""),
    rank = 11,
    shortDesc = """BM rule fitted to 32 training reactions at node Root_1R->O_N-3R->O_3CClFH->C
Total Standard Deviation in ln(k): 4.583739046564252""",
    longDesc = 
"""
BM rule fitted to 32 training reactions at node Root_1R->O_N-3R->O_3CClFH->C
Total Standard Deviation in ln(k): 4.583739046564252
""",
)

entry(
    index = 13,
    label = "Root_1R->O_N-3R->O_N-3CClFH->C",
    kinetics = ArrheniusBM(A=(1.04105,'m^3/(mol*s)'), n=2.3137, w0=(393500,'J/mol'), E0=(39350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-3CClFH->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-3CClFH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-1R->O_3R->O_Ext-3O-R",
    kinetics = ArrheniusBM(A=(3.45284e-09,'m^3/(mol*s)'), n=4.62211, w0=(356357,'J/mol'), E0=(35635.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10171074464738103, var=2.7785257378485615, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
    Total Standard Deviation in ln(k): 3.597229572042318"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 3.597229572042318""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 3.597229572042318
""",
)

entry(
    index = 15,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(1.71094e-06,'m^3/(mol*s)'), n=3.99323, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08996823073415067, var=12.789146779908148, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 7.395367692713328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 7.395367692713328""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 7.395367692713328
""",
)

entry(
    index = 16,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(1.49875e-22,'m^3/(mol*s)'), n=8.66864, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.031889322838793, var=23.01677844802024, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 17.235690240882168"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 17.235690240882168""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 17.235690240882168
""",
)

entry(
    index = 17,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F",
    kinetics = ArrheniusBM(A=(0.494938,'m^3/(mol*s)'), n=2.16832, w0=(330000,'J/mol'), E0=(33000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02409217928766982, var=6.612847181435405, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F
    Total Standard Deviation in ln(k): 5.215800940478477"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 5.215800940478477""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 5.215800940478477
""",
)

entry(
    index = 18,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F",
    kinetics = ArrheniusBM(A=(4.09058e+19,'m^3/(mol*s)'), n=-3.80683, w0=(488088,'J/mol'), E0=(220428,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.46245317197368213, var=8.78200702567086, Tref=1000.0, N=86, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F',), comment="""BM rule fitted to 86 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F
    Total Standard Deviation in ln(k): 7.102865040847387"""),
    rank = 11,
    shortDesc = """BM rule fitted to 86 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 7.102865040847387""",
    longDesc = 
"""
BM rule fitted to 86 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 7.102865040847387
""",
)

entry(
    index = 19,
    label = "Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.0487535,'m^3/(mol*s)'), n=3.06244, w0=(222000,'J/mol'), E0=(22200,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_1R->O_3R->O_Ext-1O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.00077917,'m^3/(mol*s)'), n=3.43149, w0=(222000,'J/mol'), E0=(109239,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.6924040950117203, var=5.8294800059788185, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C
    Total Standard Deviation in ln(k): 9.09256733878789"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 9.09256733878789""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 9.09256733878789
""",
)

entry(
    index = 21,
    label = "Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0839177,'m^3/(mol*s)'), n=2.53937, w0=(222000,'J/mol'), E0=(112434,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.71791,'m^3/(mol*s)'), n=1.90889, w0=(222000,'J/mol'), E0=(121164,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.00111026,'m^3/(mol*s)'), n=2.89721, w0=(222000,'J/mol'), E0=(106112,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1",
    kinetics = ArrheniusBM(A=(5.78523e-10,'m^3/(mol*s)'), n=4.65011, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08028562274922828, var=4.923580622823339, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1',), comment="""BM rule fitted to 24 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1
    Total Standard Deviation in ln(k): 4.650057979517846"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1
Total Standard Deviation in ln(k): 4.650057979517846""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1
Total Standard Deviation in ln(k): 4.650057979517846
""",
)

entry(
    index = 25,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1",
    kinetics = ArrheniusBM(A=(7.12093e-17,'m^3/(mol*s)'), n=6.89165, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.19345189671953134, var=29.15341355548338, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1',), comment="""BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1
    Total Standard Deviation in ln(k): 11.310406791228704"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1
Total Standard Deviation in ln(k): 11.310406791228704""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1
Total Standard Deviation in ln(k): 11.310406791228704
""",
)

entry(
    index = 26,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.74528e-09,'m^3/(mol*s)'), n=4.64278, w0=(361500,'J/mol'), E0=(36150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11357858969308919, var=2.547621211025371, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C
    Total Standard Deviation in ln(k): 3.4851850070562214"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 3.4851850070562214""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 3.4851850070562214
""",
)

entry(
    index = 27,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.32173e-08,'m^3/(mol*s)'), n=4.58146, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08933381113048665, var=7.883875217718983, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 5.853399934017621"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 5.853399934017621""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 5.853399934017621
""",
)

entry(
    index = 28,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(1.72013,'m^3/(mol*s)'), n=2.4493, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(1.83956e-06,'m^3/(mol*s)'), n=3.98362, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08663819695872332, var=12.824040379988816, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 7.396774407419375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 7.396774407419375""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 7.396774407419375
""",
)

entry(
    index = 30,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1",
    kinetics = ArrheniusBM(A=(8.13257e-11,'m^3/(mol*s)'), n=5.26041, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12339002307319191, var=0.3693637865012486, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1
    Total Standard Deviation in ln(k): 1.5284090689005265"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1
Total Standard Deviation in ln(k): 1.5284090689005265""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1
Total Standard Deviation in ln(k): 1.5284090689005265
""",
)

entry(
    index = 31,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1",
    kinetics = ArrheniusBM(A=(8.65896e-23,'m^3/(mol*s)'), n=8.73785, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=7.177536902812312, var=15.847696151635311, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1
    Total Standard Deviation in ln(k): 26.014695259215937"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1
Total Standard Deviation in ln(k): 26.014695259215937""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1
Total Standard Deviation in ln(k): 26.014695259215937
""",
)

entry(
    index = 32,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.000812845,'m^3/(mol*s)'), n=2.96422, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.4096276771300487, var=0.9569638669847356, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 5.502900750460233"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R
Total Standard Deviation in ln(k): 5.502900750460233""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R
Total Standard Deviation in ln(k): 5.502900750460233
""",
)

entry(
    index = 33,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C",
    kinetics = ArrheniusBM(A=(4e+06,'m^3/(mol*s)'), n=0, w0=(320000,'J/mol'), E0=(32000,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->C",
    kinetics = ArrheniusBM(A=(29364.6,'m^3/(mol*s)'), n=0.785655, w0=(360000,'J/mol'), E0=(36000,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H",
    kinetics = ArrheniusBM(A=(2.36416e+07,'m^3/(mol*s)'), n=-0.00491634, w0=(516626,'J/mol'), E0=(177099,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.233664351265448, var=3.459120346776332, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H
    Total Standard Deviation in ln(k): 4.315645106342855"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H
Total Standard Deviation in ln(k): 4.315645106342855""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H
Total Standard Deviation in ln(k): 4.315645106342855
""",
)

entry(
    index = 36,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H",
    kinetics = ArrheniusBM(A=(8.70482e+20,'m^3/(mol*s)'), n=-4.24867, w0=(482538,'J/mol'), E0=(227910,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.46546632792994375, var=6.785608258424576, Tref=1000.0, N=72, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H',), comment="""BM rule fitted to 72 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H
    Total Standard Deviation in ln(k): 6.391687904583123"""),
    rank = 11,
    shortDesc = """BM rule fitted to 72 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H
Total Standard Deviation in ln(k): 6.391687904583123""",
    longDesc = 
"""
BM rule fitted to 72 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H
Total Standard Deviation in ln(k): 6.391687904583123
""",
)

entry(
    index = 37,
    label = "Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1",
    kinetics = ArrheniusBM(A=(0.0049864,'m^3/(mol*s)'), n=3.19625, w0=(222000,'J/mol'), E0=(111068,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.640932,'m^3/(mol*s)'), n=2.39839, w0=(222000,'J/mol'), E0=(119846,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.89216e-10,'m^3/(mol*s)'), n=4.64724, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08037774014339195, var=4.932101230276218, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R',), comment="""BM rule fitted to 22 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R
    Total Standard Deviation in ln(k): 4.654136847189085"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 4.654136847189085""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R
Total Standard Deviation in ln(k): 4.654136847189085
""",
)

entry(
    index = 40,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-1O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.000476496,'m^3/(mol*s)'), n=3.27616, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-1O-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-1O-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-1O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.000849095,'m^3/(mol*s)'), n=3.17369, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-1O-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-1O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0",
    kinetics = ArrheniusBM(A=(5.4472e-10,'m^3/(mol*s)'), n=4.88747, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8386676428180353, var=1.465309332583229, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0',), comment="""BM rule fitted to 6 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0
    Total Standard Deviation in ln(k): 4.533936184217291"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0
Total Standard Deviation in ln(k): 4.533936184217291""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0
Total Standard Deviation in ln(k): 4.533936184217291
""",
)

entry(
    index = 43,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_N-1O-u0",
    kinetics = ArrheniusBM(A=(6.74733e-24,'m^3/(mol*s)'), n=8.93652, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.315851573345764, var=2.4362014641067424, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_N-1O-u0',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_N-1O-u0
    Total Standard Deviation in ln(k): 16.485468815882555"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_N-1O-u0
Total Standard Deviation in ln(k): 16.485468815882555""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_N-1O-u0
Total Standard Deviation in ln(k): 16.485468815882555
""",
)

entry(
    index = 44,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C",
    kinetics = ArrheniusBM(A=(1.54859e-09,'m^3/(mol*s)'), n=4.68226, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11493290927444048, var=4.497508162034086, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C
    Total Standard Deviation in ln(k): 4.540283849290508"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 4.540283849290508""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 4.540283849290508
""",
)

entry(
    index = 45,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_N-1BrCClFHINPSSi->C",
    kinetics = ArrheniusBM(A=(0.0215352,'m^3/(mol*s)'), n=2.37147, w0=(393500,'J/mol'), E0=(39350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_N-1BrCClFHINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_N-1BrCClFHINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_N-1BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_N-1BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(1.70887e-05,'m^3/(mol*s)'), n=3.69265, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.3915802469017444, var=3.994443868534476, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 7.5031173253752375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 7.5031173253752375""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 7.5031173253752375
""",
)

entry(
    index = 47,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(8.52317e-12,'m^3/(mol*s)'), n=5.49282, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6673971725798329, var=1.9347472091678615, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 4.465367398110213"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 4.465367398110213""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 4.465367398110213
""",
)

entry(
    index = 48,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi",
    kinetics = ArrheniusBM(A=(3.61646e-23,'m^3/(mol*s)'), n=9.15458, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3554320204658105, var=31.87299821333461, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi
    Total Standard Deviation in ln(k): 12.21101293653521"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 12.21101293653521""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 12.21101293653521
""",
)

entry(
    index = 49,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi",
    kinetics = ArrheniusBM(A=(2.23403e-06,'m^3/(mol*s)'), n=3.9575, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07865739649703661, var=12.901399079083662, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi
    Total Standard Deviation in ln(k): 7.3983428692647175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 7.3983428692647175""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 7.3983428692647175
""",
)

entry(
    index = 50,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(1.75861e-09,'m^3/(mol*s)'), n=4.84801, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09731321584979163, var=0.1329163997051695, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 0.9753858974008953"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 0.9753858974008953""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 0.9753858974008953
""",
)

entry(
    index = 51,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(1.32859,'m^3/(mol*s)'), n=2.43214, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R_4R!H->O",
    kinetics = ArrheniusBM(A=(0.00466877,'m^3/(mol*s)'), n=2.7407, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(2.65e+06,'m^3/(mol*s)'), n=0, w0=(320000,'J/mol'), E0=(32000,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_Ext-3CClFH-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C",
    kinetics = ArrheniusBM(A=(4.97069e-12,'m^3/(mol*s)'), n=5.5236, w0=(525000,'J/mol'), E0=(140719,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.033591693701774894, var=1.845430132467486, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C
    Total Standard Deviation in ln(k): 2.807765873441461"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C
Total Standard Deviation in ln(k): 2.807765873441461""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C
Total Standard Deviation in ln(k): 2.807765873441461
""",
)

entry(
    index = 55,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->C",
    kinetics = ArrheniusBM(A=(650.29,'m^3/(mol*s)'), n=1.25799, w0=(407770,'J/mol'), E0=(40777,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C",
    kinetics = ArrheniusBM(A=(1.03017e-09,'m^3/(mol*s)'), n=4.58002, w0=(492761,'J/mol'), E0=(169050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00935563781205706, var=3.4059019849475827, Tref=1000.0, N=67, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C',), comment="""BM rule fitted to 67 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C
    Total Standard Deviation in ln(k): 3.7232624495245283"""),
    rank = 11,
    shortDesc = """BM rule fitted to 67 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C
Total Standard Deviation in ln(k): 3.7232624495245283""",
    longDesc = 
"""
BM rule fitted to 67 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C
Total Standard Deviation in ln(k): 3.7232624495245283
""",
)

entry(
    index = 57,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C",
    kinetics = ArrheniusBM(A=(0.00372617,'m^3/(mol*s)'), n=2.8856, w0=(345554,'J/mol'), E0=(34555.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08254786105569109, var=12.53212824902952, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C
    Total Standard Deviation in ln(k): 7.30431843464922"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C
Total Standard Deviation in ln(k): 7.30431843464922""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C
Total Standard Deviation in ln(k): 7.30431843464922
""",
)

entry(
    index = 58,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(3.59681e-13,'m^3/(mol*s)'), n=5.48116, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.5938154419495714, var=11.753201344310492, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 13.389945929442167"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 13.389945929442167""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 13.389945929442167
""",
)

entry(
    index = 59,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(2.03567e-09,'m^3/(mol*s)'), n=4.50755, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07296472142968997, var=5.39132679268238, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl',), comment="""BM rule fitted to 18 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 4.838169092691424"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.838169092691424""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.838169092691424
""",
)

entry(
    index = 60,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.0236e-10,'m^3/(mol*s)'), n=4.99382, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08476037652085233, var=1.1989452614022609, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R
    Total Standard Deviation in ln(k): 2.4080776856429886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 2.4080776856429886""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 2.4080776856429886
""",
)

entry(
    index = 61,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.000178698,'m^3/(mol*s)'), n=3.25898, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_N-1O-u0_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0391196,'m^3/(mol*s)'), n=2.49957, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_N-1O-u0_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_N-1O-u0_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_N-1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_N-1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.6077e-09,'m^3/(mol*s)'), n=4.6769, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11441076464664032, var=4.520367715458942, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.549762835264931"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.549762835264931""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.549762835264931
""",
)

entry(
    index = 64,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(1.88389e-05,'m^3/(mol*s)'), n=3.67829, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7349188394541815, var=5.787534715097743, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 9.181942996781942"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 9.181942996781942""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 9.181942996781942
""",
)

entry(
    index = 65,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(3.55718e-06,'m^3/(mol*s)'), n=3.53988, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(7.11294e-15,'m^3/(mol*s)'), n=6.71706, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.5134766165460327, var=0.690220448585621, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 10.493354714095197"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 10.493354714095197""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 10.493354714095197
""",
)

entry(
    index = 67,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(610.807,'m^3/(mol*s)'), n=1.55186, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.550207163482078, var=45.59400644967791, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 24.969320952097068"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 24.969320952097068""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 24.969320952097068
""",
)

entry(
    index = 68,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(6.27714e-17,'m^3/(mol*s)'), n=7.15605, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.4865716102935784, var=0.295173509184747, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-4R!H-R
    Total Standard Deviation in ln(k): 9.849400196611418"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-4R!H-R
Total Standard Deviation in ln(k): 9.849400196611418""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-4R!H-R
Total Standard Deviation in ln(k): 9.849400196611418
""",
)

entry(
    index = 69,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1",
    kinetics = ArrheniusBM(A=(4.47219e-09,'m^3/(mol*s)'), n=4.59014, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.21375957846849175, var=1.0128779667724632, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1
    Total Standard Deviation in ln(k): 2.5546866080571418"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 2.5546866080571418""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 2.5546866080571418
""",
)

entry(
    index = 70,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.00208502,'m^3/(mol*s)'), n=3.22972, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi",
    kinetics = ArrheniusBM(A=(1.83761e-08,'m^3/(mol*s)'), n=4.50383, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.8781139005948866, var=0.016324873025191505, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi
    Total Standard Deviation in ln(k): 4.975021795505403"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 4.975021795505403""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 4.975021795505403
""",
)

entry(
    index = 72,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi",
    kinetics = ArrheniusBM(A=(0.0387235,'m^3/(mol*s)'), n=2.8378, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.10845e-13,'m^3/(mol*s)'), n=5.80884, w0=(525000,'J/mol'), E0=(139217,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.025154273773971246, var=1.8002289591852365, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.753007093554706"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.753007093554706""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.753007093554706
""",
)

entry(
    index = 74,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C",
    kinetics = ArrheniusBM(A=(7.64651e-07,'m^3/(mol*s)'), n=3.82801, w0=(485000,'J/mol'), E0=(179609,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0054415653667360805, var=3.0930670944047947, Tref=1000.0, N=54, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C',), comment="""BM rule fitted to 54 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C
    Total Standard Deviation in ln(k): 3.5394234536823785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 54 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C
Total Standard Deviation in ln(k): 3.5394234536823785""",
    longDesc = 
"""
BM rule fitted to 54 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C
Total Standard Deviation in ln(k): 3.5394234536823785
""",
)

entry(
    index = 75,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C",
    kinetics = ArrheniusBM(A=(1.91855e-16,'m^3/(mol*s)'), n=6.30373, w0=(525000,'J/mol'), E0=(141895,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04077023090747643, var=5.077461125863184, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C
    Total Standard Deviation in ln(k): 4.619751905118268"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C
Total Standard Deviation in ln(k): 4.619751905118268""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C
Total Standard Deviation in ln(k): 4.619751905118268
""",
)

entry(
    index = 76,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C",
    kinetics = ArrheniusBM(A=(2.45728,'m^3/(mol*s)'), n=2.32225, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.7807159912350998, var=1.629929775054755, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C
    Total Standard Deviation in ln(k): 4.52101724177321"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C
Total Standard Deviation in ln(k): 4.52101724177321""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C
Total Standard Deviation in ln(k): 4.52101724177321
""",
)

entry(
    index = 77,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C",
    kinetics = ArrheniusBM(A=(0.000140373,'m^3/(mol*s)'), n=3.17014, w0=(383885,'J/mol'), E0=(38388.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.2809006797868854, var=0.5618880873888836, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C
    Total Standard Deviation in ln(k): 4.721076686943354"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C
Total Standard Deviation in ln(k): 4.721076686943354""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C
Total Standard Deviation in ln(k): 4.721076686943354
""",
)

entry(
    index = 78,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R",
    kinetics = ArrheniusBM(A=(5.07215e-13,'m^3/(mol*s)'), n=5.43526, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.1206342268118425, var=1.6163558256894626, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R
    Total Standard Deviation in ln(k): 7.876966354307877"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R
Total Standard Deviation in ln(k): 7.876966354307877""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R
Total Standard Deviation in ln(k): 7.876966354307877
""",
)

entry(
    index = 79,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.85918e-06,'m^3/(mol*s)'), n=3.7472, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(3.99469e-10,'m^3/(mol*s)'), n=4.44455, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.133179953688285, var=4.281076974212678, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 6.995135765481606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 6.995135765481606""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 6.995135765481606
""",
)

entry(
    index = 81,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C",
    kinetics = ArrheniusBM(A=(0.00456542,'m^3/(mol*s)'), n=2.86096, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C",
    kinetics = ArrheniusBM(A=(2.9529e-09,'m^3/(mol*s)'), n=4.51469, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07215676686374747, var=5.30293785402587, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C',), comment="""BM rule fitted to 12 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C
    Total Standard Deviation in ln(k): 4.7978241155857235"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C
Total Standard Deviation in ln(k): 4.7978241155857235""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C
Total Standard Deviation in ln(k): 4.7978241155857235
""",
)

entry(
    index = 83,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-1O-R",
    kinetics = ArrheniusBM(A=(7.91658e-06,'m^3/(mol*s)'), n=3.24946, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(8.188e-11,'m^3/(mol*s)'), n=5.08894, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.2509046752593354, var=0.31981063491418454, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 4.276690389631615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 4.276690389631615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 4.276690389631615
""",
)

entry(
    index = 85,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(8.02782e-05,'m^3/(mol*s)'), n=3.4195, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(1.02794e-09,'m^3/(mol*s)'), n=4.66666, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.3517024213613915, var=13.079350306231085, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C
    Total Standard Deviation in ln(k): 10.646438714067369"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 10.646438714067369""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 10.646438714067369
""",
)

entry(
    index = 87,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(0.000298374,'m^3/(mol*s)'), n=3.29159, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-Sp-5R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-Sp-5R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi",
    kinetics = ArrheniusBM(A=(4.21084e-15,'m^3/(mol*s)'), n=6.77562, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7740884642740191, var=0.00606822146475164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
    Total Standard Deviation in ln(k): 4.613675140764854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 4.613675140764854""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 4.613675140764854
""",
)

entry(
    index = 89,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi",
    kinetics = ArrheniusBM(A=(2.35531e-05,'m^3/(mol*s)'), n=3.64716, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.36103604310279, var=10.278956778300604, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
    Total Standard Deviation in ln(k): 12.359594843869335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 12.359594843869335""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 12.359594843869335
""",
)

entry(
    index = 90,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1",
    kinetics = ArrheniusBM(A=(0.0379121,'m^3/(mol*s)'), n=2.90824, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(7.30096,'m^3/(mol*s)'), n=2.36151, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_4R!H->C",
    kinetics = ArrheniusBM(A=(852.398,'m^3/(mol*s)'), n=1.50927, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.2110503909359867, var=2.011641877370481, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_4R!H->C
    Total Standard Deviation in ln(k): 5.886203280674132"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_4R!H->C
Total Standard Deviation in ln(k): 5.886203280674132""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_4R!H->C
Total Standard Deviation in ln(k): 5.886203280674132
""",
)

entry(
    index = 93,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0308105,'m^3/(mol*s)'), n=2.88761, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.00185843,'m^3/(mol*s)'), n=3.22261, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.00381903,'m^3/(mol*s)'), n=3.24993, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(5.26673e-09,'m^3/(mol*s)'), n=4.56717, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.089338357881248, var=8.37112709106314, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl
    Total Standard Deviation in ln(k): 16.074999467436697"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl
Total Standard Deviation in ln(k): 16.074999467436697""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl
Total Standard Deviation in ln(k): 16.074999467436697
""",
)

entry(
    index = 97,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->C",
    kinetics = ArrheniusBM(A=(0.00663277,'m^3/(mol*s)'), n=2.95236, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.00474579,'m^3/(mol*s)'), n=2.96408, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F",
    kinetics = ArrheniusBM(A=(9.26201e-15,'m^3/(mol*s)'), n=6.29417, w0=(525000,'J/mol'), E0=(137597,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.027752504331027713, var=1.1939959784801408, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F
    Total Standard Deviation in ln(k): 2.260306395672714"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 2.260306395672714""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 2.260306395672714
""",
)

entry(
    index = 100,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(1.05691e-18,'m^3/(mol*s)'), n=7.53123, w0=(525000,'J/mol'), E0=(124313,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0031063417496880338, var=3.1443266045882234, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F
    Total Standard Deviation in ln(k): 3.5626510690367823"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.5626510690367823""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 3.5626510690367823
""",
)

entry(
    index = 101,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.33286e-07,'m^3/(mol*s)'), n=3.79707, w0=(485000,'J/mol'), E0=(179790,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008428489964820197, var=3.2482681072097823, Tref=1000.0, N=41, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R',), comment="""BM rule fitted to 41 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.6343015840550406"""),
    rank = 11,
    shortDesc = """BM rule fitted to 41 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.6343015840550406""",
    longDesc = 
"""
BM rule fitted to 41 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.6343015840550406
""",
)

entry(
    index = 102,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O",
    kinetics = ArrheniusBM(A=(6.42533e-07,'m^3/(mol*s)'), n=4.14388, w0=(485000,'J/mol'), E0=(181266,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.3861327134884487, var=5.050479648786694, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O
    Total Standard Deviation in ln(k): 7.988041226299611"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O
Total Standard Deviation in ln(k): 7.988041226299611""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O
Total Standard Deviation in ln(k): 7.988041226299611
""",
)

entry(
    index = 103,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.28123e-07,'m^3/(mol*s)'), n=4.01561, w0=(485000,'J/mol'), E0=(177355,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.014302190630789675, var=4.846676210333897, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O
    Total Standard Deviation in ln(k): 4.449393100059474"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O
Total Standard Deviation in ln(k): 4.449393100059474""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O
Total Standard Deviation in ln(k): 4.449393100059474
""",
)

entry(
    index = 104,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(8.08082e-18,'m^3/(mol*s)'), n=6.69698, w0=(525000,'J/mol'), E0=(139950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.025957989519145613, var=4.887093670007935, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R
    Total Standard Deviation in ln(k): 4.497043201119846"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R
Total Standard Deviation in ln(k): 4.497043201119846""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R
Total Standard Deviation in ln(k): 4.497043201119846
""",
)

entry(
    index = 105,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.31754,'m^3/(mol*s)'), n=2.33057, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.44192778566792, var=8.82980944003045, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R
    Total Standard Deviation in ln(k): 14.605129097582378"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 14.605129097582378""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R
Total Standard Deviation in ln(k): 14.605129097582378
""",
)

entry(
    index = 106,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_3ClF->F",
    kinetics = ArrheniusBM(A=(9924.64,'m^3/(mol*s)'), n=0.717092, w0=(360000,'J/mol'), E0=(36000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_3ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_3ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 107,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_N-3ClF->F",
    kinetics = ArrheniusBM(A=(1592.36,'m^3/(mol*s)'), n=1.06078, w0=(407770,'J/mol'), E0=(40777,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_N-3ClF->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_N-3ClF->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_N-3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->C_N-3ClF->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 108,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R_5R!H->C",
    kinetics = ArrheniusBM(A=(8.19658e-06,'m^3/(mol*s)'), n=3.30549, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 109,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.71299e-05,'m^3/(mol*s)'), n=3.03221, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_4R!H->Cl_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 110,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(5.71601e-10,'m^3/(mol*s)'), n=4.39638, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1514519194264068, var=0.21286846961933933, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 1.305470537665801"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 1.305470537665801""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 1.305470537665801
""",
)

entry(
    index = 111,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(6.05211e-05,'m^3/(mol*s)'), n=3.35051, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 112,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0",
    kinetics = ArrheniusBM(A=(6.18744e-08,'m^3/(mol*s)'), n=4.13941, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.047647944217067535, var=5.859998210017487, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0',), comment="""BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0
    Total Standard Deviation in ln(k): 4.972667495096242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0
Total Standard Deviation in ln(k): 4.972667495096242""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0
Total Standard Deviation in ln(k): 4.972667495096242
""",
)

entry(
    index = 113,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-1O-u0",
    kinetics = ArrheniusBM(A=(1.48522e-14,'m^3/(mol*s)'), n=6.01964, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.083876711029559, var=0.4771251245161931, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-1O-u0',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-1O-u0
    Total Standard Deviation in ln(k): 11.645752369144205"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-1O-u0
Total Standard Deviation in ln(k): 11.645752369144205""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-1O-u0
Total Standard Deviation in ln(k): 11.645752369144205
""",
)

entry(
    index = 114,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_4R!H->C",
    kinetics = ArrheniusBM(A=(2.41917e-05,'m^3/(mol*s)'), n=3.5172, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(4.33685e-06,'m^3/(mol*s)'), n=3.64876, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_N-3C-u1_1O-u0_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 116,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C",
    kinetics = ArrheniusBM(A=(4.23979e-05,'m^3/(mol*s)'), n=3.13243, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 117,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.000143384,'m^3/(mol*s)'), n=3.37398, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->C_1BrCClFHINPSSi->C_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 118,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(8.38302e-05,'m^3/(mol*s)'), n=3.60203, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 119,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.69582e-06,'m^3/(mol*s)'), n=3.94767, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 120,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(0.000776459,'m^3/(mol*s)'), n=3.19024, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 121,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C",
    kinetics = ArrheniusBM(A=(5.27349e-06,'m^3/(mol*s)'), n=3.9638, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 122,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->C",
    kinetics = ArrheniusBM(A=(6.65995e-06,'m^3/(mol*s)'), n=3.94804, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->C_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 123,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_4R!H->C_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(8894.88,'m^3/(mol*s)'), n=1.40589, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_4R!H->C_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_4R!H->C_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_4R!H->C_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R_4R!H->C_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 124,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl_4CO->C",
    kinetics = ArrheniusBM(A=(0.00184567,'m^3/(mol*s)'), n=2.97286, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl_4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl_4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl_4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 125,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl_N-4CO->C",
    kinetics = ArrheniusBM(A=(0.00678858,'m^3/(mol*s)'), n=3.1372, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl_N-4CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl_N-4CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-Sp-4R!H=1BrBrCCClClFFHHIINNPPSSSiSi_3O-u1_N-4R!H->Cl_N-4CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 126,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.03799e-10,'m^3/(mol*s)'), n=5.06486, w0=(525000,'J/mol'), E0=(152351,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02953432147731484, var=1.599096206532734, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 2.609302113527011"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 2.609302113527011""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 2.609302113527011
""",
)

entry(
    index = 127,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.032e-26,'m^3/(mol*s)'), n=9.90288, w0=(525000,'J/mol'), E0=(116562,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.058695930783885734, var=7.496794293032538, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 5.636496876150599"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 5.636496876150599""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 5.636496876150599
""",
)

entry(
    index = 128,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(5.18265e-09,'m^3/(mol*s)'), n=4.74784, w0=(525000,'J/mol'), E0=(139116,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_4BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 129,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(4.11263e-11,'m^3/(mol*s)'), n=5.27164, w0=(525000,'J/mol'), E0=(135560,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.003543011947269653, var=3.6447746491027115, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 3.836200496674773"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 3.836200496674773""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 3.836200496674773
""",
)

entry(
    index = 130,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F",
    kinetics = ArrheniusBM(A=(2.28837e-06,'m^3/(mol*s)'), n=3.71838, w0=(485000,'J/mol'), E0=(180882,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.009951614314274956, var=2.914180673481344, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F',), comment="""BM rule fitted to 20 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F
    Total Standard Deviation in ln(k): 3.4472815896341746"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 3.4472815896341746""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F
Total Standard Deviation in ln(k): 3.4472815896341746
""",
)

entry(
    index = 131,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(1.89321e-07,'m^3/(mol*s)'), n=3.94134, w0=(485000,'J/mol'), E0=(177883,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.005531939291842832, var=4.524620467278421, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F',), comment="""BM rule fitted to 21 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F
    Total Standard Deviation in ln(k): 4.278202456578295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 4.278202456578295""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F
Total Standard Deviation in ln(k): 4.278202456578295
""",
)

entry(
    index = 132,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.70352e-09,'m^3/(mol*s)'), n=4.77004, w0=(485000,'J/mol'), E0=(144580,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1",
    kinetics = ArrheniusBM(A=(5.72946e-07,'m^3/(mol*s)'), n=4.15811, w0=(485000,'J/mol'), E0=(181329,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4174748882469086, var=0.35420717895735976, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1
    Total Standard Deviation in ln(k): 2.2420561196158086"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1
Total Standard Deviation in ln(k): 2.2420561196158086""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1
Total Standard Deviation in ln(k): 2.2420561196158086
""",
)

entry(
    index = 134,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_N-3C-u1",
    kinetics = ArrheniusBM(A=(2.30271e-08,'m^3/(mol*s)'), n=4.64603, w0=(485000,'J/mol'), E0=(171336,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_N-3C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_N-3C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_N-3C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_N-3C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 135,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C",
    kinetics = ArrheniusBM(A=(4.76209e-06,'m^3/(mol*s)'), n=3.70949, w0=(485000,'J/mol'), E0=(182151,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.4311660554943038e-05, var=0.02687277046242829, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C
    Total Standard Deviation in ln(k): 0.3286956277292756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C
Total Standard Deviation in ln(k): 0.3286956277292756""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C
Total Standard Deviation in ln(k): 0.3286956277292756
""",
)

entry(
    index = 136,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C",
    kinetics = ArrheniusBM(A=(1.26737e-07,'m^3/(mol*s)'), n=4.01647, w0=(485000,'J/mol'), E0=(177340,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01581125478643037, var=4.890967654767977, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C
    Total Standard Deviation in ln(k): 4.473305090954158"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C
Total Standard Deviation in ln(k): 4.473305090954158""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C
Total Standard Deviation in ln(k): 4.473305090954158
""",
)

entry(
    index = 137,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(4.11578e-17,'m^3/(mol*s)'), n=6.40252, w0=(525000,'J/mol'), E0=(145244,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.007228633777387501, var=0.002141994196647775, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_4R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 0.11094491010866375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 0.11094491010866375""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 0.11094491010866375
""",
)

entry(
    index = 138,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(3.37419e-15,'m^3/(mol*s)'), n=5.93932, w0=(525000,'J/mol'), E0=(144641,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07527814724672165, var=5.875320500638806, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 5.048430540269719"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.048430540269719""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.048430540269719
""",
)

entry(
    index = 139,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_4R!H->O",
    kinetics = ArrheniusBM(A=(13.7245,'m^3/(mol*s)'), n=2.18372, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 140,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.01241e+11,'m^3/(mol*s)'), n=-0.712343, w0=(320000,'J/mol'), E0=(32000,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 141,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(7.78646e-05,'m^3/(mol*s)'), n=3.27081, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 142,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(7.04161e-10,'m^3/(mol*s)'), n=4.36588, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.950409384805848, var=6.080236123109848, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R
    Total Standard Deviation in ln(k): 14.868954500301331"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R
Total Standard Deviation in ln(k): 14.868954500301331""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R
Total Standard Deviation in ln(k): 14.868954500301331
""",
)

entry(
    index = 143,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.0828e-05,'m^3/(mol*s)'), n=3.32034, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.017170782830203898, var=14.207106436828447, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R
    Total Standard Deviation in ln(k): 7.599453362713257"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 7.599453362713257""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 7.599453362713257
""",
)

entry(
    index = 144,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(3.15929e-11,'m^3/(mol*s)'), n=4.93493, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.8547403917677726, var=2.197966462010349, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 5.119716998969156"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 5.119716998969156""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 5.119716998969156
""",
)

entry(
    index = 145,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(1.80369e-10,'m^3/(mol*s)'), n=4.98214, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.9466536655698956, var=0.012602250003397883, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C
    Total Standard Deviation in ln(k): 5.116140657493307"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 5.116140657493307""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C
Total Standard Deviation in ln(k): 5.116140657493307
""",
)

entry(
    index = 146,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-1O-u0_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.99453,'m^3/(mol*s)'), n=1.8271, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-1O-u0_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-1O-u0_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_N-1O-u0_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 147,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(5.79418e-12,'m^3/(mol*s)'), n=5.47211, w0=(525000,'J/mol'), E0=(150876,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.017372276833230713, var=0.7174068164312726, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F
    Total Standard Deviation in ln(k): 1.7416569632110341"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 1.7416569632110341""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 1.7416569632110341
""",
)

entry(
    index = 148,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(1.85782e-10,'m^3/(mol*s)'), n=5.15141, w0=(525000,'J/mol'), E0=(149713,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0009402769607573503, var=4.4048988860125755, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 4.2098706100473375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 4.2098706100473375""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 4.2098706100473375
""",
)

entry(
    index = 149,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.71142e-12,'m^3/(mol*s)'), n=5.47558, w0=(525000,'J/mol'), E0=(155904,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 150,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C_4ClO->O",
    kinetics = ArrheniusBM(A=(3.31829e-08,'m^3/(mol*s)'), n=4.48236, w0=(525000,'J/mol'), E0=(140114,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C_4ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C_4ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C_4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C_4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 151,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C_N-4ClO->O",
    kinetics = ArrheniusBM(A=(3.57367e-11,'m^3/(mol*s)'), n=5.32561, w0=(525000,'J/mol'), E0=(143057,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C_N-4ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C_N-4ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C_N-4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_N-4R!H->F_N-4BrCClINOPSSi->C_N-4ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 152,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.79479e-05,'m^3/(mol*s)'), n=3.46149, w0=(485000,'J/mol'), E0=(186065,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01788238434162192, var=4.127268586292572, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 4.117686269154602"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 4.117686269154602""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 4.117686269154602
""",
)

entry(
    index = 153,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.06255e-07,'m^3/(mol*s)'), n=3.98773, w0=(485000,'J/mol'), E0=(174037,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.005325835264088771, var=1.1696573866661102, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 2.1815165109235406"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 2.1815165109235406""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 2.1815165109235406
""",
)

entry(
    index = 154,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(1.307e-06,'m^3/(mol*s)'), n=3.72496, w0=(485000,'J/mol'), E0=(188161,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.016913861791866998, var=14.024226402142295, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 7.550016253362189"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 7.550016253362189""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 7.550016253362189
""",
)

entry(
    index = 155,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C",
    kinetics = ArrheniusBM(A=(6.47935e-08,'m^3/(mol*s)'), n=4.0565, w0=(485000,'J/mol'), E0=(170840,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.5097861724833356e-05, var=0.07364380905733384, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
    Total Standard Deviation in ln(k): 0.5440958934632569"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 0.5440958934632569""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C
Total Standard Deviation in ln(k): 0.5440958934632569
""",
)

entry(
    index = 156,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1_Sp-4O-3C",
    kinetics = ArrheniusBM(A=(5.08817e-08,'m^3/(mol*s)'), n=4.28857, w0=(485000,'J/mol'), E0=(172152,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1_Sp-4O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1_Sp-4O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1_Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1_Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 157,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1_N-Sp-4O-3C",
    kinetics = ArrheniusBM(A=(3.80839e-08,'m^3/(mol*s)'), n=4.48675, w0=(485000,'J/mol'), E0=(177640,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1_N-Sp-4O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1_N-Sp-4O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1_N-Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_4R!H->O_3C-u1_N-Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 158,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.75844e-07,'m^3/(mol*s)'), n=3.95233, w0=(485000,'J/mol'), E0=(177409,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 159,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(3.95048e-07,'m^3/(mol*s)'), n=3.95952, w0=(485000,'J/mol'), E0=(174094,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0012331215500945563, var=1.46495177207565, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 2.4295332468811854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 2.4295332468811854""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 2.4295332468811854
""",
)

entry(
    index = 160,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(1.32244e-07,'m^3/(mol*s)'), n=4.01041, w0=(485000,'J/mol'), E0=(177408,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.019120301368771762, var=4.970388216955861, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 4.517471011389043"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 4.517471011389043""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 4.517471011389043
""",
)

entry(
    index = 161,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.15712e-16,'m^3/(mol*s)'), n=6.26519, w0=(525000,'J/mol'), E0=(145764,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 162,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.78036e-15,'m^3/(mol*s)'), n=6.01647, w0=(525000,'J/mol'), E0=(153131,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05032725295447305, var=5.180874850450325, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 4.689535189077755"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 4.689535189077755""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 4.689535189077755
""",
)

entry(
    index = 163,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(6.65071e-12,'m^3/(mol*s)'), n=5.01807, w0=(525000,'J/mol'), E0=(133788,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 164,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.63846e-26,'m^3/(mol*s)'), n=9.24693, w0=(525000,'J/mol'), E0=(106972,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10604700487427444, var=6.921556171178569, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 5.540677314791053"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 5.540677314791053""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 5.540677314791053
""",
)

entry(
    index = 165,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.20903e-06,'m^3/(mol*s)'), n=3.28294, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 166,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(8.73382e-05,'m^3/(mol*s)'), n=3.25083, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3C_Ext-1O-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 167,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000166381,'m^3/(mol*s)'), n=3.31384, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 168,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C",
    kinetics = ArrheniusBM(A=(1.34911e-13,'m^3/(mol*s)'), n=5.81796, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.464946332269444, var=0.07527431322931927, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C
    Total Standard Deviation in ln(k): 6.743354910350834"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 6.743354910350834""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 6.743354910350834
""",
)

entry(
    index = 169,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C",
    kinetics = ArrheniusBM(A=(2.39636e-06,'m^3/(mol*s)'), n=3.56772, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.645611790368113, var=5.451035485260281, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C
    Total Standard Deviation in ln(k): 11.327811548561014"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 11.327811548561014""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 11.327811548561014
""",
)

entry(
    index = 170,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(3.25904e-11,'m^3/(mol*s)'), n=4.92926, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.370951319807854, var=3.072186093927471, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.983556954661235"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.983556954661235""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.983556954661235
""",
)

entry(
    index = 171,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(5.82554e-05,'m^3/(mol*s)'), n=3.41553, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.82278e-05,'m^3/(mol*s)'), n=3.44719, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 173,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.000493877,'m^3/(mol*s)'), n=3.13091, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_N-Sp-4BrCFINOPSSi-3C_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 174,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.15669e-12,'m^3/(mol*s)'), n=5.45839, w0=(525000,'J/mol'), E0=(151215,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006544387034775606, var=2.395818038985693, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 3.1194583958142026"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 3.1194583958142026""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 3.1194583958142026
""",
)

entry(
    index = 175,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.84865e-10,'m^3/(mol*s)'), n=5.13872, w0=(525000,'J/mol'), E0=(142746,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 176,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.97103e-12,'m^3/(mol*s)'), n=5.8457, w0=(525000,'J/mol'), E0=(161627,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 177,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(0.000246241,'m^3/(mol*s)'), n=3.17463, w0=(485000,'J/mol'), E0=(192749,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.029755635180759205, var=5.724413885025939, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F
    Total Standard Deviation in ln(k): 4.871241408417649"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 4.871241408417649""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F
Total Standard Deviation in ln(k): 4.871241408417649
""",
)

entry(
    index = 178,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(1.02012e-07,'m^3/(mol*s)'), n=3.97758, w0=(485000,'J/mol'), E0=(168494,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.001769693887978604, var=0.8762147839669387, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 1.881005701586985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 1.881005701586985""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F
Total Standard Deviation in ln(k): 1.881005701586985
""",
)

entry(
    index = 179,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.31087e-07,'m^3/(mol*s)'), n=3.93087, w0=(485000,'J/mol'), E0=(172008,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0062944775787386106, var=1.2541702991061976, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 2.2609129719253898"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 2.2609129719253898""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 2.2609129719253898
""",
)

entry(
    index = 180,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.56386e-07,'m^3/(mol*s)'), n=4.12895, w0=(485000,'J/mol'), E0=(179108,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0002754387190914514, var=7.694659843179849, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 5.561676784078894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 5.561676784078894""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 5.561676784078894
""",
)

entry(
    index = 181,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000290984,'m^3/(mol*s)'), n=2.90276, w0=(485000,'J/mol'), E0=(199541,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.010502957893935391, var=77.16445026583, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R
    Total Standard Deviation in ln(k): 17.636643449221157"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R
Total Standard Deviation in ln(k): 17.636643449221157""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R
Total Standard Deviation in ln(k): 17.636643449221157
""",
)

entry(
    index = 182,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.45303e-08,'m^3/(mol*s)'), n=4.17306, w0=(485000,'J/mol'), E0=(182438,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.001635674110206193, var=7.761657678098837, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R
    Total Standard Deviation in ln(k): 5.589251892874224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R
Total Standard Deviation in ln(k): 5.589251892874224""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R
Total Standard Deviation in ln(k): 5.589251892874224
""",
)

entry(
    index = 183,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(5.7299e-06,'m^3/(mol*s)'), n=3.76087, w0=(485000,'J/mol'), E0=(183376,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 184,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.73532e-06,'m^3/(mol*s)'), n=4.00456, w0=(485000,'J/mol'), E0=(181794,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 185,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0",
    kinetics = ArrheniusBM(A=(6.41365e-08,'m^3/(mol*s)'), n=4.05781, w0=(485000,'J/mol'), E0=(170835,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00010679715559373652, var=0.06719412645563655, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0
    Total Standard Deviation in ln(k): 0.5199323509570245"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0
Total Standard Deviation in ln(k): 0.5199323509570245""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0
Total Standard Deviation in ln(k): 0.5199323509570245
""",
)

entry(
    index = 186,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0",
    kinetics = ArrheniusBM(A=(1.71756e-05,'m^3/(mol*s)'), n=3.34293, w0=(485000,'J/mol'), E0=(173252,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0007537587377139414, var=30.19947457312595, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0
    Total Standard Deviation in ln(k): 11.018724753100692"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0
Total Standard Deviation in ln(k): 11.018724753100692""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0
Total Standard Deviation in ln(k): 11.018724753100692
""",
)

entry(
    index = 187,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.95993e-10,'m^3/(mol*s)'), n=4.92183, w0=(485000,'J/mol'), E0=(161867,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 188,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_3C-u1",
    kinetics = ArrheniusBM(A=(4.05817e-07,'m^3/(mol*s)'), n=4.03215, w0=(485000,'J/mol'), E0=(177118,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.8637572374725925e-06, var=0.12014251932492087, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_3C-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_3C-u1
    Total Standard Deviation in ln(k): 0.6948775542874985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_3C-u1
Total Standard Deviation in ln(k): 0.6948775542874985""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_3C-u1
Total Standard Deviation in ln(k): 0.6948775542874985
""",
)

entry(
    index = 189,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_N-3C-u1",
    kinetics = ArrheniusBM(A=(2.34026e-06,'m^3/(mol*s)'), n=3.43997, w0=(485000,'J/mol'), E0=(169290,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_N-3C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_N-3C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_N-3C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_N-3C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 190,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.61204e-06,'m^3/(mol*s)'), n=3.58526, w0=(485000,'J/mol'), E0=(181607,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00022631833014578358, var=12.228514838609932, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C_Ext-3C-R
    Total Standard Deviation in ln(k): 7.010985558588161"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 7.010985558588161""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 7.010985558588161
""",
)

entry(
    index = 191,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.11064e-19,'m^3/(mol*s)'), n=6.86471, w0=(525000,'J/mol'), E0=(150428,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008250898789663395, var=0.5662447045455631, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 1.529278668021001"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.529278668021001""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.529278668021001
""",
)

entry(
    index = 192,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(9.75057e-20,'m^3/(mol*s)'), n=7.42961, w0=(525000,'J/mol'), E0=(134864,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006993185198489049, var=0.758062961296386, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 1.7630297220257618"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 1.7630297220257618""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 1.7630297220257618
""",
)

entry(
    index = 193,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(7.53336e-17,'m^3/(mol*s)'), n=6.46816, w0=(525000,'J/mol'), E0=(155088,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.004092725769325478, var=3.458320173659418, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 3.7384007030001363"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.7384007030001363""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.7384007030001363
""",
)

entry(
    index = 194,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O",
    kinetics = ArrheniusBM(A=(7.08102e-11,'m^3/(mol*s)'), n=4.69071, w0=(525000,'J/mol'), E0=(135480,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 195,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->O",
    kinetics = ArrheniusBM(A=(1.30715e-40,'m^3/(mol*s)'), n=13.3384, w0=(525000,'J/mol'), E0=(77110.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1307539537427937, var=13.730307761205584, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->O
    Total Standard Deviation in ln(k): 7.756959063756332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 7.756959063756332""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 7.756959063756332
""",
)

entry(
    index = 196,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.00346669,'m^3/(mol*s)'), n=2.70977, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 197,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(4.11983e-05,'m^3/(mol*s)'), n=3.20075, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Ext-3C-R_N-Sp-4BrBrCCFFIINNOOPPSSSiSi=3C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 198,
    label = "Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(6.6276e-05,'m^3/(mol*s)'), n=3.32892, w0=(353500,'J/mol'), E0=(35350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_3CClFH->C_3C-u1_Ext-3C-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCFFFIIINNNOOOPPPSSSSiSiSi#3C_1O-u0_Sp-4BrCFINOPSSi-3C_4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 199,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.77578e-14,'m^3/(mol*s)'), n=6.28933, w0=(525000,'J/mol'), E0=(145887,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 200,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(5.8332e-12,'m^3/(mol*s)'), n=5.5678, w0=(525000,'J/mol'), E0=(161841,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 201,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000370491,'m^3/(mol*s)'), n=3.08702, w0=(485000,'J/mol'), E0=(196348,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02848650269683633, var=5.283655633344114, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 4.679699024925543"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 4.679699024925543""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 4.679699024925543
""",
)

entry(
    index = 202,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.65855e-06,'m^3/(mol*s)'), n=3.87161, w0=(485000,'J/mol'), E0=(177448,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R",
    kinetics = ArrheniusBM(A=(7.73317e-08,'m^3/(mol*s)'), n=3.99695, w0=(485000,'J/mol'), E0=(170292,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=6.975038903906338e-06, var=0.04065094690032448, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R
    Total Standard Deviation in ln(k): 0.4042138148566928"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R
Total Standard Deviation in ln(k): 0.4042138148566928""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R
Total Standard Deviation in ln(k): 0.4042138148566928
""",
)

entry(
    index = 204,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.95802e-07,'m^3/(mol*s)'), n=3.90196, w0=(485000,'J/mol'), E0=(174049,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-6.530359227673369e-06, var=2.783387116589018, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 3.344613407012691"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 3.344613407012691""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 3.344613407012691
""",
)

entry(
    index = 205,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(5.04361e-08,'m^3/(mol*s)'), n=4.10483, w0=(485000,'J/mol'), E0=(168785,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.6738307325119347e-05, var=2.4460920713873193, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 3.1354451992442574"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 3.1354451992442574""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 3.1354451992442574
""",
)

entry(
    index = 206,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrClFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(1.54468e-07,'m^3/(mol*s)'), n=4.12162, w0=(485000,'J/mol'), E0=(170449,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrClFINOPSSi-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrClFINOPSSi-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrClFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrClFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 207,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrClFINOPSSi-3C",
    kinetics = ArrheniusBM(A=(1.87844e-08,'m^3/(mol*s)'), n=4.39321, w0=(485000,'J/mol'), E0=(184841,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrClFINOPSSi-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrClFINOPSSi-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrClFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrClFINOPSSi-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 208,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000286994,'m^3/(mol*s)'), n=2.90358, w0=(485000,'J/mol'), E0=(199573,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0006636833714657947, var=78.0632175147724, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 17.714181817642082"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 17.714181817642082""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 17.714181817642082
""",
)

entry(
    index = 209,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.4001e-08,'m^3/(mol*s)'), n=4.27788, w0=(485000,'J/mol'), E0=(177321,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 210,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.16735e-08,'m^3/(mol*s)'), n=4.24972, w0=(485000,'J/mol'), E0=(186105,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 211,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O",
    kinetics = ArrheniusBM(A=(2.13344e-07,'m^3/(mol*s)'), n=3.89647, w0=(485000,'J/mol'), E0=(171814,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.003370774581583255, var=0.2200580327637282, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O
    Total Standard Deviation in ln(k): 0.948897394013514"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O
Total Standard Deviation in ln(k): 0.948897394013514""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O
Total Standard Deviation in ln(k): 0.948897394013514
""",
)

entry(
    index = 212,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O",
    kinetics = ArrheniusBM(A=(2.54344e-08,'m^3/(mol*s)'), n=4.18183, w0=(485000,'J/mol'), E0=(170079,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.001103275703674716, var=0.029434242687611217, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O
    Total Standard Deviation in ln(k): 0.34671263211222814"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O
Total Standard Deviation in ln(k): 0.34671263211222814""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O
Total Standard Deviation in ln(k): 0.34671263211222814
""",
)

entry(
    index = 213,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0_4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.00057304,'m^3/(mol*s)'), n=2.60489, w0=(485000,'J/mol'), E0=(176378,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0_4BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0_4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 214,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0_N-4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.25043e-05,'m^3/(mol*s)'), n=3.69111, w0=(485000,'J/mol'), E0=(179560,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0_N-4BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0_N-4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_N-1C-u0_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 215,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_3C-u1_Ext-4C-R",
    kinetics = ArrheniusBM(A=(3.18213e-08,'m^3/(mol*s)'), n=4.33747, w0=(485000,'J/mol'), E0=(174537,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_3C-u1_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_3C-u1_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_3C-u1_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_4BrCClFINPSSi->C_3C-u1_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 216,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.12044e-06,'m^3/(mol*s)'), n=3.28057, w0=(485000,'J/mol'), E0=(178048,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-3C-R_N-4R!H->O_N-Sp-4BrBrCCClClFFIINNPPSSSiSi=3C_N-4BrCClFINPSSi->C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 217,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.40488e-20,'m^3/(mol*s)'), n=7.16576, w0=(525000,'J/mol'), E0=(135451,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 218,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(5.16046e-17,'m^3/(mol*s)'), n=6.21158, w0=(525000,'J/mol'), E0=(153471,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_Ext-3C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 219,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(3.97188e-24,'m^3/(mol*s)'), n=8.75221, w0=(525000,'J/mol'), E0=(123923,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 220,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O",
    kinetics = ArrheniusBM(A=(3.41588e-16,'m^3/(mol*s)'), n=6.33412, w0=(525000,'J/mol'), E0=(154556,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 221,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O",
    kinetics = ArrheniusBM(A=(6.45222e-17,'m^3/(mol*s)'), n=6.24256, w0=(525000,'J/mol'), E0=(146285,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-1CClH->C_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 222,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.6722e-05,'m^3/(mol*s)'), n=3.37338, w0=(485000,'J/mol'), E0=(197549,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.018834614857479653, var=6.094709979799378, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 4.996506142274279"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 4.996506142274279""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 4.996506142274279
""",
)

entry(
    index = 223,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_6R!H->C",
    kinetics = ArrheniusBM(A=(5.66169e-06,'m^3/(mol*s)'), n=3.44838, w0=(485000,'J/mol'), E0=(175075,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 224,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3.50479e-07,'m^3/(mol*s)'), n=3.85832, w0=(485000,'J/mol'), E0=(174302,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_N-5R!H->F_Ext-5BrCClINOPSSi-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 225,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.31087e-08,'m^3/(mol*s)'), n=4.12499, w0=(485000,'J/mol'), E0=(169304,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 226,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(8.44929e-09,'m^3/(mol*s)'), n=4.37139, w0=(485000,'J/mol'), E0=(169995,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 227,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(4.03486e-08,'m^3/(mol*s)'), n=4.17928, w0=(485000,'J/mol'), E0=(166627,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 228,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3.13797e-09,'m^3/(mol*s)'), n=4.38351, w0=(485000,'J/mol'), E0=(166316,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 229,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.95992e-06,'m^3/(mol*s)'), n=3.05765, w0=(485000,'J/mol'), E0=(193184,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 230,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(2.47232e-06,'m^3/(mol*s)'), n=3.97637, w0=(485000,'J/mol'), E0=(195946,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_Ext-1C-R_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 231,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.00776e-07,'m^3/(mol*s)'), n=3.90343, w0=(485000,'J/mol'), E0=(171804,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0026484776413376303, var=0.15470862751029196, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R
    Total Standard Deviation in ln(k): 0.7951772676632365"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R
Total Standard Deviation in ln(k): 0.7951772676632365""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R
Total Standard Deviation in ln(k): 0.7951772676632365
""",
)

entry(
    index = 232,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.38922e-05,'m^3/(mol*s)'), n=3.5758, w0=(485000,'J/mol'), E0=(154793,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 233,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.5685e-08,'m^3/(mol*s)'), n=4.17975, w0=(485000,'J/mol'), E0=(170093,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0008544414652520148, var=0.014168326175359961, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R
    Total Standard Deviation in ln(k): 0.2407720143380839"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R
Total Standard Deviation in ln(k): 0.2407720143380839""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R
Total Standard Deviation in ln(k): 0.2407720143380839
""",
)

entry(
    index = 234,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.21333e-05,'m^3/(mol*s)'), n=3.66599, w0=(485000,'J/mol'), E0=(172409,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 235,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-4C-R",
    kinetics = ArrheniusBM(A=(4.51365e-06,'m^3/(mol*s)'), n=3.78897, w0=(485000,'J/mol'), E0=(179111,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 236,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(0.000380314,'m^3/(mol*s)'), n=3.12476, w0=(485000,'J/mol'), E0=(198436,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02396829568603455, var=11.894739965197545, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C
    Total Standard Deviation in ln(k): 6.97430288714413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C
Total Standard Deviation in ln(k): 6.97430288714413""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C
Total Standard Deviation in ln(k): 6.97430288714413
""",
)

entry(
    index = 237,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(6.00891e-07,'m^3/(mol*s)'), n=3.89114, w0=(485000,'J/mol'), E0=(195632,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.001697830325715902, var=0.9476927994782982, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 1.9558657723985715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C
Total Standard Deviation in ln(k): 1.9558657723985715""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C
Total Standard Deviation in ln(k): 1.9558657723985715
""",
)

entry(
    index = 238,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.38884e-07,'m^3/(mol*s)'), n=3.87759, w0=(485000,'J/mol'), E0=(172181,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0024089690340698884, var=0.48770819410998706, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 1.406081634110363"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.406081634110363""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.406081634110363
""",
)

entry(
    index = 239,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_5R!H->O",
    kinetics = ArrheniusBM(A=(9.11574e-08,'m^3/(mol*s)'), n=4.14961, w0=(485000,'J/mol'), E0=(178389,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 240,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(1.98506e-08,'m^3/(mol*s)'), n=4.17102, w0=(485000,'J/mol'), E0=(167620,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0010131353730713755, var=0.020954346719689352, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 0.29274332385204155"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O
Total Standard Deviation in ln(k): 0.29274332385204155""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O
Total Standard Deviation in ln(k): 0.29274332385204155
""",
)

entry(
    index = 241,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_6R!H->C",
    kinetics = ArrheniusBM(A=(0.000351338,'m^3/(mol*s)'), n=2.76265, w0=(485000,'J/mol'), E0=(195747,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 242,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.00012297,'m^3/(mol*s)'), n=3.40024, w0=(485000,'J/mol'), E0=(198703,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.019773130397042742, var=15.040630493671285, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C
    Total Standard Deviation in ln(k): 7.824495274804495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C
Total Standard Deviation in ln(k): 7.824495274804495""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C
Total Standard Deviation in ln(k): 7.824495274804495
""",
)

entry(
    index = 243,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C_Ext-6R!H-R_8R!H->C",
    kinetics = ArrheniusBM(A=(3.8501e-07,'m^3/(mol*s)'), n=3.92844, w0=(485000,'J/mol'), E0=(191227,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C_Ext-6R!H-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C_Ext-6R!H-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C_Ext-6R!H-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C_Ext-6R!H-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 244,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C_Ext-6R!H-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(6.83125e-07,'m^3/(mol*s)'), n=3.8806, w0=(485000,'J/mol'), E0=(198994,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C_Ext-6R!H-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C_Ext-6R!H-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C_Ext-6R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_N-7R!H->C_Ext-6R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 245,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(4.11856e-08,'m^3/(mol*s)'), n=4.0381, w0=(485000,'J/mol'), E0=(164691,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 246,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(6.32707e-08,'m^3/(mol*s)'), n=4.09227, w0=(485000,'J/mol'), E0=(175505,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_4BrCClINOPSSi->O_Ext-3C-R_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 247,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.04701e-08,'m^3/(mol*s)'), n=4.14997, w0=(485000,'J/mol'), E0=(166830,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-7.359841145413255e-05, var=0.06445471923366558, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R
    Total Standard Deviation in ln(k): 0.5091457387771255"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R
Total Standard Deviation in ln(k): 0.5091457387771255""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R
Total Standard Deviation in ln(k): 0.5091457387771255
""",
)

entry(
    index = 248,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.21606e-05,'m^3/(mol*s)'), n=3.51576, w0=(485000,'J/mol'), E0=(197400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0004834246094771695, var=9.791643155533194, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 6.274351721735911"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.274351721735911""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.274351721735911
""",
)

entry(
    index = 249,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(7.80562e-08,'m^3/(mol*s)'), n=3.96948, w0=(485000,'J/mol'), E0=(168330,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 250,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.03271e-07,'m^3/(mol*s)'), n=3.97927, w0=(485000,'J/mol'), E0=(169732,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_N-4R!H->F_N-Sp-4BrBrCCClClIINNOOPPSSSiSi=1C_1C-u0_N-4BrCClINOPSSi->O_Ext-3C-R_N-5R!H->O_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 251,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R_Ext-7C-R_10R!H->C",
    kinetics = ArrheniusBM(A=(2.85326e-05,'m^3/(mol*s)'), n=3.50515, w0=(485000,'J/mol'), E0=(194800,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R_Ext-7C-R_10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R_Ext-7C-R_10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R_Ext-7C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R_Ext-7C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 252,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R_Ext-7C-R_N-10R!H->C",
    kinetics = ArrheniusBM(A=(6.10895e-08,'m^3/(mol*s)'), n=4.11325, w0=(485000,'J/mol'), E0=(197025,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R_Ext-7C-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R_Ext-7C-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R_Ext-7C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_1CClH->C_Ext-1C-R_4R!H->F_Ext-1C-R_5R!H->F_Ext-1C-R_Ext-3C-R_7R!H->C_N-6R!H->C_Ext-7C-R_Ext-7C-R_Ext-3C-R_Ext-7C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

