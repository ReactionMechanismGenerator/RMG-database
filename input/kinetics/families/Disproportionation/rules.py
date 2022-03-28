#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(103.48,'m^3/(mol*s)'), n=1.50659, w0=(570.117,'kJ/mol'), E0=(1.98033,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0015101924383256913, var=2.261329892268574, Tref=1000.0, N=261, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 261 training reactions at node Root
    Total Standard Deviation in ln(k): 3.0184587063883126"""),
    rank = 11,
    shortDesc = """BM rule fitted to 261 training reactions at node Root
Total Standard Deviation in ln(k): 3.0184587063883126""",
    longDesc = 
"""
BM rule fitted to 261 training reactions at node Root
Total Standard Deviation in ln(k): 3.0184587063883126
""",
)

entry(
    index = 2,
    label = "Root_Ext-4R-R",
    kinetics = ArrheniusBM(A=(15.4556,'m^3/(mol*s)'), n=1.75695, w0=(569.306,'kJ/mol'), E0=(5.75579,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08632617016562141, var=3.5844341832959157, Tref=1000.0, N=116, data_mean=0.0, correlation='Root_Ext-4R-R',), comment="""BM rule fitted to 116 training reactions at node Root_Ext-4R-R
    Total Standard Deviation in ln(k): 4.012385057762079"""),
    rank = 11,
    shortDesc = """BM rule fitted to 116 training reactions at node Root_Ext-4R-R
Total Standard Deviation in ln(k): 4.012385057762079""",
    longDesc = 
"""
BM rule fitted to 116 training reactions at node Root_Ext-4R-R
Total Standard Deviation in ln(k): 4.012385057762079
""",
)

entry(
    index = 3,
    label = "Root_Ext-4R-R_5R!H-u0",
    kinetics = ArrheniusBM(A=(19.0885,'m^3/(mol*s)'), n=1.79314, w0=(568.731,'kJ/mol'), E0=(17.7591,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02463115459429821, var=2.497726017901461, Tref=1000.0, N=80, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0',), comment="""BM rule fitted to 80 training reactions at node Root_Ext-4R-R_5R!H-u0
    Total Standard Deviation in ln(k): 3.2302098725005757"""),
    rank = 11,
    shortDesc = """BM rule fitted to 80 training reactions at node Root_Ext-4R-R_5R!H-u0
Total Standard Deviation in ln(k): 3.2302098725005757""",
    longDesc = 
"""
BM rule fitted to 80 training reactions at node Root_Ext-4R-R_5R!H-u0
Total Standard Deviation in ln(k): 3.2302098725005757
""",
)

entry(
    index = 4,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(0.00219224,'m^3/(mol*s)'), n=2.46757, w0=(542.539,'kJ/mol'), E0=(-13.8595,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.059031592274031, var=32.76287702330497, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R',), comment="""BM rule fitted to 38 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R
    Total Standard Deviation in ln(k): 16.648322320083558"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R
Total Standard Deviation in ln(k): 16.648322320083558""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R
Total Standard Deviation in ln(k): 16.648322320083558
""",
)

entry(
    index = 5,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S",
    kinetics = ArrheniusBM(A=(3.12126e-13,'m^3/(mol*s)'), n=4.70087, w0=(527,'kJ/mol'), E0=(23.5413,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=10.076911631917183, var=348.0839247891389, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S
    Total Standard Deviation in ln(k): 62.7212306030378"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S
Total Standard Deviation in ln(k): 62.7212306030378""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S
Total Standard Deviation in ln(k): 62.7212306030378
""",
)

entry(
    index = 6,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(644,'m^3/(mol*s)'), n=1.19, w0=(515,'kJ/mol'), E0=(36.7344,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_5R!H->S_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S",
    kinetics = ArrheniusBM(A=(10877.4,'m^3/(mol*s)'), n=0.589799, w0=(543.403,'kJ/mol'), E0=(28.6444,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.2425637496744053, var=13.627618112319603, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S',), comment="""BM rule fitted to 36 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S
    Total Standard Deviation in ln(k): 13.0351828895765"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S
Total Standard Deviation in ln(k): 13.0351828895765""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S
Total Standard Deviation in ln(k): 13.0351828895765
""",
)

entry(
    index = 8,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O",
    kinetics = ArrheniusBM(A=(175342,'m^3/(mol*s)'), n=-0.027872, w0=(563,'kJ/mol'), E0=(47.4839,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.018892675199703706, var=0.24976002132204894, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O
    Total Standard Deviation in ln(k): 1.0493553626809675"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O
Total Standard Deviation in ln(k): 1.0493553626809675""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O
Total Standard Deviation in ln(k): 1.0493553626809675
""",
)

entry(
    index = 9,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(100000,'m^3/(mol*s)'), n=-1.85597e-08, w0=(563,'kJ/mol'), E0=(35.9227,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03771497472594962, var=0.007112095996123719, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.2638270549034027"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.2638270549034027""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.2638270549034027
""",
)

entry(
    index = 10,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(100000,'m^3/(mol*s)'), n=-5.84445e-10, w0=(563,'kJ/mol'), E0=(36.3042,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06258229369899201, var=0.011749630589917017, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 0.3745466319941149"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.3745466319941149""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.3745466319941149
""",
)

entry(
    index = 11,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(100000,'m^3/(mol*s)'), n=-4.70441e-09, w0=(563,'kJ/mol'), E0=(35.8355,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(8.36447e+07,'m^3/(mol*s)'), n=-0.75107, w0=(563,'kJ/mol'), E0=(63.3156,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04561619858759418, var=0.45758397502882403, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.470715677602948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.470715677602948""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.470715677602948
""",
)

entry(
    index = 13,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(141421,'m^3/(mol*s)'), n=4.19996e-10, w0=(563,'kJ/mol'), E0=(42.6858,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.4197539171375903e-10, var=0.960906027802473, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.9651578859371874"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.9651578859371874""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_4R->O_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.9651578859371874
""",
)

entry(
    index = 14,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O",
    kinetics = ArrheniusBM(A=(9661,'m^3/(mol*s)'), n=0.617407, w0=(534.78,'kJ/mol'), E0=(27.2148,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.95944732293745, var=18.480357678587453, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O',), comment="""BM rule fitted to 25 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O
    Total Standard Deviation in ln(k): 16.05391012419437"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O
Total Standard Deviation in ln(k): 16.05391012419437""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O
Total Standard Deviation in ln(k): 16.05391012419437
""",
)

entry(
    index = 15,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H",
    kinetics = ArrheniusBM(A=(32784.8,'m^3/(mol*s)'), n=0.506288, w0=(539,'kJ/mol'), E0=(83.0482,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3550672185289219, var=8.004050652198492, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H
    Total Standard Deviation in ln(k): 6.563811091360288"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H
Total Standard Deviation in ln(k): 6.563811091360288""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H
Total Standard Deviation in ln(k): 6.563811091360288
""",
)

entry(
    index = 16,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-5BrCClFNO-R",
    kinetics = ArrheniusBM(A=(84300,'m^3/(mol*s)'), n=7.83575e-09, w0=(539,'kJ/mol'), E0=(75.1694,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-5BrCClFNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-5BrCClFNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-5BrCClFNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-5BrCClFNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R",
    kinetics = ArrheniusBM(A=(44093.5,'m^3/(mol*s)'), n=0.692363, w0=(539,'kJ/mol'), E0=(80.123,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06587190689304198, var=8.539135154449818, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R
    Total Standard Deviation in ln(k): 6.023703778497705"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R
Total Standard Deviation in ln(k): 6.023703778497705""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R
Total Standard Deviation in ln(k): 6.023703778497705
""",
)

entry(
    index = 18,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R_Ext-4CS-R",
    kinetics = ArrheniusBM(A=(2.89e+07,'m^3/(mol*s)'), n=-8.15467e-08, w0=(539,'kJ/mol'), E0=(87.1638,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R_Ext-4CS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R_Ext-4CS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R_Ext-4CS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Ext-4CS-R_Ext-4CS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Sp-5BrCClFNO-4BrCCClFNOS",
    kinetics = ArrheniusBM(A=(964000,'m^3/(mol*s)'), n=-4.35314e-09, w0=(539,'kJ/mol'), E0=(92.2495,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Sp-5BrCClFNO-4BrCCClFNOS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Sp-5BrCClFNO-4BrCCClFNOS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Sp-5BrCClFNO-4BrCCClFNOS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_Sp-5BrCClFNO-4BrCCClFNOS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_N-Sp-5BrCClFNO-4BrCCClFNOS",
    kinetics = ArrheniusBM(A=(2.41e+06,'m^3/(mol*s)'), n=9.92746e-08, w0=(539,'kJ/mol'), E0=(104.366,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_N-Sp-5BrCClFNO-4BrCCClFNOS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_N-Sp-5BrCClFNO-4BrCCClFNOS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_N-Sp-5BrCClFNO-4BrCCClFNOS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_Sp-6R!H=1R!H_N-Sp-5BrCClFNO-4BrCCClFNOS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H",
    kinetics = ArrheniusBM(A=(14342.3,'m^3/(mol*s)'), n=0.567352, w0=(533.725,'kJ/mol'), E0=(31.2112,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.380927473619411, var=21.103527131863963, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H',), comment="""BM rule fitted to 20 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H
    Total Standard Deviation in ln(k): 17.704260005703905"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H
Total Standard Deviation in ln(k): 17.704260005703905""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H
Total Standard Deviation in ln(k): 17.704260005703905
""",
)

entry(
    index = 22,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C",
    kinetics = ArrheniusBM(A=(27604.4,'m^3/(mol*s)'), n=0.515881, w0=(537.029,'kJ/mol'), E0=(29.017,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.41877703166918656, var=0.5880255709619887, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C',), comment="""BM rule fitted to 17 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C
    Total Standard Deviation in ln(k): 2.589491096066327"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C
Total Standard Deviation in ln(k): 2.589491096066327""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C
Total Standard Deviation in ln(k): 2.589491096066327
""",
)

entry(
    index = 23,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=2.07e-09, w0=(539,'kJ/mol'), E0=(96.6108,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.6373354842722458e-09, var=1.5200504684685333e-17, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
    Total Standard Deviation in ln(k): 1.1929934212303094e-08"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
Total Standard Deviation in ln(k): 1.1929934212303094e-08""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
Total Standard Deviation in ln(k): 1.1929934212303094e-08
""",
)

entry(
    index = 24,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=-1.45588e-08, w0=(539,'kJ/mol'), E0=(98.0499,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C",
    kinetics = ArrheniusBM(A=(26224,'m^3/(mol*s)'), n=0.520794, w0=(536.767,'kJ/mol'), E0=(16.1889,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2289724588916703, var=0.21444319771196263, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C',), comment="""BM rule fitted to 15 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
    Total Standard Deviation in ln(k): 1.503660646239273"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
Total Standard Deviation in ln(k): 1.503660646239273""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C
Total Standard Deviation in ln(k): 1.503660646239273
""",
)

entry(
    index = 26,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O",
    kinetics = ArrheniusBM(A=(340826,'m^3/(mol*s)'), n=-1.08264e-07, w0=(539,'kJ/mol'), E0=(49.8746,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.243993006310062e-09, var=0.960906045742854, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O
    Total Standard Deviation in ln(k): 1.9651579216239603"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O
Total Standard Deviation in ln(k): 1.9651579216239603""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O
Total Standard Deviation in ln(k): 1.9651579216239603
""",
)

entry(
    index = 27,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(241000,'m^3/(mol*s)'), n=-4.10186e-09, w0=(539,'kJ/mol'), E0=(65.4044,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_5BrCClFNO->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O",
    kinetics = ArrheniusBM(A=(25585.2,'m^3/(mol*s)'), n=0.525802, w0=(536.423,'kJ/mol'), E0=(19.3976,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3906978248005291, var=0.2782129993917838, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O',), comment="""BM rule fitted to 13 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O
    Total Standard Deviation in ln(k): 2.039068390470709"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O
Total Standard Deviation in ln(k): 2.039068390470709""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O
Total Standard Deviation in ln(k): 2.039068390470709
""",
)

entry(
    index = 29,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(0.000754021,'m^3/(mol*s)'), n=2.68629, w0=(505.5,'kJ/mol'), E0=(-18.2862,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4735502014390809, var=1.5296047720417258, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R
    Total Standard Deviation in ln(k): 6.181787483409471"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R
Total Standard Deviation in ln(k): 6.181787483409471""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R
Total Standard Deviation in ln(k): 6.181787483409471
""",
)

entry(
    index = 30,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_1R!H-inRing",
    kinetics = ArrheniusBM(A=(20319.4,'m^3/(mol*s)'), n=0.557275, w0=(483.5,'kJ/mol'), E0=(18.6075,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=4.76064e-09, w0=(527.5,'kJ/mol'), E0=(73.0284,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_N-1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_N-1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-6R!H-R_N-1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R",
    kinetics = ArrheniusBM(A=(4.00744e+06,'m^3/(mol*s)'), n=-0.141162, w0=(545.7,'kJ/mol'), E0=(31.9097,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21232255877800607, var=0.4161859899497664, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R
    Total Standard Deviation in ln(k): 1.8267780542453573"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R
Total Standard Deviation in ln(k): 1.8267780542453573""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R
Total Standard Deviation in ln(k): 1.8267780542453573
""",
)

entry(
    index = 33,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2.56e+07,'m^3/(mol*s)'), n=-0.35, w0=(539,'kJ/mol'), E0=(67.068,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=-4.11946e-08, w0=(527.5,'kJ/mol'), E0=(67.7658,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_2R!H->C",
    kinetics = ArrheniusBM(A=(2.16e+08,'m^3/(mol*s)'), n=-0.75, w0=(539,'kJ/mol'), E0=(63.6762,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.7641e+06,'m^3/(mol*s)'), n=-0.0462318, w0=(561.5,'kJ/mol'), E0=(21.8225,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.011882880244573183, var=0.8932435450321468, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C
    Total Standard Deviation in ln(k): 1.9245629290953707"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C
Total Standard Deviation in ln(k): 1.9245629290953707""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C
Total Standard Deviation in ln(k): 1.9245629290953707
""",
)

entry(
    index = 37,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C_Ext-7R!H-R_Ext-5CF-R",
    kinetics = ArrheniusBM(A=(1.94e+06,'m^3/(mol*s)'), n=2.10553e-09, w0=(561.5,'kJ/mol'), E0=(38.5954,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C_Ext-7R!H-R_Ext-5CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C_Ext-7R!H-R_Ext-5CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C_Ext-7R!H-R_Ext-5CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-4C-R_N-2R!H->C_Ext-7R!H-R_Ext-5CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(974410,'m^3/(mol*s)'), n=-0.0210882, w0=(539,'kJ/mol'), E0=(58.4088,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12379527460480996, var=0.04508104980218605, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.7366947385544255"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.7366947385544255""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.7366947385544255
""",
)

entry(
    index = 39,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Ext-5CF-R",
    kinetics = ArrheniusBM(A=(1.30188e+06,'m^3/(mol*s)'), n=-0.0632647, w0=(539,'kJ/mol'), E0=(59.9808,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Ext-5CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Ext-5CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Ext-5CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Ext-5CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Sp-5CF-4C",
    kinetics = ArrheniusBM(A=(843000,'m^3/(mol*s)'), n=3.32941e-09, w0=(539,'kJ/mol'), E0=(69.3765,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Sp-5CF-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Sp-5CF-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Sp-5CF-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_Sp-5CF-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_N-Sp-5CF-4C",
    kinetics = ArrheniusBM(A=(843000,'m^3/(mol*s)'), n=9.01016e-09, w0=(539,'kJ/mol'), E0=(78.2166,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_N-Sp-5CF-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_N-Sp-5CF-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_N-Sp-5CF-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Ext-1R!H-R_N-Sp-5CF-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C",
    kinetics = ArrheniusBM(A=(1.8697e+06,'m^3/(mol*s)'), n=-0.0316323, w0=(539,'kJ/mol'), E0=(56.2885,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14888391573539506, var=0.09706161843692944, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C
    Total Standard Deviation in ln(k): 0.9986496636580938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C
Total Standard Deviation in ln(k): 0.9986496636580938""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C
Total Standard Deviation in ln(k): 0.9986496636580938
""",
)

entry(
    index = 43,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C_Ext-5CF-R",
    kinetics = ArrheniusBM(A=(2.41088e+06,'m^3/(mol*s)'), n=-0.0632647, w0=(539,'kJ/mol'), E0=(57.6576,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C_Ext-5CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C_Ext-5CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C_Ext-5CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_Sp-5CF-4C_Ext-5CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_N-Sp-5CF-4C",
    kinetics = ArrheniusBM(A=(1.21e+06,'m^3/(mol*s)'), n=-1.85831e-08, w0=(539,'kJ/mol'), E0=(76.2081,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_N-Sp-5CF-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_N-Sp-5CF-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_N-Sp-5CF-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_4CS->C_N-Sp-5BrBrBrCCCClClClFFFNNNOOO#4C_N-5BrCClFNO->O_N-Sp-5CF-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C",
    kinetics = ArrheniusBM(A=(6.41947,'m^3/(mol*s)'), n=1.17357, w0=(515,'kJ/mol'), E0=(53.2393,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.5769113321497894, var=36.01419751550576, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C
    Total Standard Deviation in ln(k): 21.017996487725853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C
Total Standard Deviation in ln(k): 21.017996487725853""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C
Total Standard Deviation in ln(k): 21.017996487725853
""",
)

entry(
    index = 46,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(6.55713e+06,'m^3/(mol*s)'), n=-0.267658, w0=(515,'kJ/mol'), E0=(58.1419,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.025362235778445468, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.0637242104986067"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.0637242104986067""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.0637242104986067
""",
)

entry(
    index = 47,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R_Ext-5BrCClFNO-R",
    kinetics = ArrheniusBM(A=(6.55713e+06,'m^3/(mol*s)'), n=-0.267658, w0=(515,'kJ/mol'), E0=(58.7277,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R_Ext-5BrCClFNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R_Ext-5BrCClFNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R_Ext-5BrCClFNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-1R!H-R_N-5R!H->S_N-4R->O_N-Sp-6R!H=1R!H_N-4CS->C_Ext-1R!H-R_Ext-5BrCClFNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.68661e+15,'m^3/(mol*s)'), n=-2.816, w0=(547.45,'kJ/mol'), E0=(100.118,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19176361521052568, var=2.6401805106326117, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.739238438380388"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.739238438380388""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.739238438380388
""",
)

entry(
    index = 49,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F",
    kinetics = ArrheniusBM(A=(1.41802e+07,'m^3/(mol*s)'), n=0.000363966, w0=(533.25,'kJ/mol'), E0=(67.2596,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.7238996722869935e-09, var=0.9609060319990688, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F
    Total Standard Deviation in ln(k): 1.9651578937006078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F
Total Standard Deviation in ln(k): 1.9651578937006078""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F
Total Standard Deviation in ln(k): 1.9651578937006078
""",
)

entry(
    index = 50,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=-8.7362e-10, w0=(539,'kJ/mol'), E0=(62.2411,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=-1.39711e-08, w0=(527.5,'kJ/mol'), E0=(63.2561,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_5R!H->F_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(1.24513e+11,'m^3/(mol*s)'), n=-1.63604, w0=(551,'kJ/mol'), E0=(81.0741,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03344106920634167, var=1.464701285205334, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F
    Total Standard Deviation in ln(k): 2.5102502858892723"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F
Total Standard Deviation in ln(k): 2.5102502858892723""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F
Total Standard Deviation in ln(k): 2.5102502858892723
""",
)

entry(
    index = 53,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R",
    kinetics = ArrheniusBM(A=(6.79623e+11,'m^3/(mol*s)'), n=-1.80442, w0=(539,'kJ/mol'), E0=(79.5475,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1756919933094387, var=8.131585618052993, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R
    Total Standard Deviation in ln(k): 8.670689544387095"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R
Total Standard Deviation in ln(k): 8.670689544387095""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R
Total Standard Deviation in ln(k): 8.670689544387095
""",
)

entry(
    index = 54,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-4R-R",
    kinetics = ArrheniusBM(A=(50000,'m^3/(mol*s)'), n=5.90396e-09, w0=(539,'kJ/mol'), E0=(30.8631,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-4R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-4R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-4R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.08e+08,'m^3/(mol*s)'), n=-0.75, w0=(539,'kJ/mol'), E0=(65.7325,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_Ext-5BrCClNOS-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_4R->C",
    kinetics = ArrheniusBM(A=(333333,'m^3/(mol*s)'), n=4.30577e-10, w0=(539,'kJ/mol'), E0=(57.1846,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C",
    kinetics = ArrheniusBM(A=(173205,'m^3/(mol*s)'), n=1.42964e-09, w0=(563,'kJ/mol'), E0=(47.4543,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01962490600378369, var=0.9058817125637972, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C
    Total Standard Deviation in ln(k): 1.9573719214979861"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C
Total Standard Deviation in ln(k): 1.9573719214979861""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C
Total Standard Deviation in ln(k): 1.9573719214979861
""",
)

entry(
    index = 58,
    label = "Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(173205,'m^3/(mol*s)'), n=-3.34254e-08, w0=(563,'kJ/mol'), E0=(46.4868,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.9914789396273076e-09, var=2.4138979214679144, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.114701560802306"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.114701560802306""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_Ext-2R!H-R_N-5R!H->F_N-4R->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.114701560802306
""",
)

entry(
    index = 59,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O",
    kinetics = ArrheniusBM(A=(12.4764,'m^3/(mol*s)'), n=1.90962, w0=(626.45,'kJ/mol'), E0=(4.15053,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15519987327625473, var=0.6672850079191734, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O
    Total Standard Deviation in ln(k): 2.0275676940019696"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O
Total Standard Deviation in ln(k): 2.0275676940019696""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O
Total Standard Deviation in ln(k): 2.0275676940019696
""",
)

entry(
    index = 60,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(15.3304,'m^3/(mol*s)'), n=1.9099, w0=(626.125,'kJ/mol'), E0=(5.1839,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3139209118617231, var=0.6800651165443758, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 2.441972055265988"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.441972055265988""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.441972055265988
""",
)

entry(
    index = 61,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_5R!H->Br",
    kinetics = ArrheniusBM(A=(3.33333e+06,'m^3/(mol*s)'), n=-1.29606e-09, w0=(655.5,'kJ/mol'), E0=(76.3995,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_5R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_5R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_5R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_5R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br",
    kinetics = ArrheniusBM(A=(15.2824,'m^3/(mol*s)'), n=1.91038, w0=(621.929,'kJ/mol'), E0=(4.75683,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.33664012190240206, var=0.8389711713614659, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br
    Total Standard Deviation in ln(k): 2.6820739536265257"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br
Total Standard Deviation in ln(k): 2.6820739536265257""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br
Total Standard Deviation in ln(k): 2.6820739536265257
""",
)

entry(
    index = 63,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_2R!H->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=9.98868e-09, w0=(679.5,'kJ/mol'), E0=(57.5078,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C",
    kinetics = ArrheniusBM(A=(15.2296,'m^3/(mol*s)'), n=1.91087, w0=(612.333,'kJ/mol'), E0=(5.10581,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3281578663018971, var=0.8044535142275768, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C
    Total Standard Deviation in ln(k): 2.6225908578853074"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C
Total Standard Deviation in ln(k): 2.6225908578853074""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C
Total Standard Deviation in ln(k): 2.6225908578853074
""",
)

entry(
    index = 65,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_1R!H->C",
    kinetics = ArrheniusBM(A=(8.03333e+06,'m^3/(mol*s)'), n=3.39523e-09, w0=(655.5,'kJ/mol'), E0=(73.5791,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C",
    kinetics = ArrheniusBM(A=(15.1785,'m^3/(mol*s)'), n=1.91136, w0=(603.7,'kJ/mol'), E0=(3.86499,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.33960190302821525, var=0.8509467240917166, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C
    Total Standard Deviation in ln(k): 2.7025745414018467"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C
Total Standard Deviation in ln(k): 2.7025745414018467""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C
Total Standard Deviation in ln(k): 2.7025745414018467
""",
)

entry(
    index = 67,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O",
    kinetics = ArrheniusBM(A=(15.241,'m^3/(mol*s)'), n=1.91136, w0=(648.5,'kJ/mol'), E0=(5.43305,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0079411854009772, var=2.281347972126138, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O
    Total Standard Deviation in ln(k): 5.5604938230584935"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O
Total Standard Deviation in ln(k): 5.5604938230584935""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O
Total Standard Deviation in ln(k): 5.5604938230584935
""",
)

entry(
    index = 68,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O_2NO->O",
    kinetics = ArrheniusBM(A=(15.137,'m^3/(mol*s)'), n=1.91136, w0=(635,'kJ/mol'), E0=(4.10965,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O_N-2NO->O",
    kinetics = ArrheniusBM(A=(15.3458,'m^3/(mol*s)'), n=1.91136, w0=(662,'kJ/mol'), E0=(27.1417,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_1NO->O_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O",
    kinetics = ArrheniusBM(A=(15.137,'m^3/(mol*s)'), n=1.91136, w0=(573.833,'kJ/mol'), E0=(24.2205,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04545993447137404, var=0.042655242012456955, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O
    Total Standard Deviation in ln(k): 0.5282617938309521"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O
Total Standard Deviation in ln(k): 0.5282617938309521""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O
Total Standard Deviation in ln(k): 0.5282617938309521
""",
)

entry(
    index = 71,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_2NO->O",
    kinetics = ArrheniusBM(A=(15.137,'m^3/(mol*s)'), n=1.91136, w0=(625.5,'kJ/mol'), E0=(19.6491,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O",
    kinetics = ArrheniusBM(A=(15.137,'m^3/(mol*s)'), n=1.91136, w0=(548,'kJ/mol'), E0=(35.7996,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4947908977436571, var=0.6465481379303625, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O
    Total Standard Deviation in ln(k): 2.8551649439842732"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O
Total Standard Deviation in ln(k): 2.8551649439842732""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O
Total Standard Deviation in ln(k): 2.8551649439842732
""",
)

entry(
    index = 73,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O_2N-u1",
    kinetics = ArrheniusBM(A=(15.137,'m^3/(mol*s)'), n=1.91136, w0=(548,'kJ/mol'), E0=(30.8566,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O_N-2N-u1",
    kinetics = ArrheniusBM(A=(15.137,'m^3/(mol*s)'), n=1.91136, w0=(548,'kJ/mol'), E0=(60.0521,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_Sp-2R!H-1R!H_N-5R!H->Br_N-2R!H->C_N-1R!H->C_N-1NO->O_N-2NO->O_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(7.45181,'m^3/(mol*s)'), n=1.90892, w0=(627.75,'kJ/mol'), E0=(59.2734,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6515196177110988, var=1.068119821182163, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 3.7088753109299795"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 3.7088753109299795""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 3.7088753109299795
""",
)

entry(
    index = 76,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_1R!H->C",
    kinetics = ArrheniusBM(A=(7.59897,'m^3/(mol*s)'), n=1.90649, w0=(571,'kJ/mol'), E0=(56.6097,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 77,
    label = "Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_N-1R!H->C",
    kinetics = ArrheniusBM(A=(7.3075,'m^3/(mol*s)'), n=1.91136, w0=(684.5,'kJ/mol'), E0=(92.1772,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_N-1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_N-1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_4R->O_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 78,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O",
    kinetics = ArrheniusBM(A=(55.6243,'m^3/(mol*s)'), n=1.58893, w0=(597.409,'kJ/mol'), E0=(24.1404,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4843080269762434, var=5.408187660459464, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O',), comment="""BM rule fitted to 22 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O
    Total Standard Deviation in ln(k): 5.87896809226619"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O
Total Standard Deviation in ln(k): 5.87896809226619""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O
Total Standard Deviation in ln(k): 5.87896809226619
""",
)

entry(
    index = 79,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_5R!H->N",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(598.5,'kJ/mol'), E0=(25.4926,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N",
    kinetics = ArrheniusBM(A=(26.9307,'m^3/(mol*s)'), n=1.7319, w0=(597.357,'kJ/mol'), E0=(1.77872,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.021989733136989098, var=0.8263653457642715, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N',), comment="""BM rule fitted to 21 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N
    Total Standard Deviation in ln(k): 1.8776477780518248"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N
Total Standard Deviation in ln(k): 1.8776477780518248""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N
Total Standard Deviation in ln(k): 1.8776477780518248
""",
)

entry(
    index = 81,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O",
    kinetics = ArrheniusBM(A=(0.022372,'m^3/(mol*s)'), n=2.67587, w0=(644.1,'kJ/mol'), E0=(-6.68123,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06549229330671626, var=1.074092084335976, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O
    Total Standard Deviation in ln(k): 2.2422291386189506"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O
Total Standard Deviation in ln(k): 2.2422291386189506""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O
Total Standard Deviation in ln(k): 2.2422291386189506
""",
)

entry(
    index = 82,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS",
    kinetics = ArrheniusBM(A=(16.4899,'m^3/(mol*s)'), n=1.89829, w0=(646,'kJ/mol'), E0=(12.5277,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7119916452925086, var=1.3846613918678052, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS
    Total Standard Deviation in ln(k): 4.147928294905957"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS
Total Standard Deviation in ln(k): 4.147928294905957""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS
Total Standard Deviation in ln(k): 4.147928294905957
""",
)

entry(
    index = 83,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_Ext-5BrCClOS-R",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=-4.12254e-09, w0=(655.5,'kJ/mol'), E0=(58.5176,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_Ext-5BrCClOS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_Ext-5BrCClOS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_Ext-5BrCClOS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_Ext-5BrCClOS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C",
    kinetics = ArrheniusBM(A=(9.24918e+07,'m^3/(mol*s)'), n=-0.49878, w0=(655.5,'kJ/mol'), E0=(79.0313,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.011535687046447333, var=0.033595208509387575, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C
    Total Standard Deviation in ln(k): 0.396431945382026"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C
Total Standard Deviation in ln(k): 0.396431945382026""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C
Total Standard Deviation in ln(k): 0.396431945382026
""",
)

entry(
    index = 85,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(2.89163e+07,'m^3/(mol*s)'), n=-0.373329, w0=(655.5,'kJ/mol'), E0=(72.1959,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.670511072781141e-11, var=0.06912283089195403, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_Ext-4CNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_Ext-4CNS-R
    Total Standard Deviation in ln(k): 0.5270693326185465"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.5270693326185465""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.5270693326185465
""",
)

entry(
    index = 86,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_Ext-4CNS-R_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(3.47e+08,'m^3/(mol*s)'), n=-0.75, w0=(655.5,'kJ/mol'), E0=(67.0846,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_Ext-4CNS-R_Ext-4CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_Ext-4CNS-R_Ext-4CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 87,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C",
    kinetics = ArrheniusBM(A=(15.3833,'m^3/(mol*s)'), n=1.90892, w0=(627,'kJ/mol'), E0=(11.976,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.675508212924922, var=19.316065883486637, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C
    Total Standard Deviation in ln(k): 23.07089087618408"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C
Total Standard Deviation in ln(k): 23.07089087618408""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C
Total Standard Deviation in ln(k): 23.07089087618408
""",
)

entry(
    index = 88,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C_2R!H->C",
    kinetics = ArrheniusBM(A=(4.82e+06,'m^3/(mol*s)'), n=-3.28933e-09, w0=(655.5,'kJ/mol'), E0=(66.7498,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(15.137,'m^3/(mol*s)'), n=1.91136, w0=(598.5,'kJ/mol'), E0=(6.5542,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS",
    kinetics = ArrheniusBM(A=(8.061,'m^3/(mol*s)'), n=1.89922, w0=(641.25,'kJ/mol'), E0=(14.0224,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.554616392052546, var=8.148134271691292, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS
    Total Standard Deviation in ln(k): 9.628574981315625"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS
Total Standard Deviation in ln(k): 9.628574981315625""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS
Total Standard Deviation in ln(k): 9.628574981315625
""",
)

entry(
    index = 91,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C",
    kinetics = ArrheniusBM(A=(7.88926,'m^3/(mol*s)'), n=1.90164, w0=(636.5,'kJ/mol'), E0=(8.27798,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.604390590097761, var=0.5763546944406924, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C
    Total Standard Deviation in ln(k): 8.06565028328301"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C
Total Standard Deviation in ln(k): 8.06565028328301""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C
Total Standard Deviation in ln(k): 8.06565028328301
""",
)

entry(
    index = 92,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C",
    kinetics = ArrheniusBM(A=(1.90316e+07,'m^3/(mol*s)'), n=5.40517e-08, w0=(655.5,'kJ/mol'), E0=(64.0651,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.29316537976053914, var=2.928248266702813, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C
    Total Standard Deviation in ln(k): 4.167124182449777"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C
Total Standard Deviation in ln(k): 4.167124182449777""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C
Total Standard Deviation in ln(k): 4.167124182449777
""",
)

entry(
    index = 93,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C_Sp-5C=4CNS",
    kinetics = ArrheniusBM(A=(3.01e+07,'m^3/(mol*s)'), n=1.93473e-08, w0=(655.5,'kJ/mol'), E0=(79.8442,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C_Sp-5C=4CNS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C_Sp-5C=4CNS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C_Sp-5C=4CNS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C_Sp-5C=4CNS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C_N-Sp-5C=4CNS",
    kinetics = ArrheniusBM(A=(1.20333e+07,'m^3/(mol*s)'), n=-2.26006e-08, w0=(655.5,'kJ/mol'), E0=(100.208,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C_N-Sp-5C=4CNS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C_N-Sp-5C=4CNS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C_N-Sp-5C=4CNS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_2R!H->C_N-Sp-5C=4CNS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(7.59897,'m^3/(mol*s)'), n=1.90649, w0=(598.5,'kJ/mol'), E0=(9.64021,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_5BrCClOS->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C",
    kinetics = ArrheniusBM(A=(1.81e+08,'m^3/(mol*s)'), n=1.0541e-08, w0=(655.5,'kJ/mol'), E0=(58.849,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_1R!H->O_N-Sp-5BrCClOS-4BrCCClNOSS_N-5BrCClOS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 97,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O",
    kinetics = ArrheniusBM(A=(146.347,'m^3/(mol*s)'), n=1.39949, w0=(554.864,'kJ/mol'), E0=(49.4113,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19289013079411457, var=0.479240275164173, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O
    Total Standard Deviation in ln(k): 1.8724701739521827"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O
Total Standard Deviation in ln(k): 1.8724701739521827""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O
Total Standard Deviation in ln(k): 1.8724701739521827
""",
)

entry(
    index = 98,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_2R!H->O",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=1.69962e-08, w0=(631.5,'kJ/mol'), E0=(74.5352,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_2R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_2R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O",
    kinetics = ArrheniusBM(A=(144.139,'m^3/(mol*s)'), n=1.40126, w0=(547.2,'kJ/mol'), E0=(49.3332,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14227420675438204, var=0.18803665103156347, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O
    Total Standard Deviation in ln(k): 1.226790022772078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O
Total Standard Deviation in ln(k): 1.226790022772078""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O
Total Standard Deviation in ln(k): 1.226790022772078
""",
)

entry(
    index = 100,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS",
    kinetics = ArrheniusBM(A=(3.61e+06,'m^3/(mol*s)'), n=-1.0817e-08, w0=(539,'kJ/mol'), E0=(93.3082,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 101,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS",
    kinetics = ArrheniusBM(A=(142.306,'m^3/(mol*s)'), n=1.40303, w0=(548.111,'kJ/mol'), E0=(49.3286,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2507032447770549, var=0.19938217125944627, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS
    Total Standard Deviation in ln(k): 1.5250665832466996"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS
Total Standard Deviation in ln(k): 1.5250665832466996""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS
Total Standard Deviation in ln(k): 1.5250665832466996
""",
)

entry(
    index = 102,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_2CNS->S",
    kinetics = ArrheniusBM(A=(979000,'m^3/(mol*s)'), n=-3.98006e-09, w0=(537.5,'kJ/mol'), E0=(39.0052,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_2CNS->S',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_2CNS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_2CNS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_2CNS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 103,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S",
    kinetics = ArrheniusBM(A=(139.695,'m^3/(mol*s)'), n=1.40572, w0=(549.438,'kJ/mol'), E0=(41.5715,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17478680106162892, var=0.10975835600589888, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S
    Total Standard Deviation in ln(k): 1.1033275117889518"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S
Total Standard Deviation in ln(k): 1.1033275117889518""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S
Total Standard Deviation in ln(k): 1.1033275117889518
""",
)

entry(
    index = 104,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O",
    kinetics = ArrheniusBM(A=(127.638,'m^3/(mol*s)'), n=1.41908, w0=(593.5,'kJ/mol'), E0=(58.9912,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1953269733829577, var=0.0886597043625028, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O
    Total Standard Deviation in ln(k): 1.0876967857044384"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O
Total Standard Deviation in ln(k): 1.0876967857044384""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O
Total Standard Deviation in ln(k): 1.0876967857044384
""",
)

entry(
    index = 105,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_1CNS->C",
    kinetics = ArrheniusBM(A=(2.89e+06,'m^3/(mol*s)'), n=1.98909e-09, w0=(539,'kJ/mol'), E0=(60.3624,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 106,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_N-1CNS->C",
    kinetics = ArrheniusBM(A=(126.016,'m^3/(mol*s)'), n=1.42089, w0=(648,'kJ/mol'), E0=(54.0633,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_N-1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_N-1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_5BrCClOS->O_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 107,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O",
    kinetics = ArrheniusBM(A=(1.38436e+07,'m^3/(mol*s)'), n=-0.304179, w0=(534.75,'kJ/mol'), E0=(30.0612,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14508322974677523, var=0.22718626908316414, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O
    Total Standard Deviation in ln(k): 1.3200688739406718"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O
Total Standard Deviation in ln(k): 1.3200688739406718""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O
Total Standard Deviation in ln(k): 1.3200688739406718
""",
)

entry(
    index = 108,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS",
    kinetics = ArrheniusBM(A=(8.57298e+06,'m^3/(mol*s)'), n=-0.225015, w0=(533.9,'kJ/mol'), E0=(31.6644,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1312295035868316, var=0.1304867938215465, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS
    Total Standard Deviation in ln(k): 1.0538919374253954"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS
Total Standard Deviation in ln(k): 1.0538919374253954""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS
Total Standard Deviation in ln(k): 1.0538919374253954
""",
)

entry(
    index = 109,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(7.91962e+08,'m^3/(mol*s)'), n=-0.897561, w0=(539,'kJ/mol'), E0=(65.8038,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0440742522668757e-15, var=0.0489114988441704, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R
    Total Standard Deviation in ln(k): 0.4433660913390905"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.4433660913390905""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.4433660913390905
""",
)

entry(
    index = 110,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(2.86e+09,'m^3/(mol*s)'), n=-1.1, w0=(539,'kJ/mol'), E0=(60.6937,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 111,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C",
    kinetics = ArrheniusBM(A=(2.95928e+07,'m^3/(mol*s)'), n=-0.381632, w0=(539,'kJ/mol'), E0=(53.3889,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15485077602999534, var=0.09848512049994759, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C
    Total Standard Deviation in ln(k): 1.0182050608646662"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C
Total Standard Deviation in ln(k): 1.0182050608646662""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C
Total Standard Deviation in ln(k): 1.0182050608646662
""",
)

entry(
    index = 112,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R",
    kinetics = ArrheniusBM(A=(3.80753e+07,'m^3/(mol*s)'), n=-0.413265, w0=(539,'kJ/mol'), E0=(54.3041,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_1CNS->C_Ext-5CS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 113,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_N-1CNS->C",
    kinetics = ArrheniusBM(A=(644,'m^3/(mol*s)'), n=1.19, w0=(513.5,'kJ/mol'), E0=(41.9102,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_N-1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_N-1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_Sp-5CS-4CCNSS_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 114,
    label = "Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_N-Sp-5CS-4CCNSS",
    kinetics = ArrheniusBM(A=(1.52e+08,'m^3/(mol*s)'), n=-0.7, w0=(539,'kJ/mol'), E0=(73.2955,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_N-Sp-5CS-4CCNSS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_N-Sp-5CS-4CCNSS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_N-Sp-5CS-4CCNSS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-4R->O_N-5R!H->N_N-1R!H->O_N-2R!H->O_N-Sp-5BrBrBrCCCCCClClClNNOOOSSSSS#4BrBrBrCCCCCCClClClNNNOOOSSSSSS_N-2CNS->S_N-5BrCClOS->O_N-Sp-5CS-4CCNSS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Root_Ext-4R-R_N-5R!H-u0",
    kinetics = ArrheniusBM(A=(776500,'m^3/(mol*s)'), n=-0.28929, w0=(570.583,'kJ/mol'), E0=(30.7074,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1243636117835156, var=5.51918363762847, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0',), comment="""BM rule fitted to 36 training reactions at node Root_Ext-4R-R_N-5R!H-u0
    Total Standard Deviation in ln(k): 7.534746860762618"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_Ext-4R-R_N-5R!H-u0
Total Standard Deviation in ln(k): 7.534746860762618""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_Ext-4R-R_N-5R!H-u0
Total Standard Deviation in ln(k): 7.534746860762618
""",
)

entry(
    index = 116,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(655124,'m^3/(mol*s)'), n=-0.411562, w0=(569.967,'kJ/mol'), E0=(1.79182,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06415501334490731, var=7.264455804505767, Tref=1000.0, N=30, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H',), comment="""BM rule fitted to 30 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 5.5644866759519065"""),
    rank = 11,
    shortDesc = """BM rule fitted to 30 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 5.5644866759519065""",
    longDesc = 
"""
BM rule fitted to 30 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 5.5644866759519065
""",
)

entry(
    index = 117,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C",
    kinetics = ArrheniusBM(A=(607954,'m^3/(mol*s)'), n=-0.425754, w0=(566.19,'kJ/mol'), E0=(0.547918,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.038430210090507906, var=6.353483772989122, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C',), comment="""BM rule fitted to 29 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 5.149717179610776"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 5.149717179610776""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 5.149717179610776
""",
)

entry(
    index = 118,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.72073e+07,'m^3/(mol*s)'), n=-1.02487, w0=(567.205,'kJ/mol'), E0=(0.666113,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01713673903894337, var=4.234308930350632, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R',), comment="""BM rule fitted to 22 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.168288009305458"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.168288009305458""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.168288009305458
""",
)

entry(
    index = 119,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.20183,'m^3/(mol*s)'), n=1.1452, w0=(563,'kJ/mol'), E0=(5.97203,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2957382636730137, var=1.1971718498505262, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 2.936548836454607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 2.936548836454607""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 2.936548836454607
""",
)

entry(
    index = 120,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C",
    kinetics = ArrheniusBM(A=(288843,'m^3/(mol*s)'), n=-0.320302, w0=(563,'kJ/mol'), E0=(40.1545,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11701209588070298, var=0.292066247257673, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C
    Total Standard Deviation in ln(k): 1.3774223020512757"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C
Total Standard Deviation in ln(k): 1.3774223020512757""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C
Total Standard Deviation in ln(k): 1.3774223020512757
""",
)

entry(
    index = 121,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=3.74264e-10, w0=(563,'kJ/mol'), E0=(20.6899,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.617773692538028e-10, var=3.1181350595307165e-20, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R
    Total Standard Deviation in ln(k): 7.604767709719698e-10"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R
Total Standard Deviation in ln(k): 7.604767709719698e-10""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R
Total Standard Deviation in ln(k): 7.604767709719698e-10
""",
)

entry(
    index = 122,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=-2.10386e-09, w0=(563,'kJ/mol'), E0=(20.6597,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.252493831571836e-10, var=4.893548045035749e-19, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 2.2195998652371276e-09"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.2195998652371276e-09""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.2195998652371276e-09
""",
)

entry(
    index = 123,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=-6.65017e-10, w0=(563,'kJ/mol'), E0=(21.6124,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R_Ext-8R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-6C-R_Ext-1C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 124,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(10974.5,'m^3/(mol*s)'), n=-1.1021e-09, w0=(563,'kJ/mol'), E0=(19.682,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.372810945808781e-10, var=0.06917824979652475, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.5272805791222012"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.5272805791222012""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_Sp-6C-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.5272805791222012
""",
)

entry(
    index = 125,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_N-Sp-6C-1C",
    kinetics = ArrheniusBM(A=(602200,'m^3/(mol*s)'), n=4.61664e-08, w0=(563,'kJ/mol'), E0=(40.0728,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_N-Sp-6C-1C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_N-Sp-6C-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_N-Sp-6C-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_6R!H->C_N-Sp-6C-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 126,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(4.33405e+12,'m^3/(mol*s)'), n=-2.52722, w0=(570.115,'kJ/mol'), E0=(0.95777,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.020043834452152316, var=5.12317105465127, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 13 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 4.58796357164748"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 4.58796357164748""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 4.58796357164748
""",
)

entry(
    index = 127,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.23598e+13,'m^3/(mol*s)'), n=-2.8187, w0=(563,'kJ/mol'), E0=(0.640075,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08595381096797143, var=3.4663820951529427, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.9484247240674986"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.9484247240674986""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.9484247240674986
""",
)

entry(
    index = 128,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.64836e+15,'m^3/(mol*s)'), n=-3.33251, w0=(563,'kJ/mol'), E0=(1.76458,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1412697334175288, var=5.133979752629748, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 4.897335377475607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.897335377475607""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.897335377475607
""",
)

entry(
    index = 129,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.17232e+17,'m^3/(mol*s)'), n=-3.86313, w0=(563,'kJ/mol'), E0=(-22.2352,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.16646402296399507, var=14.510596595318958, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 8.05484393860032"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 8.05484393860032""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-1C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 8.05484393860032
""",
)

entry(
    index = 130,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.63887e+13,'m^3/(mol*s)'), n=-2.80189, w0=(563,'kJ/mol'), E0=(1.77524,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.015793750389594834, var=19.788281635221352, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 8.957550606463286"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 8.957550606463286""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 8.957550606463286
""",
)

entry(
    index = 131,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C",
    kinetics = ArrheniusBM(A=(6.16313e+13,'m^3/(mol*s)'), n=-2.80189, w0=(563,'kJ/mol'), E0=(2.75644,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1342584738306164, var=16.351560980043935, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C
    Total Standard Deviation in ln(k): 8.443892795238002"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C
Total Standard Deviation in ln(k): 8.443892795238002""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C
Total Standard Deviation in ln(k): 8.443892795238002
""",
)

entry(
    index = 132,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.32924e+13,'m^3/(mol*s)'), n=-2.80189, w0=(563,'kJ/mol'), E0=(0.669821,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19627989925924563, var=48.69127306669605, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 14.482032998279706"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 14.482032998279706""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 14.482032998279706
""",
)

entry(
    index = 133,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(300000,'m^3/(mol*s)'), n=-2.45082e-09, w0=(655.5,'kJ/mol'), E0=(57.4258,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-1C-R_N-6R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 134,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.73327e+15,'m^3/(mol*s)'), n=-3.04598, w0=(563,'kJ/mol'), E0=(47.1166,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4203244291514337, var=20.786642173272043, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 10.196153903805083"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 10.196153903805083""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 10.196153903805083
""",
)

entry(
    index = 135,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(7.23e+06,'m^3/(mol*s)'), n=4.65296e-09, w0=(563,'kJ/mol'), E0=(99.5729,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 136,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(8.76105e+09,'m^3/(mol*s)'), n=-1.65753, w0=(563,'kJ/mol'), E0=(6.48886,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.012072905991731466, var=16.36491346411714, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 8.140203064343185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 8.140203064343185""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 8.140203064343185
""",
)

entry(
    index = 137,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(4.23154e+13,'m^3/(mol*s)'), n=-2.80189, w0=(563,'kJ/mol'), E0=(5.63,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1342584840613585, var=21.205889442307488, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 9.569108399118686"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F
Total Standard Deviation in ln(k): 9.569108399118686""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F
Total Standard Deviation in ln(k): 9.569108399118686
""",
)

entry(
    index = 138,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(4.23154e+13,'m^3/(mol*s)'), n=-2.80189, w0=(563,'kJ/mol'), E0=(5.63,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.18615536803375998, var=73.03247311459805, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 17.60000033027513"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 17.60000033027513""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_6BrClFINOPSSi->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 17.60000033027513
""",
)

entry(
    index = 139,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(250000,'m^3/(mol*s)'), n=1.90284e-08, w0=(563,'kJ/mol'), E0=(43.8225,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFINOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_1R!H->C_Ext-2R!H-R_N-6R!H->C_N-6BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 140,
    label = "Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_N-1R!H->C",
    kinetics = ArrheniusBM(A=(5.7209e+06,'m^3/(mol*s)'), n=-4.43934e-09, w0=(679.5,'kJ/mol'), E0=(20.4355,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_N-1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_N-1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 141,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(950165,'m^3/(mol*s)'), n=-0.308952, w0=(573.667,'kJ/mol'), E0=(59.6842,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.0468955394415076, var=6.087958136454598, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 10.089394443732958"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 10.089394443732958""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 10.089394443732958
""",
)

entry(
    index = 142,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(352958,'m^3/(mol*s)'), n=0.197935, w0=(551.5,'kJ/mol'), E0=(87.5784,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03699330182848172, var=5.1442180855320405, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 4.639861317172213"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.639861317172213""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.639861317172213
""",
)

entry(
    index = 143,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(513434,'m^3/(mol*s)'), n=0.224022, w0=(551.5,'kJ/mol'), E0=(96.3318,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05606756913246103, var=6.684355600619972, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 5.323939566736375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C
Total Standard Deviation in ln(k): 5.323939566736375""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C
Total Standard Deviation in ln(k): 5.323939566736375
""",
)

entry(
    index = 144,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(300000,'m^3/(mol*s)'), n=-2.50635e-09, w0=(551.5,'kJ/mol'), E0=(63.4442,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_6R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 145,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(300000,'m^3/(mol*s)'), n=-1.83134e-09, w0=(551.5,'kJ/mol'), E0=(62.2666,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_Ext-2R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_1R!H->C",
    kinetics = ArrheniusBM(A=(2.6e+09,'m^3/(mol*s)'), n=-1.26, w0=(551.5,'kJ/mol'), E0=(36.7181,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 147,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_N-1R!H->C",
    kinetics = ArrheniusBM(A=(1.2e+06,'m^3/(mol*s)'), n=-0.34, w0=(684.5,'kJ/mol'), E0=(61.3041,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_N-1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_N-1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Root_4R->C",
    kinetics = ArrheniusBM(A=(24.011,'m^3/(mol*s)'), n=1.51053, w0=(549.943,'kJ/mol'), E0=(72.7497,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08451911009736333, var=0.900688634295015, Tref=1000.0, N=35, data_mean=0.0, correlation='Root_4R->C',), comment="""BM rule fitted to 35 training reactions at node Root_4R->C
    Total Standard Deviation in ln(k): 2.1149457217623198"""),
    rank = 11,
    shortDesc = """BM rule fitted to 35 training reactions at node Root_4R->C
Total Standard Deviation in ln(k): 2.1149457217623198""",
    longDesc = 
"""
BM rule fitted to 35 training reactions at node Root_4R->C
Total Standard Deviation in ln(k): 2.1149457217623198
""",
)

entry(
    index = 149,
    label = "Root_4R->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(404827,'m^3/(mol*s)'), n=-0.0145807, w0=(537.647,'kJ/mol'), E0=(54.5519,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07290748688481896, var=0.8966320172176512, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R',), comment="""BM rule fitted to 17 training reactions at node Root_4R->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 2.0814814191612334"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.0814814191612334""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_4R->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.0814814191612334
""",
)

entry(
    index = 150,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1",
    kinetics = ArrheniusBM(A=(463468,'m^3/(mol*s)'), n=-0.0491774, w0=(537.562,'kJ/mol'), E0=(45.5477,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0483137282522932, var=0.6790439882299287, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1',), comment="""BM rule fitted to 16 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1
    Total Standard Deviation in ln(k): 1.7733756840516555"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1
Total Standard Deviation in ln(k): 1.7733756840516555""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1
Total Standard Deviation in ln(k): 1.7733756840516555
""",
)

entry(
    index = 151,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(7.36349e+07,'m^3/(mol*s)'), n=-0.723491, w0=(539,'kJ/mol'), E0=(78.3056,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.002702652215404856, var=0.35574106651318294, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H',), comment="""BM rule fitted to 14 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.2024954333401863"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.2024954333401863""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.2024954333401863
""",
)

entry(
    index = 152,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C",
    kinetics = ArrheniusBM(A=(1.81174e+07,'m^3/(mol*s)'), n=-0.352333, w0=(539,'kJ/mol'), E0=(89.4175,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.673043938742877, var=1.6020192393455173, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C
    Total Standard Deviation in ln(k): 4.228476376394494"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 4.228476376394494""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 4.228476376394494
""",
)

entry(
    index = 153,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H",
    kinetics = ArrheniusBM(A=(8.32046e+06,'m^3/(mol*s)'), n=-0.32, w0=(539,'kJ/mol'), E0=(51.5134,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.305460834090209e-17, var=0.8378904353806397, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H
    Total Standard Deviation in ln(k): 1.835061424603026"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H
Total Standard Deviation in ln(k): 1.835061424603026""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H
Total Standard Deviation in ln(k): 1.835061424603026
""",
)

entry(
    index = 154,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(6.02e+06,'m^3/(mol*s)'), n=-0.32, w0=(539,'kJ/mol'), E0=(73.0485,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_Sp-5C-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 155,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_N-Sp-5C-1R!H",
    kinetics = ArrheniusBM(A=(3.01e+06,'m^3/(mol*s)'), n=-5.07736e-08, w0=(539,'kJ/mol'), E0=(97.3172,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_N-Sp-5C-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_N-Sp-5C-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_N-Sp-5C-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_5R!H->C_N-Sp-5C-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 156,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C",
    kinetics = ArrheniusBM(A=(9.04475e+06,'m^3/(mol*s)'), n=-0.517587, w0=(539,'kJ/mol'), E0=(61.3831,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01629722331436013, var=0.13100754226385294, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C',), comment="""BM rule fitted to 11 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C
    Total Standard Deviation in ln(k): 0.7665609378487975"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 0.7665609378487975""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 0.7665609378487975
""",
)

entry(
    index = 157,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(6.5e+06,'m^3/(mol*s)'), n=-0.5, w0=(539,'kJ/mol'), E0=(54.1226,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.037035007078573774, var=0.006857958746550191, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 0.25907049334006665"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.25907049334006665""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 0.25907049334006665
""",
)

entry(
    index = 158,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(6.5e+06,'m^3/(mol*s)'), n=-0.5, w0=(539,'kJ/mol'), E0=(55.4061,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04415753715576519, var=0.005849664262988705, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 0.26427693498815824"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.26427693498815824""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.26427693498815824
""",
)

entry(
    index = 159,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(6.5e+06,'m^3/(mol*s)'), n=-0.5, w0=(539,'kJ/mol'), E0=(53.2409,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 160,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(9.19239e+06,'m^3/(mol*s)'), n=-0.5, w0=(539,'kJ/mol'), E0=(60.5466,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.010398873315128784, var=0.3447320429486115, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.2031856938026997"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.2031856938026997""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.2031856938026997
""",
)

entry(
    index = 161,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(9.19239e+06,'m^3/(mol*s)'), n=-0.5, w0=(539,'kJ/mol'), E0=(59.8495,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.749829501362376e-16, var=0.9609060278364042, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.9651578851126517"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.9651578851126517""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_Sp-2R!H-1R!H_N-5R!H->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.9651578851126517
""",
)

entry(
    index = 162,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(5.78471e+08,'m^3/(mol*s)'), n=-0.622949, w0=(527.5,'kJ/mol'), E0=(86.368,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07452347523879468, var=1.1867418982987987, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 2.371156875177686"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.371156875177686""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.371156875177686
""",
)

entry(
    index = 163,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_5R!H->C",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=-3.66973e-09, w0=(527.5,'kJ/mol'), E0=(79.399,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 164,
    label = "Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_N-5R!H->C",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=-8.85926e-10, w0=(527.5,'kJ/mol'), E0=(75.7495,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_4C-u1_N-Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 165,
    label = "Root_4R->C_Ext-1R!H-R_N-4C-u1",
    kinetics = ArrheniusBM(A=(1.81e+06,'m^3/(mol*s)'), n=8.75878e-09, w0=(539,'kJ/mol'), E0=(75.9553,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_Ext-1R!H-R_N-4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_N-4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_Ext-1R!H-R_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 166,
    label = "Root_4R->C_2R!H->C",
    kinetics = ArrheniusBM(A=(42.5674,'m^3/(mol*s)'), n=1.42312, w0=(560.045,'kJ/mol'), E0=(57.3194,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.506238399393772, var=1.9125601475850922, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_4R->C_2R!H->C',), comment="""BM rule fitted to 11 training reactions at node Root_4R->C_2R!H->C
    Total Standard Deviation in ln(k): 4.044410998479461"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_4R->C_2R!H->C
Total Standard Deviation in ln(k): 4.044410998479461""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_4R->C_2R!H->C
Total Standard Deviation in ln(k): 4.044410998479461
""",
)

entry(
    index = 167,
    label = "Root_4R->C_2R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.09946e+07,'m^3/(mol*s)'), n=-0.4, w0=(536.7,'kJ/mol'), E0=(47.8814,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.4636061643243945e-08, var=3.947898544578107, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_4R->C_2R!H->C_Ext-2C-R',), comment="""BM rule fitted to 5 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 3.983272198526303"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 3.983272198526303""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 3.983272198526303
""",
)

entry(
    index = 168,
    label = "Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H",
    kinetics = ArrheniusBM(A=(1.12583e+07,'m^3/(mol*s)'), n=-0.5, w0=(539,'kJ/mol'), E0=(64.4613,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01853765538601409, var=0.8440005041450588, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H
    Total Standard Deviation in ln(k): 1.8883171167316248"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H
Total Standard Deviation in ln(k): 1.8883171167316248""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H
Total Standard Deviation in ln(k): 1.8883171167316248
""",
)

entry(
    index = 169,
    label = "Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.12583e+07,'m^3/(mol*s)'), n=-0.5, w0=(539,'kJ/mol'), E0=(63.5161,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=2.413897921625164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H_Ext-2C-R
    Total Standard Deviation in ln(k): 3.1147015559000413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H_Ext-2C-R
Total Standard Deviation in ln(k): 3.1147015559000413""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_Sp-2C-1R!H_Ext-2C-R
Total Standard Deviation in ln(k): 3.1147015559000413
""",
)

entry(
    index = 170,
    label = "Root_4R->C_2R!H->C_Ext-2C-R_N-Sp-2C-1R!H",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=1.85753e-08, w0=(527.5,'kJ/mol'), E0=(62.5712,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_2R!H->C_Ext-2C-R_N-Sp-2C-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_N-Sp-2C-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_N-Sp-2C-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_Ext-2C-R_N-Sp-2C-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_4R->C_2R!H->C_1R!H->N",
    kinetics = ArrheniusBM(A=(34.41,'m^3/(mol*s)'), n=1.44661, w0=(544,'kJ/mol'), E0=(57.9458,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24762880986911356, var=0.9900765533613013, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_2R!H->C_1R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_1R!H->N
    Total Standard Deviation in ln(k): 2.6169462757920474"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_1R!H->N
Total Standard Deviation in ln(k): 2.6169462757920474""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_1R!H->N
Total Standard Deviation in ln(k): 2.6169462757920474
""",
)

entry(
    index = 172,
    label = "Root_4R->C_2R!H->C_1R!H->N_Sp-2C-1N",
    kinetics = ArrheniusBM(A=(18.8014,'m^3/(mol*s)'), n=1.56341, w0=(553.5,'kJ/mol'), E0=(68.4458,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_2R!H->C_1R!H->N_Sp-2C-1N',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_1R!H->N_Sp-2C-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_1R!H->N_Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_1R!H->N_Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 173,
    label = "Root_4R->C_2R!H->C_1R!H->N_N-Sp-2C-1N",
    kinetics = ArrheniusBM(A=(62.9763,'m^3/(mol*s)'), n=1.32982, w0=(534.5,'kJ/mol'), E0=(86.1655,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_2R!H->C_1R!H->N_N-Sp-2C-1N',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_1R!H->N_N-Sp-2C-1N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_1R!H->N_N-Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_1R!H->N_N-Sp-2C-1N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 174,
    label = "Root_4R->C_2R!H->C_N-1R!H->N",
    kinetics = ArrheniusBM(A=(7.10064e+07,'m^3/(mol*s)'), n=-0.043836, w0=(597.25,'kJ/mol'), E0=(79.0211,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.087015757721871, var=17.691032253648252, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N
    Total Standard Deviation in ln(k): 13.67581601781805"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N
Total Standard Deviation in ln(k): 13.67581601781805""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N
Total Standard Deviation in ln(k): 13.67581601781805
""",
)

entry(
    index = 175,
    label = "Root_4R->C_2R!H->C_N-1R!H->N_1CO->C",
    kinetics = ArrheniusBM(A=(8.17922e+07,'m^3/(mol*s)'), n=-0.339002, w0=(539,'kJ/mol'), E0=(78.2973,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.4653392506655262e-09, var=14.71777592319898, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N_1CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C
    Total Standard Deviation in ln(k): 7.690916265762756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C
Total Standard Deviation in ln(k): 7.690916265762756""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C
Total Standard Deviation in ln(k): 7.690916265762756
""",
)

entry(
    index = 176,
    label = "Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_4C-u1",
    kinetics = ArrheniusBM(A=(2.19e+08,'m^3/(mol*s)'), n=-0.68, w0=(539,'kJ/mol'), E0=(68.0791,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 177,
    label = "Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_N-4C-u1",
    kinetics = ArrheniusBM(A=(3.01e+07,'m^3/(mol*s)'), n=-2.23133e-08, w0=(539,'kJ/mol'), E0=(73.0412,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_N-4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_N-4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_1CO->C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 178,
    label = "Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C",
    kinetics = ArrheniusBM(A=(6.61175e+07,'m^3/(mol*s)'), n=-1.11192e-06, w0=(655.5,'kJ/mol'), E0=(8.23143e-06,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.7507532943869846, var=36.13951493134382, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C
    Total Standard Deviation in ln(k): 21.475698718372133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C
Total Standard Deviation in ln(k): 21.475698718372133""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C
Total Standard Deviation in ln(k): 21.475698718372133
""",
)

entry(
    index = 179,
    label = "Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_4C-u1",
    kinetics = ArrheniusBM(A=(8.49e+07,'m^3/(mol*s)'), n=-4.92282e-10, w0=(655.5,'kJ/mol'), E0=(74.5564,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 180,
    label = "Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_N-4C-u1",
    kinetics = ArrheniusBM(A=(1.21e+06,'m^3/(mol*s)'), n=-2.2712e-10, w0=(655.5,'kJ/mol'), E0=(79.5863,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_N-4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_N-4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_2R!H->C_N-1R!H->N_N-1CO->C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 181,
    label = "Root_4R->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(20.1675,'m^3/(mol*s)'), n=1.53791, w0=(563.929,'kJ/mol'), E0=(73.4678,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06993186214913955, var=1.1973337792402379, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_4R->C_N-2R!H->C
    Total Standard Deviation in ln(k): 2.369344409307102"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_4R->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.369344409307102""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_4R->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.369344409307102
""",
)

entry(
    index = 182,
    label = "Root_4R->C_N-2R!H->C_1R!H->C",
    kinetics = ArrheniusBM(A=(112.108,'m^3/(mol*s)'), n=1.32982, w0=(553.333,'kJ/mol'), E0=(42.7797,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27273642329866477, var=1.5643108035379913, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_1R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C
    Total Standard Deviation in ln(k): 3.192637894050504"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C
Total Standard Deviation in ln(k): 3.192637894050504""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C
Total Standard Deviation in ln(k): 3.192637894050504
""",
)

entry(
    index = 183,
    label = "Root_4R->C_N-2R!H->C_1R!H->C_Sp-2NO-1C",
    kinetics = ArrheniusBM(A=(184.321,'m^3/(mol*s)'), n=1.32982, w0=(566,'kJ/mol'), E0=(73.1071,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_1R!H->C_Sp-2NO-1C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_Sp-2NO-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_Sp-2NO-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_Sp-2NO-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 184,
    label = "Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C",
    kinetics = ArrheniusBM(A=(87.4311,'m^3/(mol*s)'), n=1.32982, w0=(547,'kJ/mol'), E0=(39.8701,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6167792362419238, var=3.6379267427559188, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C
    Total Standard Deviation in ln(k): 5.373397921060745"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C
Total Standard Deviation in ln(k): 5.373397921060745""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C
Total Standard Deviation in ln(k): 5.373397921060745
""",
)

entry(
    index = 185,
    label = "Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R",
    kinetics = ArrheniusBM(A=(122.881,'m^3/(mol*s)'), n=1.32982, w0=(547,'kJ/mol'), E0=(47.1255,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_1R!H->C_N-Sp-2NO-1C_Ext-2NO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 186,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C",
    kinetics = ArrheniusBM(A=(1.0881,'m^3/(mol*s)'), n=1.89718, w0=(571.875,'kJ/mol'), E0=(74.4635,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24644740285143793, var=0.8652544741729773, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C
    Total Standard Deviation in ln(k): 2.484000220291284"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C
Total Standard Deviation in ln(k): 2.484000220291284""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C
Total Standard Deviation in ln(k): 2.484000220291284
""",
)

entry(
    index = 187,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1",
    kinetics = ArrheniusBM(A=(0.000279549,'m^3/(mol*s)'), n=2.9189, w0=(587.833,'kJ/mol'), E0=(51.918,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1044080256279222, var=0.5013076669601615, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1
    Total Standard Deviation in ln(k): 1.6817459786508275"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1
Total Standard Deviation in ln(k): 1.6817459786508275""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1
Total Standard Deviation in ln(k): 1.6817459786508275
""",
)

entry(
    index = 188,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->O",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(638,'kJ/mol'), E0=(75.3791,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_1NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 189,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O",
    kinetics = ArrheniusBM(A=(9.98847e-05,'m^3/(mol*s)'), n=3.03309, w0=(562.75,'kJ/mol'), E0=(42.462,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07634539848181539, var=1.6540389984846129, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O
    Total Standard Deviation in ln(k): 2.7701013160162598"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O
Total Standard Deviation in ln(k): 2.7701013160162598""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O
Total Standard Deviation in ln(k): 2.7701013160162598
""",
)

entry(
    index = 190,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_2NO->O",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(601.5,'kJ/mol'), E0=(73.041,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 191,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_N-2NO->O",
    kinetics = ArrheniusBM(A=(0.82,'m^3/(mol*s)'), n=1.87, w0=(524,'kJ/mol'), E0=(76.3032,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_2NO-u1_N-1NO->O_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 192,
    label = "Root_4R->C_N-2R!H->C_N-1R!H->C_N-2NO-u1",
    kinetics = ArrheniusBM(A=(0.962303,'m^3/(mol*s)'), n=1.93326, w0=(524,'kJ/mol'), E0=(81.9813,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-2R!H->C_N-1R!H->C_N-2NO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_N-2NO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-2R!H->C_N-1R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 193,
    label = "Root_N-4R->C",
    kinetics = ArrheniusBM(A=(778.48,'m^3/(mol*s)'), n=1.29521, w0=(577.391,'kJ/mol'), E0=(50.4403,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.047862890143580535, var=1.159083637992692, Tref=1000.0, N=110, data_mean=0.0, correlation='Root_N-4R->C',), comment="""BM rule fitted to 110 training reactions at node Root_N-4R->C
    Total Standard Deviation in ln(k): 2.278571271621093"""),
    rank = 11,
    shortDesc = """BM rule fitted to 110 training reactions at node Root_N-4R->C
Total Standard Deviation in ln(k): 2.278571271621093""",
    longDesc = 
"""
BM rule fitted to 110 training reactions at node Root_N-4R->C
Total Standard Deviation in ln(k): 2.278571271621093
""",
)

entry(
    index = 194,
    label = "Root_N-4R->C_4BrClFHNOS->N",
    kinetics = ArrheniusBM(A=(136.757,'m^3/(mol*s)'), n=1.34862, w0=(569.125,'kJ/mol'), E0=(45.1193,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08800991870086565, var=0.3423856254750912, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->C_4BrClFHNOS->N
    Total Standard Deviation in ln(k): 1.394175660510808"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->C_4BrClFHNOS->N
Total Standard Deviation in ln(k): 1.394175660510808""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->C_4BrClFHNOS->N
Total Standard Deviation in ln(k): 1.394175660510808
""",
)

entry(
    index = 195,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1",
    kinetics = ArrheniusBM(A=(124.61,'m^3/(mol*s)'), n=1.35269, w0=(577.357,'kJ/mol'), E0=(43.7201,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.055263163933237616, var=0.37095305930661016, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1
    Total Standard Deviation in ln(k): 1.3598544311803422"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1
Total Standard Deviation in ln(k): 1.3598544311803422""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1
Total Standard Deviation in ln(k): 1.3598544311803422
""",
)

entry(
    index = 196,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(161.65,'m^3/(mol*s)'), n=1.38035, w0=(534.5,'kJ/mol'), E0=(49.4466,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 197,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(141.823,'m^3/(mol*s)'), n=1.33331, w0=(581.125,'kJ/mol'), E0=(43.595,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11912727995058463, var=0.9746780790729097, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 2.2785052330145694"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.2785052330145694""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.2785052330145694
""",
)

entry(
    index = 198,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N",
    kinetics = ArrheniusBM(A=(81.7183,'m^3/(mol*s)'), n=1.38035, w0=(550.25,'kJ/mol'), E0=(32.2847,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04484721154263356, var=4.276015599405756, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N
    Total Standard Deviation in ln(k): 4.258178671495467"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N
Total Standard Deviation in ln(k): 4.258178671495467""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N
Total Standard Deviation in ln(k): 4.258178671495467
""",
)

entry(
    index = 199,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->O",
    kinetics = ArrheniusBM(A=(161.65,'m^3/(mol*s)'), n=1.38035, w0=(589,'kJ/mol'), E0=(43.0021,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 200,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->O",
    kinetics = ArrheniusBM(A=(41.3107,'m^3/(mol*s)'), n=1.38035, w0=(511.5,'kJ/mol'), E0=(54.2096,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->N_N-2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 201,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N",
    kinetics = ArrheniusBM(A=(1271.49,'m^3/(mol*s)'), n=1.08195, w0=(612,'kJ/mol'), E0=(51.7396,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2073146576044246, var=0.33755186616424865, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N
    Total Standard Deviation in ln(k): 1.685626421260492"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N
Total Standard Deviation in ln(k): 1.685626421260492""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N
Total Standard Deviation in ln(k): 1.685626421260492
""",
)

entry(
    index = 202,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->O",
    kinetics = ArrheniusBM(A=(82.6213,'m^3/(mol*s)'), n=1.38035, w0=(598.5,'kJ/mol'), E0=(32.3727,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->O",
    kinetics = ArrheniusBM(A=(161.65,'m^3/(mol*s)'), n=1.38035, w0=(625.5,'kJ/mol'), E0=(50.4947,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->N_N-2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 204,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(82.6213,'m^3/(mol*s)'), n=1.38035, w0=(591.25,'kJ/mol'), E0=(84.1271,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7010492983984208, var=1.1372715824764088, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 3.8993387459907876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 3.8993387459907876""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 3.8993387459907876
""",
)

entry(
    index = 205,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C",
    kinetics = ArrheniusBM(A=(82.6213,'m^3/(mol*s)'), n=1.38035, w0=(534.5,'kJ/mol'), E0=(80.0046,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 206,
    label = "Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C",
    kinetics = ArrheniusBM(A=(82.6213,'m^3/(mol*s)'), n=1.38035, w0=(648,'kJ/mol'), E0=(115.53,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 207,
    label = "Root_N-4R->C_4BrClFHNOS->N_N-2R!H-u1",
    kinetics = ArrheniusBM(A=(161.65,'m^3/(mol*s)'), n=1.38035, w0=(511.5,'kJ/mol'), E0=(83.4051,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_4BrClFHNOS->N_N-2R!H-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_N-2R!H-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_4BrClFHNOS->N_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 208,
    label = "Root_N-4R->C_N-4BrClFHNOS->N",
    kinetics = ArrheniusBM(A=(1088.93,'m^3/(mol*s)'), n=1.29773, w0=(578.039,'kJ/mol'), E0=(43.7525,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.039685913389855436, var=0.6716253375146022, Tref=1000.0, N=102, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N',), comment="""BM rule fitted to 102 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N
    Total Standard Deviation in ln(k): 1.7426488938043392"""),
    rank = 11,
    shortDesc = """BM rule fitted to 102 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N
Total Standard Deviation in ln(k): 1.7426488938043392""",
    longDesc = 
"""
BM rule fitted to 102 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N
Total Standard Deviation in ln(k): 1.7426488938043392
""",
)

entry(
    index = 209,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O",
    kinetics = ArrheniusBM(A=(369.642,'m^3/(mol*s)'), n=1.46442, w0=(674.25,'kJ/mol'), E0=(33.0806,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.27022583670358724, var=1.7883781224145792, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O
    Total Standard Deviation in ln(k): 3.3598967289041113"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O
Total Standard Deviation in ln(k): 3.3598967289041113""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O
Total Standard Deviation in ln(k): 3.3598967289041113
""",
)

entry(
    index = 210,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_4BrClFHO->Cl",
    kinetics = ArrheniusBM(A=(4e+08,'m^3/(mol*s)'), n=8.04636e-09, w0=(664,'kJ/mol'), E0=(72.8134,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_4BrClFHO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_4BrClFHO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_4BrClFHO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_4BrClFHO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 211,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl",
    kinetics = ArrheniusBM(A=(367.482,'m^3/(mol*s)'), n=1.46504, w0=(675.714,'kJ/mol'), E0=(26.9824,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24920567325644633, var=1.6878531172378077, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl
    Total Standard Deviation in ln(k): 3.230644624092469"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl
Total Standard Deviation in ln(k): 3.230644624092469""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl
Total Standard Deviation in ln(k): 3.230644624092469
""",
)

entry(
    index = 212,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C",
    kinetics = ArrheniusBM(A=(7.34947e+07,'m^3/(mol*s)'), n=-3.29864e-08, w0=(689.375,'kJ/mol'), E0=(56.2092,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0757018353593837, var=3.35039055635274, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C
    Total Standard Deviation in ln(k): 6.372249971411763"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C
Total Standard Deviation in ln(k): 6.372249971411763""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C
Total Standard Deviation in ln(k): 6.372249971411763
""",
)

entry(
    index = 213,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1",
    kinetics = ArrheniusBM(A=(5.06938e+07,'m^3/(mol*s)'), n=-0.091178, w0=(692.667,'kJ/mol'), E0=(85.211,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09261469988876483, var=0.07745015669486155, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1
    Total Standard Deviation in ln(k): 0.7906153818261958"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1
Total Standard Deviation in ln(k): 0.7906153818261958""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1
Total Standard Deviation in ln(k): 0.7906153818261958
""",
)

entry(
    index = 214,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_4BrFHO->F",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=1.14338e-08, w0=(732.5,'kJ/mol'), E0=(103.671,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_4BrFHO->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_4BrFHO->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_4BrFHO->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_4BrFHO->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 215,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F",
    kinetics = ArrheniusBM(A=(4.36325e+07,'m^3/(mol*s)'), n=-0.0854631, w0=(672.75,'kJ/mol'), E0=(81.6531,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1613544019821038, var=0.0012625479799301582, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F
    Total Standard Deviation in ln(k): 0.4766460210869688"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F
Total Standard Deviation in ln(k): 0.4766460210869688""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F
Total Standard Deviation in ln(k): 0.4766460210869688
""",
)

entry(
    index = 216,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F_4HO->O",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=3.4192e-08, w0=(679.5,'kJ/mol'), E0=(87.3823,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F_4HO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F_4HO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F_4HO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F_4HO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 217,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F_N-4HO->O",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=7.60838e-09, w0=(666,'kJ/mol'), E0=(73.8058,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F_N-4HO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F_N-4HO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F_N-4HO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_4BrFHO-u1_N-4BrFHO->F_N-4HO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 218,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_N-4BrFHO-u1",
    kinetics = ArrheniusBM(A=(9.04e+07,'m^3/(mol*s)'), n=-1.08754e-08, w0=(679.5,'kJ/mol'), E0=(72.5741,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_N-4BrFHO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_N-4BrFHO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_N-4BrFHO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_2R!H->C_N-4BrFHO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 219,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C",
    kinetics = ArrheniusBM(A=(332.977,'m^3/(mol*s)'), n=1.47687, w0=(657.5,'kJ/mol'), E0=(41.0926,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.017984133491701006, var=0.8031311680399617, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C
    Total Standard Deviation in ln(k): 1.8417814426288217"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C
Total Standard Deviation in ln(k): 1.8417814426288217""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C
Total Standard Deviation in ln(k): 1.8417814426288217
""",
)

entry(
    index = 220,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O",
    kinetics = ArrheniusBM(A=(583.069,'m^3/(mol*s)'), n=1.37285, w0=(662,'kJ/mol'), E0=(21.146,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15008766068901996, var=2.970766180295433, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O
    Total Standard Deviation in ln(k): 3.832448154368889"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O
Total Standard Deviation in ln(k): 3.832448154368889""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O
Total Standard Deviation in ln(k): 3.832448154368889
""",
)

entry(
    index = 221,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O_4O-u1",
    kinetics = ArrheniusBM(A=(252.033,'m^3/(mol*s)'), n=1.42089, w0=(662,'kJ/mol'), E0=(62.1513,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O_4O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O_4O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O_4O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O_4O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 222,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O_N-4O-u1",
    kinetics = ArrheniusBM(A=(1348.91,'m^3/(mol*s)'), n=1.32481, w0=(662,'kJ/mol'), E0=(48.934,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O_N-4O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O_N-4O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O_N-4O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_4BrFHO->O_N-4O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 223,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_N-4BrFHO->O",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(648.5,'kJ/mol'), E0=(58.0465,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_N-4BrFHO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_N-4BrFHO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_N-4BrFHO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-2R!H->C_N-4BrFHO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 224,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O",
    kinetics = ArrheniusBM(A=(1306.3,'m^3/(mol*s)'), n=1.27134, w0=(569.851,'kJ/mol'), E0=(47.4861,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03612290327038427, var=0.7216043241553365, Tref=1000.0, N=94, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O',), comment="""BM rule fitted to 94 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O
    Total Standard Deviation in ln(k): 1.7937293206763996"""),
    rank = 11,
    shortDesc = """BM rule fitted to 94 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O
Total Standard Deviation in ln(k): 1.7937293206763996""",
    longDesc = 
"""
BM rule fitted to 94 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O
Total Standard Deviation in ln(k): 1.7937293206763996
""",
)

entry(
    index = 225,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl",
    kinetics = ArrheniusBM(A=(3.33953e+09,'m^3/(mol*s)'), n=-0.656021, w0=(551.367,'kJ/mol'), E0=(85.8741,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12829630917955775, var=1.5972657667064218, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl',), comment="""BM rule fitted to 15 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl
    Total Standard Deviation in ln(k): 2.855996470190777"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl
Total Standard Deviation in ln(k): 2.855996470190777""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl
Total Standard Deviation in ln(k): 2.855996470190777
""",
)

entry(
    index = 226,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.12269e+07,'m^3/(mol*s)'), n=-0.0292851, w0=(545.2,'kJ/mol'), E0=(62.8135,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.061250275675480415, var=1.1618367304909276, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.3147696451280253"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.3147696451280253""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.3147696451280253
""",
)

entry(
    index = 227,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_5R!H->O",
    kinetics = ArrheniusBM(A=(3.66667e+07,'m^3/(mol*s)'), n=-1.86025e-09, w0=(547.5,'kJ/mol'), E0=(59.8102,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 228,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(7.3276e+08,'m^3/(mol*s)'), n=-0.568755, w0=(544.944,'kJ/mol'), E0=(77.4793,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11555422701164063, var=0.9541728384093751, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O
    Total Standard Deviation in ln(k): 2.248597981090442"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O
Total Standard Deviation in ln(k): 2.248597981090442""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O
Total Standard Deviation in ln(k): 2.248597981090442
""",
)

entry(
    index = 229,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.10064e+07,'m^3/(mol*s)'), n=1.00526e-07, w0=(547.5,'kJ/mol'), E0=(50.54,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2059859864551167e-08, var=0.6944264694749787, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.6705909736252742"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.6705909736252742""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.6705909736252742
""",
)

entry(
    index = 230,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1.41421e+07,'m^3/(mol*s)'), n=-9.89949e-08, w0=(547.5,'kJ/mol'), E0=(45.6403,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.263211790127127e-10, var=0.960906009528041, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 1.965157868467531"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R
Total Standard Deviation in ln(k): 1.965157868467531""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R
Total Standard Deviation in ln(k): 1.965157868467531
""",
)

entry(
    index = 231,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=2.61403e-08, w0=(547.5,'kJ/mol'), E0=(59.4248,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 232,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(7.53121e+06,'m^3/(mol*s)'), n=0.00112828, w0=(547.5,'kJ/mol'), E0=(67.1967,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0018949510213299918, var=1.434965409410206, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 2.4062341689580746"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 2.4062341689580746""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 2.4062341689580746
""",
)

entry(
    index = 233,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1.41422e+07,'m^3/(mol*s)'), n=-2.17951e-07, w0=(547.5,'kJ/mol'), E0=(49.238,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.4047458309616576e-10, var=0.9609060180753904, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R
    Total Standard Deviation in ln(k): 1.9651578757356867"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 1.9651578757356867""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 1.9651578757356867
""",
)

entry(
    index = 234,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=1.5748e-08, w0=(547.5,'kJ/mol'), E0=(63.1404,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 235,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(3.9176e+12,'m^3/(mol*s)'), n=-1.70261, w0=(536,'kJ/mol'), E0=(90.6112,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04674064237088943, var=4.884045523601987, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 4.547878612585423"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 4.547878612585423""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 4.547878612585423
""",
)

entry(
    index = 236,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=5.43144e-09, w0=(536,'kJ/mol'), E0=(52.7984,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 237,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(2.15443e+07,'m^3/(mol*s)'), n=3.11314e-07, w0=(543.667,'kJ/mol'), E0=(-2.48854e-06,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03213819095416457, var=4.2015243673812535, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R
    Total Standard Deviation in ln(k): 4.18997905936483"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R
Total Standard Deviation in ln(k): 4.18997905936483""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R
Total Standard Deviation in ln(k): 4.18997905936483
""",
)

entry(
    index = 238,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=1.59453e-09, w0=(547.5,'kJ/mol'), E0=(67.3436,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=6.195859365858086e-10, var=5.332371188787123e-18, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 6.1860683047245515e-09"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 6.1860683047245515e-09""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 6.1860683047245515e-09
""",
)

entry(
    index = 239,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=-1.25732e-08, w0=(547.5,'kJ/mol'), E0=(67.4112,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 240,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=2.99823e-08, w0=(536,'kJ/mol'), E0=(61.626,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 241,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_2R!H->C",
    kinetics = ArrheniusBM(A=(6e+07,'m^3/(mol*s)'), n=1.25176e-08, w0=(547.5,'kJ/mol'), E0=(66.3696,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 242,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.33333e+08,'m^3/(mol*s)'), n=-1.78203e-08, w0=(640,'kJ/mol'), E0=(80.5154,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 243,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl",
    kinetics = ArrheniusBM(A=(1297.12,'m^3/(mol*s)'), n=1.2723, w0=(573.361,'kJ/mol'), E0=(47.4912,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03656474406255658, var=0.7199869424714758, Tref=1000.0, N=79, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl',), comment="""BM rule fitted to 79 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl
    Total Standard Deviation in ln(k): 1.7929299125394802"""),
    rank = 11,
    shortDesc = """BM rule fitted to 79 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl
Total Standard Deviation in ln(k): 1.7929299125394802""",
    longDesc = 
"""
BM rule fitted to 79 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl
Total Standard Deviation in ln(k): 1.7929299125394802
""",
)

entry(
    index = 244,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1",
    kinetics = ArrheniusBM(A=(740.831,'m^3/(mol*s)'), n=1.33202, w0=(572.735,'kJ/mol'), E0=(39.9652,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03902041912896311, var=0.9139756585933148, Tref=1000.0, N=66, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1',), comment="""BM rule fitted to 66 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1
    Total Standard Deviation in ln(k): 2.014609569729501"""),
    rank = 11,
    shortDesc = """BM rule fitted to 66 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1
Total Standard Deviation in ln(k): 2.014609569729501""",
    longDesc = 
"""
BM rule fitted to 66 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1
Total Standard Deviation in ln(k): 2.014609569729501
""",
)

entry(
    index = 245,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F",
    kinetics = ArrheniusBM(A=(2.61215e+07,'m^3/(mol*s)'), n=-0.0690593, w0=(619.889,'kJ/mol'), E0=(98.9457,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.012965273460728666, var=0.42003872809845844, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F
    Total Standard Deviation in ln(k): 1.3318527833847555"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F
Total Standard Deviation in ln(k): 1.3318527833847555""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F
Total Standard Deviation in ln(k): 1.3318527833847555
""",
)

entry(
    index = 246,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(2.8736e+10,'m^3/(mol*s)'), n=-0.962138, w0=(608.333,'kJ/mol'), E0=(117.542,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17517973290637548, var=0.4902836635172774, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R
    Total Standard Deviation in ln(k): 1.8438707710877658"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R
Total Standard Deviation in ln(k): 1.8438707710877658""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R
Total Standard Deviation in ln(k): 1.8438707710877658
""",
)

entry(
    index = 247,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=-9.58632e-09, w0=(616,'kJ/mol'), E0=(95.6409,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 248,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=2.33666e-09, w0=(604.5,'kJ/mol'), E0=(94.9071,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 249,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=2.44196e-08, w0=(604.5,'kJ/mol'), E0=(97.9554,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-1CN-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 250,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.15501e+07,'m^3/(mol*s)'), n=3.63056e-05, w0=(612.167,'kJ/mol'), E0=(98.9457,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05686866589502796, var=1.699074053183515, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.7560288957820798"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.7560288957820798""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.7560288957820798
""",
)

entry(
    index = 251,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(1.43995e+07,'m^3/(mol*s)'), n=0.00242563, w0=(616,'kJ/mol'), E0=(99.9225,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0763871233181978e-09, var=0.9609060372880484, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.9651578974819623"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.9651578974819623""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.9651578974819623
""",
)

entry(
    index = 252,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=-1.88843e-08, w0=(616,'kJ/mol'), E0=(92.5051,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 253,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=-5.03277e-09, w0=(604.5,'kJ/mol'), E0=(91.5406,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 254,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_2R!H->C",
    kinetics = ArrheniusBM(A=(1.41421e+07,'m^3/(mol*s)'), n=2.01847e-08, w0=(604.5,'kJ/mol'), E0=(96.8315,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.7214830848666713e-10, var=0.9609060321609082, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_2R!H->C
    Total Standard Deviation in ln(k): 1.9651578902184808"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_2R!H->C
Total Standard Deviation in ln(k): 1.9651578902184808""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_2R!H->C
Total Standard Deviation in ln(k): 1.9651578902184808
""",
)

entry(
    index = 255,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=-1.29534e-08, w0=(708.5,'kJ/mol'), E0=(111.031,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->F_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 256,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F",
    kinetics = ArrheniusBM(A=(736.578,'m^3/(mol*s)'), n=1.3328, w0=(565.289,'kJ/mol'), E0=(38.8895,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03902956088316832, var=0.9141314583311871, Tref=1000.0, N=57, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F',), comment="""BM rule fitted to 57 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F
    Total Standard Deviation in ln(k): 2.0147958847320973"""),
    rank = 11,
    shortDesc = """BM rule fitted to 57 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F
Total Standard Deviation in ln(k): 2.0147958847320973""",
    longDesc = 
"""
BM rule fitted to 57 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F
Total Standard Deviation in ln(k): 2.0147958847320973
""",
)

entry(
    index = 257,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(41.0823,'m^3/(mol*s)'), n=1.7247, w0=(556.26,'kJ/mol'), E0=(-4.16075,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09111888447019038, var=6.178822189954367, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R',), comment="""BM rule fitted to 25 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 5.212159365365344"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.212159365365344""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.212159365365344
""",
)

entry(
    index = 258,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(123459,'m^3/(mol*s)'), n=0.637833, w0=(561.071,'kJ/mol'), E0=(89.3849,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04646443070779681, var=0.35179651879216745, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN',), comment="""BM rule fitted to 14 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.3058020314218621"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.3058020314218621""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.3058020314218621
""",
)

entry(
    index = 259,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O",
    kinetics = ArrheniusBM(A=(1.17786e+06,'m^3/(mol*s)'), n=0.389032, w0=(563,'kJ/mol'), E0=(100.702,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.019798037294047843, var=0.24093979244798794, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O
    Total Standard Deviation in ln(k): 1.033780420432282"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O
Total Standard Deviation in ln(k): 1.033780420432282""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O
Total Standard Deviation in ln(k): 1.033780420432282
""",
)

entry(
    index = 260,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1.0962e+06,'m^3/(mol*s)'), n=0.397836, w0=(563,'kJ/mol'), E0=(100.359,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02939409830442325, var=0.1724814742321302, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R
    Total Standard Deviation in ln(k): 0.9064388183768929"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R
Total Standard Deviation in ln(k): 0.9064388183768929""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R
Total Standard Deviation in ln(k): 0.9064388183768929
""",
)

entry(
    index = 261,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1132.27,'m^3/(mol*s)'), n=1.22871, w0=(563,'kJ/mol'), E0=(79.5982,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1058048320576809, var=0.12388348619976208, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 0.971449615585132"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 0.971449615585132""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 0.971449615585132
""",
)

entry(
    index = 262,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.2e+07,'m^3/(mol*s)'), n=4.7343e-08, w0=(563,'kJ/mol'), E0=(99.9111,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-1CN-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 263,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.11132e+07,'m^3/(mol*s)'), n=-1.83751e-06, w0=(563,'kJ/mol'), E0=(107.375,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03382356032751249, var=0.9609060273442741, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.0501417045277925"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.0501417045277925""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_Ext-1CN-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.0501417045277925
""",
)

entry(
    index = 264,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F",
    kinetics = ArrheniusBM(A=(3.22232e+06,'m^3/(mol*s)'), n=0.307376, w0=(563,'kJ/mol'), E0=(108.254,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.043731499509550395, var=0.9358344615944323, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F
    Total Standard Deviation in ln(k): 2.049229531843901"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F
Total Standard Deviation in ln(k): 2.049229531843901""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F
Total Standard Deviation in ln(k): 2.049229531843901
""",
)

entry(
    index = 265,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.81028e+07,'m^3/(mol*s)'), n=7.5083e-06, w0=(563,'kJ/mol'), E0=(111.49,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.026494324946853585, var=2.413897885754386, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.181270188403005"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.181270188403005""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_5R!H->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.181270188403005
""",
)

entry(
    index = 266,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_N-5R!H->F",
    kinetics = ArrheniusBM(A=(6.66667e+06,'m^3/(mol*s)'), n=-1.17855e-10, w0=(563,'kJ/mol'), E0=(77.6637,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_4BrHO->O_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 267,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O",
    kinetics = ArrheniusBM(A=(4.47801e+06,'m^3/(mol*s)'), n=0.000177943, w0=(549.5,'kJ/mol'), E0=(68.1314,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.735788089288397e-10, var=5.180580779861975, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O
    Total Standard Deviation in ln(k): 4.562955301704631"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O
Total Standard Deviation in ln(k): 4.562955301704631""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O
Total Standard Deviation in ln(k): 4.562955301704631
""",
)

entry(
    index = 268,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=-4.79388e-09, w0=(549.5,'kJ/mol'), E0=(62.7729,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_Sp-2R!H-1CN_N-4BrHO->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 269,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(2007.44,'m^3/(mol*s)'), n=1.24159, w0=(550.136,'kJ/mol'), E0=(42.5778,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08340636979458585, var=6.418723189434626, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 5.28859999784322"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 5.28859999784322""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 5.28859999784322
""",
)

entry(
    index = 270,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl",
    kinetics = ArrheniusBM(A=(3.53553e+06,'m^3/(mol*s)'), n=2.19588e-08, w0=(551.5,'kJ/mol'), E0=(49.3379,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.3802249398732633e-10, var=0.9609060280094611, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl
    Total Standard Deviation in ln(k): 1.9651578858876562"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl
Total Standard Deviation in ln(k): 1.9651578858876562""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl
Total Standard Deviation in ln(k): 1.9651578858876562
""",
)

entry(
    index = 271,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=7.02546e-09, w0=(551.5,'kJ/mol'), E0=(67.4806,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_5R!H->Cl_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 272,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(1988.48,'m^3/(mol*s)'), n=1.24316, w0=(549.833,'kJ/mol'), E0=(42.4132,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08266119051449551, var=6.457713872904693, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl
    Total Standard Deviation in ln(k): 5.302130694025698"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl
Total Standard Deviation in ln(k): 5.302130694025698""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl
Total Standard Deviation in ln(k): 5.302130694025698
""",
)

entry(
    index = 273,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O",
    kinetics = ArrheniusBM(A=(254.888,'m^3/(mol*s)'), n=1.41958, w0=(555.4,'kJ/mol'), E0=(55.9207,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4881063349452077, var=0.9941788183609503, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O
    Total Standard Deviation in ln(k): 3.225289423976324"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O
Total Standard Deviation in ln(k): 3.225289423976324""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O
Total Standard Deviation in ln(k): 3.225289423976324
""",
)

entry(
    index = 274,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=7.95959e-09, w0=(551.5,'kJ/mol'), E0=(62.5769,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3268511269322496e-09, var=4.625125576634905e-18, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R
    Total Standard Deviation in ln(k): 7.645201133632927e-09"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R
Total Standard Deviation in ln(k): 7.645201133632927e-09""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R
Total Standard Deviation in ln(k): 7.645201133632927e-09
""",
)

entry(
    index = 275,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R_5CFO->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=7.14499e-10, w0=(551.5,'kJ/mol'), E0=(64.844,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R_5CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R_5CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R_5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R_5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 276,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R_N-5CFO->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=-1.13706e-08, w0=(551.5,'kJ/mol'), E0=(61.8186,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R_N-5CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R_N-5CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R_N-5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_Ext-1CN-R_N-5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 277,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_2R!H->C",
    kinetics = ArrheniusBM(A=(3.53553e+07,'m^3/(mol*s)'), n=4.315e-09, w0=(551.5,'kJ/mol'), E0=(123.494,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.012004598604129092, var=0.9609060205425632, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_2R!H->C
    Total Standard Deviation in ln(k): 1.995320185704874"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_2R!H->C
Total Standard Deviation in ln(k): 1.995320185704874""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_2R!H->C
Total Standard Deviation in ln(k): 1.995320185704874
""",
)

entry(
    index = 278,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_N-2R!H->C",
    kinetics = ArrheniusBM(A=(252.033,'m^3/(mol*s)'), n=1.42089, w0=(571,'kJ/mol'), E0=(61.1032,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_4BrHO->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 279,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O",
    kinetics = ArrheniusBM(A=(15553.5,'m^3/(mol*s)'), n=1.06652, w0=(542.875,'kJ/mol'), E0=(42.7585,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.632432581783514, var=4.3377845375580995, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O
    Total Standard Deviation in ln(k): 8.276921051710762"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O
Total Standard Deviation in ln(k): 8.276921051710762""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O
Total Standard Deviation in ln(k): 8.276921051710762
""",
)

entry(
    index = 280,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1.63457e+06,'m^3/(mol*s)'), n=0.31162, w0=(538,'kJ/mol'), E0=(75.754,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0012039250975677035, var=0.14229162808105306, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R
    Total Standard Deviation in ln(k): 0.759242333504997"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R
Total Standard Deviation in ln(k): 0.759242333504997""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R
Total Standard Deviation in ln(k): 0.759242333504997
""",
)

entry(
    index = 281,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R_5CFO->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=4.29121e-08, w0=(538,'kJ/mol'), E0=(82.1665,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R_5CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R_5CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R_5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R_5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 282,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R_N-5CFO->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=-7.45103e-08, w0=(538,'kJ/mol'), E0=(78.4617,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R_N-5CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R_N-5CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R_N-5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_Ext-1CN-R_N-5CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 283,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_2R!H->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=8.83049e-09, w0=(538,'kJ/mol'), E0=(61.8294,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 284,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_N-2R!H->C",
    kinetics = ArrheniusBM(A=(15593,'m^3/(mol*s)'), n=1.06688, w0=(557.5,'kJ/mol'), E0=(47.1318,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-2R!H-R_N-Sp-2R!H-1CN_N-5R!H->Cl_N-4BrHO->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 285,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(3.96811e+14,'m^3/(mol*s)'), n=-2.17491, w0=(558.273,'kJ/mol'), E0=(132.989,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.275746692100462, var=0.6119802250926305, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R',), comment="""BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R
    Total Standard Deviation in ln(k): 2.261118395455435"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R
Total Standard Deviation in ln(k): 2.261118395455435""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R
Total Standard Deviation in ln(k): 2.261118395455435
""",
)

entry(
    index = 286,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN",
    kinetics = ArrheniusBM(A=(4.58144e+12,'m^3/(mol*s)'), n=-1.61326, w0=(557.8,'kJ/mol'), E0=(124.23,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20314751278159526, var=0.5189302333920458, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN
    Total Standard Deviation in ln(k): 1.9545681322546287"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN
Total Standard Deviation in ln(k): 1.9545681322546287""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN
Total Standard Deviation in ln(k): 1.9545681322546287
""",
)

entry(
    index = 287,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O",
    kinetics = ArrheniusBM(A=(7.10293e+08,'m^3/(mol*s)'), n=-0.416318, w0=(561.357,'kJ/mol'), E0=(113.641,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0888868182399889, var=0.22593082937040312, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O
    Total Standard Deviation in ln(k): 1.1762280330322579"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O
Total Standard Deviation in ln(k): 1.1762280330322579""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O
Total Standard Deviation in ln(k): 1.1762280330322579
""",
)

entry(
    index = 288,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(5.92242e+07,'m^3/(mol*s)'), n=-0.0737884, w0=(563,'kJ/mol'), E0=(110.962,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04992247684637377, var=0.22704593828074532, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.0806763458355644"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.0806763458355644""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.0806763458355644
""",
)

entry(
    index = 289,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C",
    kinetics = ArrheniusBM(A=(1.70766e+07,'m^3/(mol*s)'), n=8.37992e-08, w0=(563,'kJ/mol'), E0=(62.5849,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=6.982361733112044e-10, var=0.9494595835536717, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C
    Total Standard Deviation in ln(k): 1.9534182059418268"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C
Total Standard Deviation in ln(k): 1.9534182059418268""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C
Total Standard Deviation in ln(k): 1.9534182059418268
""",
)

entry(
    index = 290,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=-4.09701e-08, w0=(563,'kJ/mol'), E0=(85.6548,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 291,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C",
    kinetics = ArrheniusBM(A=(8.38837e+06,'m^3/(mol*s)'), n=0.20989, w0=(563,'kJ/mol'), E0=(113.476,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.007252354772385198, var=0.19974669739845227, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C
    Total Standard Deviation in ln(k): 0.9141988562103135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C
Total Standard Deviation in ln(k): 0.9141988562103135""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C
Total Standard Deviation in ln(k): 0.9141988562103135
""",
)

entry(
    index = 292,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(4.4e+07,'m^3/(mol*s)'), n=1.75726e-08, w0=(563,'kJ/mol'), E0=(115.111,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03619075358142335, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C_Ext-1CN-R
    Total Standard Deviation in ln(k): 0.09093154166186772"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 0.09093154166186772""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_Sp-2R!H-1CN_N-5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 0.09093154166186772
""",
)

entry(
    index = 293,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=-2.43167e-08, w0=(551.5,'kJ/mol'), E0=(76.1,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_4BrHO->O_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 294,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O",
    kinetics = ArrheniusBM(A=(1.48466e+06,'m^3/(mol*s)'), n=1.14661e-08, w0=(549.5,'kJ/mol'), E0=(54.1121,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.2011118793046898e-08, var=0.4209386671949848, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O
    Total Standard Deviation in ln(k): 1.3006678896484658"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O
Total Standard Deviation in ln(k): 1.3006678896484658""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O
Total Standard Deviation in ln(k): 1.3006678896484658
""",
)

entry(
    index = 295,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C",
    kinetics = ArrheniusBM(A=(1.27916e+06,'m^3/(mol*s)'), n=-8.25368e-08, w0=(549.5,'kJ/mol'), E0=(55.4715,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-8.282333202783488e-10, var=0.9639738046065783, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C
    Total Standard Deviation in ln(k): 1.9682923568711375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C
Total Standard Deviation in ln(k): 1.9682923568711375""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C
Total Standard Deviation in ln(k): 1.9682923568711375
""",
)

entry(
    index = 296,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(904000,'m^3/(mol*s)'), n=8.11702e-09, w0=(549.5,'kJ/mol'), E0=(72.3416,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 297,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=3.43541e-10, w0=(549.5,'kJ/mol'), E0=(66.0237,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_Sp-5R!H-1CN_N-4BrHO->O_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 298,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_N-Sp-5R!H-1CN",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=3.55988e-08, w0=(563,'kJ/mol'), E0=(114.157,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_N-Sp-5R!H-1CN',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_N-Sp-5R!H-1CN
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_N-Sp-5R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_Ext-1CN-R_N-Sp-5R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 299,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H",
    kinetics = ArrheniusBM(A=(10284.2,'m^3/(mol*s)'), n=1.07894, w0=(578.65,'kJ/mol'), E0=(67.1751,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02548761570354585, var=0.30341572836647107, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H
    Total Standard Deviation in ln(k): 1.1683111694101072"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H
Total Standard Deviation in ln(k): 1.1683111694101072""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H
Total Standard Deviation in ln(k): 1.1683111694101072
""",
)

entry(
    index = 300,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(64177.8,'m^3/(mol*s)'), n=0.878992, w0=(573.286,'kJ/mol'), E0=(73.9766,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.031756029753733886, var=0.297562729966121, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.1733581858950668"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.1733581858950668""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.1733581858950668
""",
)

entry(
    index = 301,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1",
    kinetics = ArrheniusBM(A=(139450,'m^3/(mol*s)'), n=0.77947, w0=(579.75,'kJ/mol'), E0=(75.2812,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07938820002259513, var=0.5427877980313873, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1
    Total Standard Deviation in ln(k): 1.6764390410292163"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1
Total Standard Deviation in ln(k): 1.6764390410292163""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1
Total Standard Deviation in ln(k): 1.6764390410292163
""",
)

entry(
    index = 302,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C",
    kinetics = ArrheniusBM(A=(23739.9,'m^3/(mol*s)'), n=1.06417, w0=(589.333,'kJ/mol'), E0=(55.4979,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.400717068063205, var=4.767212676184642, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C
    Total Standard Deviation in ln(k): 7.8965176805884845"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C
Total Standard Deviation in ln(k): 7.8965176805884845""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C
Total Standard Deviation in ln(k): 7.8965176805884845
""",
)

entry(
    index = 303,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(3.61e+06,'m^3/(mol*s)'), n=3.07521e-09, w0=(549.5,'kJ/mol'), E0=(67.353,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 304,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(23588.5,'m^3/(mol*s)'), n=1.06552, w0=(609.25,'kJ/mol'), E0=(57.3707,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8765435942543714, var=1.2751169028983975, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 4.466139226800341"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 4.466139226800341""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 4.466139226800341
""",
)

entry(
    index = 305,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C_2NO->O",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=-2.51399e-08, w0=(642,'kJ/mol'), E0=(81.4955,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 306,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C_N-2NO->O",
    kinetics = ArrheniusBM(A=(23389.5,'m^3/(mol*s)'), n=1.06688, w0=(576.5,'kJ/mol'), E0=(73.1134,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_1CN->C_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 307,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C",
    kinetics = ArrheniusBM(A=(9701.16,'m^3/(mol*s)'), n=1.08962, w0=(570.167,'kJ/mol'), E0=(67.3963,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.31631361918853174, var=0.7278827298524121, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C
    Total Standard Deviation in ln(k): 2.5051184901997794"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C
Total Standard Deviation in ln(k): 2.5051184901997794""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C
Total Standard Deviation in ln(k): 2.5051184901997794
""",
)

entry(
    index = 308,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(12994.1,'m^3/(mol*s)'), n=1.06688, w0=(564,'kJ/mol'), E0=(66.4438,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 309,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(26.4236,'m^3/(mol*s)'), n=1.81767, w0=(573.25,'kJ/mol'), E0=(48.6997,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.16252617676288564, var=0.23465306997700014, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 1.3794709921570223"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 1.3794709921570223""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 1.3794709921570223
""",
)

entry(
    index = 310,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C_2NO->O",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(612,'kJ/mol'), E0=(62.1343,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 311,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C_N-2NO->O",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(534.5,'kJ/mol'), E0=(52.8808,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_2R!H-u1_N-1CN->C_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 312,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_N-2R!H-u1",
    kinetics = ArrheniusBM(A=(15593,'m^3/(mol*s)'), n=1.06688, w0=(534.5,'kJ/mol'), E0=(81.0903,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_N-2R!H-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_N-2R!H-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_Sp-2R!H-1CN_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 313,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(7796.49,'m^3/(mol*s)'), n=1.06688, w0=(591.167,'kJ/mol'), E0=(80.9211,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.057011751043032396, var=0.028842858770419186, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 0.4837134814190469"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.4837134814190469""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.4837134814190469
""",
)

entry(
    index = 314,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->C",
    kinetics = ArrheniusBM(A=(7796.49,'m^3/(mol*s)'), n=1.06688, w0=(557.5,'kJ/mol'), E0=(77.6898,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 315,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C",
    kinetics = ArrheniusBM(A=(7796.49,'m^3/(mol*s)'), n=1.06688, w0=(608,'kJ/mol'), E0=(87.5182,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.49507337468596346, var=0.574836626457476, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C
    Total Standard Deviation in ln(k): 2.763852614414684"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 2.763852614414684""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 2.763852614414684
""",
)

entry(
    index = 316,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(7796.49,'m^3/(mol*s)'), n=1.06688, w0=(545,'kJ/mol'), E0=(86.1718,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 317,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(7796.49,'m^3/(mol*s)'), n=1.06688, w0=(671,'kJ/mol'), E0=(113.215,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 318,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H",
    kinetics = ArrheniusBM(A=(188.441,'m^3/(mol*s)'), n=1.42021, w0=(580.682,'kJ/mol'), E0=(51.2818,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0478878818998446, var=0.42326652168253054, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H',), comment="""BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H
    Total Standard Deviation in ln(k): 1.4245806320414967"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H
Total Standard Deviation in ln(k): 1.4245806320414967""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H
Total Standard Deviation in ln(k): 1.4245806320414967
""",
)

entry(
    index = 319,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(215.536,'m^3/(mol*s)'), n=1.4347, w0=(571.688,'kJ/mol'), E0=(59.6376,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17431095829825538, var=0.5766309494250792, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.960287268892163"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.960287268892163""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.960287268892163
""",
)

entry(
    index = 320,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C",
    kinetics = ArrheniusBM(A=(397.05,'m^3/(mol*s)'), n=1.41411, w0=(568.625,'kJ/mol'), E0=(73.9152,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.4804158052411018, var=2.131708491083907, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C
    Total Standard Deviation in ln(k): 6.6466253985494355"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 6.6466253985494355""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 6.6466253985494355
""",
)

entry(
    index = 321,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(9.67138e+11,'m^3/(mol*s)'), n=-1.46326, w0=(538.75,'kJ/mol'), E0=(96.0237,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6656089753303559, var=5.469532786017205, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 6.360864755781332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C
Total Standard Deviation in ln(k): 6.360864755781332""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C
Total Standard Deviation in ln(k): 6.360864755781332
""",
)

entry(
    index = 322,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C_4BrO->O",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=-1.34279e-09, w0=(563,'kJ/mol'), E0=(80.7697,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C_4BrO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C_4BrO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C_4BrO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C_4BrO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 323,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C_N-4BrO->O",
    kinetics = ArrheniusBM(A=(2.37e+06,'m^3/(mol*s)'), n=8.94542e-09, w0=(514.5,'kJ/mol'), E0=(51.4476,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C_N-4BrO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C_N-4BrO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C_N-4BrO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_2R!H->C_N-4BrO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 324,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(382.985,'m^3/(mol*s)'), n=1.41908, w0=(598.5,'kJ/mol'), E0=(63.0061,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4208821242048962, var=1.1578802812670888, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 3.21468486060022"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 3.21468486060022""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 3.21468486060022
""",
)

entry(
    index = 325,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C_2NO->O",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=1.3714e-08, w0=(607,'kJ/mol'), E0=(65.6653,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 326,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C_N-2NO->O",
    kinetics = ArrheniusBM(A=(378.049,'m^3/(mol*s)'), n=1.42089, w0=(590,'kJ/mol'), E0=(87.0848,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_1CN->C_N-2R!H->C_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 327,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C",
    kinetics = ArrheniusBM(A=(211.933,'m^3/(mol*s)'), n=1.42089, w0=(574.75,'kJ/mol'), E0=(52.9829,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18555929312150604, var=0.5929073925262265, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C
    Total Standard Deviation in ln(k): 2.009885012679163"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 2.009885012679163""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 2.009885012679163
""",
)

entry(
    index = 328,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N",
    kinetics = ArrheniusBM(A=(2120.6,'m^3/(mol*s)'), n=1.11273, w0=(548,'kJ/mol'), E0=(85.436,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4957220867214385, var=0.04064125112183595, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N
    Total Standard Deviation in ln(k): 1.6496809649375654"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N
Total Standard Deviation in ln(k): 1.6496809649375654""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N
Total Standard Deviation in ln(k): 1.6496809649375654
""",
)

entry(
    index = 329,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N_2N-u1",
    kinetics = ArrheniusBM(A=(126.016,'m^3/(mol*s)'), n=1.42089, w0=(548,'kJ/mol'), E0=(65.8663,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 330,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N_N-2N-u1",
    kinetics = ArrheniusBM(A=(252.033,'m^3/(mol*s)'), n=1.42089, w0=(548,'kJ/mol'), E0=(95.0617,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_2R!H->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 331,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N",
    kinetics = ArrheniusBM(A=(252.033,'m^3/(mol*s)'), n=1.42089, w0=(601.5,'kJ/mol'), E0=(55.8376,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3952282719518495, var=0.405185312480099, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N
    Total Standard Deviation in ln(k): 2.2691332966063107"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N
Total Standard Deviation in ln(k): 2.2691332966063107""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N
Total Standard Deviation in ln(k): 2.2691332966063107
""",
)

entry(
    index = 332,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N_2CO->C",
    kinetics = ArrheniusBM(A=(252.033,'m^3/(mol*s)'), n=1.42089, w0=(577.5,'kJ/mol'), E0=(80.4152,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N_2CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N_2CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 333,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N_N-2CO->C",
    kinetics = ArrheniusBM(A=(252.033,'m^3/(mol*s)'), n=1.42089, w0=(625.5,'kJ/mol'), E0=(54.6587,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N_N-2CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N_N-2CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N_N-2CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_Sp-2R!H-1CN_N-1CN->C_N-2R!H->N_N-2CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 334,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(126.016,'m^3/(mol*s)'), n=1.42089, w0=(604.667,'kJ/mol'), E0=(93.6128,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03378285749923737, var=0.023580468179042528, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 0.39272732909583924"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.39272732909583924""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.39272732909583924
""",
)

entry(
    index = 335,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->C",
    kinetics = ArrheniusBM(A=(126.016,'m^3/(mol*s)'), n=1.42089, w0=(571,'kJ/mol'), E0=(91.6612,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 336,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C",
    kinetics = ArrheniusBM(A=(126.016,'m^3/(mol*s)'), n=1.42089, w0=(621.5,'kJ/mol'), E0=(100.087,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.46238895372303496, var=0.5351232967112397, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C
    Total Standard Deviation in ln(k): 2.6282875422732004"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 2.6282875422732004""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 2.6282875422732004
""",
)

entry(
    index = 337,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(126.016,'m^3/(mol*s)'), n=1.42089, w0=(558.5,'kJ/mol'), E0=(100.143,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 338,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(126.016,'m^3/(mol*s)'), n=1.42089, w0=(684.5,'kJ/mol'), E0=(127.187,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->F_N-4BrHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 339,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1",
    kinetics = ArrheniusBM(A=(7054.09,'m^3/(mol*s)'), n=1.0841, w0=(576.538,'kJ/mol'), E0=(56.837,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02419518439204284, var=0.34565319208141554, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1',), comment="""BM rule fitted to 13 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1
    Total Standard Deviation in ln(k): 1.2394213350579366"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1
Total Standard Deviation in ln(k): 1.2394213350579366""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1
Total Standard Deviation in ln(k): 1.2394213350579366
""",
)

entry(
    index = 340,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(26310,'m^3/(mol*s)'), n=0.948906, w0=(572.25,'kJ/mol'), E0=(64.2788,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03566210818466407, var=0.3716976012920232, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.3118302734341163"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.3118302734341163""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.3118302734341163
""",
)

entry(
    index = 341,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C",
    kinetics = ArrheniusBM(A=(16831.7,'m^3/(mol*s)'), n=1.06177, w0=(569.75,'kJ/mol'), E0=(73.7328,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11403900742135568, var=0.20491336433261828, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C
    Total Standard Deviation in ln(k): 1.1940207612200657"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 1.1940207612200657""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 1.1940207612200657
""",
)

entry(
    index = 342,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.73205e+07,'m^3/(mol*s)'), n=2.98355e-07, w0=(563,'kJ/mol'), E0=(42.8607,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.850400662220912e-09, var=2.413897915575754, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.1147015616715765"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.1147015616715765""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.1147015616715765
""",
)

entry(
    index = 343,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=1.9444e-08, w0=(563,'kJ/mol'), E0=(61.5494,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 344,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=2.28759e-09, w0=(563,'kJ/mol'), E0=(64.8167,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_1CN->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 345,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C",
    kinetics = ArrheniusBM(A=(14964.5,'m^3/(mol*s)'), n=1.00474, w0=(574.75,'kJ/mol'), E0=(61.1126,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13973654848076847, var=0.3568136002652523, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C
    Total Standard Deviation in ln(k): 1.548602830919053"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 1.548602830919053""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 1.548602830919053
""",
)

entry(
    index = 346,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(10720.2,'m^3/(mol*s)'), n=1.06688, w0=(577.5,'kJ/mol'), E0=(64.9804,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 347,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(9539.22,'m^3/(mol*s)'), n=1.05389, w0=(573.833,'kJ/mol'), E0=(58.9174,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2730453966012547, var=0.6906212917859244, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 2.3520512828456757"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.3520512828456757""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 2.3520512828456757
""",
)

entry(
    index = 348,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1",
    kinetics = ArrheniusBM(A=(323.865,'m^3/(mol*s)'), n=1.46107, w0=(586.75,'kJ/mol'), E0=(41.8876,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.004546882652337396, var=0.219990087425385, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1
    Total Standard Deviation in ln(k): 0.9517072444467146"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1
Total Standard Deviation in ln(k): 0.9517072444467146""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1
Total Standard Deviation in ln(k): 0.9517072444467146
""",
)

entry(
    index = 349,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_2NO->O",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(625.5,'kJ/mol'), E0=(50.71,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 350,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_N-2NO->O",
    kinetics = ArrheniusBM(A=(2160.18,'m^3/(mol*s)'), n=1.18368, w0=(548,'kJ/mol'), E0=(51.4356,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_2NO-u1_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 351,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_N-2NO-u1",
    kinetics = ArrheniusBM(A=(10720.2,'m^3/(mol*s)'), n=1.06688, w0=(548,'kJ/mol'), E0=(79.6269,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_N-2NO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_N-2NO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Sp-2R!H-1CN_N-1CN->C_N-2R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 352,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(5519.78,'m^3/(mol*s)'), n=1.06696, w0=(583.4,'kJ/mol'), E0=(57.8319,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.040831960741316224, var=0.00046822933154973343, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 0.1459725415269507"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.1459725415269507""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.1459725415269507
""",
)

entry(
    index = 353,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.53495e+07,'m^3/(mol*s)'), n=2.08086e-05, w0=(551.5,'kJ/mol'), E0=(88.7899,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.003893619204528533, var=0.960906002441363, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.97494082197028"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.97494082197028""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.97494082197028
""",
)

entry(
    index = 354,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->C",
    kinetics = ArrheniusBM(A=(5522.51,'m^3/(mol*s)'), n=1.06688, w0=(571,'kJ/mol'), E0=(76.2264,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 355,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C",
    kinetics = ArrheniusBM(A=(5522.51,'m^3/(mol*s)'), n=1.06688, w0=(621.5,'kJ/mol'), E0=(86.3737,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4892709302946329, var=0.5624608749369729, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C
    Total Standard Deviation in ln(k): 2.732822962342696"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 2.732822962342696""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 2.732822962342696
""",
)

entry(
    index = 356,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(5522.51,'m^3/(mol*s)'), n=1.06688, w0=(558.5,'kJ/mol'), E0=(84.7084,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 357,
    label = "Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(5522.51,'m^3/(mol*s)'), n=1.06688, w0=(684.5,'kJ/mol'), E0=(111.752,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

