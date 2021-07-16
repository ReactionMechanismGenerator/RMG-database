#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(221.01,'m^3/(mol*s)'), n=1.39829, w0=(570329,'J/mol'), E0=(16972.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.011946704168069176, var=2.259745487620514, Tref=1000.0, N=316, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 316 training reactions at node Root
    Total Standard Deviation in ln(k): 3.043624797785317"""),
    rank = 11,
    shortDesc = """BM rule fitted to 316 training reactions at node Root
Total Standard Deviation in ln(k): 3.043624797785317""",
    longDesc = 
"""
BM rule fitted to 316 training reactions at node Root
Total Standard Deviation in ln(k): 3.043624797785317
""",
)

entry(
    index = 2,
    label = "Root_Ext-4R-R",
    kinetics = ArrheniusBM(A=(70.9301,'m^3/(mol*s)'), n=1.54486, w0=(570370,'J/mol'), E0=(15336.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.030022820943838714, var=3.5795240369659616, Tref=1000.0, N=131, data_mean=0.0, correlation='Root_Ext-4R-R',), comment="""BM rule fitted to 131 training reactions at node Root_Ext-4R-R
    Total Standard Deviation in ln(k): 3.8683188378066173"""),
    rank = 11,
    shortDesc = """BM rule fitted to 131 training reactions at node Root_Ext-4R-R
Total Standard Deviation in ln(k): 3.8683188378066173""",
    longDesc = 
"""
BM rule fitted to 131 training reactions at node Root_Ext-4R-R
Total Standard Deviation in ln(k): 3.8683188378066173
""",
)

entry(
    index = 3,
    label = "Root_4R->C",
    kinetics = ArrheniusBM(A=(35.5603,'m^3/(mol*s)'), n=1.44501, w0=(546415,'J/mol'), E0=(73318.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12533146483060567, var=1.1731280443544436, Tref=1000.0, N=47, data_mean=0.0, correlation='Root_4R->C',), comment="""BM rule fitted to 47 training reactions at node Root_4R->C
    Total Standard Deviation in ln(k): 2.48625250232788"""),
    rank = 11,
    shortDesc = """BM rule fitted to 47 training reactions at node Root_4R->C
Total Standard Deviation in ln(k): 2.48625250232788""",
    longDesc = 
"""
BM rule fitted to 47 training reactions at node Root_4R->C
Total Standard Deviation in ln(k): 2.48625250232788
""",
)

entry(
    index = 4,
    label = "Root_N-4R->C",
    kinetics = ArrheniusBM(A=(1765.33,'m^3/(mol*s)'), n=1.17594, w0=(578435,'J/mol'), E0=(52066.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03445458812513443, var=1.1542777959527137, Tref=1000.0, N=138, data_mean=0.0, correlation='Root_N-4R->C',), comment="""BM rule fitted to 138 training reactions at node Root_N-4R->C
    Total Standard Deviation in ln(k): 2.2404029786775035"""),
    rank = 11,
    shortDesc = """BM rule fitted to 138 training reactions at node Root_N-4R->C
Total Standard Deviation in ln(k): 2.2404029786775035""",
    longDesc = 
"""
BM rule fitted to 138 training reactions at node Root_N-4R->C
Total Standard Deviation in ln(k): 2.2404029786775035
""",
)

entry(
    index = 5,
    label = "Root_Ext-4R-R_5R!H-u0",
    kinetics = ArrheniusBM(A=(65.9323,'m^3/(mol*s)'), n=1.61518, w0=(568031,'J/mol'), E0=(19429.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00010955087984623423, var=2.3943460958774976, Tref=1000.0, N=80, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0',), comment="""BM rule fitted to 80 training reactions at node Root_Ext-4R-R_5R!H-u0
    Total Standard Deviation in ln(k): 3.1023371038065535"""),
    rank = 11,
    shortDesc = """BM rule fitted to 80 training reactions at node Root_Ext-4R-R_5R!H-u0
Total Standard Deviation in ln(k): 3.1023371038065535""",
    longDesc = 
"""
BM rule fitted to 80 training reactions at node Root_Ext-4R-R_5R!H-u0
Total Standard Deviation in ln(k): 3.1023371038065535
""",
)

entry(
    index = 6,
    label = "Root_Ext-4R-R_N-5R!H-u0",
    kinetics = ArrheniusBM(A=(728215,'m^3/(mol*s)'), n=-0.28089, w0=(574039,'J/mol'), E0=(30590.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.5057115515045048, var=5.681088630311148, Tref=1000.0, N=51, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0',), comment="""BM rule fitted to 51 training reactions at node Root_Ext-4R-R_N-5R!H-u0
    Total Standard Deviation in ln(k): 8.561487798638204"""),
    rank = 11,
    shortDesc = """BM rule fitted to 51 training reactions at node Root_Ext-4R-R_N-5R!H-u0
Total Standard Deviation in ln(k): 8.561487798638204""",
    longDesc = 
"""
BM rule fitted to 51 training reactions at node Root_Ext-4R-R_N-5R!H-u0
Total Standard Deviation in ln(k): 8.561487798638204
""",
)

entry(
    index = 7,
    label = "Root_4R->C_1R!H->O",
    kinetics = ArrheniusBM(A=(1.62546e+09,'m^3/(mol*s)'), n=-0.811648, w0=(649667,'J/mol'), E0=(103005,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.08580691686234, var=50.11563954133438, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_1R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_1R!H->O
    Total Standard Deviation in ln(k): 26.970410167962328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_1R!H->O
Total Standard Deviation in ln(k): 26.970410167962328""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_1R!H->O
Total Standard Deviation in ln(k): 26.970410167962328
""",
)

entry(
    index = 8,
    label = "Root_4R->C_N-1R!H->O",
    kinetics = ArrheniusBM(A=(32.8407,'m^3/(mol*s)'), n=1.45297, w0=(539375,'J/mol'), E0=(71362.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1154799667742425, var=1.3560662151115772, Tref=1000.0, N=44, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O',), comment="""BM rule fitted to 44 training reactions at node Root_4R->C_N-1R!H->O
    Total Standard Deviation in ln(k): 2.624669802500432"""),
    rank = 11,
    shortDesc = """BM rule fitted to 44 training reactions at node Root_4R->C_N-1R!H->O
Total Standard Deviation in ln(k): 2.624669802500432""",
    longDesc = 
"""
BM rule fitted to 44 training reactions at node Root_4R->C_N-1R!H->O
Total Standard Deviation in ln(k): 2.624669802500432
""",
)

entry(
    index = 9,
    label = "Root_N-4R->C_1R!H-inRing",
    kinetics = ArrheniusBM(A=(100000,'m^3/(mol*s)'), n=1.1, w0=(494000,'J/mol'), E0=(150490,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_N-4R->C_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(1761.48,'m^3/(mol*s)'), n=1.17604, w0=(579051,'J/mol'), E0=(51793.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03682333249492808, var=1.1606586466958084, Tref=1000.0, N=137, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing',), comment="""BM rule fitted to 137 training reactions at node Root_N-4R->C_N-1R!H-inRing
    Total Standard Deviation in ln(k): 2.2522995921553215"""),
    rank = 11,
    shortDesc = """BM rule fitted to 137 training reactions at node Root_N-4R->C_N-1R!H-inRing
Total Standard Deviation in ln(k): 2.2522995921553215""",
    longDesc = 
"""
BM rule fitted to 137 training reactions at node Root_N-4R->C_N-1R!H-inRing
Total Standard Deviation in ln(k): 2.2522995921553215
""",
)

entry(
    index = 11,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C",
    kinetics = ArrheniusBM(A=(1342.03,'m^3/(mol*s)'), n=1.09666, w0=(545415,'J/mol'), E0=(60180.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.5858683008939745, var=10.530425761142494, Tref=1000.0, N=59, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C',), comment="""BM rule fitted to 59 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C
    Total Standard Deviation in ln(k): 10.490082839321438"""),
    rank = 11,
    shortDesc = """BM rule fitted to 59 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C
Total Standard Deviation in ln(k): 10.490082839321438""",
    longDesc = 
"""
BM rule fitted to 59 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C
Total Standard Deviation in ln(k): 10.490082839321438
""",
)

entry(
    index = 12,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C",
    kinetics = ArrheniusBM(A=(98.4904,'m^3/(mol*s)'), n=1.58193, w0=(631571,'J/mol'), E0=(21404.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02386218194009892, var=2.2730418190091917, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C',), comment="""BM rule fitted to 21 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C
    Total Standard Deviation in ln(k): 3.082416207683749"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C
Total Standard Deviation in ln(k): 3.082416207683749""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C
Total Standard Deviation in ln(k): 3.082416207683749
""",
)

entry(
    index = 13,
    label = "Root_Ext-4R-R_N-5R!H-u0_1R!H->O",
    kinetics = ArrheniusBM(A=(4.00926e+06,'m^3/(mol*s)'), n=0.0695165, w0=(679500,'J/mol'), E0=(25903.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.5906659597197343e-15, var=8.110181091599317e-08, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_1R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->O
    Total Standard Deviation in ln(k): 0.0005709160669089575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->O
Total Standard Deviation in ln(k): 0.0005709160669089575""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->O
Total Standard Deviation in ln(k): 0.0005709160669089575
""",
)

entry(
    index = 14,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O",
    kinetics = ArrheniusBM(A=(764671,'m^3/(mol*s)'), n=-0.288523, w0=(569735,'J/mol'), E0=(31770.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7246231507689538, var=5.990627219388711, Tref=1000.0, N=49, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O',), comment="""BM rule fitted to 49 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O
    Total Standard Deviation in ln(k): 9.239965026067571"""),
    rank = 11,
    shortDesc = """BM rule fitted to 49 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O
Total Standard Deviation in ln(k): 9.239965026067571""",
    longDesc = 
"""
BM rule fitted to 49 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O
Total Standard Deviation in ln(k): 9.239965026067571
""",
)

entry(
    index = 15,
    label = "Root_4R->C_1R!H->O_2R!H->C",
    kinetics = ArrheniusBM(A=(6.61174e+07,'m^3/(mol*s)'), n=-1.09962e-06, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.7507532944488107, var=36.13951493076956, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_1R!H->O_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_1R!H->O_2R!H->C
    Total Standard Deviation in ln(k): 21.475698718431726"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_1R!H->O_2R!H->C
Total Standard Deviation in ln(k): 21.475698718431726""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_1R!H->O_2R!H->C
Total Standard Deviation in ln(k): 21.475698718431726
""",
)

entry(
    index = 16,
    label = "Root_4R->C_1R!H->O_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(638000,'J/mol'), E0=(77506.6,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_1R!H->O_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_1R!H->O_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_1R!H->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_1R!H->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_4R->C_N-1R!H->O_4C-u1",
    kinetics = ArrheniusBM(A=(32.5748,'m^3/(mol*s)'), n=1.45397, w0=(539393,'J/mol'), E0=(71343,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1155080182829585, var=1.3542800759370561, Tref=1000.0, N=42, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1',), comment="""BM rule fitted to 42 training reactions at node Root_4R->C_N-1R!H->O_4C-u1
    Total Standard Deviation in ln(k): 2.6232023241055136"""),
    rank = 11,
    shortDesc = """BM rule fitted to 42 training reactions at node Root_4R->C_N-1R!H->O_4C-u1
Total Standard Deviation in ln(k): 2.6232023241055136""",
    longDesc = 
"""
BM rule fitted to 42 training reactions at node Root_4R->C_N-1R!H->O_4C-u1
Total Standard Deviation in ln(k): 2.6232023241055136
""",
)

entry(
    index = 18,
    label = "Root_4R->C_N-1R!H->O_N-4C-u1",
    kinetics = ArrheniusBM(A=(7.38116e+06,'m^3/(mol*s)'), n=-7.68901e-07, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=15.80567206157525, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_N-4C-u1',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_N-4C-u1
    Total Standard Deviation in ln(k): 7.970094538116895"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_N-4C-u1
Total Standard Deviation in ln(k): 7.970094538116895""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_N-4C-u1
Total Standard Deviation in ln(k): 7.970094538116895
""",
)

entry(
    index = 19,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N",
    kinetics = ArrheniusBM(A=(357.109,'m^3/(mol*s)'), n=1.20693, w0=(569125,'J/mol'), E0=(45095.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06985474913508474, var=0.3429093852723291, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N
    Total Standard Deviation in ln(k): 1.349456538762701"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N
Total Standard Deviation in ln(k): 1.349456538762701""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N
Total Standard Deviation in ln(k): 1.349456538762701
""",
)

entry(
    index = 20,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N",
    kinetics = ArrheniusBM(A=(1471.11,'m^3/(mol*s)'), n=1.25351, w0=(579667,'J/mol'), E0=(50332,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03214201229347551, var=0.6683682274533008, Tref=1000.0, N=129, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N',), comment="""BM rule fitted to 129 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N
    Total Standard Deviation in ln(k): 1.7197057417555937"""),
    rank = 11,
    shortDesc = """BM rule fitted to 129 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N
Total Standard Deviation in ln(k): 1.7197057417555937""",
    longDesc = 
"""
BM rule fitted to 129 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N
Total Standard Deviation in ln(k): 1.7197057417555937
""",
)

entry(
    index = 21,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_5R!H->S",
    kinetics = ArrheniusBM(A=(1.27667e-13,'m^3/(mol*s)'), n=4.8323, w0=(527000,'J/mol'), E0=(25354.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=10.238614422136449, var=279.3313223037818, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_5R!H->S',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_5R!H->S
    Total Standard Deviation in ln(k): 59.23071623718318"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_5R!H->S
Total Standard Deviation in ln(k): 59.23071623718318""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_5R!H->S
Total Standard Deviation in ln(k): 59.23071623718318
""",
)

entry(
    index = 22,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S",
    kinetics = ArrheniusBM(A=(4227.93,'m^3/(mol*s)'), n=0.965519, w0=(546061,'J/mol'), E0=(63828.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.322381878906825, var=3.380883378221132, Tref=1000.0, N=57, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S',), comment="""BM rule fitted to 57 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S
    Total Standard Deviation in ln(k): 7.008709731514522"""),
    rank = 11,
    shortDesc = """BM rule fitted to 57 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S
Total Standard Deviation in ln(k): 7.008709731514522""",
    longDesc = 
"""
BM rule fitted to 57 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S
Total Standard Deviation in ln(k): 7.008709731514522
""",
)

entry(
    index = 23,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O",
    kinetics = ArrheniusBM(A=(49.4192,'m^3/(mol*s)'), n=1.71995, w0=(632750,'J/mol'), E0=(4933.17,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.27168087925620377, var=0.8748541283484499, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O
    Total Standard Deviation in ln(k): 2.557716908155005"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O
Total Standard Deviation in ln(k): 2.557716908155005""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O
Total Standard Deviation in ln(k): 2.557716908155005
""",
)

entry(
    index = 24,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O",
    kinetics = ArrheniusBM(A=(196.579,'m^3/(mol*s)'), n=1.41443, w0=(630846,'J/mol'), E0=(25712.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6455971303255976, var=5.89938602635595, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O',), comment="""BM rule fitted to 13 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O
    Total Standard Deviation in ln(k): 6.491334552169518"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O
Total Standard Deviation in ln(k): 6.491334552169518""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O
Total Standard Deviation in ln(k): 6.491334552169518
""",
)

entry(
    index = 25,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS",
    kinetics = ArrheniusBM(A=(2.39883e-10,'m^3/(mol*s)'), n=4.12909, w0=(569607,'J/mol'), E0=(-19157.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.557094049892679, var=5.308239059849127, Tref=1000.0, N=42, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS',), comment="""BM rule fitted to 42 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS
    Total Standard Deviation in ln(k): 13.556254874825653"""),
    rank = 11,
    shortDesc = """BM rule fitted to 42 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 13.556254874825653""",
    longDesc = 
"""
BM rule fitted to 42 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 13.556254874825653
""",
)

entry(
    index = 26,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS",
    kinetics = ArrheniusBM(A=(528669,'m^3/(mol*s)'), n=-0.232742, w0=(570500,'J/mol'), E0=(56372.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.625277747353188, var=8.212054453774941, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS
    Total Standard Deviation in ln(k): 12.34108088272061"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 12.34108088272061""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 12.34108088272061
""",
)

entry(
    index = 27,
    label = "Root_4R->C_1R!H->O_2R!H->C_4C-u1",
    kinetics = ArrheniusBM(A=(8.49e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_1R!H->O_2R!H->C_4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_1R!H->O_2R!H->C_4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_1R!H->O_2R!H->C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_1R!H->O_2R!H->C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_4R->C_1R!H->O_2R!H->C_N-4C-u1",
    kinetics = ArrheniusBM(A=(1.21e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_1R!H->O_2R!H->C_N-4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_1R!H->O_2R!H->C_N-4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_1R!H->O_2R!H->C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_1R!H->O_2R!H->C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_4R->C_N-1R!H->O_4C-u1_2R!H->O",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(601500,'J/mol'), E0=(75469.3,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_2R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_2R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O",
    kinetics = ArrheniusBM(A=(11.22,'m^3/(mol*s)'), n=1.58905, w0=(537878,'J/mol'), E0=(25120,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16806908328327985, var=1.4089700086131842, Tref=1000.0, N=41, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O',), comment="""BM rule fitted to 41 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O
    Total Standard Deviation in ln(k): 2.801905517447129"""),
    rank = 11,
    shortDesc = """BM rule fitted to 41 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O
Total Standard Deviation in ln(k): 2.801905517447129""",
    longDesc = 
"""
BM rule fitted to 41 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O
Total Standard Deviation in ln(k): 2.801905517447129
""",
)

entry(
    index = 31,
    label = "Root_4R->C_N-1R!H->O_N-4C-u1_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1.81e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_N-4C-u1_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_N-4C-u1_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_N-4C-u1_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_N-4C-u1_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1",
    kinetics = ArrheniusBM(A=(324.71,'m^3/(mol*s)'), n=1.21139, w0=(577357,'J/mol'), E0=(43789,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06587093377643148, var=0.37537174784171157, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1
    Total Standard Deviation in ln(k): 1.393757709198133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1
Total Standard Deviation in ln(k): 1.393757709198133""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1
Total Standard Deviation in ln(k): 1.393757709198133
""",
)

entry(
    index = 33,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_N-2R!H-u1",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(511500,'J/mol'), E0=(51150,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_N-2R!H-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_N-2R!H-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1",
    kinetics = ArrheniusBM(A=(1247.41,'m^3/(mol*s)'), n=1.25534, w0=(576147,'J/mol'), E0=(40258.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.027060219146463664, var=0.842655393109565, Tref=1000.0, N=109, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1',), comment="""BM rule fitted to 109 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1
    Total Standard Deviation in ln(k): 1.908262387777903"""),
    rank = 11,
    shortDesc = """BM rule fitted to 109 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1
Total Standard Deviation in ln(k): 1.908262387777903""",
    longDesc = 
"""
BM rule fitted to 109 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1
Total Standard Deviation in ln(k): 1.908262387777903
""",
)

entry(
    index = 35,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1",
    kinetics = ArrheniusBM(A=(10027.9,'m^3/(mol*s)'), n=1.02862, w0=(598850,'J/mol'), E0=(54336.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.036266501933350646, var=0.23721171500453309, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1',), comment="""BM rule fitted to 20 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1
    Total Standard Deviation in ln(k): 1.067515761026399"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1
Total Standard Deviation in ln(k): 1.067515761026399""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1
Total Standard Deviation in ln(k): 1.067515761026399
""",
)

entry(
    index = 36,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_5R!H->S_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(644,'m^3/(mol*s)'), n=1.19, w0=(515000,'J/mol'), E0=(39525.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_5R!H->S_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_5R!H->S_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_5R!H->S_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_5R!H->S_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O",
    kinetics = ArrheniusBM(A=(17151,'m^3/(mol*s)'), n=0.880751, w0=(559800,'J/mol'), E0=(80061.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.33003191181165, var=10.860090777649967, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O',), comment="""BM rule fitted to 20 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O
    Total Standard Deviation in ln(k): 12.460886187513816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O
Total Standard Deviation in ln(k): 12.460886187513816""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O
Total Standard Deviation in ln(k): 12.460886187513816
""",
)

entry(
    index = 38,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O",
    kinetics = ArrheniusBM(A=(263990,'m^3/(mol*s)'), n=0.140312, w0=(538635,'J/mol'), E0=(26226.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8648471768986148, var=7.2674810012264714, Tref=1000.0, N=37, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O',), comment="""BM rule fitted to 37 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O
    Total Standard Deviation in ln(k): 7.57740098328404"""),
    rank = 11,
    shortDesc = """BM rule fitted to 37 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O
Total Standard Deviation in ln(k): 7.57740098328404""",
    longDesc = 
"""
BM rule fitted to 37 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O
Total Standard Deviation in ln(k): 7.57740098328404
""",
)

entry(
    index = 39,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_5R!H->C",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(67950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C",
    kinetics = ArrheniusBM(A=(49.2818,'m^3/(mol*s)'), n=1.72032, w0=(626071,'J/mol'), E0=(4884.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2680323142748556, var=0.8590264676555326, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C
    Total Standard Deviation in ln(k): 2.531510284743583"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C
Total Standard Deviation in ln(k): 2.531510284743583""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C
Total Standard Deviation in ln(k): 2.531510284743583
""",
)

entry(
    index = 41,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_5R!H->N",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(598500,'J/mol'), E0=(24800.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N",
    kinetics = ArrheniusBM(A=(83.4523,'m^3/(mol*s)'), n=1.56579, w0=(633542,'J/mol'), E0=(4153.81,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05007354116423361, var=0.8970933981570514, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N
    Total Standard Deviation in ln(k): 2.0245980377793833"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N
Total Standard Deviation in ln(k): 2.0245980377793833""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N
Total Standard Deviation in ln(k): 2.0245980377793833
""",
)

entry(
    index = 43,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(5.39505e+06,'m^3/(mol*s)'), n=-0.787899, w0=(563000,'J/mol'), E0=(-7312.12,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.819167364774766, var=4.760567625337857, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R',), comment="""BM rule fitted to 18 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R
    Total Standard Deviation in ln(k): 6.432285803150937"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.432285803150937""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.432285803150937
""",
)

entry(
    index = 44,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_1CNS-inRing",
    kinetics = ArrheniusBM(A=(50000,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(36930.5,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_1CNS-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_1CNS-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_1CNS-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_1CNS-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing",
    kinetics = ArrheniusBM(A=(172.737,'m^3/(mol*s)'), n=0.695623, w0=(571043,'J/mol'), E0=(21992.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.014693820409886251, var=5.65173903453728, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing',), comment="""BM rule fitted to 23 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing
    Total Standard Deviation in ln(k): 4.802853319878419"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing
Total Standard Deviation in ln(k): 4.802853319878419""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing
Total Standard Deviation in ln(k): 4.802853319878419
""",
)

entry(
    index = 46,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(521886,'m^3/(mol*s)'), n=0.152476, w0=(551500,'J/mol'), E0=(87360.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.017620664343511283, var=5.156740901418075, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R
    Total Standard Deviation in ln(k): 4.596717368737125"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.596717368737125""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.596717368737125
""",
)

entry(
    index = 47,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_1CNS->C",
    kinetics = ArrheniusBM(A=(105812,'m^3/(mol*s)'), n=0.0187788, w0=(551500,'J/mol'), E0=(28711.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09646707572050597, var=2.8085567758521424, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_1CNS->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_1CNS->C
    Total Standard Deviation in ln(k): 3.602064841653377"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_1CNS->C
Total Standard Deviation in ln(k): 3.602064841653377""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_1CNS->C
Total Standard Deviation in ln(k): 3.602064841653377
""",
)

entry(
    index = 48,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C",
    kinetics = ArrheniusBM(A=(1.2e+06,'m^3/(mol*s)'), n=-0.34, w0=(684500,'J/mol'), E0=(61113.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN",
    kinetics = ArrheniusBM(A=(150.603,'m^3/(mol*s)'), n=1.27246, w0=(539359,'J/mol'), E0=(84656.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3345198687655444, var=1.9494524006734706, Tref=1000.0, N=32, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN',), comment="""BM rule fitted to 32 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN
    Total Standard Deviation in ln(k): 3.6395692672791076"""),
    rank = 11,
    shortDesc = """BM rule fitted to 32 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN
Total Standard Deviation in ln(k): 3.6395692672791076""",
    longDesc = 
"""
BM rule fitted to 32 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN
Total Standard Deviation in ln(k): 3.6395692672791076
""",
)

entry(
    index = 50,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN",
    kinetics = ArrheniusBM(A=(194.83,'m^3/(mol*s)'), n=1.19577, w0=(532611,'J/mol'), E0=(24498.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.015326182662846839, var=0.3956292467129464, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN',), comment="""BM rule fitted to 9 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN
    Total Standard Deviation in ln(k): 1.299467630272084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN
Total Standard Deviation in ln(k): 1.299467630272084""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN
Total Standard Deviation in ln(k): 1.299467630272084
""",
)

entry(
    index = 51,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(246.827,'m^3/(mol*s)'), n=1.2433, w0=(581125,'J/mol'), E0=(29015.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09502092991108324, var=0.9409657996420207, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 2.183407074220283"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.183407074220283""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.183407074220283
""",
)

entry(
    index = 53,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(209.849,'m^3/(mol*s)'), n=1.2433, w0=(591250,'J/mol'), E0=(59125,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5787018105298811, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.4540246495725655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.4540246495725655""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.4540246495725655
""",
)

entry(
    index = 54,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F",
    kinetics = ArrheniusBM(A=(6.27784e+06,'m^3/(mol*s)'), n=0.121164, w0=(631150,'J/mol'), E0=(63115,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.006690106870515731, var=0.593584426511705, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F
    Total Standard Deviation in ln(k): 1.5613460363826523"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F
Total Standard Deviation in ln(k): 1.5613460363826523""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F
Total Standard Deviation in ln(k): 1.5613460363826523
""",
)

entry(
    index = 55,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F",
    kinetics = ArrheniusBM(A=(1240.68,'m^3/(mol*s)'), n=1.25606, w0=(570591,'J/mol'), E0=(39780.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.027057573146712092, var=0.8426671277724367, Tref=1000.0, N=99, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F',), comment="""BM rule fitted to 99 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F
    Total Standard Deviation in ln(k): 1.9082685531353747"""),
    rank = 11,
    shortDesc = """BM rule fitted to 99 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F
Total Standard Deviation in ln(k): 1.9082685531353747""",
    longDesc = 
"""
BM rule fitted to 99 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F
Total Standard Deviation in ln(k): 1.9082685531353747
""",
)

entry(
    index = 56,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_1R!H->O",
    kinetics = ArrheniusBM(A=(1.72553e+08,'m^3/(mol*s)'), n=-0.207634, w0=(675125,'J/mol'), E0=(74900.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.1433111407657404, var=4.597661629890631, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_1R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_1R!H->O
    Total Standard Deviation in ln(k): 7.171225793847845"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_1R!H->O
Total Standard Deviation in ln(k): 7.171225793847845""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_1R!H->O
Total Standard Deviation in ln(k): 7.171225793847845
""",
)

entry(
    index = 57,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O",
    kinetics = ArrheniusBM(A=(10936,'m^3/(mol*s)'), n=1.01373, w0=(579781,'J/mol'), E0=(55160.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.009877719888224192, var=0.25859545121498756, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O',), comment="""BM rule fitted to 16 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O
    Total Standard Deviation in ln(k): 1.0442719123059518"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O
Total Standard Deviation in ln(k): 1.0442719123059518""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O
Total Standard Deviation in ln(k): 1.0442719123059518
""",
)

entry(
    index = 58,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C",
    kinetics = ArrheniusBM(A=(6.96423e+06,'m^3/(mol*s)'), n=-0.444773, w0=(559211,'J/mol'), E0=(64089.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013849722779827966, var=0.7972774167812374, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C',), comment="""BM rule fitted to 19 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C
    Total Standard Deviation in ln(k): 1.8248341148266316"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C
Total Standard Deviation in ln(k): 1.8248341148266316""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C
Total Standard Deviation in ln(k): 1.8248341148266316
""",
)

entry(
    index = 59,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_N-2R!H->C",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R",
    kinetics = ArrheniusBM(A=(305492,'m^3/(mol*s)'), n=0.10765, w0=(533150,'J/mol'), E0=(-784.441,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.30043786218505, var=20.883137184028147, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R
    Total Standard Deviation in ln(k): 14.941247274354899"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R
Total Standard Deviation in ln(k): 14.941247274354899""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R
Total Standard Deviation in ln(k): 14.941247274354899
""",
)

entry(
    index = 61,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Sp-5BrBrBrCCCFFF#4R",
    kinetics = ArrheniusBM(A=(5.08213e+06,'m^3/(mol*s)'), n=6.07908e-07, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.8756592302892024e-09, var=0.1974069254280893, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Sp-5BrBrBrCCCFFF#4R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Sp-5BrBrBrCCCFFF#4R
    Total Standard Deviation in ln(k): 0.8907138061354173"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Sp-5BrBrBrCCCFFF#4R
Total Standard Deviation in ln(k): 0.8907138061354173""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Sp-5BrBrBrCCCFFF#4R
Total Standard Deviation in ln(k): 0.8907138061354173
""",
)

entry(
    index = 62,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R",
    kinetics = ArrheniusBM(A=(1.15775e+06,'m^3/(mol*s)'), n=0.0498814, w0=(540875,'J/mol'), E0=(68032.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01998953528046016, var=1.552602842185119, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R',), comment="""BM rule fitted to 24 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R
    Total Standard Deviation in ln(k): 2.548194730259998"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R
Total Standard Deviation in ln(k): 2.548194730259998""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R
Total Standard Deviation in ln(k): 2.548194730259998
""",
)

entry(
    index = 63,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS",
    kinetics = ArrheniusBM(A=(55.6945,'m^3/(mol*s)'), n=1.72025, w0=(616333,'J/mol'), E0=(3477.11,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.500126634572629, var=0.7252921215150004, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS
    Total Standard Deviation in ln(k): 2.9639138510069802"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS
Total Standard Deviation in ln(k): 2.9639138510069802""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS
Total Standard Deviation in ln(k): 2.9639138510069802
""",
)

entry(
    index = 64,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_N-Sp-2R!H-1NOS",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_N-Sp-2R!H-1NOS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_N-Sp-2R!H-1NOS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_N-Sp-2R!H-1NOS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_N-Sp-2R!H-1NOS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS",
    kinetics = ArrheniusBM(A=(59.8209,'m^3/(mol*s)'), n=1.70856, w0=(627071,'J/mol'), E0=(3507.14,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.9703495166746663, var=11.991203966740146, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS
    Total Standard Deviation in ln(k): 16.917812899671013"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS
Total Standard Deviation in ln(k): 16.917812899671013""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS
Total Standard Deviation in ln(k): 16.917812899671013
""",
)

entry(
    index = 66,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS",
    kinetics = ArrheniusBM(A=(98.661,'m^3/(mol*s)'), n=1.49399, w0=(642600,'J/mol'), E0=(9688.41,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.6696723449848017, var=10.141110319932299, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS
    Total Standard Deviation in ln(k): 10.579257555140929"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS
Total Standard Deviation in ln(k): 10.579257555140929""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS
Total Standard Deviation in ln(k): 10.579257555140929
""",
)

entry(
    index = 67,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(0.168776,'m^3/(mol*s)'), n=1.70516, w0=(563000,'J/mol'), E0=(24192,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8280189475555421, var=18.403500218137257, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 10.680622957556837"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 10.680622957556837""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 10.680622957556837
""",
)

entry(
    index = 68,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(310278,'m^3/(mol*s)'), n=-0.341761, w0=(563000,'J/mol'), E0=(21614.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10148486523307332, var=0.857929643361812, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 2.1118627707980844"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C
Total Standard Deviation in ln(k): 2.1118627707980844""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C
Total Standard Deviation in ln(k): 2.1118627707980844
""",
)

entry(
    index = 69,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(2.29889e+11,'m^3/(mol*s)'), n=-2.23863, w0=(563000,'J/mol'), E0=(-6719.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0249505707520306, var=6.015724314114222, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 7.492261111678506"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 7.492261111678506""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 7.492261111678506
""",
)

entry(
    index = 70,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C",
    kinetics = ArrheniusBM(A=(433.103,'m^3/(mol*s)'), n=0.547612, w0=(563000,'J/mol'), E0=(20676.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01744907379281405, var=5.79586125367231, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C',), comment="""BM rule fitted to 21 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C
    Total Standard Deviation in ln(k): 4.870160404976297"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C
Total Standard Deviation in ln(k): 4.870160404976297""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C
Total Standard Deviation in ln(k): 4.870160404976297
""",
)

entry(
    index = 71,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C",
    kinetics = ArrheniusBM(A=(2.02828e-05,'m^3/(mol*s)'), n=3.06393, w0=(655500,'J/mol'), E0=(23030.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1060934568671006, var=14.07756414075277, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C
    Total Standard Deviation in ln(k): 10.30091136591096"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C
Total Standard Deviation in ln(k): 10.30091136591096""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C
Total Standard Deviation in ln(k): 10.30091136591096
""",
)

entry(
    index = 72,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(442387,'m^3/(mol*s)'), n=0.250595, w0=(551500,'J/mol'), E0=(95697.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.026547653896902897, var=6.6826228440374145, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 5.249097089975617"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C
Total Standard Deviation in ln(k): 5.249097089975617""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C
Total Standard Deviation in ln(k): 5.249097089975617
""",
)

entry(
    index = 73,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(300000,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(61668.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R",
    kinetics = ArrheniusBM(A=(1.69265e+07,'m^3/(mol*s)'), n=-0.569333, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.241017733647975e-11, var=0.2901052209401143, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R',), comment="""BM rule fitted to 15 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R
    Total Standard Deviation in ln(k): 1.0797787139352417"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R
Total Standard Deviation in ln(k): 1.0797787139352417""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R
Total Standard Deviation in ln(k): 1.0797787139352417
""",
)

entry(
    index = 75,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C",
    kinetics = ArrheniusBM(A=(326.524,'m^3/(mol*s)'), n=1.24322, w0=(540929,'J/mol'), E0=(77666.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3814150353313706, var=1.0847208093511105, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C',), comment="""BM rule fitted to 14 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C
    Total Standard Deviation in ln(k): 3.0462594310873237"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C
Total Standard Deviation in ln(k): 3.0462594310873237""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C
Total Standard Deviation in ln(k): 3.0462594310873237
""",
)

entry(
    index = 76,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C",
    kinetics = ArrheniusBM(A=(0.160367,'m^3/(mol*s)'), n=2.13656, w0=(533833,'J/mol'), E0=(53383.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.014718234167879004, var=2.338943902760151, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C
    Total Standard Deviation in ln(k): 3.102943366630338"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C
Total Standard Deviation in ln(k): 3.102943366630338""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C
Total Standard Deviation in ln(k): 3.102943366630338
""",
)

entry(
    index = 77,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R",
    kinetics = ArrheniusBM(A=(306.327,'m^3/(mol*s)'), n=1.1953, w0=(531400,'J/mol'), E0=(30381.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2946877378776176, var=2.0271864868454412, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R',), comment="""BM rule fitted to 5 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R
    Total Standard Deviation in ln(k): 3.5947492079192913"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R
Total Standard Deviation in ln(k): 3.5947492079192913""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R
Total Standard Deviation in ln(k): 3.5947492079192913
""",
)

entry(
    index = 78,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(100000,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(52750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C",
    kinetics = ArrheniusBM(A=(154.363,'m^3/(mol*s)'), n=1.19601, w0=(537250,'J/mol'), E0=(53725,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0774457332350715, var=1.2806334483339823, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C
    Total Standard Deviation in ln(k): 4.975810062508253"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C
Total Standard Deviation in ln(k): 4.975810062508253""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C
Total Standard Deviation in ln(k): 4.975810062508253
""",
)

entry(
    index = 80,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C",
    kinetics = ArrheniusBM(A=(0.82,'m^3/(mol*s)'), n=1.87, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 81,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N",
    kinetics = ArrheniusBM(A=(207.556,'m^3/(mol*s)'), n=1.2433, w0=(550250,'J/mol'), E0=(17424.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6172896801193773, var=3.9362754729278144, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N
    Total Standard Deviation in ln(k): 5.528383327536255"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N
Total Standard Deviation in ln(k): 5.528383327536255""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N
Total Standard Deviation in ln(k): 5.528383327536255
""",
)

entry(
    index = 82,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N",
    kinetics = ArrheniusBM(A=(4147.31,'m^3/(mol*s)'), n=0.9029, w0=(612000,'J/mol'), E0=(51367.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8754987103028704, var=0.28030785144339526, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N
    Total Standard Deviation in ln(k): 3.2611345968802175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N
Total Standard Deviation in ln(k): 3.2611345968802175""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N
Total Standard Deviation in ln(k): 3.2611345968802175
""",
)

entry(
    index = 83,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(648000,'J/mol'), E0=(64800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(541149,'m^3/(mol*s)'), n=0.403881, w0=(608333,'J/mol'), E0=(60833.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.022300353306577345, var=1.0935717572740768, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_Ext-1R!H-R
    Total Standard Deviation in ln(k): 2.152462324155837"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.152462324155837""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.152462324155837
""",
)

entry(
    index = 86,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C",
    kinetics = ArrheniusBM(A=(1.9786e+07,'m^3/(mol*s)'), n=3.00959e-07, w0=(629667,'J/mol'), E0=(62966.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.5021738378249796e-09, var=0.565690313839239, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C
    Total Standard Deviation in ln(k): 1.5078091134015947"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C
Total Standard Deviation in ln(k): 1.5078091134015947""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C
Total Standard Deviation in ln(k): 1.5078091134015947
""",
)

entry(
    index = 87,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(708500,'J/mol'), E0=(70850,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H",
    kinetics = ArrheniusBM(A=(7250.31,'m^3/(mol*s)'), n=1.11599, w0=(563726,'J/mol'), E0=(57800.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.023995878507980507, var=0.44678662240689887, Tref=1000.0, N=42, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H',), comment="""BM rule fitted to 42 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H
    Total Standard Deviation in ln(k): 1.4002981609500926"""),
    rank = 11,
    shortDesc = """BM rule fitted to 42 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H
Total Standard Deviation in ln(k): 1.4002981609500926""",
    longDesc = 
"""
BM rule fitted to 42 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H
Total Standard Deviation in ln(k): 1.4002981609500926
""",
)

entry(
    index = 89,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H",
    kinetics = ArrheniusBM(A=(533.678,'m^3/(mol*s)'), n=1.27625, w0=(575649,'J/mol'), E0=(48408.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.039615543057498134, var=0.2146953990751925, Tref=1000.0, N=57, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H',), comment="""BM rule fitted to 57 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H
    Total Standard Deviation in ln(k): 1.0284352470408917"""),
    rank = 11,
    shortDesc = """BM rule fitted to 57 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H
Total Standard Deviation in ln(k): 1.0284352470408917""",
    longDesc = 
"""
BM rule fitted to 57 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H
Total Standard Deviation in ln(k): 1.0284352470408917
""",
)

entry(
    index = 90,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_1R!H->O_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(67950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_1R!H->O_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_1R!H->O_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_1R!H->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_1R!H->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_1R!H->O_2R!H->C",
    kinetics = ArrheniusBM(A=(7.94176e+07,'m^3/(mol*s)'), n=2.19788e-06, w0=(679500,'J/mol'), E0=(67950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.9426404480036046, var=9.694606240475355, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_1R!H->O_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_1R!H->O_2R!H->C
    Total Standard Deviation in ln(k): 11.1229818930801"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_1R!H->O_2R!H->C
Total Standard Deviation in ln(k): 11.1229818930801""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_1R!H->O_2R!H->C
Total Standard Deviation in ln(k): 11.1229818930801
""",
)

entry(
    index = 92,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_1R!H->O_N-2R!H->C",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(662000,'J/mol'), E0=(48035.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_1R!H->O_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_1R!H->O_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_1R!H->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_1R!H->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_2R!H->O",
    kinetics = ArrheniusBM(A=(165.835,'m^3/(mol*s)'), n=1.5823, w0=(640500,'J/mol'), E0=(49223.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.888347326583373, var=4.6009210074755265, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_2R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_2R!H->O
    Total Standard Deviation in ln(k): 9.044699417413472"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_2R!H->O
Total Standard Deviation in ln(k): 9.044699417413472""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_2R!H->O
Total Standard Deviation in ln(k): 9.044699417413472
""",
)

entry(
    index = 94,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O",
    kinetics = ArrheniusBM(A=(13653.3,'m^3/(mol*s)'), n=0.981307, w0=(571107,'J/mol'), E0=(57110.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.028545797104123596, var=0.29834570847680436, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O',), comment="""BM rule fitted to 14 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O
    Total Standard Deviation in ln(k): 1.1667300869020354"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O
Total Standard Deviation in ln(k): 1.1667300869020354""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O
Total Standard Deviation in ln(k): 1.1667300869020354
""",
)

entry(
    index = 95,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_4R->C",
    kinetics = ArrheniusBM(A=(695006,'m^3/(mol*s)'), n=-5.08253e-07, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.6643208264050226e-08, var=3.6973873113656555, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_4R->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_4R->C
    Total Standard Deviation in ln(k): 3.854823279288445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_4R->C
Total Standard Deviation in ln(k): 3.854823279288445""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_4R->C
Total Standard Deviation in ln(k): 3.854823279288445
""",
)

entry(
    index = 96,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C",
    kinetics = ArrheniusBM(A=(173106,'m^3/(mol*s)'), n=-0.0212727, w0=(563000,'J/mol'), E0=(47852.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0035412246992254518, var=0.26399074118163646, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C',), comment="""BM rule fitted to 16 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C
    Total Standard Deviation in ln(k): 1.0389310198328732"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C
Total Standard Deviation in ln(k): 1.0389310198328732""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C
Total Standard Deviation in ln(k): 1.0389310198328732
""",
)

entry(
    index = 97,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C",
    kinetics = ArrheniusBM(A=(300405,'m^3/(mol*s)'), n=0.109166, w0=(526062,'J/mol'), E0=(-2017.49,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.9020227488664405, var=27.01209130273415, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C
    Total Standard Deviation in ln(k): 17.71075569408961"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C
Total Standard Deviation in ln(k): 17.71075569408961""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C
Total Standard Deviation in ln(k): 17.71075569408961
""",
)

entry(
    index = 98,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.9053e+06,'m^3/(mol*s)'), n=-0.0575531, w0=(561500,'J/mol'), E0=(19207.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.14646054465202069, var=1.2892176048609387, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_N-2R!H->C
    Total Standard Deviation in ln(k): 2.6442420745054953"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_N-2R!H->C
Total Standard Deviation in ln(k): 2.6442420745054953""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_N-2R!H->C
Total Standard Deviation in ln(k): 2.6442420745054953
""",
)

entry(
    index = 99,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Sp-5BrBrBrCCCFFF#4R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=1.90562e-08, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Sp-5BrBrBrCCCFFF#4R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Sp-5BrBrBrCCCFFF#4R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Sp-5BrBrBrCCCFFF#4R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Sp-5BrBrBrCCCFFF#4R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 100,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C",
    kinetics = ArrheniusBM(A=(800993,'m^3/(mol*s)'), n=0.0587737, w0=(537053,'J/mol'), E0=(67668.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.005138424705040985, var=1.3332883428971334, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C',), comment="""BM rule fitted to 19 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C
    Total Standard Deviation in ln(k): 2.3277402325753433"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C
Total Standard Deviation in ln(k): 2.3277402325753433""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C
Total Standard Deviation in ln(k): 2.3277402325753433
""",
)

entry(
    index = 101,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C",
    kinetics = ArrheniusBM(A=(8.51053e+07,'m^3/(mol*s)'), n=-0.355805, w0=(555400,'J/mol'), E0=(76497.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3133783293358169, var=2.78213661371081, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C
    Total Standard Deviation in ln(k): 4.1312283318090754"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C
Total Standard Deviation in ln(k): 4.1312283318090754""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C
Total Standard Deviation in ln(k): 4.1312283318090754
""",
)

entry(
    index = 102,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_2R!H->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(56131,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 103,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C",
    kinetics = ArrheniusBM(A=(55.5201,'m^3/(mol*s)'), n=1.72068, w0=(603700,'J/mol'), E0=(5726.82,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4974265036478005, var=0.715585916381764, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C
    Total Standard Deviation in ln(k): 2.945667077087709"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C
Total Standard Deviation in ln(k): 2.945667077087709""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C
Total Standard Deviation in ln(k): 2.945667077087709
""",
)

entry(
    index = 104,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_Ext-5COS-R",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(57475.1,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_Ext-5COS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_Ext-5COS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_Ext-5COS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_Ext-5COS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 105,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O",
    kinetics = ArrheniusBM(A=(56.1763,'m^3/(mol*s)'), n=1.71849, w0=(627000,'J/mol'), E0=(-1662.01,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.406650984474472, var=12.833305395099408, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O
    Total Standard Deviation in ln(k): 20.766233586810195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O
Total Standard Deviation in ln(k): 20.766233586810195""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O
Total Standard Deviation in ln(k): 20.766233586810195
""",
)

entry(
    index = 106,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O",
    kinetics = ArrheniusBM(A=(1.15945e+06,'m^3/(mol*s)'), n=0.0981285, w0=(620000,'J/mol'), E0=(43306.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.39543666877401673, var=0.7533751072931021, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O
    Total Standard Deviation in ln(k): 2.7336130541814603"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O
Total Standard Deviation in ln(k): 2.7336130541814603""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O
Total Standard Deviation in ln(k): 2.7336130541814603
""",
)

entry(
    index = 107,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C",
    kinetics = ArrheniusBM(A=(4.03222e+07,'m^3/(mol*s)'), n=-1.06537e-07, w0=(655500,'J/mol'), E0=(-8267.17,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04053193339062449, var=4.55660944302888, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C
    Total Standard Deviation in ln(k): 4.381189858959989"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C
Total Standard Deviation in ln(k): 4.381189858959989""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C
Total Standard Deviation in ln(k): 4.381189858959989
""",
)

entry(
    index = 108,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C",
    kinetics = ArrheniusBM(A=(96.2519,'m^3/(mol*s)'), n=1.49685, w0=(623250,'J/mol'), E0=(11940.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.1881264617506124, var=7.255212047919393, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C
    Total Standard Deviation in ln(k): 10.89765951374958"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C
Total Standard Deviation in ln(k): 10.89765951374958""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C
Total Standard Deviation in ln(k): 10.89765951374958
""",
)

entry(
    index = 109,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R_1CNS-inRing",
    kinetics = ArrheniusBM(A=(25000,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(-3048.12,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R_1CNS-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R_1CNS-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R_1CNS-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R_1CNS-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 110,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R_N-1CNS-inRing",
    kinetics = ArrheniusBM(A=(2.25086e+14,'m^3/(mol*s)'), n=-2.63818, w0=(563000,'J/mol'), E0=(80556.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6529717124666723, var=16.12399362977971, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R_N-1CNS-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R_N-1CNS-inRing
    Total Standard Deviation in ln(k): 9.690584583953118"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R_N-1CNS-inRing
Total Standard Deviation in ln(k): 9.690584583953118""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R_N-1CNS-inRing
Total Standard Deviation in ln(k): 9.690584583953118
""",
)

entry(
    index = 111,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(30000,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(16338,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C_Ext-1CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C_Ext-1CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 112,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(26666.7,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(12108.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 113,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(5.20695e+09,'m^3/(mol*s)'), n=-1.78352, w0=(563000,'J/mol'), E0=(-7171.36,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.076458680558956, var=1.2483619426967265, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-1CNS-R',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-1CNS-R
    Total Standard Deviation in ln(k): 4.944562933450632"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 4.944562933450632""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 4.944562933450632
""",
)

entry(
    index = 114,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(4.48111e+14,'m^3/(mol*s)'), n=-3.14885, w0=(563000,'J/mol'), E0=(2889.35,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.96255396614481, var=30.52594293923303, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 16.007259100198016"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 16.007259100198016""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 16.007259100198016
""",
)

entry(
    index = 115,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(4226.46,'m^3/(mol*s)'), n=0.23454, w0=(563000,'J/mol'), E0=(18338.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.011912473309836417, var=5.946347177673556, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R',), comment="""BM rule fitted to 19 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R
    Total Standard Deviation in ln(k): 4.918504012723658"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 4.918504012723658""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 4.918504012723658
""",
)

entry(
    index = 116,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(47009.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C_Ext-1CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C_Ext-1CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 117,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(300000,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(62563.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C_Ext-1CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C_Ext-1CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 118,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C",
    kinetics = ArrheniusBM(A=(9.60603e+07,'m^3/(mol*s)'), n=-0.76, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.240168944759434e-11, var=0.22100123677280187, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C
    Total Standard Deviation in ln(k): 0.9424413690506191"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C
Total Standard Deviation in ln(k): 0.9424413690506191""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C
Total Standard Deviation in ln(k): 0.9424413690506191
""",
)

entry(
    index = 119,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(9.00317e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.028879687253878e-10, var=0.26709359018693596, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C',), comment="""BM rule fitted to 11 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C
    Total Standard Deviation in ln(k): 1.0360691027061144"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C
Total Standard Deviation in ln(k): 1.0360691027061144""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C
Total Standard Deviation in ln(k): 1.0360691027061144
""",
)

entry(
    index = 120,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.01791e+09,'m^3/(mol*s)'), n=-1.02782, w0=(539000,'J/mol'), E0=(88356.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.030334856222267732, var=1.9235017269590435, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R',), comment="""BM rule fitted to 12 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.8565926224693916"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.8565926224693916""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.8565926224693916
""",
)

entry(
    index = 121,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C",
    kinetics = ArrheniusBM(A=(2.19e+08,'m^3/(mol*s)'), n=-0.68, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 122,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_N-2CN->C",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=1.87, w0=(566000,'J/mol'), E0=(56600,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_N-2CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_N-2CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 123,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_2CN->C",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(553500,'J/mol'), E0=(55350,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_2CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_2CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 124,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C",
    kinetics = ArrheniusBM(A=(0.0114734,'m^3/(mol*s)'), n=2.46068, w0=(524000,'J/mol'), E0=(52400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.4906384915362034, var=2.392248234980461, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C
    Total Standard Deviation in ln(k): 4.33346261042941"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 4.33346261042941""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 4.33346261042941
""",
)

entry(
    index = 125,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(62942.8,'m^3/(mol*s)'), n=0.605822, w0=(527500,'J/mol'), E0=(52750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5032189656781573, var=2.8625839117292187, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 4.656215078672301"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.656215078672301""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.656215078672301
""",
)

entry(
    index = 126,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C",
    kinetics = ArrheniusBM(A=(50000,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(52750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 127,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(300.244,'m^3/(mol*s)'), n=1.19833, w0=(537250,'J/mol'), E0=(27317.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5464711156970123, var=0.14054889629027748, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C
    Total Standard Deviation in ln(k): 2.124615207055025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C
Total Standard Deviation in ln(k): 2.124615207055025""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C
Total Standard Deviation in ln(k): 2.124615207055025
""",
)

entry(
    index = 128,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C_2CN->C",
    kinetics = ArrheniusBM(A=(196000,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(52750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C_2CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C_2CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 129,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C_N-2CN->C",
    kinetics = ArrheniusBM(A=(0.81,'m^3/(mol*s)'), n=1.87, w0=(547000,'J/mol'), E0=(54700,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C_N-2CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C_N-2CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 130,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->N",
    kinetics = ArrheniusBM(A=(0.46,'m^3/(mol*s)'), n=1.94, w0=(511500,'J/mol'), E0=(51150,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->N",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(589000,'J/mol'), E0=(45647.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 132,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->N",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(625500,'J/mol'), E0=(52086.6,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->N",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(598500,'J/mol'), E0=(35577.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 134,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_Ext-1R!H-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(616000,'J/mol'), E0=(61600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_Ext-1R!H-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_Ext-1R!H-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_Ext-1R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_Ext-1R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 135,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_Ext-1R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(604500,'J/mol'), E0=(60450,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_Ext-1R!H-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_Ext-1R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_Ext-1R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_Ext-1R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 136,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_Ext-1R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(604500,'J/mol'), E0=(60450,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_Ext-1R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_Ext-1R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_Ext-1R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_Ext-1R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 137,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C",
    kinetics = ArrheniusBM(A=(1.82056e+07,'m^3/(mol*s)'), n=3.07861e-07, w0=(609100,'J/mol'), E0=(60910,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.3508313635714363e-08, var=0.6860601797691862, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C
    Total Standard Deviation in ln(k): 1.6604970358637463"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C
Total Standard Deviation in ln(k): 1.6604970358637463""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C
Total Standard Deviation in ln(k): 1.6604970358637463
""",
)

entry(
    index = 138,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_N-1R!H->C",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(732500,'J/mol'), E0=(73250,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_N-1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_N-1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 139,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(126433,'m^3/(mol*s)'), n=0.766429, w0=(571389,'J/mol'), E0=(72988.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.023284266041109142, var=0.3057712324837437, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H',), comment="""BM rule fitted to 27 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.1670532193108896"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.1670532193108896""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.1670532193108896
""",
)

entry(
    index = 140,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(19350.4,'m^3/(mol*s)'), n=0.958615, w0=(549933,'J/mol'), E0=(31738.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1187470496578346, var=0.5778873137821621, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 15 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.8223369724435035"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.8223369724435035""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.8223369724435035
""",
)

entry(
    index = 141,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N",
    kinetics = ArrheniusBM(A=(467.561,'m^3/(mol*s)'), n=1.27907, w0=(590333,'J/mol'), E0=(59033.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03980613378453951, var=0.20755570191645634, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N
    Total Standard Deviation in ln(k): 1.0133382627124077"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N
Total Standard Deviation in ln(k): 1.0133382627124077""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N
Total Standard Deviation in ln(k): 1.0133382627124077
""",
)

entry(
    index = 142,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N",
    kinetics = ArrheniusBM(A=(649.744,'m^3/(mol*s)'), n=1.27193, w0=(573922,'J/mol'), E0=(65720.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06583176594798405, var=0.5173942129043839, Tref=1000.0, N=51, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N',), comment="""BM rule fitted to 51 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N
    Total Standard Deviation in ln(k): 1.607414789195412"""),
    rank = 11,
    shortDesc = """BM rule fitted to 51 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N
Total Standard Deviation in ln(k): 1.607414789195412""",
    longDesc = 
"""
BM rule fitted to 51 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N
Total Standard Deviation in ln(k): 1.607414789195412
""",
)

entry(
    index = 143,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_2R!H->O_1CN->C",
    kinetics = ArrheniusBM(A=(3.33333e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_2R!H->O_1CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_2R!H->O_1CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_2R!H->O_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_2R!H->O_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 144,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_2R!H->O_N-1CN->C",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(625500,'J/mol'), E0=(52192.4,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_2R!H->O_N-1CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_2R!H->O_N-1CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_2R!H->O_N-1CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_2R!H->O_N-1CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 145,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN",
    kinetics = ArrheniusBM(A=(15701.7,'m^3/(mol*s)'), n=0.996352, w0=(564278,'J/mol'), E0=(56427.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.027631579425753113, var=0.4481901255487541, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN
    Total Standard Deviation in ln(k): 1.4115361380728138"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN
Total Standard Deviation in ln(k): 1.4115361380728138""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN
Total Standard Deviation in ln(k): 1.4115361380728138
""",
)

entry(
    index = 146,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN",
    kinetics = ArrheniusBM(A=(11330.1,'m^3/(mol*s)'), n=0.961232, w0=(583400,'J/mol'), E0=(58340,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.029729958794657493, var=0.00022219016772130848, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN
    Total Standard Deviation in ln(k): 0.10458105954761464"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN
Total Standard Deviation in ln(k): 0.10458105954761464""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN
Total Standard Deviation in ln(k): 0.10458105954761464
""",
)

entry(
    index = 147,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_4R->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(340825,'m^3/(mol*s)'), n=2.54075e-07, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_4R->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_4R->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_4R->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_4R->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 148,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(771722,'m^3/(mol*s)'), n=-0.202727, w0=(563000,'J/mol'), E0=(51738.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008150981760086853, var=0.36389386041050115, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 1.2298085363930353"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R
Total Standard Deviation in ln(k): 1.2298085363930353""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R
Total Standard Deviation in ln(k): 1.2298085363930353
""",
)

entry(
    index = 149,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.01408e+07,'m^3/(mol*s)'), n=-0.569105, w0=(563000,'J/mol'), E0=(66950.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006975637248293038, var=0.24421192574548606, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.0082227588062938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.0082227588062938""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.0082227588062938
""",
)

entry(
    index = 150,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_1C-inRing",
    kinetics = ArrheniusBM(A=(0.000675,'m^3/(mol*s)'), n=2.7, w0=(483500,'J/mol'), E0=(35785.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 151,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing",
    kinetics = ArrheniusBM(A=(259.019,'m^3/(mol*s)'), n=0.695354, w0=(532143,'J/mol'), E0=(49523.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.4913713612270407, var=25.139955164001062, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing
    Total Standard Deviation in ln(k): 16.311420569770277"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing
Total Standard Deviation in ln(k): 16.311420569770277""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing
Total Standard Deviation in ln(k): 16.311420569770277
""",
)

entry(
    index = 152,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_N-2R!H->C_Ext-4R-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.94e+06,'m^3/(mol*s)'), n=0, w0=(561500,'J/mol'), E0=(39441.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_N-2R!H->C_Ext-4R-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_N-2R!H->C_Ext-4R-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_N-2R!H->C_Ext-4R-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_N-2R!H->C_Ext-4R-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 153,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Sp-5BrBrBrCCCFFF#4R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Sp-5BrBrBrCCCFFF#4R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Sp-5BrBrBrCCCFFF#4R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Sp-5BrBrBrCCCFFF#4R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Sp-5BrBrBrCCCFFF#4R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 154,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(326590,'m^3/(mol*s)'), n=0.203125, w0=(537154,'J/mol'), E0=(74055.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03321502938527199, var=1.8030156612626735, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R',), comment="""BM rule fitted to 13 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.7753413135810794"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.7753413135810794""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.7753413135810794
""",
)

entry(
    index = 155,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C",
    kinetics = ArrheniusBM(A=(1.80365e+08,'m^3/(mol*s)'), n=-0.687472, w0=(538700,'J/mol'), E0=(52477.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.009157567226053534, var=0.06694438778192863, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C
    Total Standard Deviation in ln(k): 0.5417063693835721"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C
Total Standard Deviation in ln(k): 0.5417063693835721""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C
Total Standard Deviation in ln(k): 0.5417063693835721
""",
)

entry(
    index = 156,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_N-Sp-2R!H-1C",
    kinetics = ArrheniusBM(A=(480000,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(52750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_N-Sp-2R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_N-Sp-2R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_N-Sp-2R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_N-Sp-2R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 157,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.0298e+10,'m^3/(mol*s)'), n=-1.07035, w0=(527500,'J/mol'), E0=(84041.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3266364186452244, var=2.117054052564888, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.7376040714210426"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.7376040714210426""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.7376040714210426
""",
)

entry(
    index = 158,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_2R!H->C",
    kinetics = ArrheniusBM(A=(1.41421e+07,'m^3/(mol*s)'), n=7.62613e-07, w0=(533250,'J/mol'), E0=(53325,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_2R!H->C
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_2R!H->C
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_2R!H->C
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 159,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(3.33333e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 160,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N",
    kinetics = ArrheniusBM(A=(55.3682,'m^3/(mol*s)'), n=1.72068, w0=(573833,'J/mol'), E0=(26375.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16479020172419373, var=0.14297914762848185, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N
    Total Standard Deviation in ln(k): 1.1720878594844713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N
Total Standard Deviation in ln(k): 1.1720878594844713""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N
Total Standard Deviation in ln(k): 1.1720878594844713
""",
)

entry(
    index = 161,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N",
    kinetics = ArrheniusBM(A=(6.23614e-40,'m^3/(mol*s)'), n=13.8207, w0=(648500,'J/mol'), E0=(-47906.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.127611593067805, var=3.4257180582824334, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N
    Total Standard Deviation in ln(k): 9.056260864310659"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N
Total Standard Deviation in ln(k): 9.056260864310659""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N
Total Standard Deviation in ln(k): 9.056260864310659
""",
)

entry(
    index = 162,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O_2R!H->C",
    kinetics = ArrheniusBM(A=(4.82e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 163,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O_N-2R!H->C",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(598500,'J/mol'), E0=(13428.6,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 164,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O",
    kinetics = ArrheniusBM(A=(1.25258e+07,'m^3/(mol*s)'), n=-0.25, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.6129510735315866e-09, var=0.029913004620106633, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O
    Total Standard Deviation in ln(k): 0.34672649236279346"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O
Total Standard Deviation in ln(k): 0.34672649236279346""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O
Total Standard Deviation in ln(k): 0.34672649236279346
""",
)

entry(
    index = 165,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_N-1NOS->O",
    kinetics = ArrheniusBM(A=(644,'m^3/(mol*s)'), n=1.19, w0=(513500,'J/mol'), E0=(42507.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_N-1NOS->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_N-1NOS->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_N-1NOS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_N-1NOS->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 166,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C",
    kinetics = ArrheniusBM(A=(1.90317e+07,'m^3/(mol*s)'), n=-4.02332e-07, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=1.6812080230698707, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C
    Total Standard Deviation in ln(k): 2.599367689841769"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C
Total Standard Deviation in ln(k): 2.599367689841769""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C
Total Standard Deviation in ln(k): 2.599367689841769
""",
)

entry(
    index = 167,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_N-5COS->C",
    kinetics = ArrheniusBM(A=(1.81e+08,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(56990.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_N-5COS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_N-5COS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_N-5COS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_N-5COS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 168,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C_1NOS->N",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(648000,'J/mol'), E0=(54170.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C_1NOS->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C_1NOS->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C_1NOS->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C_1NOS->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 169,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C_N-1NOS->N",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(598500,'J/mol'), E0=(17401.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C_N-1NOS->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C_N-1NOS->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C_N-1NOS->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C_N-1NOS->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 170,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R_N-1CNS-inRing_Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(8500,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(13198.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R_N-1CNS-inRing_Sp-7R!H-6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R_N-1CNS-inRing_Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R_N-1CNS-inRing_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R_N-1CNS-inRing_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R_N-1CNS-inRing_N-Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(7.23e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(99204.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R_N-1CNS-inRing_N-Sp-7R!H-6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R_N-1CNS-inRing_N-Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R_N-1CNS-inRing_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_Ext-6R!H-R_N-1CNS-inRing_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-1CNS-R_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(2.85329e+12,'m^3/(mol*s)'), n=-2.58013, w0=(563000,'J/mol'), E0=(-11377.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3530200646193378, var=3.9569501506101985, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-1CNS-R_Ext-1CNS-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-1CNS-R_Ext-1CNS-R
    Total Standard Deviation in ln(k): 4.8748209890591125"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-1CNS-R_Ext-1CNS-R
Total Standard Deviation in ln(k): 4.8748209890591125""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-1CNS-R_Ext-1CNS-R
Total Standard Deviation in ln(k): 4.8748209890591125
""",
)

entry(
    index = 173,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-1CNS-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.73553e+14,'m^3/(mol*s)'), n=-3.14885, w0=(563000,'J/mol'), E0=(-3396.91,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.9625539661448168, var=2.873931729472134, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-1CNS-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-1CNS-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 8.32960223996552"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-1CNS-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 8.32960223996552""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-1CNS-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 8.32960223996552
""",
)

entry(
    index = 174,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS",
    kinetics = ArrheniusBM(A=(119000,'m^3/(mol*s)'), n=-0.224934, w0=(563000,'J/mol'), E0=(-6044.83,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.061193034853913926, var=4.1126151071935615, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS',), comment="""BM rule fitted to 16 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS
    Total Standard Deviation in ln(k): 4.219270602306033"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS
Total Standard Deviation in ln(k): 4.219270602306033""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS
Total Standard Deviation in ln(k): 4.219270602306033
""",
)

entry(
    index = 175,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS",
    kinetics = ArrheniusBM(A=(1.68714e+16,'m^3/(mol*s)'), n=-3.31041, w0=(563000,'J/mol'), E0=(66353.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1093955463446234, var=24.094403248658786, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS
    Total Standard Deviation in ln(k): 10.115315847721718"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS
Total Standard Deviation in ln(k): 10.115315847721718""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS
Total Standard Deviation in ln(k): 10.115315847721718
""",
)

entry(
    index = 176,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(7.5e+07,'m^3/(mol*s)'), n=-0.68, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 177,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(7.33333e+07,'m^3/(mol*s)'), n=-0.68, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 178,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-2CN-R",
    kinetics = ArrheniusBM(A=(4.22222e+08,'m^3/(mol*s)'), n=-1, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-2CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-2CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-2CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-2CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 179,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(7.92359e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.2330461563346795e-10, var=0.15570236552121783, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R',), comment="""BM rule fitted to 7 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R
    Total Standard Deviation in ln(k): 0.7910512022467198"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 0.7910512022467198""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 0.7910512022467198
""",
)

entry(
    index = 180,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-2CN-R",
    kinetics = ArrheniusBM(A=(1.12583e+07,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=2.413897921625164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-2CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-2CN-R
    Total Standard Deviation in ln(k): 3.1147015559000413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-2CN-R
Total Standard Deviation in ln(k): 3.1147015559000413""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-2CN-R
Total Standard Deviation in ln(k): 3.1147015559000413
""",
)

entry(
    index = 181,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.5e+06,'m^3/(mol*s)'), n=-4.60922e-08, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 182,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(3.89177e+08,'m^3/(mol*s)'), n=-0.776484, w0=(539000,'J/mol'), E0=(85460.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0366763005874044, var=1.4524396831142532, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 2.5082022027668103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 2.5082022027668103""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 2.5082022027668103
""",
)

entry(
    index = 183,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.72985e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.8988603214016866e-11, var=0.21353467287039427, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 0.9263843112218227"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.9263843112218227""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.9263843112218227
""",
)

entry(
    index = 184,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_2N-u1",
    kinetics = ArrheniusBM(A=(0.82,'m^3/(mol*s)'), n=1.87, w0=(524000,'J/mol'), E0=(52400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 185,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_N-2N-u1",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(524000,'J/mol'), E0=(52400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 186,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_Ext-5R!H-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(52750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_Ext-5R!H-R_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_Ext-5R!H-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_Ext-5R!H-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_Ext-5R!H-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 187,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(80345.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 188,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.15443e+07,'m^3/(mol*s)'), n=7.06236e-08, w0=(612167,'J/mol'), E0=(61216.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.4502455195451049e-08, var=1.4663745010001799, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 2.4276129521491097"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 2.4276129521491097""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 2.4276129521491097
""",
)

entry(
    index = 189,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C",
    kinetics = ArrheniusBM(A=(51740.6,'m^3/(mol*s)'), n=0.94027, w0=(560100,'J/mol'), E0=(62471.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.791508110279443, var=17.28840401236003, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C',), comment="""BM rule fitted to 20 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 15.349392927760109"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 15.349392927760109""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 15.349392927760109
""",
)

entry(
    index = 190,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C",
    kinetics = ArrheniusBM(A=(29105.5,'m^3/(mol*s)'), n=0.944587, w0=(603643,'J/mol'), E0=(69342.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06741631883960762, var=0.23179824076464509, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C
    Total Standard Deviation in ln(k): 1.134576054520196"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 1.134576054520196""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 1.134576054520196
""",
)

entry(
    index = 191,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C",
    kinetics = ArrheniusBM(A=(23314.3,'m^3/(mol*s)'), n=0.956427, w0=(541000,'J/mol'), E0=(29798.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.27346822579208163, var=1.9429105842251286, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 3.481472790068871"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 3.481472790068871""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 3.481472790068871
""",
)

entry(
    index = 192,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_N-1R!H->C",
    kinetics = ArrheniusBM(A=(16039.5,'m^3/(mol*s)'), n=0.960818, w0=(608000,'J/mol'), E0=(60800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4478648794535599, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_N-1R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_N-1R!H->C
    Total Standard Deviation in ln(k): 1.1252886418431154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 1.1252886418431154""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 1.1252886418431154
""",
)

entry(
    index = 193,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N",
    kinetics = ArrheniusBM(A=(556.026,'m^3/(mol*s)'), n=1.27907, w0=(574750,'J/mol'), E0=(57475,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03980613384668196, var=0.21353467318894948, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N
    Total Standard Deviation in ln(k): 1.0263997235150666"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N
Total Standard Deviation in ln(k): 1.0263997235150666""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N
Total Standard Deviation in ln(k): 1.0263997235150666
""",
)

entry(
    index = 194,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_N-Sp-2R!H-1N",
    kinetics = ArrheniusBM(A=(330.615,'m^3/(mol*s)'), n=1.27907, w0=(621500,'J/mol'), E0=(62150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570073, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_N-Sp-2R!H-1N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_N-Sp-2R!H-1N
    Total Standard Deviation in ln(k): 1.5045994199924806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_N-Sp-2R!H-1N
Total Standard Deviation in ln(k): 1.5045994199924806""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_N-Sp-2R!H-1N
Total Standard Deviation in ln(k): 1.5045994199924806
""",
)

entry(
    index = 195,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO",
    kinetics = ArrheniusBM(A=(5254.85,'m^3/(mol*s)'), n=1.03369, w0=(579821,'J/mol'), E0=(76686.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1819718629794673, var=0.03795237652685327, Tref=1000.0, N=39, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO',), comment="""BM rule fitted to 39 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO
    Total Standard Deviation in ln(k): 0.847765588000538"""),
    rank = 11,
    shortDesc = """BM rule fitted to 39 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO
Total Standard Deviation in ln(k): 0.847765588000538""",
    longDesc = 
"""
BM rule fitted to 39 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO
Total Standard Deviation in ln(k): 0.847765588000538
""",
)

entry(
    index = 196,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO",
    kinetics = ArrheniusBM(A=(483.082,'m^3/(mol*s)'), n=1.27464, w0=(554750,'J/mol'), E0=(55475,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04133157099809278, var=0.944304875919702, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO
    Total Standard Deviation in ln(k): 2.0519565078763926"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO
Total Standard Deviation in ln(k): 2.0519565078763926""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO
Total Standard Deviation in ln(k): 2.0519565078763926
""",
)

entry(
    index = 197,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1940.87,'m^3/(mol*s)'), n=1.21164, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0064379313563148, var=3.9869403856980674, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_Ext-1CN-R
    Total Standard Deviation in ln(k): 6.531658057906698"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_Ext-1CN-R
Total Standard Deviation in ln(k): 6.531658057906698""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_Ext-1CN-R
Total Standard Deviation in ln(k): 6.531658057906698
""",
)

entry(
    index = 198,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C",
    kinetics = ArrheniusBM(A=(34239.1,'m^3/(mol*s)'), n=0.957156, w0=(569750,'J/mol'), E0=(56975,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21950411944805648, var=0.16971708467487845, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C
    Total Standard Deviation in ln(k): 1.3774032542241128"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C
Total Standard Deviation in ln(k): 1.3774032542241128""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C
Total Standard Deviation in ln(k): 1.3774032542241128
""",
)

entry(
    index = 199,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C",
    kinetics = ArrheniusBM(A=(12117.9,'m^3/(mol*s)'), n=1.00928, w0=(557833,'J/mol'), E0=(55783.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0270949316202428, var=0.4642231890447657, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C
    Total Standard Deviation in ln(k): 1.4339824344550103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C
Total Standard Deviation in ln(k): 1.4339824344550103""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C
Total Standard Deviation in ln(k): 1.4339824344550103
""",
)

entry(
    index = 200,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R",
    kinetics = ArrheniusBM(A=(444.29,'m^3/(mol*s)'), n=1.44792, w0=(551500,'J/mol'), E0=(55150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.202693327970796, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R
    Total Standard Deviation in ln(k): 4.987000417702588"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R
Total Standard Deviation in ln(k): 4.987000417702588""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R
Total Standard Deviation in ln(k): 4.987000417702588
""",
)

entry(
    index = 201,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 202,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C",
    kinetics = ArrheniusBM(A=(11361.3,'m^3/(mol*s)'), n=0.960818, w0=(621500,'J/mol'), E0=(62150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4478648794535599, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C
    Total Standard Deviation in ln(k): 1.1252886418431154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C
Total Standard Deviation in ln(k): 1.1252886418431154""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C
Total Standard Deviation in ln(k): 1.1252886418431154
""",
)

entry(
    index = 203,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_4R->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(241000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_4R->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_4R->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_4R->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_4R->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 204,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(778190,'m^3/(mol*s)'), n=-0.21556, w0=(563000,'J/mol'), E0=(50033.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0034432446971360926, var=0.43955606728714963, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 1.3377711722179901"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 1.3377711722179901""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 1.3377711722179901
""",
)

entry(
    index = 205,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.88334e+10,'m^3/(mol*s)'), n=-1.58074, w0=(563000,'J/mol'), E0=(71995.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07570908089824784, var=0.5255064297933685, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 1.643492810905167"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.643492810905167""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.643492810905167
""",
)

entry(
    index = 206,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(100000,'m^3/(mol*s)'), n=6.09542e-08, w0=(563000,'J/mol'), E0=(52067.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 207,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-2C-R",
    kinetics = ArrheniusBM(A=(50000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(30223,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 208,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.44236e+06,'m^3/(mol*s)'), n=-0.431641, w0=(529400,'J/mol'), E0=(78976.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.7793646544631607, var=23.210837956338935, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R
    Total Standard Deviation in ln(k): 16.641666265574468"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 16.641666265574468""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 16.641666265574468
""",
)

entry(
    index = 209,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C",
    kinetics = ArrheniusBM(A=(9.00963e+06,'m^3/(mol*s)'), n=-0.281467, w0=(536333,'J/mol'), E0=(53633.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.002044199029788728, var=0.46475903096820703, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C
    Total Standard Deviation in ln(k): 1.371828983796715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C
Total Standard Deviation in ln(k): 1.371828983796715""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C
Total Standard Deviation in ln(k): 1.371828983796715
""",
)

entry(
    index = 210,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C",
    kinetics = ArrheniusBM(A=(2.08319e-06,'m^3/(mol*s)'), n=3.63493, w0=(539000,'J/mol'), E0=(22888,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.20070319676038806, var=3.675346909440732, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C
    Total Standard Deviation in ln(k): 4.3475959580113805"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C
Total Standard Deviation in ln(k): 4.3475959580113805""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C
Total Standard Deviation in ln(k): 4.3475959580113805
""",
)

entry(
    index = 211,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C",
    kinetics = ArrheniusBM(A=(2.14316e+08,'m^3/(mol*s)'), n=-0.7125, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.7124446309376658e-11, var=0.09039604171732793, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C
    Total Standard Deviation in ln(k): 0.6027423352743158"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C
Total Standard Deviation in ln(k): 0.6027423352743158""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C
Total Standard Deviation in ln(k): 0.6027423352743158
""",
)

entry(
    index = 212,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(979000,'m^3/(mol*s)'), n=0, w0=(537500,'J/mol'), E0=(38210.6,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 213,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(73314,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 214,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(52750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 215,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_2R!H->C_Sp-2C-1C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_2R!H->C_Sp-2C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_2R!H->C_Sp-2C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_2R!H->C_Sp-2C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_2R!H->C_Sp-2C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 216,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_2R!H->C_N-Sp-2C-1C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(52750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_2R!H->C_N-Sp-2C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_2R!H->C_N-Sp-2C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_2R!H->C_N-Sp-2C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_N-5BrCF->C_2R!H->C_N-Sp-2C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 217,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N",
    kinetics = ArrheniusBM(A=(55.3682,'m^3/(mol*s)'), n=1.72068, w0=(548000,'J/mol'), E0=(42013.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0406619764046778, var=0.11093145697366305, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N
    Total Standard Deviation in ln(k): 3.2824331527498067"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N
Total Standard Deviation in ln(k): 3.2824331527498067""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N
Total Standard Deviation in ln(k): 3.2824331527498067
""",
)

entry(
    index = 218,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_N-2NO->N",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(625500,'J/mol'), E0=(26769.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 219,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N_2NO->N",
    kinetics = ArrheniusBM(A=(0.0294,'m^3/(mol*s)'), n=2.69, w0=(662000,'J/mol'), E0=(33510,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 220,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N_N-2NO->N",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(635000,'J/mol'), E0=(6334.04,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 221,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(2.85561e+07,'m^3/(mol*s)'), n=-0.375, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.305460834090209e-17, var=0.06912283083491383, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O_Ext-4CNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O_Ext-4CNS-R
    Total Standard Deviation in ln(k): 0.5270693322083513"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.5270693322083513""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.5270693322083513
""",
)

entry(
    index = 222,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C_Sp-5C=4CNS",
    kinetics = ArrheniusBM(A=(3.01e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C_Sp-5C=4CNS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C_Sp-5C=4CNS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C_Sp-5C=4CNS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C_Sp-5C=4CNS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 223,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C_N-Sp-5C=4CNS",
    kinetics = ArrheniusBM(A=(1.20333e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C_N-Sp-5C=4CNS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C_N-Sp-5C=4CNS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C_N-Sp-5C=4CNS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C_N-Sp-5C=4CNS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 224,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-1CNS-R_Ext-1CNS-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(6.76056e+19,'m^3/(mol*s)'), n=-4.75849, w0=(563000,'J/mol'), E0=(-16313.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.1336541640536497, var=0.9158136442810729, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-1CNS-R_Ext-1CNS-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-1CNS-R_Ext-1CNS-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 7.279434547604328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-1CNS-R_Ext-1CNS-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 7.279434547604328""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C_Ext-1CNS-R_Ext-1CNS-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 7.279434547604328
""",
)

entry(
    index = 225,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C",
    kinetics = ArrheniusBM(A=(86.4598,'m^3/(mol*s)'), n=0.717439, w0=(563000,'J/mol'), E0=(20126.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05872744968515391, var=0.8167992296176627, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C
    Total Standard Deviation in ln(k): 1.9593747365859329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C
Total Standard Deviation in ln(k): 1.9593747365859329""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C
Total Standard Deviation in ln(k): 1.9593747365859329
""",
)

entry(
    index = 226,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_N-6R!H->C",
    kinetics = ArrheniusBM(A=(6.52663e+14,'m^3/(mol*s)'), n=-3.14885, w0=(563000,'J/mol'), E0=(2489.62,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.8409285322525404, var=18.467111861243236, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_N-6R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_N-6R!H->C
    Total Standard Deviation in ln(k): 13.240472329179818"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_N-6R!H->C
Total Standard Deviation in ln(k): 13.240472329179818""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_N-6R!H->C
Total Standard Deviation in ln(k): 13.240472329179818
""",
)

entry(
    index = 227,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS_6R!H->C",
    kinetics = ArrheniusBM(A=(1.47637e+08,'m^3/(mol*s)'), n=-0.906138, w0=(563000,'J/mol'), E0=(58234.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1366416601998153e-14, var=67.49420639145738, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS_6R!H->C
    Total Standard Deviation in ln(k): 16.469872495385907"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS_6R!H->C
Total Standard Deviation in ln(k): 16.469872495385907""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS_6R!H->C
Total Standard Deviation in ln(k): 16.469872495385907
""",
)

entry(
    index = 228,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS_N-6R!H->C",
    kinetics = ArrheniusBM(A=(70000,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(14365.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 229,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(6.5e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.996003610813218e-15, var=9.334522916791711e-61, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-1CN-R',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 1.2552772891490499e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 1.2552772891490499e-14""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 1.2552772891490499e-14
""",
)

entry(
    index = 230,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-2CN-R",
    kinetics = ArrheniusBM(A=(9.19239e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-2CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-2CN-R
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-2CN-R
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-2CN-R
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 231,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(5.5e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 232,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(5.5e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 233,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_Sp-5C-1C",
    kinetics = ArrheniusBM(A=(6.91356e+06,'m^3/(mol*s)'), n=-0.24, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.494092434445075e-11, var=1.7801088207517621, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_Sp-5C-1C',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_Sp-5C-1C
    Total Standard Deviation in ln(k): 2.6747319505637615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_Sp-5C-1C
Total Standard Deviation in ln(k): 2.6747319505637615""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_Sp-5C-1C
Total Standard Deviation in ln(k): 2.6747319505637615
""",
)

entry(
    index = 234,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_N-Sp-5C-1C",
    kinetics = ArrheniusBM(A=(1.23686e+06,'m^3/(mol*s)'), n=-0.0613002, w0=(539000,'J/mol'), E0=(76866.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.032960842251921633, var=1.4060476388514789, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_N-Sp-5C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_N-Sp-5C-1C
    Total Standard Deviation in ln(k): 2.459968486668792"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_N-Sp-5C-1C
Total Standard Deviation in ln(k): 2.459968486668792""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_N-Sp-5C-1C
Total Standard Deviation in ln(k): 2.459968486668792
""",
)

entry(
    index = 235,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_N-5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.5e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_N-5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_N-5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_N-5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_N-5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 236,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C_Ext-2C-R_Sp-2C-1C",
    kinetics = ArrheniusBM(A=(1.41421e+07,'m^3/(mol*s)'), n=7.62613e-07, w0=(616000,'J/mol'), E0=(61600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C_Ext-2C-R_Sp-2C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C_Ext-2C-R_Sp-2C-1C
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C_Ext-2C-R_Sp-2C-1C
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C_Ext-2C-R_Sp-2C-1C
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 237,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C_Ext-2C-R_N-Sp-2C-1C",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(604500,'J/mol'), E0=(60450,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C_Ext-2C-R_N-Sp-2C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C_Ext-2C-R_N-Sp-2C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C_Ext-2C-R_N-Sp-2C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C_Ext-2C-R_N-Sp-2C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 238,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C",
    kinetics = ArrheniusBM(A=(579021,'m^3/(mol*s)'), n=0.142546, w0=(549500,'J/mol'), E0=(-16053.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01722159858567493, var=1.1479233330110858, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C',), comment="""BM rule fitted to 17 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C
    Total Standard Deviation in ln(k): 2.191167248170958"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 2.191167248170958""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 2.191167248170958
""",
)

entry(
    index = 239,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(48788.1,'m^3/(mol*s)'), n=0.958373, w0=(620167,'J/mol'), E0=(62016.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1706622755278215, var=2.959645032278743, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_N-2R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_N-2R!H->C
    Total Standard Deviation in ln(k): 6.390232327854832"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 6.390232327854832""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 6.390232327854832
""",
)

entry(
    index = 240,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_2R!H->C",
    kinetics = ArrheniusBM(A=(27186.5,'m^3/(mol*s)'), n=0.958373, w0=(632000,'J/mol'), E0=(63200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.010303860207582392, var=4.2156786882136064e-05, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_2R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_2R!H->C
    Total Standard Deviation in ln(k): 0.03890549163362583"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 0.03890549163362583""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 0.03890549163362583
""",
)

entry(
    index = 241,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(25579.5,'m^3/(mol*s)'), n=0.960017, w0=(582375,'J/mol'), E0=(68865.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03991439304426502, var=0.6157593648146018, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C
    Total Standard Deviation in ln(k): 1.6734097729187294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 1.6734097729187294""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 1.6734097729187294
""",
)

entry(
    index = 242,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(32402.1,'m^3/(mol*s)'), n=0.958122, w0=(540786,'J/mol'), E0=(27816.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.5307381202648955, var=3.9963436822178093, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 7.853712927766576"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 7.853712927766576""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 7.853712927766576
""",
)

entry(
    index = 243,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C",
    kinetics = ArrheniusBM(A=(1.78009e+07,'m^3/(mol*s)'), n=-1.4487e-08, w0=(538000,'J/mol'), E0=(53800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=9.939681085063708e-09, var=1.5683487451695521, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C
    Total Standard Deviation in ln(k): 2.5106045647845394"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 2.5106045647845394""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 2.5106045647845394
""",
)

entry(
    index = 244,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(557500,'J/mol'), E0=(55750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 245,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_N-1R!H->C_2R!H->C",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(545000,'J/mol'), E0=(54500,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_N-1R!H->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_N-1R!H->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_N-1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_N-1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 246,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(671000,'J/mol'), E0=(67100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 247,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_2R!H->N",
    kinetics = ArrheniusBM(A=(467.561,'m^3/(mol*s)'), n=1.27907, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570074, var=0.9609060278364029, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_2R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_2R!H->N
    Total Standard Deviation in ln(k): 3.469757305105129"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_2R!H->N
Total Standard Deviation in ln(k): 3.469757305105129""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_2R!H->N
Total Standard Deviation in ln(k): 3.469757305105129
""",
)

entry(
    index = 248,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_N-2R!H->N",
    kinetics = ArrheniusBM(A=(661.23,'m^3/(mol*s)'), n=1.27907, w0=(601500,'J/mol'), E0=(60150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570073, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_N-2R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_N-2R!H->N
    Total Standard Deviation in ln(k): 1.5045994199924806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_N-2R!H->N
Total Standard Deviation in ln(k): 1.5045994199924806""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_N-2R!H->N
Total Standard Deviation in ln(k): 1.5045994199924806
""",
)

entry(
    index = 249,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_N-Sp-2R!H-1N_2R!H->C",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(558500,'J/mol'), E0=(55850,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_N-Sp-2R!H-1N_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_N-Sp-2R!H-1N_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_N-Sp-2R!H-1N_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_N-Sp-2R!H-1N_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 250,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_N-Sp-2R!H-1N_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_N-Sp-2R!H-1N_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_N-Sp-2R!H-1N_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_N-Sp-2R!H-1N_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_N-Sp-2R!H-1N_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 251,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1642.92,'m^3/(mol*s)'), n=1.17601, w0=(569853,'J/mol'), E0=(56985.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06493338716153542, var=0.2870286907396131, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R',), comment="""BM rule fitted to 17 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.2371872070990004"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.2371872070990004""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.2371872070990004
""",
)

entry(
    index = 252,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C",
    kinetics = ArrheniusBM(A=(6.80636e+06,'m^3/(mol*s)'), n=0.0916888, w0=(573853,'J/mol'), E0=(92930.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11155390811836169, var=1.0160842234593066, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C',), comment="""BM rule fitted to 17 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C
    Total Standard Deviation in ln(k): 2.301079269671121"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C
Total Standard Deviation in ln(k): 2.301079269671121""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C
Total Standard Deviation in ln(k): 2.301079269671121
""",
)

entry(
    index = 253,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C",
    kinetics = ArrheniusBM(A=(823.237,'m^3/(mol*s)'), n=1.27663, w0=(634000,'J/mol'), E0=(63400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03926987404702595, var=0.3279145588862597, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C
    Total Standard Deviation in ln(k): 1.2466560003391358"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C
Total Standard Deviation in ln(k): 1.2466560003391358""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C
Total Standard Deviation in ln(k): 1.2466560003391358
""",
)

entry(
    index = 254,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R",
    kinetics = ArrheniusBM(A=(5.77079e+06,'m^3/(mol*s)'), n=2.68542e-07, w0=(551500,'J/mol'), E0=(55150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.4776817958368396e-07, var=2.136646797593307, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R
    Total Standard Deviation in ln(k): 2.930376681649643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R
Total Standard Deviation in ln(k): 2.930376681649643""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R
Total Standard Deviation in ln(k): 2.930376681649643
""",
)

entry(
    index = 255,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(655.104,'m^3/(mol*s)'), n=1.27993, w0=(555400,'J/mol'), E0=(55540,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6214857931727823, var=0.7913763674391623, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.344921130788996"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.344921130788996""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.344921130788996
""",
)

entry(
    index = 256,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_2R!H->C",
    kinetics = ArrheniusBM(A=(1.5055e+07,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 257,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 258,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_Ext-1CN-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_Ext-1CN-R_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_Ext-1CN-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 259,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C",
    kinetics = ArrheniusBM(A=(1.98319e+07,'m^3/(mol*s)'), n=3.51368e-07, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7791215597669213e-08, var=0.3934825388480819, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C
    Total Standard Deviation in ln(k): 1.2575340039831724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C
Total Standard Deviation in ln(k): 1.2575340039831724""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C
Total Standard Deviation in ln(k): 1.2575340039831724
""",
)

entry(
    index = 260,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_N-2CN->C",
    kinetics = ArrheniusBM(A=(500,'m^3/(mol*s)'), n=1.5, w0=(590000,'J/mol'), E0=(59000,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_N-2CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_N-2CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 261,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_2CN->C",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(577500,'J/mol'), E0=(57750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_2CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_2CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 262,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C",
    kinetics = ArrheniusBM(A=(8982.49,'m^3/(mol*s)'), n=1.03352, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.38747860357218106, var=1.0474269127416715, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C
    Total Standard Deviation in ln(k): 3.0252879292358665"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 3.0252879292358665""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 3.0252879292358665
""",
)

entry(
    index = 263,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C_2CN->C",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(558500,'J/mol'), E0=(55850,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C_2CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C_2CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 264,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C_N-2CN->C",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C_N-2CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C_N-2CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 265,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(588495,'m^3/(mol*s)'), n=-0.196073, w0=(563000,'J/mol'), E0=(47285.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04130539845100877, var=0.46310082589748625, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 1.4680349360244522"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.4680349360244522""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.4680349360244522
""",
)

entry(
    index = 266,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(100000,'m^3/(mol*s)'), n=3.08101e-08, w0=(563000,'J/mol'), E0=(43666.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 267,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.84881e+06,'m^3/(mol*s)'), n=-0.20598, w0=(527000,'J/mol'), E0=(52700,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.17109444833057352, var=0.012736500736547286, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.6561321436322961"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.6561321436322961""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.6561321436322961
""",
)

entry(
    index = 268,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C",
    kinetics = ArrheniusBM(A=(43.6935,'m^3/(mol*s)'), n=0.860072, w0=(527000,'J/mol'), E0=(52700,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.189097793822231, var=67.87381372743074, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C
    Total Standard Deviation in ln(k): 27.041494607627474"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C
Total Standard Deviation in ln(k): 27.041494607627474""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C
Total Standard Deviation in ln(k): 27.041494607627474
""",
)

entry(
    index = 269,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-7R!H-1C",
    kinetics = ArrheniusBM(A=(84300,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(76679.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-7R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-7R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-7R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-7R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 270,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-4R-R",
    kinetics = ArrheniusBM(A=(7.43976e+07,'m^3/(mol*s)'), n=-0.55, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.2362898290204996e-10, var=1.3251618100913625, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-4R-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-4R-R
    Total Standard Deviation in ln(k): 2.307764270483118"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-4R-R
Total Standard Deviation in ln(k): 2.307764270483118""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-4R-R
Total Standard Deviation in ln(k): 2.307764270483118
""",
)

entry(
    index = 271,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.93787e+06,'m^3/(mol*s)'), n=-0.111067, w0=(531000,'J/mol'), E0=(53100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.006132605713426282, var=0.025170055322906393, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.3334612480939217"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.3334612480939217""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.3334612480939217
""",
)

entry(
    index = 272,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Sp-5C-4R",
    kinetics = ArrheniusBM(A=(1.45e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Sp-5C-4R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Sp-5C-4R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Sp-5C-4R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Sp-5C-4R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 273,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_N-Sp-5C-4R",
    kinetics = ArrheniusBM(A=(1.21e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_N-Sp-5C-4R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_N-Sp-5C-4R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_N-Sp-5C-4R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_N-Sp-5C-4R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 274,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C_Ext-4R-R",
    kinetics = ArrheniusBM(A=(5.7233e-06,'m^3/(mol*s)'), n=3.63493, w0=(539000,'J/mol'), E0=(-13237.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.010920421321496423, var=10.414710282788562, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C_Ext-4R-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C_Ext-4R-R
    Total Standard Deviation in ln(k): 6.497085257759883"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C_Ext-4R-R
Total Standard Deviation in ln(k): 6.497085257759883""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C_Ext-4R-R
Total Standard Deviation in ln(k): 6.497085257759883
""",
)

entry(
    index = 275,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C_Sp-5C-4R",
    kinetics = ArrheniusBM(A=(964000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(91985.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C_Sp-5C-4R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C_Sp-5C-4R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C_Sp-5C-4R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C_Sp-5C-4R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 276,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C_N-Sp-5C-4R",
    kinetics = ArrheniusBM(A=(2.41e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C_N-Sp-5C-4R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C_N-Sp-5C-4R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C_N-Sp-5C-4R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C_N-Sp-5C-4R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 277,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C_Sp-5C-4R",
    kinetics = ArrheniusBM(A=(2.40321e+08,'m^3/(mol*s)'), n=-0.716667, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.8558287082334665e-11, var=0.07236419861267644, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C_Sp-5C-4R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C_Sp-5C-4R
    Total Standard Deviation in ln(k): 0.5392856546392023"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C_Sp-5C-4R
Total Standard Deviation in ln(k): 0.5392856546392023""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C_Sp-5C-4R
Total Standard Deviation in ln(k): 0.5392856546392023
""",
)

entry(
    index = 278,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C_N-Sp-5C-4R",
    kinetics = ArrheniusBM(A=(1.52e+08,'m^3/(mol*s)'), n=-0.7, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C_N-Sp-5C-4R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C_N-Sp-5C-4R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C_N-Sp-5C-4R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C_N-Sp-5C-4R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 279,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N_2N-u1",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(548000,'J/mol'), E0=(39690.4,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 280,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N_N-2N-u1",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 281,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O_Ext-4CNS-R_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(3.47e+08,'m^3/(mol*s)'), n=-0.75, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O_Ext-4CNS-R_Ext-4CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O_Ext-4CNS-R_Ext-4CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 282,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(10764.4,'m^3/(mol*s)'), n=2.42815e-08, w0=(563000,'J/mol'), E0=(17736.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.843380512469269e-09, var=0.01589876918724251, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R
    Total Standard Deviation in ln(k): 0.25277770268983674"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 0.25277770268983674""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 0.25277770268983674
""",
)

entry(
    index = 283,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R",
    kinetics = ArrheniusBM(A=(20268,'m^3/(mol*s)'), n=-1.58689e-07, w0=(563000,'J/mol'), E0=(13257,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.017646221985221817, var=1.5520525800818628, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R
    Total Standard Deviation in ln(k): 2.5418643131300547"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R
Total Standard Deviation in ln(k): 2.5418643131300547""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R
Total Standard Deviation in ln(k): 2.5418643131300547
""",
)

entry(
    index = 284,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_N-6R!H->C_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(7.76152e+14,'m^3/(mol*s)'), n=-3.14885, w0=(563000,'J/mol'), E0=(7412.02,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.9625539661448155, var=15.77167145155163, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_N-6R!H->C_Ext-1CNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_N-6R!H->C_Ext-1CNS-R
    Total Standard Deviation in ln(k): 12.892557544298002"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_N-6R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 12.892557544298002""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_N-6R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 12.892557544298002
""",
)

entry(
    index = 285,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-1CN-R_Ext-2CN-R",
    kinetics = ArrheniusBM(A=(6.5e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-1CN-R_Ext-2CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-1CN-R_Ext-2CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-1CN-R_Ext-2CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-1CN-R_Ext-2CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 286,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.00999e+06,'m^3/(mol*s)'), n=-0.32, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.7581858468390404e-17, var=2.2148373801805805e-05, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.00943469601266542"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.00943469601266542""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.00943469601266542
""",
)

entry(
    index = 287,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C_Ext-2C-R_Sp-2C-1C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(616000,'J/mol'), E0=(61600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C_Ext-2C-R_Sp-2C-1C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C_Ext-2C-R_Sp-2C-1C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C_Ext-2C-R_Sp-2C-1C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_4BrFHO->F_2R!H->C_1R!H->C_Ext-2C-R_Sp-2C-1C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 288,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(936268,'m^3/(mol*s)'), n=2.37741e-07, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=9.423714773231596e-08, var=0.4365798833415042, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 1.3246127386242141"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 1.3246127386242141""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 1.3246127386242141
""",
)

entry(
    index = 289,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(373885,'m^3/(mol*s)'), n=0.242329, w0=(549500,'J/mol'), E0=(-12231.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.029276721674584397, var=1.5973964986306355, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.6073072206241084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.6073072206241084""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.6073072206241084
""",
)

entry(
    index = 290,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_N-2R!H->C_2NO->N",
    kinetics = ArrheniusBM(A=(720,'m^3/(mol*s)'), n=1.5, w0=(576500,'J/mol'), E0=(57650,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_N-2R!H->C_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_N-2R!H->C_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_N-2R!H->C_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_N-2R!H->C_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 291,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_N-2R!H->C_N-2NO->N",
    kinetics = ArrheniusBM(A=(1.09848e+07,'m^3/(mol*s)'), n=2.56317e-07, w0=(642000,'J/mol'), E0=(64200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.610921668180418e-17, var=1.9951707322968388, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_N-2R!H->C_N-2NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_N-2R!H->C_N-2NO->N
    Total Standard Deviation in ln(k): 2.831698574028343"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_N-2R!H->C_N-2NO->N
Total Standard Deviation in ln(k): 2.831698574028343""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_N-2R!H->C_N-2NO->N
Total Standard Deviation in ln(k): 2.831698574028343
""",
)

entry(
    index = 292,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_2R!H->C_1NO->N",
    kinetics = ArrheniusBM(A=(400,'m^3/(mol*s)'), n=1.5, w0=(564000,'J/mol'), E0=(56400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_2R!H->C_1NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_2R!H->C_1NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_2R!H->C_1NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_2R!H->C_1NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 293,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_2R!H->C_N-1NO->N",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=-8.33353e-08, w0=(666000,'J/mol'), E0=(66600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_2R!H->C_N-1NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_2R!H->C_N-1NO->N
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_2R!H->C_N-1NO->N
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_2R!H->C_N-1NO->N
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 294,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1",
    kinetics = ArrheniusBM(A=(27.0566,'m^3/(mol*s)'), n=1.84071, w0=(598333,'J/mol'), E0=(52752.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.24103806381123166, var=0.4437543275243893, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1
    Total Standard Deviation in ln(k): 1.9410752981959152"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1
Total Standard Deviation in ln(k): 1.9410752981959152""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1
Total Standard Deviation in ln(k): 1.9410752981959152
""",
)

entry(
    index = 295,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_N-2NO-u1",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_N-2NO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_N-2NO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 296,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(14.1063,'m^3/(mol*s)'), n=1.81747, w0=(538000,'J/mol'), E0=(49991.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00914657571632494, var=0.13660130397161369, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.7639236849409741"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.7639236849409741""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.7639236849409741
""",
)

entry(
    index = 297,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.08008e+07,'m^3/(mol*s)'), n=2.89777e-07, w0=(538000,'J/mol'), E0=(53800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.031374851813639e-08, var=0.27285596210542634, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.0471858513505898"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.0471858513505898""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.0471858513505898
""",
)

entry(
    index = 298,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_2R!H->C",
    kinetics = ArrheniusBM(A=(1.67e+06,'m^3/(mol*s)'), n=0, w0=(538000,'J/mol'), E0=(53800,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 299,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-2R!H->C",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(557500,'J/mol'), E0=(46201.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 300,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.4572e+07,'m^3/(mol*s)'), n=-6.53027e-08, w0=(538000,'J/mol'), E0=(53800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.508120210243694e-08, var=1.904472164786679, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.766586936706844"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.766586936706844""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.766586936706844
""",
)

entry(
    index = 301,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_2R!H->N_2N-u1",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_2R!H->N_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_2R!H->N_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_2R!H->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_2R!H->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 302,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_2R!H->N_N-2N-u1",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_2R!H->N_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_2R!H->N_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_2R!H->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_2R!H->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 303,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_N-2R!H->N_2CO->C",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(577500,'J/mol'), E0=(57750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_N-2R!H->N_2CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_N-2R!H->N_2CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_N-2R!H->N_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_N-2R!H->N_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 304,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_N-2R!H->N_N-2CO->C",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(625500,'J/mol'), E0=(55881.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_N-2R!H->N_N-2CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_N-2R!H->N_N-2CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_N-2R!H->N_N-2CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_1R!H->N_Sp-2R!H-1N_N-2R!H->N_N-2CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 305,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F",
    kinetics = ArrheniusBM(A=(21.4925,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1003516016859414, var=0.2670935974246947, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F',), comment="""BM rule fitted to 11 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F
    Total Standard Deviation in ln(k): 1.2882088189626515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F
Total Standard Deviation in ln(k): 1.2882088189626515""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F
Total Standard Deviation in ln(k): 1.2882088189626515
""",
)

entry(
    index = 306,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(4.65997e+06,'m^3/(mol*s)'), n=-5.59003e-09, w0=(582417,'J/mol'), E0=(58241.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.2707575238105266e-07, var=0.3891515311137906, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F
    Total Standard Deviation in ln(k): 1.2505946294104147"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F
Total Standard Deviation in ln(k): 1.2505946294104147""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F
Total Standard Deviation in ln(k): 1.2505946294104147
""",
)

entry(
    index = 307,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_4BrO->Br",
    kinetics = ArrheniusBM(A=(2.37e+06,'m^3/(mol*s)'), n=0, w0=(514500,'J/mol'), E0=(51450,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_4BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_4BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_4BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_4BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 308,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br",
    kinetics = ArrheniusBM(A=(44778.9,'m^3/(mol*s)'), n=0.757278, w0=(577562,'J/mol'), E0=(57756.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04181316533898115, var=1.2672014665917155, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br',), comment="""BM rule fitted to 16 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br
    Total Standard Deviation in ln(k): 2.3617893505873684"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br
Total Standard Deviation in ln(k): 2.3617893505873684""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br
Total Standard Deviation in ln(k): 2.3617893505873684
""",
)

entry(
    index = 309,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_4BrO->Br",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(607000,'J/mol'), E0=(60700,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_4BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_4BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_4BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_4BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 310,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br",
    kinetics = ArrheniusBM(A=(818.32,'m^3/(mol*s)'), n=1.27744, w0=(640750,'J/mol'), E0=(64075,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03892258045015562, var=0.3284562628958774, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br
    Total Standard Deviation in ln(k): 1.24673123116833"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br
Total Standard Deviation in ln(k): 1.24673123116833""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br
Total Standard Deviation in ln(k): 1.24673123116833
""",
)

entry(
    index = 311,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=-8.33353e-08, w0=(551500,'J/mol'), E0=(55150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 312,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-5R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(4e+06,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-5R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-5R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 313,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-5R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-5R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 314,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-5R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 315,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_2R!H->C",
    kinetics = ArrheniusBM(A=(105.671,'m^3/(mol*s)'), n=1.44792, w0=(551500,'J/mol'), E0=(55150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07994677116248543, var=0.2503740114467667, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_2R!H->C
    Total Standard Deviation in ln(k): 1.2039883366696844"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_2R!H->C
Total Standard Deviation in ln(k): 1.2039883366696844""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_2R!H->C
Total Standard Deviation in ln(k): 1.2039883366696844
""",
)

entry(
    index = 316,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_N-2R!H->C",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 317,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.44948e+07,'m^3/(mol*s)'), n=3.91461e-07, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.305460834090209e-17, var=0.32880390778633084, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 1.1495436707873932"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 1.1495436707873932""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 1.1495436707873932
""",
)

entry(
    index = 318,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_2N-u1",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 319,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_N-2N-u1",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 320,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(100000,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(34811.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 321,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R_4R->C",
    kinetics = ArrheniusBM(A=(783000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R_4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 322,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R_N-4R->C",
    kinetics = ArrheniusBM(A=(763000,'m^3/(mol*s)'), n=0, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R_N-4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R_N-4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 323,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C_4R->C",
    kinetics = ArrheniusBM(A=(1.45e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C_4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 324,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C_N-4R->C",
    kinetics = ArrheniusBM(A=(7.19e-07,'m^3/(mol*s)'), n=3.13, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C_N-4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C_N-4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_Ext-5BrCF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 325,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-4R-R_Ext-4R-R",
    kinetics = ArrheniusBM(A=(1.52735e+08,'m^3/(mol*s)'), n=-0.75, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-4R-R_Ext-4R-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-4R-R_Ext-4R-R
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-4R-R_Ext-4R-R
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-4R-R_Ext-4R-R
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 326,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-4R-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.56e+07,'m^3/(mol*s)'), n=-0.35, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-4R-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-4R-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-4R-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-4R-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 327,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_4R->C",
    kinetics = ArrheniusBM(A=(843000,'m^3/(mol*s)'), n=-3.92367e-08, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_4R->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_4R->C
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_4R->C
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_4R->C
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 328,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_N-4R->C",
    kinetics = ArrheniusBM(A=(763000,'m^3/(mol*s)'), n=0, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_N-4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_N-4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 329,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C_Ext-4R-R_Ext-4R-R",
    kinetics = ArrheniusBM(A=(2.89e+07,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(83476.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C_Ext-4R-R_Ext-4R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C_Ext-4R-R_Ext-4R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C_Ext-4R-R_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_N-Sp-6R!H-1C_Ext-4R-R_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 330,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C_Sp-5C-4R_Ext-4R-R",
    kinetics = ArrheniusBM(A=(7.76827e+08,'m^3/(mol*s)'), n=-0.9, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0763652085225523e-17, var=0.04891149884417046, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C_Sp-5C-4R_Ext-4R-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C_Sp-5C-4R_Ext-4R-R
    Total Standard Deviation in ln(k): 0.4433660913390881"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C_Sp-5C-4R_Ext-4R-R
Total Standard Deviation in ln(k): 0.4433660913390881""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C_Sp-5C-4R_Ext-4R-R
Total Standard Deviation in ln(k): 0.4433660913390881
""",
)

entry(
    index = 331,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R_Ext-6C-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=4.6177e-08, w0=(563000,'J/mol'), E0=(20937.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R_Ext-6C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R_Ext-6C-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R_Ext-6C-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R_Ext-6C-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 332,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R_Sp-7R!H-6C",
    kinetics = ArrheniusBM(A=(67500,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(16605.5,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R_Sp-7R!H-6C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R_Sp-7R!H-6C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R_Sp-7R!H-6C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R_Sp-7R!H-6C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 333,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R_N-Sp-7R!H-6C",
    kinetics = ArrheniusBM(A=(13571.8,'m^3/(mol*s)'), n=2.80368e-06, w0=(563000,'J/mol'), E0=(20084.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=8.432406102244557e-08, var=0.6296916452046188, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R_N-Sp-7R!H-6C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R_N-Sp-7R!H-6C
    Total Standard Deviation in ln(k): 1.5908198917220893"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R_N-Sp-7R!H-6C
Total Standard Deviation in ln(k): 1.5908198917220893""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R_N-Sp-7R!H-6C
Total Standard Deviation in ln(k): 1.5908198917220893
""",
)

entry(
    index = 334,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(774450,'m^3/(mol*s)'), n=-1.98908e-08, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=7.107495827623396e-08, var=0.2355817332363053, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_5R!H->C
    Total Standard Deviation in ln(k): 0.973033685645405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_5R!H->C
Total Standard Deviation in ln(k): 0.973033685645405""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_5R!H->C
Total Standard Deviation in ln(k): 0.973033685645405
""",
)

entry(
    index = 335,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 336,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(1.11534e+06,'m^3/(mol*s)'), n=1.21072e-07, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.2712594181390784e-07, var=0.1823142204075943, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C
    Total Standard Deviation in ln(k): 0.8559875021807728"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 0.8559875021807728""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 0.8559875021807728
""",
)

entry(
    index = 337,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_N-Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(29186.3,'m^3/(mol*s)'), n=0.807763, w0=(549500,'J/mol'), E0=(15513.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09758905201122342, var=2.521665006783426, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_N-Sp-5R!H-1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_N-Sp-5R!H-1C
    Total Standard Deviation in ln(k): 3.428668064045563"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 3.428668064045563""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 3.428668064045563
""",
)

entry(
    index = 338,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1_1NO->N",
    kinetics = ArrheniusBM(A=(26.4912,'m^3/(mol*s)'), n=1.82399, w0=(573250,'J/mol'), E0=(52118.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.20148362850470902, var=0.27147237417689896, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1_1NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1_1NO->N
    Total Standard Deviation in ln(k): 1.5507676079238173"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1_1NO->N
Total Standard Deviation in ln(k): 1.5507676079238173""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1_1NO->N
Total Standard Deviation in ln(k): 1.5507676079238173
""",
)

entry(
    index = 339,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1_N-1NO->N",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(648500,'J/mol'), E0=(59320.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1_N-1NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1_N-1NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1_N-1NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1_N-1NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 340,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(538000,'J/mol'), E0=(82230,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 341,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(538000,'J/mol'), E0=(78689.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 342,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(538000,'J/mol'), E0=(53800,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 343,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H",
    kinetics = ArrheniusBM(A=(1.73205e+07,'m^3/(mol*s)'), n=3.73492e-07, w0=(538000,'J/mol'), E0=(53800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=6.458191251135313e-17, var=0.1655219496203035, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H
    Total Standard Deviation in ln(k): 0.8156142143252552"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H
Total Standard Deviation in ln(k): 0.8156142143252552""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H
Total Standard Deviation in ln(k): 0.8156142143252552
""",
)

entry(
    index = 344,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.3811e+07,'m^3/(mol*s)'), n=1.98531e-07, w0=(538000,'J/mol'), E0=(53800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.202772333702684e-09, var=0.36033976853782135, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.2034085547674045"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.2034085547674045""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.2034085547674045
""",
)

entry(
    index = 345,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-1CO-R",
    kinetics = ArrheniusBM(A=(18.9153,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10035160543507311, var=0.15570237264362138, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-1CO-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-1CO-R
    Total Standard Deviation in ln(k): 1.0431909321781416"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-1CO-R
Total Standard Deviation in ln(k): 1.0431909321781416""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-1CO-R
Total Standard Deviation in ln(k): 1.0431909321781416
""",
)

entry(
    index = 346,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(26.8761,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.5096568970344721, var=2.413897921625164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 6.907809337393689"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.907809337393689""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.907809337393689
""",
)

entry(
    index = 347,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 348,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_Ext-1CO-R",
    kinetics = ArrheniusBM(A=(8e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_Ext-1CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_Ext-1CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_Ext-1CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_Ext-1CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 349,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClINOPSSi-R",
    kinetics = ArrheniusBM(A=(8e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 350,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_1CO->C",
    kinetics = ArrheniusBM(A=(4e+06,'m^3/(mol*s)'), n=6.4521e-08, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_1CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_1CO->C
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_1CO->C
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_1CO->C
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 351,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_N-1CO->C",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(67950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_N-1CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_N-1CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_N-1CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_N-1CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 352,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R",
    kinetics = ArrheniusBM(A=(11841.3,'m^3/(mol*s)'), n=0.932034, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.051462352195148865, var=1.3863207513923612, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R',), comment="""BM rule fitted to 13 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R
    Total Standard Deviation in ln(k): 2.4897200318547332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R
Total Standard Deviation in ln(k): 2.4897200318547332""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R
Total Standard Deviation in ln(k): 2.4897200318547332
""",
)

entry(
    index = 353,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_1CO->C",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_1CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_1CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_1CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_1CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 354,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_N-1CO->C",
    kinetics = ArrheniusBM(A=(1.09772e+07,'m^3/(mol*s)'), n=2.36609e-07, w0=(679500,'J/mol'), E0=(67950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7221843336360836e-16, var=4.947235657586348, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_N-1CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_N-1CO->C
    Total Standard Deviation in ln(k): 4.459008379338471"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_N-1CO->C
Total Standard Deviation in ln(k): 4.459008379338471""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_N-1CO->C
Total Standard Deviation in ln(k): 4.459008379338471
""",
)

entry(
    index = 355,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_2NO->N",
    kinetics = ArrheniusBM(A=(809.839,'m^3/(mol*s)'), n=1.27907, w0=(626000,'J/mol'), E0=(62600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570074, var=0.32880390778633134, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_2NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_2NO->N
    Total Standard Deviation in ln(k): 2.6541430907798746"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_2NO->N
Total Standard Deviation in ln(k): 2.6541430907798746""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_2NO->N
Total Standard Deviation in ln(k): 2.6541430907798746
""",
)

entry(
    index = 356,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_N-2NO->N",
    kinetics = ArrheniusBM(A=(2.88674e+06,'m^3/(mol*s)'), n=5.26425e-07, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=2.413897921625164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_N-2NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_N-2NO->N
    Total Standard Deviation in ln(k): 3.1147015559000413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_N-2NO->N
Total Standard Deviation in ln(k): 3.1147015559000413""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_N-2NO->N
Total Standard Deviation in ln(k): 3.1147015559000413
""",
)

entry(
    index = 357,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-2R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-2R!H-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-2R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-2R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-2R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 358,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-2R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-2R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-2R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-2R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-1CO-R_Ext-2R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 359,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_2R!H->C_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(0.00558313,'m^3/(mol*s)'), n=2.89583, w0=(551500,'J/mol'), E0=(55150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.4053866559415926, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_2R!H->C_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_2R!H->C_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 8.008842950292529"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_2R!H->C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 8.008842950292529""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_2R!H->C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 8.008842950292529
""",
)

entry(
    index = 360,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_2R!H->C_Ext-5R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_2R!H->C_Ext-5R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_2R!H->C_Ext-5R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_2R!H->C_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_2R!H->C_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 361,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_2R!H->C_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_2R!H->C_Ext-5R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_2R!H->C_Ext-5R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_2R!H->C_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_N-Sp-2R!H-1CO_Ext-2R!H-R_2R!H->C_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 362,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 363,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_N-4BrFHO-u1_N-1R!H->O_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 364,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-4R-R_Ext-4R-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.08e+08,'m^3/(mol*s)'), n=-0.75, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-4R-R_Ext-4R-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-4R-R_Ext-4R-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-4R-R_Ext-4R-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-4R-R_Ext-4R-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 365,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_4R->C_Sp-5C-4C",
    kinetics = ArrheniusBM(A=(843000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_4R->C_Sp-5C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_4R->C_Sp-5C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_4R->C_Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_4R->C_Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 366,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_4R->C_N-Sp-5C-4C",
    kinetics = ArrheniusBM(A=(843000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_4R->C_N-Sp-5C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_4R->C_N-Sp-5C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_4R->C_N-Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_4R->C_N-Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 367,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C_Sp-5C-4R_Ext-4R-R_Ext-4R-R",
    kinetics = ArrheniusBM(A=(2.86e+09,'m^3/(mol*s)'), n=-1.1, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C_Sp-5C-4R_Ext-4R-R_Ext-4R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C_Sp-5C-4R_Ext-4R-R_Ext-4R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C_Sp-5C-4R_Ext-4R-R_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCFNO->O_N-Sp-5BrBrBrCCCFFF#4R_5BrCF->C_Sp-2R!H-1C_2R!H->C_Sp-5C-4R_Ext-4R-R_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 368,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R_Ext-6C-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(20643.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R_Ext-6C-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R_Ext-6C-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R_Ext-6C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R_Ext-6C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 369,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.06667e+06,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 370,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.05e+06,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 371,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_5R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(602222,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_5R!H->C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_5R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_5R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-2C-R_5R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 372,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C",
    kinetics = ArrheniusBM(A=(1.0119e+06,'m^3/(mol*s)'), n=-2.72185e-08, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=8.371635008370871e-08, var=0.1168666827194647, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C
    Total Standard Deviation in ln(k): 0.6853343203143046"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C
Total Standard Deviation in ln(k): 0.6853343203143046""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C
Total Standard Deviation in ln(k): 0.6853343203143046
""",
)

entry(
    index = 373,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 374,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_N-Sp-5R!H-1C_5R!H->C",
    kinetics = ArrheniusBM(A=(1.8e+07,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(46024.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_N-Sp-5R!H-1C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_N-Sp-5R!H-1C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_N-Sp-5R!H-1C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_N-Sp-5R!H-1C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 375,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_N-Sp-5R!H-1C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1175.26,'m^3/(mol*s)'), n=1.21164, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0064379313563148, var=0.3339094409755069, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_N-Sp-5R!H-1C_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_N-Sp-5R!H-1C_N-5R!H->C
    Total Standard Deviation in ln(k): 3.687172635934617"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_N-Sp-5R!H-1C_N-5R!H->C
Total Standard Deviation in ln(k): 3.687172635934617""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_N-Sp-5R!H-1C_N-5R!H->C
Total Standard Deviation in ln(k): 3.687172635934617
""",
)

entry(
    index = 376,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1_1NO->N_2NO->N",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1_1NO->N_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1_1NO->N_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1_1NO->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1_1NO->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 377,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1_1NO->N_N-2NO->N",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(612000,'J/mol'), E0=(63725,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1_1NO->N_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1_1NO->N_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1_1NO->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_N-1R!H->C_N-2R!H->C_2NO-u1_1NO->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 378,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(538000,'J/mol'), E0=(53800,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 379,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(1.5e+07,'m^3/(mol*s)'), n=0, w0=(538000,'J/mol'), E0=(53800,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 380,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=1.03647e-07, w0=(538000,'J/mol'), E0=(53800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 381,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-1CO-R_Ext-1CO-R",
    kinetics = ArrheniusBM(A=(15.5169,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10035159271588616, var=0.0, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-1CO-R_Ext-1CO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-1CO-R_Ext-1CO-R
    Total Standard Deviation in ln(k): 0.25213968019066874"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-1CO-R_Ext-1CO-R
Total Standard Deviation in ln(k): 0.25213968019066874""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-1CO-R_Ext-1CO-R
Total Standard Deviation in ln(k): 0.25213968019066874
""",
)

entry(
    index = 382,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-1CO-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(21.9442,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.5096568970344717, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-1CO-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-1CO-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 5.758265666606295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-1CO-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.758265666606295""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-1CO-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.758265666606295
""",
)

entry(
    index = 383,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_1CO->C_5BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(4e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_1CO->C_5BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_1CO->C_5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_1CO->C_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_1CO->C_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 384,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_1CO->C_N-5BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(4e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_1CO->C_N-5BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_1CO->C_N-5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_1CO->C_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_N-5R!H->F_1CO->C_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 385,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO",
    kinetics = ArrheniusBM(A=(43216.4,'m^3/(mol*s)'), n=0.807763, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.044600708811499516, var=0.1387658964498666, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO
    Total Standard Deviation in ln(k): 0.8588518561398296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO
Total Standard Deviation in ln(k): 0.8588518561398296""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO
Total Standard Deviation in ln(k): 0.8588518561398296
""",
)

entry(
    index = 386,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_N-Sp-5R!H-1CO",
    kinetics = ArrheniusBM(A=(643.182,'m^3/(mol*s)'), n=1.21164, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06690106479011634, var=4.77344894659504, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_N-Sp-5R!H-1CO',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_N-Sp-5R!H-1CO
    Total Standard Deviation in ln(k): 4.548083243181481"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_N-Sp-5R!H-1CO
Total Standard Deviation in ln(k): 4.548083243181481""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_N-Sp-5R!H-1CO
Total Standard Deviation in ln(k): 4.548083243181481
""",
)

entry(
    index = 387,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_2NO->N_1CO->C",
    kinetics = ArrheniusBM(A=(3.6,'m^3/(mol*s)'), n=2, w0=(590000,'J/mol'), E0=(59000,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_2NO->N_1CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_2NO->N_1CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_2NO->N_1CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_2NO->N_1CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 388,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_2NO->N_N-1CO->C",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(662000,'J/mol'), E0=(66200,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_2NO->N_N-1CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_2NO->N_N-1CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_2NO->N_N-1CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_2NO->N_N-1CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 389,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_N-2NO->N_Ext-1CO-R",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_N-2NO->N_Ext-1CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_N-2NO->N_Ext-1CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_N-2NO->N_Ext-1CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_N-2R!H->C_N-4BrO->Br_N-2NO->N_Ext-1CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 390,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(900000,'m^3/(mol*s)'), n=-1.57583e-09, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 391,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(901998,'m^3/(mol*s)'), n=3.77371e-08, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0763652085225523e-17, var=3.9331302308647265e-05, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.01257263051719242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.01257263051719242""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.01257263051719242
""",
)

entry(
    index = 392,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(538000,'J/mol'), E0=(53800,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 393,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-1CO-R_Ext-1CO-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.2e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-1CO-R_Ext-1CO-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-1CO-R_Ext-1CO-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-1CO-R_Ext-1CO-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_Ext-2R!H-R_5R!H->F_Ext-1CO-R_Ext-1CO-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 394,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_Ext-1CO-R",
    kinetics = ArrheniusBM(A=(19337.9,'m^3/(mol*s)'), n=0.908733, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.050175799781273386, var=0.03404324048259046, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_Ext-1CO-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_Ext-1CO-R
    Total Standard Deviation in ln(k): 0.495959717071232"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_Ext-1CO-R
Total Standard Deviation in ln(k): 0.495959717071232""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_Ext-1CO-R
Total Standard Deviation in ln(k): 0.495959717071232
""",
)

entry(
    index = 395,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_5R!H->C",
    kinetics = ArrheniusBM(A=(1.514e+07,'m^3/(mol*s)'), n=2.61625e-07, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.036502523045642e-08, var=0.36467594120944413, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_5R!H->C
    Total Standard Deviation in ln(k): 1.2106276063144492"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_5R!H->C
Total Standard Deviation in ln(k): 1.2106276063144492""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_5R!H->C
Total Standard Deviation in ln(k): 1.2106276063144492
""",
)

entry(
    index = 396,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_N-5R!H->C",
    kinetics = ArrheniusBM(A=(32.9163,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.5096568970344717, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_N-5R!H->C
    Total Standard Deviation in ln(k): 5.758265666606295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_N-5R!H->C
Total Standard Deviation in ln(k): 5.758265666606295""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_N-5R!H->C
Total Standard Deviation in ln(k): 5.758265666606295
""",
)

entry(
    index = 397,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_N-Sp-5R!H-1CO_5R!H->C",
    kinetics = ArrheniusBM(A=(4.24245,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.509656897034472, var=4.528059738902607, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_N-Sp-5R!H-1CO_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_N-Sp-5R!H-1CO_5R!H->C
    Total Standard Deviation in ln(k): 8.059031284357149"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_N-Sp-5R!H-1CO_5R!H->C
Total Standard Deviation in ln(k): 8.059031284357149""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_N-Sp-5R!H-1CO_5R!H->C
Total Standard Deviation in ln(k): 8.059031284357149
""",
)

entry(
    index = 398,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_N-Sp-5R!H-1CO_N-5R!H->C",
    kinetics = ArrheniusBM(A=(97510.5,'m^3/(mol*s)'), n=0.605822, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5032189656781574, var=0.9399316159026726, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_N-Sp-5R!H-1CO_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_N-Sp-5R!H-1CO_N-5R!H->C
    Total Standard Deviation in ln(k): 3.2079613302398537"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_N-Sp-5R!H-1CO_N-5R!H->C
Total Standard Deviation in ln(k): 3.2079613302398537""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_N-Sp-5R!H-1CO_N-5R!H->C
Total Standard Deviation in ln(k): 3.2079613302398537
""",
)

entry(
    index = 399,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R_Sp-6R!H-5C",
    kinetics = ArrheniusBM(A=(900000,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R_Sp-6R!H-5C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R_Sp-6R!H-5C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R_Sp-6R!H-5C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R_Sp-6R!H-5C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 400,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C",
    kinetics = ArrheniusBM(A=(900000,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1R!H_1R!H->C_2R!H->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 401,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_Ext-1CO-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.20499e+07,'m^3/(mol*s)'), n=6.26727e-08, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.3454565106531903e-18, var=0.00013774025631438147, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_Ext-1CO-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_Ext-1CO-R_5R!H->C
    Total Standard Deviation in ln(k): 0.023528131175717372"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_Ext-1CO-R_5R!H->C
Total Standard Deviation in ln(k): 0.023528131175717372""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_Ext-1CO-R_5R!H->C
Total Standard Deviation in ln(k): 0.023528131175717372
""",
)

entry(
    index = 402,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_Ext-1CO-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(31.0338,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.509656897034472, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_Ext-1CO-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_Ext-1CO-R_N-5R!H->C
    Total Standard Deviation in ln(k): 3.793107781493648"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_Ext-1CO-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.793107781493648""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_Ext-1CO-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.793107781493648
""",
)

entry(
    index = 403,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.2e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrFHNOS->N_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-1R!H->N_Sp-2R!H-1CO_2R!H->C_N-4BrO->Br_Ext-1CO-R_Sp-5R!H-1CO_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

