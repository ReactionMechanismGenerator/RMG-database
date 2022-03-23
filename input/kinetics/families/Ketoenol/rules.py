#!/usr/bin/env python
# encoding: utf-8

name = "Ketoenol/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.76838e-20,'s^-1'), n=9.51934, w0=(790938,'J/mol'), E0=(132573,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0692840094936698, var=37.30464287970276, Tref=1000.0, N=104, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 104 training reactions at node Root
    Total Standard Deviation in ln(k): 12.418506480580113"""),
    rank = 11,
    shortDesc = """BM rule fitted to 104 training reactions at node Root
Total Standard Deviation in ln(k): 12.418506480580113""",
    longDesc = 
"""
BM rule fitted to 104 training reactions at node Root
Total Standard Deviation in ln(k): 12.418506480580113
""",
)

entry(
    index = 2,
    label = "Root_3R!H->C",
    kinetics = ArrheniusBM(A=(1.28568e-29,'s^-1'), n=12.1507, w0=(783698,'J/mol'), E0=(155054,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09922772206091167, var=10.046655596750956, Tref=1000.0, N=48, data_mean=0.0, correlation='Root_3R!H->C',), comment="""BM rule fitted to 48 training reactions at node Root_3R!H->C
    Total Standard Deviation in ln(k): 6.603616350390221"""),
    rank = 11,
    shortDesc = """BM rule fitted to 48 training reactions at node Root_3R!H->C
Total Standard Deviation in ln(k): 6.603616350390221""",
    longDesc = 
"""
BM rule fitted to 48 training reactions at node Root_3R!H->C
Total Standard Deviation in ln(k): 6.603616350390221
""",
)

entry(
    index = 3,
    label = "Root_N-3R!H->C",
    kinetics = ArrheniusBM(A=(8.89686e-09,'s^-1'), n=6.15574, w0=(797143,'J/mol'), E0=(123730,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15198732759701325, var=11.459767347743577, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_N-3R!H->C',), comment="""BM rule fitted to 56 training reactions at node Root_N-3R!H->C
    Total Standard Deviation in ln(k): 7.168362649764804"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_N-3R!H->C
Total Standard Deviation in ln(k): 7.168362649764804""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_N-3R!H->C
Total Standard Deviation in ln(k): 7.168362649764804
""",
)

entry(
    index = 4,
    label = "Root_3R!H->C_3C-inRing",
    kinetics = ArrheniusBM(A=(6.39312e-20,'s^-1'), n=9.28196, w0=(783500,'J/mol'), E0=(172103,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05177845734786932, var=3.027945469263943, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing',), comment="""BM rule fitted to 13 training reactions at node Root_3R!H->C_3C-inRing
    Total Standard Deviation in ln(k): 3.6185346711093223"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_3R!H->C_3C-inRing
Total Standard Deviation in ln(k): 3.6185346711093223""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_3R!H->C_3C-inRing
Total Standard Deviation in ln(k): 3.6185346711093223
""",
)

entry(
    index = 5,
    label = "Root_3R!H->C_N-3C-inRing",
    kinetics = ArrheniusBM(A=(9.92275e-34,'s^-1'), n=13.3659, w0=(783771,'J/mol'), E0=(147816,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1129384407839629, var=13.330470556655888, Tref=1000.0, N=35, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing',), comment="""BM rule fitted to 35 training reactions at node Root_3R!H->C_N-3C-inRing
    Total Standard Deviation in ln(k): 7.6032365159691855"""),
    rank = 11,
    shortDesc = """BM rule fitted to 35 training reactions at node Root_3R!H->C_N-3C-inRing
Total Standard Deviation in ln(k): 7.6032365159691855""",
    longDesc = 
"""
BM rule fitted to 35 training reactions at node Root_3R!H->C_N-3C-inRing
Total Standard Deviation in ln(k): 7.6032365159691855
""",
)

entry(
    index = 6,
    label = "Root_N-3R!H->C_1R!H-inRing",
    kinetics = ArrheniusBM(A=(2.10561e-09,'s^-1'), n=6.34, w0=(798000,'J/mol'), E0=(145533,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.23998388176772487, var=8.456408506358963, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing',), comment="""BM rule fitted to 24 training reactions at node Root_N-3R!H->C_1R!H-inRing
    Total Standard Deviation in ln(k): 6.432725054061367"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-3R!H->C_1R!H-inRing
Total Standard Deviation in ln(k): 6.432725054061367""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-3R!H->C_1R!H-inRing
Total Standard Deviation in ln(k): 6.432725054061367
""",
)

entry(
    index = 7,
    label = "Root_N-3R!H->C_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.11915e-11,'s^-1'), n=6.98284, w0=(796500,'J/mol'), E0=(97373.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.018529862444859643, var=1.7045016838505962, Tref=1000.0, N=32, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing',), comment="""BM rule fitted to 32 training reactions at node Root_N-3R!H->C_N-1R!H-inRing
    Total Standard Deviation in ln(k): 2.6638707110766147"""),
    rank = 11,
    shortDesc = """BM rule fitted to 32 training reactions at node Root_N-3R!H->C_N-1R!H-inRing
Total Standard Deviation in ln(k): 2.6638707110766147""",
    longDesc = 
"""
BM rule fitted to 32 training reactions at node Root_N-3R!H->C_N-1R!H-inRing
Total Standard Deviation in ln(k): 2.6638707110766147
""",
)

entry(
    index = 8,
    label = "Root_3R!H->C_3C-inRing_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(4.11555e-10,'s^-1'), n=6.40743, w0=(783500,'J/mol'), E0=(180362,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05801351630604745, var=6.028099843723627, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-1R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R
    Total Standard Deviation in ln(k): 5.067826053991267"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R
Total Standard Deviation in ln(k): 5.067826053991267""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R
Total Standard Deviation in ln(k): 5.067826053991267
""",
)

entry(
    index = 9,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_5R!H->O",
    kinetics = ArrheniusBM(A=(6.74681e-29,'s^-1'), n=11.8652, w0=(783500,'J/mol'), E0=(159410,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0023429600482609584, var=0.03529471902352428, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_5R!H->O
    Total Standard Deviation in ln(k): 0.38251418372418733"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_5R!H->O
Total Standard Deviation in ln(k): 0.38251418372418733""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_5R!H->O
Total Standard Deviation in ln(k): 0.38251418372418733
""",
)

entry(
    index = 10,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(2.87045e-25,'s^-1'), n=10.8475, w0=(783500,'J/mol'), E0=(165263,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004029042513347415, var=0.5211813278651625, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O',), comment="""BM rule fitted to 7 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 1.4573993994053007"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O
Total Standard Deviation in ln(k): 1.4573993994053007""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O
Total Standard Deviation in ln(k): 1.4573993994053007
""",
)

entry(
    index = 11,
    label = "Root_3R!H->C_N-3C-inRing_1R!H->N",
    kinetics = ArrheniusBM(A=(9.27692e-54,'s^-1'), n=19.1913, w0=(793000,'J/mol'), E0=(143942,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_1R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_1R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_1R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N",
    kinetics = ArrheniusBM(A=(6.28598e-33,'s^-1'), n=13.1347, w0=(783500,'J/mol'), E0=(148411,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12040560732940568, var=12.763302160649639, Tref=1000.0, N=34, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N',), comment="""BM rule fitted to 34 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N
    Total Standard Deviation in ln(k): 7.464595884854784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 34 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N
Total Standard Deviation in ln(k): 7.464595884854784""",
    longDesc = 
"""
BM rule fitted to 34 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N
Total Standard Deviation in ln(k): 7.464595884854784
""",
)

entry(
    index = 13,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(5.35688e-05,'s^-1'), n=5.08296, w0=(798000,'J/mol'), E0=(150839,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.33809283805023616, var=12.612698240770657, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 14 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 7.96916798023565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 7.96916798023565""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 7.96916798023565
""",
)

entry(
    index = 14,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(1.6726e-17,'s^-1'), n=8.65336, w0=(798000,'J/mol'), E0=(133311,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02719223077483626, var=3.2866152813970424, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 10 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 3.702711314750445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 3.702711314750445""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 3.702711314750445
""",
)

entry(
    index = 15,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFINOPSSi->S",
    kinetics = ArrheniusBM(A=(1583.91,'s^-1'), n=2.85161, w0=(782000,'J/mol'), E0=(88955.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.003045184023974304, var=0.28211849898893376, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFINOPSSi->S',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFINOPSSi->S
    Total Standard Deviation in ln(k): 1.0724628112272296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFINOPSSi->S
Total Standard Deviation in ln(k): 1.0724628112272296""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFINOPSSi->S
Total Standard Deviation in ln(k): 1.0724628112272296
""",
)

entry(
    index = 16,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S",
    kinetics = ArrheniusBM(A=(1.57125e-11,'s^-1'), n=6.94204, w0=(798000,'J/mol'), E0=(98584.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.010049252580498404, var=1.2248685251132718, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S',), comment="""BM rule fitted to 29 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S
    Total Standard Deviation in ln(k): 2.243965437741945"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S
Total Standard Deviation in ln(k): 2.243965437741945""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S
Total Standard Deviation in ln(k): 2.243965437741945
""",
)

entry(
    index = 17,
    label = "Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.59677e-16,'s^-1'), n=8.29403, w0=(783500,'J/mol'), E0=(173470,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.005973981573233584, var=1.466149892623437, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 2.442436990667526"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C
Total Standard Deviation in ln(k): 2.442436990667526""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C
Total Standard Deviation in ln(k): 2.442436990667526
""",
)

entry(
    index = 18,
    label = "Root_3R!H->C_3C-inRing_Ext-1R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0332916,'s^-1'), n=3.98637, w0=(783500,'J/mol'), E0=(171985,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-1R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5.66974e-32,'s^-1'), n=12.7337, w0=(783500,'J/mol'), E0=(150797,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_5R!H->O_Ext-5O-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.89196e-24,'s^-1'), n=10.6025, w0=(783500,'J/mol'), E0=(164616,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.002089150051635779, var=0.18931816314976802, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R',), comment="""BM rule fitted to 5 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R
    Total Standard Deviation in ln(k): 0.8775235281941672"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.8775235281941672""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.8775235281941672
""",
)

entry(
    index = 21,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_5BrCClFINPSSi->N",
    kinetics = ArrheniusBM(A=(7.8149e-27,'s^-1'), n=11.304, w0=(783500,'J/mol'), E0=(171568,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_5BrCClFINPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_5BrCClFINPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_5BrCClFINPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_5BrCClFINPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_N-5BrCClFINPSSi->N",
    kinetics = ArrheniusBM(A=(2.16654e-24,'s^-1'), n=10.6408, w0=(783500,'J/mol'), E0=(171460,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_N-5BrCClFINPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_N-5BrCClFINPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_N-5BrCClFINPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_N-5BrCClFINPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.12687e-31,'s^-1'), n=12.5518, w0=(783500,'J/mol'), E0=(150326,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15967312167986036, var=17.0288881882057, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R',), comment="""BM rule fitted to 22 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R
    Total Standard Deviation in ln(k): 8.673943245132968"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R
Total Standard Deviation in ln(k): 8.673943245132968""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R
Total Standard Deviation in ln(k): 8.673943245132968
""",
)

entry(
    index = 24,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R",
    kinetics = ArrheniusBM(A=(7.84375e-39,'s^-1'), n=14.821, w0=(783500,'J/mol'), E0=(140629,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.008036413422190726, var=5.867009535524812, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R',), comment="""BM rule fitted to 9 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R
    Total Standard Deviation in ln(k): 4.8760433774685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R
Total Standard Deviation in ln(k): 4.8760433774685""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R
Total Standard Deviation in ln(k): 4.8760433774685
""",
)

entry(
    index = 25,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C",
    kinetics = ArrheniusBM(A=(2.48826e-19,'s^-1'), n=9.18271, w0=(798000,'J/mol'), E0=(123275,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00853348498558203, var=1.1330821104625106, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C
    Total Standard Deviation in ln(k): 2.1554078269576387"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C
Total Standard Deviation in ln(k): 2.1554078269576387""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C
Total Standard Deviation in ln(k): 2.1554078269576387
""",
)

entry(
    index = 26,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C",
    kinetics = ArrheniusBM(A=(8728.95,'s^-1'), n=2.73666, w0=(798000,'J/mol'), E0=(163324,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.47157079064189145, var=28.019416092142862, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C
    Total Standard Deviation in ln(k): 11.79658949780601"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C
Total Standard Deviation in ln(k): 11.79658949780601""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C
Total Standard Deviation in ln(k): 11.79658949780601
""",
)

entry(
    index = 27,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.21015e-08,'s^-1'), n=6.03421, w0=(798000,'J/mol'), E0=(132081,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.50083e-19,'s^-1'), n=9.25255, w0=(798000,'J/mol'), E0=(127699,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0006427823284157327, var=0.5967826247970905, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 1.5503071008497333"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 1.5503071008497333""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 1.5503071008497333
""",
)

entry(
    index = 29,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2.30353e-18,'s^-1'), n=8.91582, w0=(798000,'J/mol'), E0=(136829,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.035586230607452495, var=5.809982458271787, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 4.921607065115819"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 4.921607065115819""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 4.921607065115819
""",
)

entry(
    index = 30,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFINOPSSi->S_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2857.3,'s^-1'), n=2.79065, w0=(782000,'J/mol'), E0=(88663.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.015825826525184e-07, var=0.0007766175206250726, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFINOPSSi->S_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFINOPSSi->S_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.05586817935319939"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFINOPSSi->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.05586817935319939""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFINOPSSi->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.05586817935319939
""",
)

entry(
    index = 31,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(8.82754e-12,'s^-1'), n=7.02434, w0=(798000,'J/mol'), E0=(97383.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02145633278380776, var=1.7436479446789037, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R',), comment="""BM rule fitted to 19 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R
    Total Standard Deviation in ln(k): 2.7011081673544015"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.7011081673544015""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.7011081673544015
""",
)

entry(
    index = 32,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(7.24956e-11,'s^-1'), n=6.76655, w0=(798000,'J/mol'), E0=(99955.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0007747771928123646, var=0.25480797716605197, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.013907033133442"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.013907033133442""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.013907033133442
""",
)

entry(
    index = 33,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.76833e-11,'s^-1'), n=6.92692, w0=(798000,'J/mol'), E0=(101353,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.006227847479353703, var=0.2545942328714686, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.0271836869728679"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.0271836869728679""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.0271836869728679
""",
)

entry(
    index = 34,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_6R!H->N",
    kinetics = ArrheniusBM(A=(3.10725e-11,'s^-1'), n=6.76455, w0=(798000,'J/mol'), E0=(102204,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N",
    kinetics = ArrheniusBM(A=(6.36022e-11,'s^-1'), n=6.62861, w0=(798000,'J/mol'), E0=(100596,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_6R!H->N",
    kinetics = ArrheniusBM(A=(3.65781e-21,'s^-1'), n=9.63784, w0=(783500,'J/mol'), E0=(169134,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N",
    kinetics = ArrheniusBM(A=(2.75059e-13,'s^-1'), n=7.35321, w0=(783500,'J/mol'), E0=(177699,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.000997566440040575, var=0.3154583489682882, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N
    Total Standard Deviation in ln(k): 1.1284795153107703"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N
Total Standard Deviation in ln(k): 1.1284795153107703""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N
Total Standard Deviation in ln(k): 1.1284795153107703
""",
)

entry(
    index = 38,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_5BrCClFINPSSi->N",
    kinetics = ArrheniusBM(A=(1.29619e-20,'s^-1'), n=9.49921, w0=(783500,'J/mol'), E0=(172955,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0015278345520543426, var=0.001002786860426071, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_5BrCClFINPSSi->N',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_5BrCClFINPSSi->N
    Total Standard Deviation in ln(k): 0.0673223452312378"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_5BrCClFINPSSi->N
Total Standard Deviation in ln(k): 0.0673223452312378""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_5BrCClFINPSSi->N
Total Standard Deviation in ln(k): 0.0673223452312378
""",
)

entry(
    index = 39,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N",
    kinetics = ArrheniusBM(A=(5.29297e-27,'s^-1'), n=11.3369, w0=(783500,'J/mol'), E0=(159055,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00368447309266697, var=0.3545110352579805, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N',), comment="""BM rule fitted to 3 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N
    Total Standard Deviation in ln(k): 1.2028933602366145"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N
Total Standard Deviation in ln(k): 1.2028933602366145""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N
Total Standard Deviation in ln(k): 1.2028933602366145
""",
)

entry(
    index = 40,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.69228e-41,'s^-1'), n=15.5972, w0=(783500,'J/mol'), E0=(139652,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.034666433046162584, var=6.385993774218826, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 17 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 5.153172156204951"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 5.153172156204951""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 5.153172156204951
""",
)

entry(
    index = 41,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.30612e-17,'s^-1'), n=8.56328, w0=(783500,'J/mol'), E0=(134362,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.022660677363961, var=24.016459378921425, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 9.881459527240331"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 9.881459527240331""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 9.881459527240331
""",
)

entry(
    index = 42,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.15187e-37,'s^-1'), n=14.407, w0=(783500,'J/mol'), E0=(141076,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.007211973193153581, var=4.798146021865665, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 4.409426723749229"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.409426723749229""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.409426723749229
""",
)

entry(
    index = 43,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N",
    kinetics = ArrheniusBM(A=(1.2243e-18,'s^-1'), n=8.98338, w0=(798000,'J/mol'), E0=(122888,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.015261423392135449, var=1.4553369561866838, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N
    Total Standard Deviation in ln(k): 2.4568045025233345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N
Total Standard Deviation in ln(k): 2.4568045025233345""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N
Total Standard Deviation in ln(k): 2.4568045025233345
""",
)

entry(
    index = 44,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_N-7R!H->N",
    kinetics = ArrheniusBM(A=(3.14253e-21,'s^-1'), n=9.72938, w0=(798000,'J/mol'), E0=(123824,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.427944658970612e-06, var=0.049309430357815286, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_N-7R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_N-7R!H->N
    Total Standard Deviation in ln(k): 0.44517712022807143"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_N-7R!H->N
Total Standard Deviation in ln(k): 0.44517712022807143""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_N-7R!H->N
Total Standard Deviation in ln(k): 0.44517712022807143
""",
)

entry(
    index = 45,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_5R!H->N",
    kinetics = ArrheniusBM(A=(7.03103e-17,'s^-1'), n=8.43292, w0=(798000,'J/mol'), E0=(45092.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N",
    kinetics = ArrheniusBM(A=(2.33364e-18,'s^-1'), n=8.89528, w0=(798000,'J/mol'), E0=(120565,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.007217064126337527, var=6.661339248779683, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N
    Total Standard Deviation in ln(k): 5.192268440792522"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N
Total Standard Deviation in ln(k): 5.192268440792522""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N
Total Standard Deviation in ln(k): 5.192268440792522
""",
)

entry(
    index = 47,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->C",
    kinetics = ArrheniusBM(A=(1.2013e-18,'s^-1'), n=8.97925, w0=(798000,'J/mol'), E0=(126845,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.007503612341907746, var=0.008054470110497336, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->C
    Total Standard Deviation in ln(k): 0.1987716543490167"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->C
Total Standard Deviation in ln(k): 0.1987716543490167""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->C
Total Standard Deviation in ln(k): 0.1987716543490167
""",
)

entry(
    index = 48,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.18952e-19,'s^-1'), n=9.32392, w0=(798000,'J/mol'), E0=(137103,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_5R!H->C",
    kinetics = ArrheniusBM(A=(6.87223e-13,'s^-1'), n=7.30388, w0=(798000,'J/mol'), E0=(124360,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.33668e-20,'s^-1'), n=9.45072, w0=(798000,'J/mol'), E0=(138622,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.025999023929210666, var=2.2367127697893783, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C
    Total Standard Deviation in ln(k): 3.0635345236969505"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 3.0635345236969505""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 3.0635345236969505
""",
)

entry(
    index = 51,
    label = "Root_N-3R!H->C_N-1R!H-inRing_3BrClFINOPSSi->S_Ext-1R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(87.5,'s^-1'), n=3.23, w0=(782000,'J/mol'), E0=(85014.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_3BrClFINOPSSi->S_Ext-1R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFINOPSSi->S_Ext-1R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFINOPSSi->S_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_3BrClFINOPSSi->S_Ext-1R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_Ext-3N-R",
    kinetics = ArrheniusBM(A=(6.49091e-10,'s^-1'), n=6.47564, w0=(798000,'J/mol'), E0=(91433.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.050948687716974514, var=4.356214748630402, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_Ext-3N-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_Ext-3N-R
    Total Standard Deviation in ln(k): 4.3122040205343355"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_Ext-3N-R
Total Standard Deviation in ln(k): 4.3122040205343355""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_Ext-3N-R
Total Standard Deviation in ln(k): 4.3122040205343355
""",
)

entry(
    index = 53,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_5R!H->O",
    kinetics = ArrheniusBM(A=(5.2062e-13,'s^-1'), n=7.41511, w0=(798000,'J/mol'), E0=(98886.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0007950118702081248, var=3.035432359577416, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_5R!H->O
    Total Standard Deviation in ln(k): 3.4947456507807533"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_5R!H->O
Total Standard Deviation in ln(k): 3.4947456507807533""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_5R!H->O
Total Standard Deviation in ln(k): 3.4947456507807533
""",
)

entry(
    index = 54,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(1.18117e-12,'s^-1'), n=7.2722, w0=(798000,'J/mol'), E0=(96798.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03205121162957773, var=1.6037855417277935, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O',), comment="""BM rule fitted to 14 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O
    Total Standard Deviation in ln(k): 2.619340309058252"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O
Total Standard Deviation in ln(k): 2.619340309058252""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O
Total Standard Deviation in ln(k): 2.619340309058252
""",
)

entry(
    index = 55,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(5.31044e-11,'s^-1'), n=6.81698, w0=(798000,'J/mol'), E0=(98809.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.003001110983615405, var=0.0884541218470009, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 0.6037735039900458"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 0.6037735039900458""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 0.6037735039900458
""",
)

entry(
    index = 56,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(6.24893e-09,'s^-1'), n=6.18216, w0=(798000,'J/mol'), E0=(107861,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(7.96668e-12,'s^-1'), n=7.03092, w0=(798000,'J/mol'), E0=(99812,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.004795327190430439, var=0.334359768750165, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 1.1712635750016842"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 1.1712635750016842""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 1.1712635750016842
""",
)

entry(
    index = 58,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(6.42858e-10,'s^-1'), n=6.4885, w0=(798000,'J/mol'), E0=(108792,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N_6BrCClFIOPSSi->O",
    kinetics = ArrheniusBM(A=(8.47848e-14,'s^-1'), n=7.46671, w0=(783500,'J/mol'), E0=(172647,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N_6BrCClFIOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N_6BrCClFIOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N_6BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N_6BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N_N-6BrCClFIOPSSi->O",
    kinetics = ArrheniusBM(A=(6.84389e-11,'s^-1'), n=6.70227, w0=(783500,'J/mol'), E0=(188014,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N_N-6BrCClFIOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N_N-6BrCClFIOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N_N-6BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-1R!H-R_5R!H->C_Ext-3C-R_N-6R!H->N_N-6BrCClFIOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_5BrCClFINPSSi->N_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.77862e-15,'s^-1'), n=8.01018, w0=(783500,'J/mol'), E0=(186087,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_5BrCClFINPSSi->N_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_5BrCClFINPSSi->N_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_5BrCClFINPSSi->N_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_5BrCClFINPSSi->N_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N_6R!H->C",
    kinetics = ArrheniusBM(A=(4.76535e-29,'s^-1'), n=11.9206, w0=(783500,'J/mol'), E0=(153536,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.191789256932443e-05, var=1.2430025856755769, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N_6R!H->C
    Total Standard Deviation in ln(k): 2.2351347254382397"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N_6R!H->C
Total Standard Deviation in ln(k): 2.2351347254382397""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N_6R!H->C
Total Standard Deviation in ln(k): 2.2351347254382397
""",
)

entry(
    index = 63,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N_N-6R!H->C",
    kinetics = ArrheniusBM(A=(8.55896e-23,'s^-1'), n=10.1131, w0=(783500,'J/mol'), E0=(169037,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.18923e-46,'s^-1'), n=16.9465, w0=(783500,'J/mol'), E0=(138086,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.007588345048758297, var=14.322148179332126, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R',), comment="""BM rule fitted to 6 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 7.605908735380721"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 7.605908735380721""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 7.605908735380721
""",
)

entry(
    index = 65,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing",
    kinetics = ArrheniusBM(A=(8.61547e-36,'s^-1'), n=13.9493, w0=(783500,'J/mol'), E0=(131318,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.388707861713522e-05, var=0.5506957678026614, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing
    Total Standard Deviation in ln(k): 1.4878268165252302"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing
Total Standard Deviation in ln(k): 1.4878268165252302""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing
Total Standard Deviation in ln(k): 1.4878268165252302
""",
)

entry(
    index = 66,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing",
    kinetics = ArrheniusBM(A=(1.37354e-40,'s^-1'), n=15.4134, w0=(783500,'J/mol'), E0=(139306,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.023411914775309003, var=2.2294398135979376, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing',), comment="""BM rule fitted to 9 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing
    Total Standard Deviation in ln(k): 3.0521557492204088"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing
Total Standard Deviation in ln(k): 3.0521557492204088""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing
Total Standard Deviation in ln(k): 3.0521557492204088
""",
)

entry(
    index = 67,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(5.03787e-12,'s^-1'), n=6.96525, w0=(783500,'J/mol'), E0=(138689,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0959880072472223, var=17.59453408894693, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N',), comment="""BM rule fitted to 4 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 8.650205375767989"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N
Total Standard Deviation in ln(k): 8.650205375767989""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N
Total Standard Deviation in ln(k): 8.650205375767989
""",
)

entry(
    index = 68,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(1.76964e-27,'s^-1'), n=11.3857, w0=(783500,'J/mol'), E0=(149824,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_N-5BrClFINOPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_6R!H->O",
    kinetics = ArrheniusBM(A=(9.72018e-31,'s^-1'), n=12.4085, w0=(783500,'J/mol'), E0=(140307,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0010171218693333563, var=8.259939515435356, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_6R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_6R!H->O
    Total Standard Deviation in ln(k): 5.764186347309356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_6R!H->O
Total Standard Deviation in ln(k): 5.764186347309356""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_6R!H->O
Total Standard Deviation in ln(k): 5.764186347309356
""",
)

entry(
    index = 70,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(1.45312e-39,'s^-1'), n=15.0595, w0=(783500,'J/mol'), E0=(141451,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0038146995811367415, var=4.810563762111573, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O
    Total Standard Deviation in ln(k): 4.406569602102788"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O
Total Standard Deviation in ln(k): 4.406569602102788""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O
Total Standard Deviation in ln(k): 4.406569602102788
""",
)

entry(
    index = 71,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_5R!H->N",
    kinetics = ArrheniusBM(A=(3.22052e-18,'s^-1'), n=8.86451, w0=(798000,'J/mol'), E0=(132813,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.298119424757154e-05, var=0.04751076658266557, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_5R!H->N
    Total Standard Deviation in ln(k): 0.43705426248998613"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_5R!H->N
Total Standard Deviation in ln(k): 0.43705426248998613""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_5R!H->N
Total Standard Deviation in ln(k): 0.43705426248998613
""",
)

entry(
    index = 72,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_N-5R!H->N",
    kinetics = ArrheniusBM(A=(1.02008e-17,'s^-1'), n=8.71849, w0=(798000,'J/mol'), E0=(119287,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.003881804765101457, var=0.009199804740706677, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_N-5R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_N-5R!H->N
    Total Standard Deviation in ln(k): 0.20203867135609896"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_N-5R!H->N
Total Standard Deviation in ln(k): 0.20203867135609896""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_N-5R!H->N
Total Standard Deviation in ln(k): 0.20203867135609896
""",
)

entry(
    index = 73,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_N-7R!H->N_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.23245e-20,'s^-1'), n=9.38178, w0=(798000,'J/mol'), E0=(126650,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_N-7R!H->N_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_N-7R!H->N_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_N-7R!H->N_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_N-7R!H->N_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.03729e-10,'s^-1'), n=6.68631, w0=(798000,'J/mol'), E0=(105099,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_7R!H->N",
    kinetics = ArrheniusBM(A=(3.96828e-18,'s^-1'), n=8.83096, w0=(798000,'J/mol'), E0=(123934,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005248291867854506, var=0.020819608889374595, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_7R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_7R!H->N
    Total Standard Deviation in ln(k): 0.30244992057304115"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_7R!H->N
Total Standard Deviation in ln(k): 0.30244992057304115""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_7R!H->N
Total Standard Deviation in ln(k): 0.30244992057304115
""",
)

entry(
    index = 76,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_N-7R!H->N",
    kinetics = ArrheniusBM(A=(5.26306e-21,'s^-1'), n=9.67718, w0=(798000,'J/mol'), E0=(128106,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-7.852972029802102e-05, var=0.07843541824040957, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_N-7R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_N-7R!H->N
    Total Standard Deviation in ln(k): 0.5616499114029998"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_N-7R!H->N
Total Standard Deviation in ln(k): 0.5616499114029998""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_N-7R!H->N
Total Standard Deviation in ln(k): 0.5616499114029998
""",
)

entry(
    index = 77,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->C_5R!H->N",
    kinetics = ArrheniusBM(A=(2.9852e-20,'s^-1'), n=9.42069, w0=(798000,'J/mol'), E0=(121194,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00033558131741877046, var=0.002267350901758185, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->C_5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->C_5R!H->N
    Total Standard Deviation in ln(k): 0.09630205437896223"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->C_5R!H->N
Total Standard Deviation in ln(k): 0.09630205437896223""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->C_5R!H->N
Total Standard Deviation in ln(k): 0.09630205437896223
""",
)

entry(
    index = 78,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->C_N-5R!H->N",
    kinetics = ArrheniusBM(A=(2.95366e-14,'s^-1'), n=7.77475, w0=(798000,'J/mol'), E0=(142358,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->C_N-5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->C_N-5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->C_N-5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->C_N-5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C",
    kinetics = ArrheniusBM(A=(5.35193e-22,'s^-1'), n=9.96064, w0=(798000,'J/mol'), E0=(136695,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0025574536717999116, var=2.4594978159443808, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C
    Total Standard Deviation in ln(k): 3.1504089146845984"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C
Total Standard Deviation in ln(k): 3.1504089146845984""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C
Total Standard Deviation in ln(k): 3.1504089146845984
""",
)

entry(
    index = 80,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C",
    kinetics = ArrheniusBM(A=(2.27189e-19,'s^-1'), n=9.21636, w0=(798000,'J/mol'), E0=(138167,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0005520236756471257, var=10.279324647875598, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C
    Total Standard Deviation in ln(k): 6.428845485264807"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C
Total Standard Deviation in ln(k): 6.428845485264807""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C
Total Standard Deviation in ln(k): 6.428845485264807
""",
)

entry(
    index = 81,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_Ext-3N-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.14206e-08,'s^-1'), n=5.89269, w0=(798000,'J/mol'), E0=(96466.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.007103816317503689, var=1.2657848014962294, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_Ext-3N-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_Ext-3N-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 2.2733181243649305"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_Ext-3N-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.2733181243649305""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_Ext-3N-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.2733181243649305
""",
)

entry(
    index = 82,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_5R!H->O_Ext-5O-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(7.80609e-12,'s^-1'), n=7.13985, w0=(798000,'J/mol'), E0=(100522,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_5R!H->O_Ext-5O-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_5R!H->O_Ext-5O-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_5R!H->O_Ext-5O-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_5R!H->O_Ext-5O-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing",
    kinetics = ArrheniusBM(A=(1.91384e-12,'s^-1'), n=7.25794, w0=(798000,'J/mol'), E0=(97947.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.009397196092007891, var=0.7686028833011719, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing
    Total Standard Deviation in ln(k): 1.781162280149695"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing
Total Standard Deviation in ln(k): 1.781162280149695""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing
Total Standard Deviation in ln(k): 1.781162280149695
""",
)

entry(
    index = 84,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing",
    kinetics = ArrheniusBM(A=(9.93544e-13,'s^-1'), n=7.26829, w0=(798000,'J/mol'), E0=(96262.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04339039264007516, var=2.4655520875278722, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing',), comment="""BM rule fitted to 9 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing
    Total Standard Deviation in ln(k): 3.256871456726714"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing
Total Standard Deviation in ln(k): 3.256871456726714""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing
Total Standard Deviation in ln(k): 3.256871456726714
""",
)

entry(
    index = 85,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_5R!H-inRing",
    kinetics = ArrheniusBM(A=(3.03926e-10,'s^-1'), n=6.64444, w0=(798000,'J/mol'), E0=(102217,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_5R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_5R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(5.48296e-11,'s^-1'), n=6.80463, w0=(798000,'J/mol'), E0=(98982.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0007442885720676981, var=0.183155239978996, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_N-5R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_N-5R!H-inRing
    Total Standard Deviation in ln(k): 0.859829326869262"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_N-5R!H-inRing
Total Standard Deviation in ln(k): 0.859829326869262""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_N-5R!H-inRing
Total Standard Deviation in ln(k): 0.859829326869262
""",
)

entry(
    index = 87,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_Sp-7C-6R!H",
    kinetics = ArrheniusBM(A=(4.78578e-12,'s^-1'), n=7.10286, w0=(798000,'J/mol'), E0=(99080.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0002745781153866372, var=1.0547827373537062, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_Sp-7C-6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_Sp-7C-6R!H
    Total Standard Deviation in ln(k): 2.0596052670482954"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_Sp-7C-6R!H
Total Standard Deviation in ln(k): 2.0596052670482954""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_Sp-7C-6R!H
Total Standard Deviation in ln(k): 2.0596052670482954
""",
)

entry(
    index = 88,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_N-Sp-7C-6R!H",
    kinetics = ArrheniusBM(A=(1.03652e-10,'s^-1'), n=6.72069, w0=(798000,'J/mol'), E0=(104667,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_N-Sp-7C-6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_N-Sp-7C-6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_N-Sp-7C-6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_N-Sp-7C-6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N_6R!H->C_7R!H->N",
    kinetics = ArrheniusBM(A=(2.33301e-26,'s^-1'), n=11.129, w0=(783500,'J/mol'), E0=(156331,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N_6R!H->C_7R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N_6R!H->C_7R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N_6R!H->C_7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N_6R!H->C_7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N_6R!H->C_N-7R!H->N",
    kinetics = ArrheniusBM(A=(9.38708e-30,'s^-1'), n=12.1418, w0=(783500,'J/mol'), E0=(156046,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N_6R!H->C_N-7R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N_6R!H->C_N-7R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N_6R!H->C_N-7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_3C-inRing_Ext-3C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R_Ext-3C-R_N-5BrCClFINPSSi->N_6R!H->C_N-7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(5.45324e-49,'s^-1'), n=17.7861, w0=(783500,'J/mol'), E0=(138875,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0011611715969363837, var=3.9909851232198013, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R',), comment="""BM rule fitted to 5 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R
    Total Standard Deviation in ln(k): 4.007867012928184"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R
Total Standard Deviation in ln(k): 4.007867012928184""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R
Total Standard Deviation in ln(k): 4.007867012928184
""",
)

entry(
    index = 92,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing_Ext-5C-R_6R!H->N",
    kinetics = ArrheniusBM(A=(2.59344e-34,'s^-1'), n=13.552, w0=(783500,'J/mol'), E0=(139140,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing_Ext-5C-R_6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing_Ext-5C-R_6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing_Ext-5C-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing_Ext-5C-R_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing_Ext-5C-R_N-6R!H->N",
    kinetics = ArrheniusBM(A=(1.41171e-33,'s^-1'), n=13.3174, w0=(783500,'J/mol'), E0=(135339,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing_Ext-5C-R_N-6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing_Ext-5C-R_N-6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing_Ext-5C-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_5C-inRing_Ext-5C-R_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.49939e-41,'s^-1'), n=15.6867, w0=(783500,'J/mol'), E0=(139332,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.017635097520241096, var=1.3716297688364298, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R',), comment="""BM rule fitted to 8 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R
    Total Standard Deviation in ln(k): 2.3921868256112373"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R
Total Standard Deviation in ln(k): 2.3921868256112373""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R
Total Standard Deviation in ln(k): 2.3921868256112373
""",
)

entry(
    index = 95,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.028142,'s^-1'), n=4.2054, w0=(783500,'J/mol'), E0=(152969,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10964590770372955, var=77.7466469442805, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N_Ext-3C-R
    Total Standard Deviation in ln(k): 17.95205514555652"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N_Ext-3C-R
Total Standard Deviation in ln(k): 17.95205514555652""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N_Ext-3C-R
Total Standard Deviation in ln(k): 17.95205514555652
""",
)

entry(
    index = 96,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N_Ext-5N-R_Ext-5N-R",
    kinetics = ArrheniusBM(A=(1.5544e-16,'s^-1'), n=8.25988, w0=(783500,'J/mol'), E0=(135169,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N_Ext-5N-R_Ext-5N-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N_Ext-5N-R_Ext-5N-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N_Ext-5N-R_Ext-5N-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N_Ext-5N-R_Ext-5N-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 97,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_6R!H->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.80714e-28,'s^-1'), n=11.6116, w0=(783500,'J/mol'), E0=(139131,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_6R!H->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_6R!H->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_6R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_6R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.42468e-39,'s^-1'), n=15.0373, w0=(783500,'J/mol'), E0=(149617,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0005211803673611572, var=3.921589378971721, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-3C-R
    Total Standard Deviation in ln(k): 3.9712870246122276"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 3.9712870246122276""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 3.9712870246122276
""",
)

entry(
    index = 99,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6BrCClFINPSSi-5R!H",
    kinetics = ArrheniusBM(A=(3.9707e-44,'s^-1'), n=16.3291, w0=(783500,'J/mol'), E0=(138718,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0005557120191888678, var=10.235706611528846, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6BrCClFINPSSi-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6BrCClFINPSSi-5R!H
    Total Standard Deviation in ln(k): 6.415203507633639"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6BrCClFINPSSi-5R!H
Total Standard Deviation in ln(k): 6.415203507633639""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6BrCClFINPSSi-5R!H
Total Standard Deviation in ln(k): 6.415203507633639
""",
)

entry(
    index = 100,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_N-Sp-6BrCClFINPSSi-5R!H",
    kinetics = ArrheniusBM(A=(1.70296e-34,'s^-1'), n=13.6036, w0=(783500,'J/mol'), E0=(137799,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00018330541447844498, var=0.0007798796061297237, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_N-Sp-6BrCClFINPSSi-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_N-Sp-6BrCClFINPSSi-5R!H
    Total Standard Deviation in ln(k): 0.056445448893047076"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_N-Sp-6BrCClFINPSSi-5R!H
Total Standard Deviation in ln(k): 0.056445448893047076""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_N-Sp-6BrCClFINPSSi-5R!H
Total Standard Deviation in ln(k): 0.056445448893047076
""",
)

entry(
    index = 101,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_5R!H->N_Ext-6C-R",
    kinetics = ArrheniusBM(A=(1.19581e-17,'s^-1'), n=8.72753, w0=(798000,'J/mol'), E0=(135275,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_5R!H->N_Ext-6C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_5R!H->N_Ext-6C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_5R!H->N_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_5R!H->N_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 102,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_N-5R!H->N_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.36428e-17,'s^-1'), n=8.68106, w0=(798000,'J/mol'), E0=(119355,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=9.875757718463376e-05, var=0.019447819937148978, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_N-5R!H->N_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_N-5R!H->N_Ext-5C-R
    Total Standard Deviation in ln(k): 0.2798193482943225"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_N-5R!H->N_Ext-5C-R
Total Standard Deviation in ln(k): 0.2798193482943225""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_N-5R!H->N_Ext-5C-R
Total Standard Deviation in ln(k): 0.2798193482943225
""",
)

entry(
    index = 103,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_7R!H->N_Ext-5C-R",
    kinetics = ArrheniusBM(A=(4.83626e-18,'s^-1'), n=8.80389, w0=(798000,'J/mol'), E0=(123595,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00010214101403961101, var=0.010815603590169066, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_7R!H->N_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_7R!H->N_Ext-5C-R
    Total Standard Deviation in ln(k): 0.20874526307047123"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_7R!H->N_Ext-5C-R
Total Standard Deviation in ln(k): 0.20874526307047123""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_7R!H->N_Ext-5C-R
Total Standard Deviation in ln(k): 0.20874526307047123
""",
)

entry(
    index = 104,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_N-7R!H->N_Ext-5C-R",
    kinetics = ArrheniusBM(A=(4.43945e-20,'s^-1'), n=9.41864, w0=(798000,'J/mol'), E0=(130190,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_N-7R!H->N_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_N-7R!H->N_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_N-7R!H->N_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_N-7R!H->N_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 105,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->C_5R!H->N_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.57404e-19,'s^-1'), n=9.1193, w0=(798000,'J/mol'), E0=(124449,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->C_5R!H->N_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->C_5R!H->N_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->C_5R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_7R!H->C_6R!H->C_5R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 106,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C_5NO->N",
    kinetics = ArrheniusBM(A=(2.52338e-22,'s^-1'), n=10.05, w0=(798000,'J/mol'), E0=(131010,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C_5NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C_5NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C_5NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C_5NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 107,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C_N-5NO->N",
    kinetics = ArrheniusBM(A=(1.62343e-20,'s^-1'), n=9.5285, w0=(798000,'J/mol'), E0=(144945,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C_N-5NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C_N-5NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C_N-5NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_6R!H->C_N-5NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 108,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C_Sp-5NO-3BrClFINNOOPSSi",
    kinetics = ArrheniusBM(A=(4.58562e-24,'s^-1'), n=10.6226, w0=(798000,'J/mol'), E0=(138683,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C_Sp-5NO-3BrClFINNOOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C_Sp-5NO-3BrClFINNOOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C_Sp-5NO-3BrClFINNOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C_Sp-5NO-3BrClFINNOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 109,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C_N-Sp-5NO-3BrClFINNOOPSSi",
    kinetics = ArrheniusBM(A=(2.02819e-14,'s^-1'), n=7.71417, w0=(798000,'J/mol'), E0=(137432,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C_N-Sp-5NO-3BrClFINNOOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C_N-Sp-5NO-3BrClFINNOOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C_N-Sp-5NO-3BrClFINNOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R_N-7R!H->C_N-5R!H->C_N-6R!H->C_N-Sp-5NO-3BrClFINNOOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 110,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_Ext-3N-R_Ext-5R!H-R_5R!H->N",
    kinetics = ArrheniusBM(A=(5.39095e-06,'s^-1'), n=5.24031, w0=(798000,'J/mol'), E0=(98425.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_Ext-3N-R_Ext-5R!H-R_5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_Ext-3N-R_Ext-5R!H-R_5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_Ext-3N-R_Ext-5R!H-R_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_Ext-3N-R_Ext-5R!H-R_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 111,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_Ext-3N-R_Ext-5R!H-R_N-5R!H->N",
    kinetics = ArrheniusBM(A=(6.85036e-08,'s^-1'), n=5.86332, w0=(798000,'J/mol'), E0=(104769,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_Ext-3N-R_Ext-5R!H-R_N-5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_Ext-3N-R_Ext-5R!H-R_N-5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_Ext-3N-R_Ext-5R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_Ext-3N-R_Ext-5R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 112,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_5CN->N",
    kinetics = ArrheniusBM(A=(1.68509e-11,'s^-1'), n=6.88807, w0=(798000,'J/mol'), E0=(102832,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_5CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_5CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_5CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_5CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 113,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N",
    kinetics = ArrheniusBM(A=(4.62114e-12,'s^-1'), n=7.17889, w0=(798000,'J/mol'), E0=(98672.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0008524116468629175, var=0.4723812140851986, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N
    Total Standard Deviation in ln(k): 1.3799960457840075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N
Total Standard Deviation in ln(k): 1.3799960457840075""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N
Total Standard Deviation in ln(k): 1.3799960457840075
""",
)

entry(
    index = 114,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R",
    kinetics = ArrheniusBM(A=(2.57961e-13,'s^-1'), n=7.43939, w0=(798000,'J/mol'), E0=(95490.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.051030762361128856, var=2.8410684978671963, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R
    Total Standard Deviation in ln(k): 3.5072930775908056"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R
Total Standard Deviation in ln(k): 3.5072930775908056""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R
Total Standard Deviation in ln(k): 3.5072930775908056
""",
)

entry(
    index = 115,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_N-5R!H-inRing_7R!H->C",
    kinetics = ArrheniusBM(A=(4.06473e-10,'s^-1'), n=6.60955, w0=(798000,'J/mol'), E0=(103273,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_N-5R!H-inRing_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_N-5R!H-inRing_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_N-5R!H-inRing_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_N-5R!H-inRing_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 116,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_N-5R!H-inRing_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2.81779e-10,'s^-1'), n=6.57871, w0=(798000,'J/mol'), E0=(100933,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_N-5R!H-inRing_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_N-5R!H-inRing_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_N-5R!H-inRing_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-5R!H-R_6R!H->C_N-5R!H-inRing_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 117,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_Sp-7C-6R!H_6R!H->N",
    kinetics = ArrheniusBM(A=(3.2546e-11,'s^-1'), n=6.85152, w0=(798000,'J/mol'), E0=(103720,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_Sp-7C-6R!H_6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_Sp-7C-6R!H_6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_Sp-7C-6R!H_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_Sp-7C-6R!H_6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 118,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_Sp-7C-6R!H_N-6R!H->N",
    kinetics = ArrheniusBM(A=(4.48783e-11,'s^-1'), n=6.87686, w0=(798000,'J/mol'), E0=(101775,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_Sp-7C-6R!H_N-6R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_Sp-7C-6R!H_N-6R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_Sp-7C-6R!H_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-3N-R_Ext-5R!H-R_Ext-6R!H-R_7R!H->C_Sp-7C-6R!H_N-6R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 119,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.00799e-42,'s^-1'), n=15.8601, w0=(783500,'J/mol'), E0=(132757,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 120,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(5.42629e-48,'s^-1'), n=17.4421, w0=(783500,'J/mol'), E0=(138255,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00033121585661176204, var=0.046867947233288555, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 0.43483742317927815"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 0.43483742317927815""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 0.43483742317927815
""",
)

entry(
    index = 121,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.683e-52,'s^-1'), n=18.8808, w0=(783500,'J/mol'), E0=(145094,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0014539038435330003, var=1.9889329677050145, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 2.830921577724545"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 2.830921577724545""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 2.830921577724545
""",
)

entry(
    index = 122,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(3.12991e-42,'s^-1'), n=16.0032, w0=(783500,'J/mol'), E0=(147725,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005104197619452722, var=0.6514006771320477, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O
    Total Standard Deviation in ln(k): 1.6308342104428886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 1.6308342104428886""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 1.6308342104428886
""",
)

entry(
    index = 123,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(2.23905e-41,'s^-1'), n=15.5459, w0=(783500,'J/mol'), E0=(132179,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01764662734538523, var=2.762297332654543, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 3.376240123551729"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 3.376240123551729""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 3.376240123551729
""",
)

entry(
    index = 124,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N_Ext-3C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(5.51726e-18,'s^-1'), n=8.84109, w0=(783500,'J/mol'), E0=(146092,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N_Ext-3C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N_Ext-3C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 125,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N_Ext-3C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(6.6955e-09,'s^-1'), n=6.06879, w0=(783500,'J/mol'), E0=(107995,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N_Ext-3C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N_Ext-3C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_N-5R!H->C_5BrClFINOPSSi->N_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 126,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-3C-R_6BrCClFINPSSi->N",
    kinetics = ArrheniusBM(A=(6.97955e-36,'s^-1'), n=14.0901, w0=(783500,'J/mol'), E0=(155645,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-3C-R_6BrCClFINPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-3C-R_6BrCClFINPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-3C-R_6BrCClFINPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-3C-R_6BrCClFINPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 127,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-3C-R_N-6BrCClFINPSSi->N",
    kinetics = ArrheniusBM(A=(1.49793e-42,'s^-1'), n=15.9135, w0=(783500,'J/mol'), E0=(144341,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-3C-R_N-6BrCClFINPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-3C-R_N-6BrCClFINPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-3C-R_N-6BrCClFINPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Ext-3C-R_N-6BrCClFINPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 128,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6BrCClFINPSSi-5R!H_5R!H->N",
    kinetics = ArrheniusBM(A=(6.56099e-43,'s^-1'), n=15.9484, w0=(783500,'J/mol'), E0=(130721,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6BrCClFINPSSi-5R!H_5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6BrCClFINPSSi-5R!H_5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6BrCClFINPSSi-5R!H_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6BrCClFINPSSi-5R!H_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 129,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6BrCClFINPSSi-5R!H_N-5R!H->N",
    kinetics = ArrheniusBM(A=(7.84947e-45,'s^-1'), n=16.5411, w0=(783500,'J/mol'), E0=(146853,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6BrCClFINPSSi-5R!H_N-5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6BrCClFINPSSi-5R!H_N-5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6BrCClFINPSSi-5R!H_N-5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_Sp-6BrCClFINPSSi-5R!H_N-5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 130,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_N-Sp-6BrCClFINPSSi-5R!H_6BrCClFINPSSi->N",
    kinetics = ArrheniusBM(A=(5.93747e-32,'s^-1'), n=12.864, w0=(783500,'J/mol'), E0=(144121,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_N-Sp-6BrCClFINPSSi-5R!H_6BrCClFINPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_N-Sp-6BrCClFINPSSi-5R!H_6BrCClFINPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_N-Sp-6BrCClFINPSSi-5R!H_6BrCClFINPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_N-Sp-6BrCClFINPSSi-5R!H_6BrCClFINPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_N-Sp-6BrCClFINPSSi-5R!H_N-6BrCClFINPSSi->N",
    kinetics = ArrheniusBM(A=(4.21191e-35,'s^-1'), n=13.8299, w0=(783500,'J/mol'), E0=(139136,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_N-Sp-6BrCClFINPSSi-5R!H_N-6BrCClFINPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_N-Sp-6BrCClFINPSSi-5R!H_N-6BrCClFINPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_N-Sp-6BrCClFINPSSi-5R!H_N-6BrCClFINPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-3C-R_Ext-5R!H-R_N-6R!H->O_N-Sp-6BrCClFINPSSi-5R!H_N-6BrCClFINPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 132,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_N-5R!H->N_Ext-5C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(9.14825e-17,'s^-1'), n=8.45574, w0=(798000,'J/mol'), E0=(121877,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_N-5R!H->N_Ext-5C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_N-5R!H->N_Ext-5C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_N-5R!H->N_Ext-5C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_N-5R!H->N_Ext-5C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_N-5R!H->N_Ext-5C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(4.10787e-17,'s^-1'), n=8.57309, w0=(798000,'J/mol'), E0=(122784,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_N-5R!H->N_Ext-5C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_N-5R!H->N_Ext-5C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_N-5R!H->N_Ext-5C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_6R!H->C_Ext-6C-R_7R!H->N_N-5R!H->N_Ext-5C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 134,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_7R!H->N_Ext-5C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(2.18792e-17,'s^-1'), n=8.63308, w0=(798000,'J/mol'), E0=(126694,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_7R!H->N_Ext-5C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_7R!H->N_Ext-5C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_7R!H->N_Ext-5C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_7R!H->N_Ext-5C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 135,
    label = "Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_7R!H->N_Ext-5C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(9.00746e-18,'s^-1'), n=8.75254, w0=(798000,'J/mol'), E0=(125562,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_7R!H->N_Ext-5C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_7R!H->N_Ext-5C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_7R!H->N_Ext-5C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_1R!H-inRing_Ext-3BrClFINOPSSi-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Sp-6R!H=5R!H_N-6R!H->C_N-5R!H->N_Ext-6NO-R_7R!H->N_Ext-5C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 136,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(2.50132e-12,'s^-1'), n=7.25319, w0=(798000,'J/mol'), E0=(100833,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00011345744626205915, var=0.1436923898370318, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->O
    Total Standard Deviation in ln(k): 0.7602155653984278"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 0.7602155653984278""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 0.7602155653984278
""",
)

entry(
    index = 137,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(9.45314e-12,'s^-1'), n=7.09189, w0=(798000,'J/mol'), E0=(96623.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.002283801048831891, var=1.002884062322813, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 2.0133620800594025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 2.0133620800594025""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 2.0133620800594025
""",
)

entry(
    index = 138,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_6R!H->O",
    kinetics = ArrheniusBM(A=(5.12223e-14,'s^-1'), n=7.69896, w0=(798000,'J/mol'), E0=(103788,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0008528973385954304, var=0.051142726364650844, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_6R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_6R!H->O
    Total Standard Deviation in ln(k): 0.455508937449092"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_6R!H->O
Total Standard Deviation in ln(k): 0.455508937449092""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_6R!H->O
Total Standard Deviation in ln(k): 0.455508937449092
""",
)

entry(
    index = 139,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(2.90665e-13,'s^-1'), n=7.40509, w0=(798000,'J/mol'), E0=(92260.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07366063458372907, var=3.8238479155275864, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O
    Total Standard Deviation in ln(k): 4.105268581395347"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O
Total Standard Deviation in ln(k): 4.105268581395347""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O
Total Standard Deviation in ln(k): 4.105268581395347
""",
)

entry(
    index = 140,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.63468e-47,'s^-1'), n=17.3183, w0=(783500,'J/mol'), E0=(139713,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 141,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C_7NO->N",
    kinetics = ArrheniusBM(A=(2.12859e-53,'s^-1'), n=18.9999, w0=(783500,'J/mol'), E0=(138885,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C_7NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C_7NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C_7NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C_7NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 142,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C_N-7NO->N",
    kinetics = ArrheniusBM(A=(7.04433e-53,'s^-1'), n=19.1929, w0=(783500,'J/mol'), E0=(151641,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C_N-7NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C_N-7NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C_N-7NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C_N-7NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 143,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O_Ext-5C-R",
    kinetics = ArrheniusBM(A=(7.90666e-42,'s^-1'), n=15.8943, w0=(783500,'J/mol'), E0=(146796,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.000190200256858076, var=0.37522901375334483, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O_Ext-5C-R
    Total Standard Deviation in ln(k): 1.2284971984464699"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O_Ext-5C-R
Total Standard Deviation in ln(k): 1.2284971984464699""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O_Ext-5C-R
Total Standard Deviation in ln(k): 1.2284971984464699
""",
)

entry(
    index = 144,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->N",
    kinetics = ArrheniusBM(A=(2.74964e-45,'s^-1'), n=16.6685, w0=(783500,'J/mol'), E0=(135903,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 145,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N",
    kinetics = ArrheniusBM(A=(4.00881e-40,'s^-1'), n=15.1916, w0=(783500,'J/mol'), E0=(131229,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.013577205760681086, var=1.0511336006433443, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N',), comment="""BM rule fitted to 4 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N
    Total Standard Deviation in ln(k): 2.0894643469756167"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N
Total Standard Deviation in ln(k): 2.0894643469756167""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N
Total Standard Deviation in ln(k): 2.0894643469756167
""",
)

entry(
    index = 146,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(4.42405e-12,'s^-1'), n=7.19519, w0=(798000,'J/mol'), E0=(101144,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_6R!H->O_Ext-6O-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 147,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->N",
    kinetics = ArrheniusBM(A=(2.83728e-12,'s^-1'), n=7.25327, w0=(798000,'J/mol'), E0=(98862.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N",
    kinetics = ArrheniusBM(A=(1.32223e-12,'s^-1'), n=7.33725, w0=(798000,'J/mol'), E0=(91315.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_5CN-inRing_N-5CN->N_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_6R!H->O_Ext-5CN-R",
    kinetics = ArrheniusBM(A=(1.30511e-12,'s^-1'), n=7.26372, w0=(798000,'J/mol'), E0=(105105,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_6R!H->O_Ext-5CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_6R!H->O_Ext-5CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_6R!H->O_Ext-5CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_6R!H->O_Ext-5CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 150,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_6BrCClFINPSSi->N",
    kinetics = ArrheniusBM(A=(3.63987e-11,'s^-1'), n=6.94923, w0=(798000,'J/mol'), E0=(85767,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_6BrCClFINPSSi->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_6BrCClFINPSSi->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_6BrCClFINPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_6BrCClFINPSSi->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 151,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N",
    kinetics = ArrheniusBM(A=(1.41704e-11,'s^-1'), n=6.88498, w0=(798000,'J/mol'), E0=(98454.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.028001385421443217, var=2.557436828057148, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N
    Total Standard Deviation in ln(k): 3.27632518622067"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N
Total Standard Deviation in ln(k): 3.27632518622067""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N
Total Standard Deviation in ln(k): 3.27632518622067
""",
)

entry(
    index = 152,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O_Ext-5C-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.10569e-41,'s^-1'), n=15.9357, w0=(783500,'J/mol'), E0=(153831,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O_Ext-5C-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O_Ext-5C-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O_Ext-5C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_6R!H->O_Ext-5C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 153,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N_Sp-6C-5C",
    kinetics = ArrheniusBM(A=(4.11673e-40,'s^-1'), n=15.217, w0=(783500,'J/mol'), E0=(130288,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.269021400113391, var=22.06068708684146, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N_Sp-6C-5C',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N_Sp-6C-5C
    Total Standard Deviation in ln(k): 17.629622840907796"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N_Sp-6C-5C
Total Standard Deviation in ln(k): 17.629622840907796""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N_Sp-6C-5C
Total Standard Deviation in ln(k): 17.629622840907796
""",
)

entry(
    index = 154,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N_N-Sp-6C-5C",
    kinetics = ArrheniusBM(A=(3.05337e-40,'s^-1'), n=15.211, w0=(783500,'J/mol'), E0=(131424,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-6.547473076073497e-05, var=3.0139654942257157, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N_N-Sp-6C-5C',), comment="""BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N_N-Sp-6C-5C
    Total Standard Deviation in ln(k): 3.480540206394142"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N_N-Sp-6C-5C
Total Standard Deviation in ln(k): 3.480540206394142""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N_N-Sp-6C-5C
Total Standard Deviation in ln(k): 3.480540206394142
""",
)

entry(
    index = 155,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R",
    kinetics = ArrheniusBM(A=(7.51544e-12,'s^-1'), n=6.89895, w0=(798000,'J/mol'), E0=(100379,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02396879786862422, var=1.4973731060490867, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R
    Total Standard Deviation in ln(k): 2.513361244718143"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R
Total Standard Deviation in ln(k): 2.513361244718143""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R
Total Standard Deviation in ln(k): 2.513361244718143
""",
)

entry(
    index = 156,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_5CN->N",
    kinetics = ArrheniusBM(A=(6.33821e-07,'s^-1'), n=5.68082, w0=(798000,'J/mol'), E0=(103662,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_5CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_5CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_5CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_5CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 157,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_N-5CN->N",
    kinetics = ArrheniusBM(A=(3.02789e-13,'s^-1'), n=7.48219, w0=(798000,'J/mol'), E0=(95953.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_N-5CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_N-5CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_N-5CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_N-5CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 158,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N_Sp-6C-5C_Ext-6C-R",
    kinetics = ArrheniusBM(A=(2.34803e-38,'s^-1'), n=14.7488, w0=(783500,'J/mol'), E0=(137450,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N_Sp-6C-5C_Ext-6C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N_Sp-6C-5C_Ext-6C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N_Sp-6C-5C_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N_Sp-6C-5C_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 159,
    label = "Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N_N-Sp-6C-5C_Ext-6C-R",
    kinetics = ArrheniusBM(A=(1.06626e-37,'s^-1'), n=14.5413, w0=(783500,'J/mol'), E0=(136642,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N_N-Sp-6C-5C_Ext-6C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N_N-Sp-6C-5C_Ext-6C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N_N-Sp-6C-5C_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R!H->C_N-3C-inRing_N-1R!H->N_Ext-1C-R_5R!H->C_N-5C-inRing_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->N_N-Sp-6C-5C_Ext-6C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 160,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R_5CN->N",
    kinetics = ArrheniusBM(A=(8.42992e-10,'s^-1'), n=6.22192, w0=(798000,'J/mol'), E0=(104542,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.0517082806578122e-05, var=0.15820189146844285, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R_5CN->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R_5CN->N
    Total Standard Deviation in ln(k): 0.7974520617821278"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R_5CN->N
Total Standard Deviation in ln(k): 0.7974520617821278""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R_5CN->N
Total Standard Deviation in ln(k): 0.7974520617821278
""",
)

entry(
    index = 161,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R_N-5CN->N",
    kinetics = ArrheniusBM(A=(1.3825e-13,'s^-1'), n=7.5932, w0=(798000,'J/mol'), E0=(98979.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R_N-5CN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R_N-5CN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R_N-5CN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R_N-5CN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 162,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R_5CN->N_7R!H->N",
    kinetics = ArrheniusBM(A=(1.95577e-10,'s^-1'), n=6.41822, w0=(798000,'J/mol'), E0=(102434,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R_5CN->N_7R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R_5CN->N_7R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R_5CN->N_7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R_5CN->N_7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 163,
    label = "Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R_5CN->N_N-7R!H->N",
    kinetics = ArrheniusBM(A=(5.58698e-10,'s^-1'), n=6.27942, w0=(798000,'J/mol'), E0=(105618,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R_5CN->N_N-7R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R_5CN->N_N-7R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R_5CN->N_N-7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R!H->C_N-1R!H-inRing_N-3BrClFINOPSSi->S_Ext-1R!H-R_N-5R!H->O_N-5CN-inRing_Ext-5CN-R_N-6R!H->O_N-6BrCClFINPSSi->N_Ext-6C-R_5CN->N_N-7R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

