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
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(0.110625,'s^-1'), n=4.12916, w0=(300894,'J/mol'), E0=(27241.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.36282023133735397, var=25.53306712889397, Tref=1000.0, N=374, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 374 training reactions at node Root
    Total Standard Deviation in ln(k): 11.041586172623171"""),
    rank = 11,
    shortDesc = """BM rule fitted to 374 training reactions at node Root
Total Standard Deviation in ln(k): 11.041586172623171""",
    longDesc = 
"""
BM rule fitted to 374 training reactions at node Root
Total Standard Deviation in ln(k): 11.041586172623171
""",
)

entry(
    index = 2,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H",
    kinetics = ArrheniusBM(A=(11997.6,'s^-1'), n=2.63963, w0=(300798,'J/mol'), E0=(-2878.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20024878737488722, var=8.518754855412338, Tref=1000.0, N=84, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H',), comment="""BM rule fitted to 84 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H
    Total Standard Deviation in ln(k): 6.354339095268439"""),
    rank = 11,
    shortDesc = """BM rule fitted to 84 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H
Total Standard Deviation in ln(k): 6.354339095268439""",
    longDesc = 
"""
BM rule fitted to 84 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H
Total Standard Deviation in ln(k): 6.354339095268439
""",
)

entry(
    index = 3,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H",
    kinetics = ArrheniusBM(A=(1.23419e-18,'s^-1'), n=8.88169, w0=(301081,'J/mol'), E0=(-36844.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.021329143829078, var=20.55390546208333, Tref=1000.0, N=74, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H',), comment="""BM rule fitted to 74 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H
    Total Standard Deviation in ln(k): 19.19259226007726"""),
    rank = 11,
    shortDesc = """BM rule fitted to 74 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H
Total Standard Deviation in ln(k): 19.19259226007726""",
    longDesc = 
"""
BM rule fitted to 74 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H
Total Standard Deviation in ln(k): 19.19259226007726
""",
)

entry(
    index = 4,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-=4R!H",
    kinetics = ArrheniusBM(A=(5.33038e+12,'s^-1'), n=1.03998, w0=(297167,'J/mol'), E0=(309803,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=9.350414338450632, var=244.68765359384147, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-=4R!H',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-=4R!H
    Total Standard Deviation in ln(k): 54.852562028908544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-=4R!H
Total Standard Deviation in ln(k): 54.852562028908544""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-=4R!H
Total Standard Deviation in ln(k): 54.852562028908544
""",
)

entry(
    index = 5,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H",
    kinetics = ArrheniusBM(A=(2.98828e+21,'s^-1'), n=-2.24539, w0=(300920,'J/mol'), E0=(100906,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20958850237015758, var=24.989569255409855, Tref=1000.0, N=213, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H',), comment="""BM rule fitted to 213 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H
    Total Standard Deviation in ln(k): 10.548188358164746"""),
    rank = 11,
    shortDesc = """BM rule fitted to 213 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H
Total Standard Deviation in ln(k): 10.548188358164746""",
    longDesc = 
"""
BM rule fitted to 213 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H
Total Standard Deviation in ln(k): 10.548188358164746
""",
)

entry(
    index = 6,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3248.17,'s^-1'), n=2.76626, w0=(301375,'J/mol'), E0=(3096.21,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2888859502721009, var=8.08831579806261, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R',), comment="""BM rule fitted to 16 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 6.427303536094552"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 6.427303536094552""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 6.427303536094552
""",
)

entry(
    index = 7,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.64244e-11,'s^-1'), n=6.80343, w0=(298125,'J/mol'), E0=(-48569.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.063035906849624, var=29.373797893844156, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 21.073815810575734"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 21.073815810575734""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 21.073815810575734
""",
)

entry(
    index = 8,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.10939e-17,'s^-1'), n=8.56173, w0=(300755,'J/mol'), E0=(-58817.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-7.894219466473662, var=22.418055745398398, Tref=1000.0, N=47, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R',), comment="""BM rule fitted to 47 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 29.32668364136823"""),
    rank = 11,
    shortDesc = """BM rule fitted to 47 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 29.32668364136823""",
    longDesc = 
"""
BM rule fitted to 47 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 29.32668364136823
""",
)

entry(
    index = 9,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.30367e+09,'s^-1'), n=1.25528, w0=(301000,'J/mol'), E0=(21530.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0714272133604483, var=2.658937336286014, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 3.4484361550181504"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.4484361550181504""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.4484361550181504
""",
)

entry(
    index = 10,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H",
    kinetics = ArrheniusBM(A=(4.13352e-19,'s^-1'), n=9.03355, w0=(301085,'J/mol'), E0=(-42432.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.639240346195301, var=18.463250620226685, Tref=1000.0, N=71, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H',), comment="""BM rule fitted to 71 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H
    Total Standard Deviation in ln(k): 20.270505841381002"""),
    rank = 11,
    shortDesc = """BM rule fitted to 71 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H
Total Standard Deviation in ln(k): 20.270505841381002""",
    longDesc = 
"""
BM rule fitted to 71 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H
Total Standard Deviation in ln(k): 20.270505841381002
""",
)

entry(
    index = 11,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_N-Sp-5R!H-2R!H",
    kinetics = ArrheniusBM(A=(1.64789e+10,'s^-1'), n=0.672884, w0=(301000,'J/mol'), E0=(70344.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3680246895880845, var=35.10003597313911, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_N-Sp-5R!H-2R!H',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_N-Sp-5R!H-2R!H
    Total Standard Deviation in ln(k): 15.314357730751198"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_N-Sp-5R!H-2R!H
Total Standard Deviation in ln(k): 15.314357730751198""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_N-Sp-5R!H-2R!H
Total Standard Deviation in ln(k): 15.314357730751198
""",
)

entry(
    index = 12,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-=4R!H_Sp-3R!H-1R!H",
    kinetics = ArrheniusBM(A=(5.2475e+35,'s^-1'), n=-5.87931, w0=(301000,'J/mol'), E0=(265922,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=9.074237433759484, var=589.1393634461404, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-=4R!H_Sp-3R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-=4R!H_Sp-3R!H-1R!H
    Total Standard Deviation in ln(k): 71.45890868467546"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-=4R!H_Sp-3R!H-1R!H
Total Standard Deviation in ln(k): 71.45890868467546""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-=4R!H_Sp-3R!H-1R!H
Total Standard Deviation in ln(k): 71.45890868467546
""",
)

entry(
    index = 13,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-=4R!H_N-Sp-3R!H-1R!H",
    kinetics = ArrheniusBM(A=(2.43513e+14,'s^-1'), n=0.593597, w0=(289500,'J/mol'), E0=(28950,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-=4R!H_N-Sp-3R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-=4R!H_N-Sp-3R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-=4R!H_N-Sp-3R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-=4R!H_N-Sp-3R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(8.75866e+22,'s^-1'), n=-2.64726, w0=(301030,'J/mol'), E0=(101653,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24680520709347767, var=18.081216742544864, Tref=1000.0, N=203, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H',), comment="""BM rule fitted to 203 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 9.144650887533794"""),
    rank = 11,
    shortDesc = """BM rule fitted to 203 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 9.144650887533794""",
    longDesc = 
"""
BM rule fitted to 203 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 9.144650887533794
""",
)

entry(
    index = 15,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.03951e+33,'s^-1'), n=-5.67992, w0=(298700,'J/mol'), E0=(152677,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7468081403174006, var=100.63900920067783, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 21.987703345273946"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 21.987703345273946""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 21.987703345273946
""",
)

entry(
    index = 16,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(0.902351,'s^-1'), n=3.72934, w0=(301000,'J/mol'), E0=(566.292,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6270396047684902, var=3.179393167587616, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 5.150090029831008"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.150090029831008""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.150090029831008
""",
)

entry(
    index = 17,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C",
    kinetics = ArrheniusBM(A=(6.10871e+06,'s^-1'), n=1.85938, w0=(301000,'J/mol'), E0=(4139.66,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.010852069118690504, var=9.39042866777529, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C
    Total Standard Deviation in ln(k): 6.170537852051509"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C
Total Standard Deviation in ln(k): 6.170537852051509""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C
Total Standard Deviation in ln(k): 6.170537852051509
""",
)

entry(
    index = 18,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_N-2R!H->C",
    kinetics = ArrheniusBM(A=(3.31581e+13,'s^-1'), n=-0.047641, w0=(307000,'J/mol'), E0=(71399,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_5R!H-inRing",
    kinetics = ArrheniusBM(A=(4.24695e-05,'s^-1'), n=4.91804, w0=(295250,'J/mol'), E0=(3207.54,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.018075138612034594, var=6.172696303847085, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_5R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_5R!H-inRing
    Total Standard Deviation in ln(k): 5.026161490885051"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_5R!H-inRing
Total Standard Deviation in ln(k): 5.026161490885051""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_5R!H-inRing
Total Standard Deviation in ln(k): 5.026161490885051
""",
)

entry(
    index = 20,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(2.98656e+12,'s^-1'), n=0.343598, w0=(301000,'J/mol'), E0=(19545.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0028858365052598744, var=1.584574486785568, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_N-5R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_N-5R!H-inRing
    Total Standard Deviation in ln(k): 2.5308090093035505"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_N-5R!H-inRing
Total Standard Deviation in ln(k): 2.5308090093035505""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_N-5R!H-inRing
Total Standard Deviation in ln(k): 2.5308090093035505
""",
)

entry(
    index = 21,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.92927e+17,'s^-1'), n=-0.934624, w0=(301000,'J/mol'), E0=(32204.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.050178043762468476, var=4.552871950937902, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 36 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 4.403670919757698"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.403670919757698""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.403670919757698
""",
)

entry(
    index = 22,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(8.9473e+17,'s^-1'), n=-1.5835, w0=(299357,'J/mol'), E0=(69875.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3305836077181582, var=20.815061891370924, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 9.976920513985153"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 9.976920513985153""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 9.976920513985153
""",
)

entry(
    index = 23,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(4.3667e+14,'s^-1'), n=-0.211272, w0=(301000,'J/mol'), E0=(22804.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1523727802902152, var=0.05275434936978969, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 0.8433000490197664"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.8433000490197664""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.8433000490197664
""",
)

entry(
    index = 24,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(4.43706e+16,'s^-1'), n=-0.740169, w0=(301000,'J/mol'), E0=(38465,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.014091920198814875, var=2.024408008682349, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 2.887777837588812"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.887777837588812""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.887777837588812
""",
)

entry(
    index = 25,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.06056e+11,'s^-1'), n=0.856033, w0=(301000,'J/mol'), E0=(25293.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.4137206761136047, var=4.5412008092774965, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 7.824171175430569"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 7.824171175430569""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 7.824171175430569
""",
)

entry(
    index = 26,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(2.63734e+09,'s^-1'), n=0.251074, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_Sp-5R!H=4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(0.000823468,'s^-1'), n=4.77531, w0=(301086,'J/mol'), E0=(14179.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22609064113925556, var=5.029088064828466, Tref=1000.0, N=70, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 70 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 5.063811314290495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 70 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 5.063811314290495""",
    longDesc = 
"""
BM rule fitted to 70 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 5.063811314290495
""",
)

entry(
    index = 28,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_N-Sp-5R!H-2R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.26605e+09,'s^-1'), n=0.795243, w0=(301000,'J/mol'), E0=(76516.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_N-Sp-5R!H-2R!H_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_N-Sp-5R!H-2R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_N-Sp-5R!H-2R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_N-Sp-5R!H-2R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-=4R!H_Sp-3R!H-1R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.05426e+12,'s^-1'), n=1.22397, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-=4R!H_Sp-3R!H-1R!H_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-=4R!H_Sp-3R!H-1R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-=4R!H_Sp-3R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-5R!H-=4R!H_Sp-3R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(1.08055e+18,'s^-1'), n=-1.31034, w0=(301000,'J/mol'), E0=(67269.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08866794325825889, var=3.1291920838866445, Tref=1000.0, N=136, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H',), comment="""BM rule fitted to 136 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 3.769064414801013"""),
    rank = 11,
    shortDesc = """BM rule fitted to 136 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 3.769064414801013""",
    longDesc = 
"""
BM rule fitted to 136 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 3.769064414801013
""",
)

entry(
    index = 31,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(3.9343e+15,'s^-1'), n=-0.43197, w0=(301090,'J/mol'), E0=(119165,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.057159408483403416, var=28.615744970897488, Tref=1000.0, N=67, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 67 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 10.867683582037843"""),
    rank = 11,
    shortDesc = """BM rule fitted to 67 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 10.867683582037843""",
    longDesc = 
"""
BM rule fitted to 67 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 10.867683582037843
""",
)

entry(
    index = 32,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(1.60675e+35,'s^-1'), n=-6.2483, w0=(299562,'J/mol'), E0=(159976,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6022731131926002, var=124.59993473250533, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 23.890972190163545"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 23.890972190163545""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 23.890972190163545
""",
)

entry(
    index = 33,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(1.92623,'s^-1'), n=3.41208, w0=(295250,'J/mol'), E0=(29525,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.326005698502542, var=151.0390106376149, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 35.507140062808205"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 35.507140062808205""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 35.507140062808205
""",
)

entry(
    index = 34,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing",
    kinetics = ArrheniusBM(A=(0.0296211,'s^-1'), n=4.15922, w0=(301000,'J/mol'), E0=(-1438.93,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.8365796722750622, var=7.124430732420004, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing
    Total Standard Deviation in ln(k): 9.965486337254362"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing
Total Standard Deviation in ln(k): 9.965486337254362""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing
Total Standard Deviation in ln(k): 9.965486337254362
""",
)

entry(
    index = 35,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(2.95e+12,'s^-1'), n=0.12, w0=(301000,'J/mol'), E0=(39914.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_N-3R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_N-3R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_N-3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_N-3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.650981,'s^-1'), n=3.81177, w0=(301000,'J/mol'), E0=(-11125.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.878747731205789, var=10.027355177105425, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 13.581228475390425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 13.581228475390425""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 13.581228475390425
""",
)

entry(
    index = 37,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_3R!H-inRing",
    kinetics = ArrheniusBM(A=(2.37081e+13,'s^-1'), n=0.0631839, w0=(301000,'J/mol'), E0=(-4177.63,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.6800325658325637, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_3R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_3R!H-inRing
    Total Standard Deviation in ln(k): 6.733750165408451"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_3R!H-inRing
Total Standard Deviation in ln(k): 6.733750165408451""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_3R!H-inRing
Total Standard Deviation in ln(k): 6.733750165408451
""",
)

entry(
    index = 38,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(1.34102e+12,'s^-1'), n=0.486964, w0=(301000,'J/mol'), E0=(31374.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_N-3R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_N-3R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_N-3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_N-3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_5R!H-inRing_Sp-3R!H-1R!H",
    kinetics = ArrheniusBM(A=(8.48215e+10,'s^-1'), n=0.391708, w0=(301000,'J/mol'), E0=(55940.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_5R!H-inRing_Sp-3R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_5R!H-inRing_Sp-3R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_5R!H-inRing_Sp-3R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_5R!H-inRing_Sp-3R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_5R!H-inRing_N-Sp-3R!H-1R!H",
    kinetics = ArrheniusBM(A=(1.74949e+08,'s^-1'), n=1.44626, w0=(289500,'J/mol'), E0=(50218,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_5R!H-inRing_N-Sp-3R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_5R!H-inRing_N-Sp-3R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_5R!H-inRing_N-Sp-3R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_5R!H-inRing_N-Sp-3R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_N-5R!H-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.12836e+11,'s^-1'), n=0.600799, w0=(301000,'J/mol'), E0=(15876.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_N-5R!H-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_N-5R!H-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_N-5R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-4R!H-R_N-5R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.63391e+08,'s^-1'), n=1.79826, w0=(301000,'J/mol'), E0=(4467.74,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1824312039103066, var=3.869485359954745, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 24 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 4.401885733009866"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 4.401885733009866""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 4.401885733009866
""",
)

entry(
    index = 43,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(5.43133e+21,'s^-1'), n=-2.15454, w0=(301000,'J/mol'), E0=(25509.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1721597994239878, var=10.925803213240952, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 7.059054286652038"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 7.059054286652038""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 7.059054286652038
""",
)

entry(
    index = 44,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.61491e+14,'s^-1'), n=0.243577, w0=(301000,'J/mol'), E0=(4187.46,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12713764467878896, var=0.19047201132647382, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.1943698380721945"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.1943698380721945""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.1943698380721945
""",
)

entry(
    index = 45,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.16647e+17,'s^-1'), n=-0.867063, w0=(301000,'J/mol'), E0=(7388.74,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4931619384039732, var=0.41960411398504355, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 5.050267526390788"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 5.050267526390788""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 5.050267526390788
""",
)

entry(
    index = 46,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H",
    kinetics = ArrheniusBM(A=(1.1176e+28,'s^-1'), n=-4.17088, w0=(301000,'J/mol'), E0=(47903.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.1252744627996742, var=14.009380883988205, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H
    Total Standard Deviation in ln(k): 12.843430057412162"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H
Total Standard Deviation in ln(k): 12.843430057412162""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H
Total Standard Deviation in ln(k): 12.843430057412162
""",
)

entry(
    index = 47,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H",
    kinetics = ArrheniusBM(A=(9.9515e+17,'s^-1'), n=-1.60307, w0=(298700,'J/mol'), E0=(71018.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.26580068487315034, var=20.078621617642433, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H
    Total Standard Deviation in ln(k): 9.650893402520566"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H
Total Standard Deviation in ln(k): 9.650893402520566""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H
Total Standard Deviation in ln(k): 9.650893402520566
""",
)

entry(
    index = 48,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.73492e+17,'s^-1'), n=-0.875557, w0=(301000,'J/mol'), E0=(40587.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0023927803698909, var=11.36085966481986, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.763146875679551"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.763146875679551""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.763146875679551
""",
)

entry(
    index = 49,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(9.04197e+12,'s^-1'), n=0.248664, w0=(301000,'J/mol'), E0=(29963.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(5.11071e+12,'s^-1'), n=0.453674, w0=(301000,'J/mol'), E0=(29122,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.69583e+11,'s^-1'), n=0.742864, w0=(301000,'J/mol'), E0=(47906,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00029071915281205304, var=1.8507183726164815, Tref=1000.0, N=45, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R',), comment="""BM rule fitted to 45 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.7279943105358333"""),
    rank = 11,
    shortDesc = """BM rule fitted to 45 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.7279943105358333""",
    longDesc = 
"""
BM rule fitted to 45 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.7279943105358333
""",
)

entry(
    index = 52,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.14881e+11,'s^-1'), n=0.657516, w0=(301000,'J/mol'), E0=(52675.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0021214668646906258, var=0.6083752319597746, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.568991849722674"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.568991849722674""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.568991849722674
""",
)

entry(
    index = 53,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C",
    kinetics = ArrheniusBM(A=(4.97543e-13,'s^-1'), n=7.42044, w0=(301000,'J/mol'), E0=(-6501.94,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.5003467591691253, var=8.73630935703452, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C',), comment="""BM rule fitted to 15 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C
    Total Standard Deviation in ln(k): 9.695160750410814"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C
Total Standard Deviation in ln(k): 9.695160750410814""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C
Total Standard Deviation in ln(k): 9.695160750410814
""",
)

entry(
    index = 54,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_N-2R!H->C",
    kinetics = ArrheniusBM(A=(8.88068e+15,'s^-1'), n=-0.571378, w0=(307000,'J/mol'), E0=(113040,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H",
    kinetics = ArrheniusBM(A=(2.82835e+18,'s^-1'), n=-1.42931, w0=(301000,'J/mol'), E0=(68260.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10185336963351976, var=3.1779371839975767, Tref=1000.0, N=134, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H',), comment="""BM rule fitted to 134 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H
    Total Standard Deviation in ln(k): 3.829708045053549"""),
    rank = 11,
    shortDesc = """BM rule fitted to 134 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H
Total Standard Deviation in ln(k): 3.829708045053549""",
    longDesc = 
"""
BM rule fitted to 134 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H
Total Standard Deviation in ln(k): 3.829708045053549
""",
)

entry(
    index = 56,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-Sp-4R!H-2R!H",
    kinetics = ArrheniusBM(A=(6.30612e+16,'s^-1'), n=-0.979503, w0=(301000,'J/mol'), E0=(71138.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.6000439869240688, var=4.4527500314232875e-31, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-Sp-4R!H-2R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-Sp-4R!H-2R!H
    Total Standard Deviation in ln(k): 4.020211022422284"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-Sp-4R!H-2R!H
Total Standard Deviation in ln(k): 4.020211022422284""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-Sp-4R!H-2R!H
Total Standard Deviation in ln(k): 4.020211022422284
""",
)

entry(
    index = 57,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_3R!H-inRing",
    kinetics = ArrheniusBM(A=(8.76109e+16,'s^-1'), n=-0.831714, w0=(301000,'J/mol'), E0=(131859,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1227933050745186, var=18.25104657696566, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_3R!H-inRing',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_3R!H-inRing
    Total Standard Deviation in ln(k): 8.873003458588174"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_3R!H-inRing
Total Standard Deviation in ln(k): 8.873003458588174""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_3R!H-inRing
Total Standard Deviation in ln(k): 8.873003458588174
""",
)

entry(
    index = 58,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(5.46315e+15,'s^-1'), n=-0.466375, w0=(301097,'J/mol'), E0=(115050,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18293849660920208, var=41.005256161649946, Tref=1000.0, N=62, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing',), comment="""BM rule fitted to 62 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing
    Total Standard Deviation in ln(k): 13.29703501915718"""),
    rank = 11,
    shortDesc = """BM rule fitted to 62 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing
Total Standard Deviation in ln(k): 13.29703501915718""",
    longDesc = 
"""
BM rule fitted to 62 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing
Total Standard Deviation in ln(k): 13.29703501915718
""",
)

entry(
    index = 59,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_3R!H-inRing",
    kinetics = ArrheniusBM(A=(4.71077e+12,'s^-1'), n=0.290083, w0=(301000,'J/mol'), E0=(66580.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_3R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_3R!H-inRing
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_3R!H-inRing
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_3R!H-inRing
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 60,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(3.2938e+55,'s^-1'), n=-12.1217, w0=(299083,'J/mol'), E0=(235633,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2508537553417158, var=253.548742642172, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing
    Total Standard Deviation in ln(k): 35.06467419103716"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing
Total Standard Deviation in ln(k): 35.06467419103716""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing
Total Standard Deviation in ln(k): 35.06467419103716
""",
)

entry(
    index = 61,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(6.41268e+11,'s^-1'), n=0.100946, w0=(289500,'J/mol'), E0=(28950,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H",
    kinetics = ArrheniusBM(A=(7.59639e-10,'s^-1'), n=6.32134, w0=(301000,'J/mol'), E0=(-13532.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.82156556500732, var=21.842978876283155, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H
    Total Standard Deviation in ln(k): 16.45878535305669"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H
Total Standard Deviation in ln(k): 16.45878535305669""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H
Total Standard Deviation in ln(k): 16.45878535305669
""",
)

entry(
    index = 63,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_N-Sp-6R!H-2R!H",
    kinetics = ArrheniusBM(A=(7.17822e+11,'s^-1'), n=0.364349, w0=(301000,'J/mol'), E0=(67981.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_N-Sp-6R!H-2R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_N-Sp-6R!H-2R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_N-Sp-6R!H-2R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_N-Sp-6R!H-2R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.48452e-15,'s^-1'), n=8.07921, w0=(301000,'J/mol'), E0=(-82380.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.354571361579417, var=105.97485722571156, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 34.091259766885756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 34.091259766885756""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 34.091259766885756
""",
)

entry(
    index = 65,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(11079.1,'s^-1'), n=2.45052, w0=(301000,'J/mol'), E0=(21944.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.370141440480876, var=0.8789202829483216, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Sp-4R!H-2C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Sp-4R!H-2C
    Total Standard Deviation in ln(k): 5.322020572282807"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Sp-4R!H-2C
Total Standard Deviation in ln(k): 5.322020572282807""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Sp-4R!H-2C
Total Standard Deviation in ln(k): 5.322020572282807
""",
)

entry(
    index = 66,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_N-Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(2.65009e+12,'s^-1'), n=0.0755546, w0=(301000,'J/mol'), E0=(55257.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_N-Sp-4R!H-2C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_N-Sp-4R!H-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.22182e+11,'s^-1'), n=0.940103, w0=(301000,'J/mol'), E0=(9393.98,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.137839221173414, var=8.167505497900969, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 6.075631595869005"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.075631595869005""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.075631595869005
""",
)

entry(
    index = 68,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.5872e+06,'s^-1'), n=2.51978, w0=(301000,'J/mol'), E0=(413.906,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20133235749918693, var=2.0291733356703814, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 3.3615863737964466"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 3.3615863737964466""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 3.3615863737964466
""",
)

entry(
    index = 69,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.0242e+06,'s^-1'), n=2.3832, w0=(301000,'J/mol'), E0=(1400.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24934781297238034, var=1.4454250506738362, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 3.0367114543839557"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 3.0367114543839557""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 3.0367114543839557
""",
)

entry(
    index = 70,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.50151e+22,'s^-1'), n=-2.42833, w0=(301000,'J/mol'), E0=(-3883.17,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.730120539221496, var=65.25792360764493, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 30.59201417711921"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 30.59201417711921""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 30.59201417711921
""",
)

entry(
    index = 71,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.2501e+17,'s^-1'), n=-0.60525, w0=(301000,'J/mol'), E0=(21323.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.85158e+16,'s^-1'), n=-0.448272, w0=(301000,'J/mol'), E0=(8246.05,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3956465582386104, var=0.4175056692058309, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 4.802002771084413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.802002771084413""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.802002771084413
""",
)

entry(
    index = 73,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-5R!H-R_Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(1.50653e+12,'s^-1'), n=0.66575, w0=(301000,'J/mol'), E0=(18371.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-5R!H-R_Sp-7R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-5R!H-R_Sp-7R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-5R!H-R_Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-5R!H-R_Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-7R!H=5R!H",
    kinetics = ArrheniusBM(A=(2.82005e+12,'s^-1'), n=0.477662, w0=(301000,'J/mol'), E0=(17036.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-7R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(9.52563e+15,'s^-1'), n=-0.635747, w0=(301000,'J/mol'), E0=(21990.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_5R!H-inRing",
    kinetics = ArrheniusBM(A=(267002,'s^-1'), n=2.17307, w0=(295250,'J/mol'), E0=(19914.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03605194324457761, var=3.0416701097682135, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_5R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_5R!H-inRing
    Total Standard Deviation in ln(k): 3.5869178259584213"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_5R!H-inRing
Total Standard Deviation in ln(k): 3.5869178259584213""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_5R!H-inRing
Total Standard Deviation in ln(k): 3.5869178259584213
""",
)

entry(
    index = 77,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(1.42948e+13,'s^-1'), n=-0.536181, w0=(301000,'J/mol'), E0=(64234.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.768336909234558, var=17.0561850764182, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-5R!H-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-5R!H-inRing
    Total Standard Deviation in ln(k): 15.235002727964526"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-5R!H-inRing
Total Standard Deviation in ln(k): 15.235002727964526""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-5R!H-inRing
Total Standard Deviation in ln(k): 15.235002727964526
""",
)

entry(
    index = 78,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(2.0987e+12,'s^-1'), n=0.748952, w0=(301000,'J/mol'), E0=(29735.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-3R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(2.19481e+14,'s^-1'), n=-0.167308, w0=(301000,'J/mol'), E0=(35750,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-3R!H-R_Ext-5R!H-R_Ext-3R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5.38675e+11,'s^-1'), n=0.747773, w0=(301000,'J/mol'), E0=(56726.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09434208547848823, var=3.378348531487367, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 29 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 3.92180049464096"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.92180049464096""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.92180049464096
""",
)

entry(
    index = 81,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.90866e+19,'s^-1'), n=-1.26794, w0=(301000,'J/mol'), E0=(70557.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.014613164085637207, var=1.4299859611815948, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.43401920263639"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.43401920263639""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.43401920263639
""",
)

entry(
    index = 82,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.09028e+13,'s^-1'), n=0.100838, w0=(301000,'J/mol'), E0=(40169.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1150155255466134, var=2.824914554736655, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 6.171001445011288"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.171001445011288""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.171001445011288
""",
)

entry(
    index = 83,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.94755e+13,'s^-1'), n=-0.0262454, w0=(301000,'J/mol'), E0=(57996.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9386383375367449, var=2.9754405161086654, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 5.816448589213931"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 5.816448589213931""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 5.816448589213931
""",
)

entry(
    index = 84,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.74299e+11,'s^-1'), n=0.623766, w0=(301000,'J/mol'), E0=(53116.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2531813912948913, var=3.568382179090689, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.935673987813645"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.935673987813645""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.935673987813645
""",
)

entry(
    index = 85,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.72941e-08,'s^-1'), n=5.82496, w0=(301000,'J/mol'), E0=(-16653.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.722164068223479, var=37.03613644220058, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-4R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 16.527326215797846"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 16.527326215797846""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 16.527326215797846
""",
)

entry(
    index = 86,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.64509e+12,'s^-1'), n=0.352668, w0=(301000,'J/mol'), E0=(46952.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00016274042781216138, var=0.20730256250580095, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.9131746226947672"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.9131746226947672""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.9131746226947672
""",
)

entry(
    index = 87,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(5.55974e+10,'s^-1'), n=0.800885, w0=(301000,'J/mol'), E0=(55078.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.57949e+23,'s^-1'), n=-2.82553, w0=(301000,'J/mol'), E0=(81684.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2911303975593504, var=6.795554926607495, Tref=1000.0, N=90, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R',), comment="""BM rule fitted to 90 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 5.957483983411528"""),
    rank = 11,
    shortDesc = """BM rule fitted to 90 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.957483983411528""",
    longDesc = 
"""
BM rule fitted to 90 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.957483983411528
""",
)

entry(
    index = 89,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(6.68144e+11,'s^-1'), n=0.504859, w0=(301000,'J/mol'), E0=(50363.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10178315407859502, var=1.7114518071421025, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R',), comment="""BM rule fitted to 18 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.8783804683803615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.8783804683803615""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.8783804683803615
""",
)

entry(
    index = 90,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H",
    kinetics = ArrheniusBM(A=(1.57789e+15,'s^-1'), n=-0.534655, w0=(301000,'J/mol'), E0=(58636.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.031152961691649494, var=0.9796150252661436, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H',), comment="""BM rule fitted to 16 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H
    Total Standard Deviation in ln(k): 2.062470405693344"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H
Total Standard Deviation in ln(k): 2.062470405693344""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H
Total Standard Deviation in ln(k): 2.062470405693344
""",
)

entry(
    index = 91,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-6R!H-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.64311e+14,'s^-1'), n=-0.187975, w0=(301000,'J/mol'), E0=(72898.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-6R!H-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-6R!H-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-6R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-6R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_3R!H-inRing_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.87284e+14,'s^-1'), n=-0.169909, w0=(301000,'J/mol'), E0=(133441,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.057603078471636975, var=45.409104572368165, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_3R!H-inRing_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_3R!H-inRing_Ext-1R!H-R
    Total Standard Deviation in ln(k): 13.653894868990605"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_3R!H-inRing_Ext-1R!H-R
Total Standard Deviation in ln(k): 13.653894868990605""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_3R!H-inRing_Ext-1R!H-R
Total Standard Deviation in ln(k): 13.653894868990605
""",
)

entry(
    index = 93,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(8.29156e+13,'s^-1'), n=0.181571, w0=(301140,'J/mol'), E0=(102142,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05187017046675275, var=2.021011938917717, Tref=1000.0, N=43, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R',), comment="""BM rule fitted to 43 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.98030454567926"""),
    rank = 11,
    shortDesc = """BM rule fitted to 43 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.98030454567926""",
    longDesc = 
"""
BM rule fitted to 43 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.98030454567926
""",
)

entry(
    index = 94,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.86875e+14,'s^-1'), n=-0.246021, w0=(301000,'J/mol'), E0=(108767,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.006121325207568091, var=4.353427002467063, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R
    Total Standard Deviation in ln(k): 4.198233411730601"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.198233411730601""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.198233411730601
""",
)

entry(
    index = 95,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(9.99427e+15,'s^-1'), n=-0.465719, w0=(301000,'J/mol'), E0=(107596,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.5356582978187088, var=21.23283838422407, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-1R!H-R
    Total Standard Deviation in ln(k): 13.096077574821848"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-1R!H-R
Total Standard Deviation in ln(k): 13.096077574821848""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-1R!H-R
Total Standard Deviation in ln(k): 13.096077574821848
""",
)

entry(
    index = 96,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(7.08822e+20,'s^-1'), n=-2.08602, w0=(297167,'J/mol'), E0=(92171,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.018616506223364446, var=17.67044602231849, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-5R!H-R
    Total Standard Deviation in ln(k): 8.473925549060894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-5R!H-R
Total Standard Deviation in ln(k): 8.473925549060894""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-5R!H-R
Total Standard Deviation in ln(k): 8.473925549060894
""",
)

entry(
    index = 97,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2.53049e+12,'s^-1'), n=0.792268, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H_Sp-4R!H-2R!H",
    kinetics = ArrheniusBM(A=(8.21274e+08,'s^-1'), n=1.16495, w0=(301000,'J/mol'), E0=(34615.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.005546036768711659, var=0.9916331258342385, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H_Sp-4R!H-2R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H_Sp-4R!H-2R!H
    Total Standard Deviation in ln(k): 2.0102655437257644"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H_Sp-4R!H-2R!H
Total Standard Deviation in ln(k): 2.0102655437257644""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H_Sp-4R!H-2R!H
Total Standard Deviation in ln(k): 2.0102655437257644
""",
)

entry(
    index = 99,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H_N-Sp-4R!H-2R!H",
    kinetics = ArrheniusBM(A=(3.86475e+11,'s^-1'), n=0.371591, w0=(301000,'J/mol'), E0=(74363.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.014844479229505016, var=11.63719306688566, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H_N-Sp-4R!H-2R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H_N-Sp-4R!H-2R!H
    Total Standard Deviation in ln(k): 6.876116679859425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H_N-Sp-4R!H-2R!H
Total Standard Deviation in ln(k): 6.876116679859425""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H_N-Sp-4R!H-2R!H
Total Standard Deviation in ln(k): 6.876116679859425
""",
)

entry(
    index = 100,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R_Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(1.59844e+13,'s^-1'), n=0.246515, w0=(301000,'J/mol'), E0=(24956.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0719946534097791, var=4.138504082270081, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R_Sp-4R!H-2C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R_Sp-4R!H-2C
    Total Standard Deviation in ln(k): 4.259186525399592"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R_Sp-4R!H-2C
Total Standard Deviation in ln(k): 4.259186525399592""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R_Sp-4R!H-2C
Total Standard Deviation in ln(k): 4.259186525399592
""",
)

entry(
    index = 101,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R_N-Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(6.06716e+10,'s^-1'), n=0.448537, w0=(301000,'J/mol'), E0=(52990.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R_N-Sp-4R!H-2C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R_N-Sp-4R!H-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 102,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Sp-4R!H-2C_Sp-6R!H-4R!H",
    kinetics = ArrheniusBM(A=(1.57681e+10,'s^-1'), n=0.750244, w0=(301000,'J/mol'), E0=(42292.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Sp-4R!H-2C_Sp-6R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Sp-4R!H-2C_Sp-6R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Sp-4R!H-2C_Sp-6R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Sp-4R!H-2C_Sp-6R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 103,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Sp-4R!H-2C_N-Sp-6R!H-4R!H",
    kinetics = ArrheniusBM(A=(7.26538e+10,'s^-1'), n=0.434095, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Sp-4R!H-2C_N-Sp-6R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Sp-4R!H-2C_N-Sp-6R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Sp-4R!H-2C_N-Sp-6R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Sp-4R!H-2C_N-Sp-6R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 104,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(4.69307e+15,'s^-1'), n=-0.416139, w0=(301000,'J/mol'), E0=(28487.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.021161931880898086, var=11.7073555898158, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 6.912574869239544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.912574869239544""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 6.912574869239544
""",
)

entry(
    index = 105,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.11166e+19,'s^-1'), n=-1.3383, w0=(301000,'J/mol'), E0=(33052.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.000529418309149231, var=11.170271667147414, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.701547023114632"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.701547023114632""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.701547023114632
""",
)

entry(
    index = 106,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.47025e+18,'s^-1'), n=-1.05948, w0=(301000,'J/mol'), E0=(33506.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 107,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(8.31622e+17,'s^-1'), n=-0.854779, w0=(301000,'J/mol'), E0=(33054.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 108,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(457987,'s^-1'), n=2.89649, w0=(301000,'J/mol'), E0=(-2026.83,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3909315471483327, var=2.733936061674935, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 4.296993021229014"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.296993021229014""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.296993021229014
""",
)

entry(
    index = 109,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(6.63627e+13,'s^-1'), n=0.191205, w0=(301000,'J/mol'), E0=(31391.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.011721487860898648, var=0.000688998588942062, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.08207282977864346"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.08207282977864346""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.08207282977864346
""",
)

entry(
    index = 110,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.00318e+06,'s^-1'), n=2.34567, w0=(301000,'J/mol'), E0=(-22.5239,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.49043341412955177, var=2.3464475278266166, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-3R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 4.303121696329743"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.303121696329743""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.303121696329743
""",
)

entry(
    index = 111,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(4.32687e+14,'s^-1'), n=0.0877408, w0=(301000,'J/mol'), E0=(34607.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.009779215101779213, var=5.361181813522686e-07, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.026038761075477625"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.026038761075477625""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.026038761075477625
""",
)

entry(
    index = 112,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-8R!H=5R!H",
    kinetics = ArrheniusBM(A=(2.86895e+19,'s^-1'), n=-1.79261, w0=(301000,'J/mol'), E0=(-20284.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.6914874902999293, var=3.0098829063281616, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-8R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-8R!H=5R!H
    Total Standard Deviation in ln(k): 7.727986283298341"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 7.727986283298341""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 7.727986283298341
""",
)

entry(
    index = 113,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-8R!H=5R!H",
    kinetics = ArrheniusBM(A=(3.99796e-12,'s^-1'), n=7.54033, w0=(301000,'J/mol'), E0=(-34469.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.891796929423401, var=2.987986877857263, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-8R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-8R!H=5R!H
    Total Standard Deviation in ln(k): 10.731165266673276"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 10.731165266673276""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 10.731165266673276
""",
)

entry(
    index = 114,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R_Sp-8R!H=5R!H",
    kinetics = ArrheniusBM(A=(5.72713e+11,'s^-1'), n=0.989769, w0=(301000,'J/mol'), E0=(17287.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R_Sp-8R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R_Sp-8R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R_Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R_Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-8R!H=5R!H",
    kinetics = ArrheniusBM(A=(1.07524e+12,'s^-1'), n=0.801714, w0=(301000,'J/mol'), E0=(15924.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-8R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-8R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-5R!H-R_N-Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 116,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_5R!H-inRing_Sp-3R!H-1R!H",
    kinetics = ArrheniusBM(A=(1.57862e+15,'s^-1'), n=-0.655953, w0=(301000,'J/mol'), E0=(64615.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_5R!H-inRing_Sp-3R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_5R!H-inRing_Sp-3R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_5R!H-inRing_Sp-3R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_5R!H-inRing_Sp-3R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 117,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_5R!H-inRing_N-Sp-3R!H-1R!H",
    kinetics = ArrheniusBM(A=(1.28668e+11,'s^-1'), n=0.574109, w0=(289500,'J/mol'), E0=(42584.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_5R!H-inRing_N-Sp-3R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_5R!H-inRing_N-Sp-3R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_5R!H-inRing_N-Sp-3R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_5R!H-inRing_N-Sp-3R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 118,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-5R!H-inRing_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(7.18199e+13,'s^-1'), n=-0.525038, w0=(301000,'J/mol'), E0=(21593.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-5R!H-inRing_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-5R!H-inRing_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-5R!H-inRing_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_N-5R!H-inRing_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 119,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H",
    kinetics = ArrheniusBM(A=(2.34403e+19,'s^-1'), n=-1.33007, w0=(301000,'J/mol'), E0=(71180.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0956680306348123, var=3.1777591163771235, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H',), comment="""BM rule fitted to 14 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H
    Total Standard Deviation in ln(k): 3.8140668666360713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H
Total Standard Deviation in ln(k): 3.8140668666360713""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H
Total Standard Deviation in ln(k): 3.8140668666360713
""",
)

entry(
    index = 120,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H",
    kinetics = ArrheniusBM(A=(103809,'s^-1'), n=2.63806, w0=(301000,'J/mol'), E0=(40768.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5911509801890884, var=3.3475974521592646, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H',), comment="""BM rule fitted to 15 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H
    Total Standard Deviation in ln(k): 5.153255632636731"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H
Total Standard Deviation in ln(k): 5.153255632636731""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H
Total Standard Deviation in ln(k): 5.153255632636731
""",
)

entry(
    index = 121,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(2.84279e+20,'s^-1'), n=-1.54574, w0=(301000,'J/mol'), E0=(74692.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.018365600207838544, var=1.7602377459949903, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 2.7059059724544876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.7059059724544876""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.7059059724544876
""",
)

entry(
    index = 122,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.58992e+17,'s^-1'), n=-0.626385, w0=(301000,'J/mol'), E0=(62628.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00020050864062246261, var=2.5062015999651783, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 3.174197352552067"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.174197352552067""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.174197352552067
""",
)

entry(
    index = 123,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(7.08262e+17,'s^-1'), n=-0.975349, w0=(301000,'J/mol'), E0=(64840.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 124,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(7.0336e+12,'s^-1'), n=0.135082, w0=(301000,'J/mol'), E0=(59666.6,'J/mol'), Tmin=(500,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 125,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.63461e+18,'s^-1'), n=-1.18788, w0=(301000,'J/mol'), E0=(79371.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0006828425517370902, var=11.258039646267532, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.728203754905664"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.728203754905664""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.728203754905664
""",
)

entry(
    index = 126,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.94837e+13,'s^-1'), n=0.202585, w0=(301000,'J/mol'), E0=(67709,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 127,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.10598e+13,'s^-1'), n=0.407408, w0=(301000,'J/mol'), E0=(67036.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 128,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-4R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.0308e+10,'s^-1'), n=0.594665, w0=(301000,'J/mol'), E0=(70808.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-4R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-4R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-4R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-4R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 129,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(5.63473e+09,'s^-1'), n=1.05259, w0=(301000,'J/mol'), E0=(47505.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 130,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(4.06092e+09,'s^-1'), n=1.09871, w0=(301000,'J/mol'), E0=(41195.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_2R!H->C_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(7.60908e+17,'s^-1'), n=-1.10814, w0=(301000,'J/mol'), E0=(78982.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.42367647921865986, var=8.638086561187649, Tref=1000.0, N=57, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 57 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 6.956554835351621"""),
    rank = 11,
    shortDesc = """BM rule fitted to 57 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 6.956554835351621""",
    longDesc = 
"""
BM rule fitted to 57 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 6.956554835351621
""",
)

entry(
    index = 132,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_3R!H-inRing",
    kinetics = ArrheniusBM(A=(125707,'s^-1'), n=2.04553, w0=(301000,'J/mol'), E0=(43936.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_3R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_3R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(1.87687e+24,'s^-1'), n=-3.07691, w0=(301000,'J/mol'), E0=(74961,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.31053536541635934, var=2.8059261992876747, Tref=1000.0, N=32, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing',), comment="""BM rule fitted to 32 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing
    Total Standard Deviation in ln(k): 4.138351107598897"""),
    rank = 11,
    shortDesc = """BM rule fitted to 32 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing
Total Standard Deviation in ln(k): 4.138351107598897""",
    longDesc = 
"""
BM rule fitted to 32 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing
Total Standard Deviation in ln(k): 4.138351107598897
""",
)

entry(
    index = 134,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_3R!H-inRing",
    kinetics = ArrheniusBM(A=(1.35536e+13,'s^-1'), n=0.285767, w0=(301000,'J/mol'), E0=(54275.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0066903209622441555, var=0.6290355226134092, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_3R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_3R!H-inRing
    Total Standard Deviation in ln(k): 1.6068005187955208"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_3R!H-inRing
Total Standard Deviation in ln(k): 1.6068005187955208""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_3R!H-inRing
Total Standard Deviation in ln(k): 1.6068005187955208
""",
)

entry(
    index = 135,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(4.37269e+18,'s^-1'), n=-1.51018, w0=(301000,'J/mol'), E0=(69819.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13144403516543943, var=1.2732475286585487, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing',), comment="""BM rule fitted to 16 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing
    Total Standard Deviation in ln(k): 2.5923697840736275"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing
Total Standard Deviation in ln(k): 2.5923697840736275""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing
Total Standard Deviation in ln(k): 2.5923697840736275
""",
)

entry(
    index = 136,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.24984e+14,'s^-1'), n=-0.211642, w0=(301000,'J/mol'), E0=(52733.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00047916841364686484, var=0.04140330734034589, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.40912347829602874"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.40912347829602874""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.40912347829602874
""",
)

entry(
    index = 137,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.79099e+14,'s^-1'), n=-0.250904, w0=(301000,'J/mol'), E0=(56165.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0020358283500333473, var=0.7073560006407887, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.69118673577486"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.69118673577486""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.69118673577486
""",
)

entry(
    index = 138,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(6.52929e+14,'s^-1'), n=-0.41705, w0=(301000,'J/mol'), E0=(55320.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0021672255514139085, var=0.825192960115918, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.8265492830239822"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.8265492830239822""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.8265492830239822
""",
)

entry(
    index = 139,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.37491e+08,'s^-1'), n=1.39714, w0=(301000,'J/mol'), E0=(52652.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 140,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_3R!H-inRing_Ext-1R!H-R_Int-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(1.87049e+12,'s^-1'), n=0.499766, w0=(301000,'J/mol'), E0=(148440,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0003257738771712278, var=15.305897188196337, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_3R!H-inRing_Ext-1R!H-R_Int-7R!H-6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_3R!H-inRing_Ext-1R!H-R_Int-7R!H-6R!H
    Total Standard Deviation in ln(k): 7.843893839778981"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_3R!H-inRing_Ext-1R!H-R_Int-7R!H-6R!H
Total Standard Deviation in ln(k): 7.843893839778981""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_3R!H-inRing_Ext-1R!H-R_Int-7R!H-6R!H
Total Standard Deviation in ln(k): 7.843893839778981
""",
)

entry(
    index = 141,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(9.8233e+14,'s^-1'), n=-0.0223511, w0=(301000,'J/mol'), E0=(112920,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0340689960658877, var=3.081614281349004, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 28 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 3.6048181537884174"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 3.6048181537884174""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 3.6048181537884174
""",
)

entry(
    index = 142,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2.27377e+12,'s^-1'), n=0.495333, w0=(307000,'J/mol'), E0=(88763.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 143,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(6.26933e+13,'s^-1'), n=0.307888, w0=(301000,'J/mol'), E0=(106042,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0032690527430875513, var=3.9339887759775403, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.9844624693621085"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.9844624693621085""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.9844624693621085
""",
)

entry(
    index = 144,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.36289e+10,'s^-1'), n=1.2799, w0=(301000,'J/mol'), E0=(91654.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 145,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.91045e+14,'s^-1'), n=-0.279549, w0=(301000,'J/mol'), E0=(103123,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00341418368633092, var=1.2206865085562224, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.223503537868355"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.223503537868355""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.223503537868355
""",
)

entry(
    index = 146,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(6.12434e+14,'s^-1'), n=-0.201885, w0=(301000,'J/mol'), E0=(121930,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005048742647039391, var=50.16593752192652, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 14.211806144654554"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 14.211806144654554""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 14.211806144654554
""",
)

entry(
    index = 147,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-1R!H-R_Int-7R!H-6R!H_Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(4.60575e+12,'s^-1'), n=0.509323, w0=(301000,'J/mol'), E0=(92283.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-1R!H-R_Int-7R!H-6R!H_Sp-7R!H-6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-1R!H-R_Int-7R!H-6R!H_Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-1R!H-R_Int-7R!H-6R!H_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-1R!H-R_Int-7R!H-6R!H_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-1R!H-R_Int-7R!H-6R!H_N-Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(3.72248e+11,'s^-1'), n=0.880949, w0=(301000,'J/mol'), E0=(120318,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.215402716989295, var=61.8043701559802, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-1R!H-R_Int-7R!H-6R!H_N-Sp-7R!H-6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-1R!H-R_Int-7R!H-6R!H_N-Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 28.864403199299776"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-1R!H-R_Int-7R!H-6R!H_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 28.864403199299776""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-1R!H-R_Int-7R!H-6R!H_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 28.864403199299776
""",
)

entry(
    index = 149,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-5R!H-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(5.65691e+10,'s^-1'), n=1.63148, w0=(301000,'J/mol'), E0=(198016,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-5R!H-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-5R!H-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-5R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-5R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 150,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-5R!H-R_Sp-3R!H-1R!H",
    kinetics = ArrheniusBM(A=(8.46653e+09,'s^-1'), n=0.779126, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-5R!H-R_Sp-3R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-5R!H-R_Sp-3R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-5R!H-R_Sp-3R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-5R!H-R_Sp-3R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 151,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-5R!H-R_N-Sp-3R!H-1R!H",
    kinetics = ArrheniusBM(A=(1.08935e+11,'s^-1'), n=0.932679, w0=(289500,'J/mol'), E0=(28950,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-5R!H-R_N-Sp-3R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-5R!H-R_N-Sp-3R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-5R!H-R_N-Sp-3R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_N-Sp-6R!H-5R!H_Sp-5R!H-4R!H_N-3R!H-inRing_Ext-5R!H-R_N-Sp-3R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 152,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H_Sp-4R!H-2R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(8.06779e+08,'s^-1'), n=1.16121, w0=(301000,'J/mol'), E0=(30871.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H_Sp-4R!H-2R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H_Sp-4R!H-2R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H_Sp-4R!H-2R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H_Sp-4R!H-2R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 153,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H_N-Sp-4R!H-2R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(3.42748e+13,'s^-1'), n=-0.0934402, w0=(301000,'J/mol'), E0=(96852.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H_N-Sp-4R!H-2R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H_N-Sp-4R!H-2R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H_N-Sp-4R!H-2R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_Ext-2R!H-R_3R!H-inRing_Sp-6R!H-2R!H_N-Sp-4R!H-2R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 154,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R_Sp-4R!H-2C_3R!H-inRing",
    kinetics = ArrheniusBM(A=(4.1705e+13,'s^-1'), n=0.383545, w0=(301000,'J/mol'), E0=(36811.9,'J/mol'), Tmin=(500,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R_Sp-4R!H-2C_3R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R_Sp-4R!H-2C_3R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R_Sp-4R!H-2C_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R_Sp-4R!H-2C_3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 155,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R_Sp-4R!H-2C_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(9.04643e+11,'s^-1'), n=0.377977, w0=(301000,'J/mol'), E0=(11218.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R_Sp-4R!H-2C_N-3R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R_Sp-4R!H-2C_N-3R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R_Sp-4R!H-2C_N-3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-1R!H-R_2R!H->C_Ext-4R!H-R_Ext-6R!H-R_Sp-4R!H-2C_N-3R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 156,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H",
    kinetics = ArrheniusBM(A=(2.99129e+08,'s^-1'), n=1.41653, w0=(301000,'J/mol'), E0=(4106.93,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08933014075547967, var=1.6505959113406674, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H
    Total Standard Deviation in ln(k): 2.8000413953225016"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H
Total Standard Deviation in ln(k): 2.8000413953225016""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H
Total Standard Deviation in ln(k): 2.8000413953225016
""",
)

entry(
    index = 157,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H",
    kinetics = ArrheniusBM(A=(4.46187e+14,'s^-1'), n=0.145112, w0=(301000,'J/mol'), E0=(5416.19,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0689219456565276, var=1.5898788826544639, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H
    Total Standard Deviation in ln(k): 2.700949184180711"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H
Total Standard Deviation in ln(k): 2.700949184180711""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H
Total Standard Deviation in ln(k): 2.700949184180711
""",
)

entry(
    index = 158,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.4223e+17,'s^-1'), n=-0.559188, w0=(301000,'J/mol'), E0=(33819.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 159,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.57821e+19,'s^-1'), n=-1.47553, w0=(301000,'J/mol'), E0=(39510.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 160,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.77406e+14,'s^-1'), n=0.297511, w0=(301000,'J/mol'), E0=(37107.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.008374639108898192, var=0.0001354122512068848, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.044370261338419384"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.044370261338419384""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.044370261338419384
""",
)

entry(
    index = 161,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R_Sp-8R!H=5R!H",
    kinetics = ArrheniusBM(A=(6.7443e+12,'s^-1'), n=0.535544, w0=(301000,'J/mol'), E0=(32229,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R_Sp-8R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R_Sp-8R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R_Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R_Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 162,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R_N-Sp-8R!H=5R!H",
    kinetics = ArrheniusBM(A=(1.2624e+13,'s^-1'), n=0.347464, w0=(301000,'J/mol'), E0=(26171.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R_N-Sp-8R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R_N-Sp-8R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R_N-Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-5R!H-R_N-Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 163,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(7.18826e+15,'s^-1'), n=-0.438306, w0=(301000,'J/mol'), E0=(38752.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.006613712653273028, var=0.0006574846078920461, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.06802170812717148"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.06802170812717148""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.06802170812717148
""",
)

entry(
    index = 164,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R_Sp-8R!H=5R!H",
    kinetics = ArrheniusBM(A=(3.81863e+12,'s^-1'), n=0.740286, w0=(301000,'J/mol'), E0=(32647.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R_Sp-8R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R_Sp-8R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R_Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R_Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 165,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R_N-Sp-8R!H=5R!H",
    kinetics = ArrheniusBM(A=(7.03976e+12,'s^-1'), n=0.554863, w0=(301000,'J/mol'), E0=(26643.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R_N-Sp-8R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R_N-Sp-8R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R_N-Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-5R!H-R_N-Sp-8R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 166,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-8R!H=5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.46046e+13,'s^-1'), n=0.00519422, w0=(301000,'J/mol'), E0=(20611,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-8R!H=5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-8R!H=5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-8R!H=5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-8R!H=5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 167,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-8R!H=5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.56872e+15,'s^-1'), n=-0.105443, w0=(301000,'J/mol'), E0=(20961.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-8R!H=5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-8R!H=5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-8R!H=5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-8R!H=5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 168,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.27333e+17,'s^-1'), n=-0.736869, w0=(301000,'J/mol'), E0=(60189.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.026943206233152495, var=2.1096472894216047, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.979499003525581"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.979499003525581""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.979499003525581
""",
)

entry(
    index = 169,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.12337e+17,'s^-1'), n=-0.671118, w0=(301000,'J/mol'), E0=(71980,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04711251715104104, var=1.458941329538958, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.5398253736554848"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.5398253736554848""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.5398253736554848
""",
)

entry(
    index = 170,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.96315e+15,'s^-1'), n=-0.601009, w0=(301000,'J/mol'), E0=(69921.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.010974056949181802, var=2.0544214710286353, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.901010552385339"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.901010552385339""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.901010552385339
""",
)

entry(
    index = 171,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(4.80449e+07,'s^-1'), n=1.89314, w0=(301000,'J/mol'), E0=(46132.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.50178e+17,'s^-1'), n=-0.659412, w0=(301000,'J/mol'), E0=(79187.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04616059398600358, var=1.4731519884272477, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.5491979745374187"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.5491979745374187""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.5491979745374187
""",
)

entry(
    index = 173,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(9.82762e+19,'s^-1'), n=-1.34892, w0=(301000,'J/mol'), E0=(74085.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.024160358025887962, var=3.1322766283635133, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 3.6087324653932016"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 3.6087324653932016""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 3.6087324653932016
""",
)

entry(
    index = 174,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(8.6527e+20,'s^-1'), n=-1.74888, w0=(301000,'J/mol'), E0=(75355.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.011847675938004738, var=1.8271510306254664, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 2.739611548566011"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 2.739611548566011""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 2.739611548566011
""",
)

entry(
    index = 175,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.69697e+17,'s^-1'), n=-0.65133, w0=(301000,'J/mol'), E0=(63497.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 176,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(4.53523e+12,'s^-1'), n=0.702873, w0=(301000,'J/mol'), E0=(67728.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 177,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(4.74686e+14,'s^-1'), n=-0.213439, w0=(301000,'J/mol'), E0=(73555.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-6R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 178,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H",
    kinetics = ArrheniusBM(A=(1.80548e+21,'s^-1'), n=-1.84619, w0=(301000,'J/mol'), E0=(82791.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05530584583322498, var=4.629786737167218, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H',), comment="""BM rule fitted to 28 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H
    Total Standard Deviation in ln(k): 4.45253569437904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H
Total Standard Deviation in ln(k): 4.45253569437904""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H
Total Standard Deviation in ln(k): 4.45253569437904
""",
)

entry(
    index = 179,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H",
    kinetics = ArrheniusBM(A=(6.65731e+14,'s^-1'), n=-0.340092, w0=(301000,'J/mol'), E0=(73519,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4345812332963721, var=5.661457198657437, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H',), comment="""BM rule fitted to 29 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H
    Total Standard Deviation in ln(k): 5.8619425711090205"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H
Total Standard Deviation in ln(k): 5.8619425711090205""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H
Total Standard Deviation in ln(k): 5.8619425711090205
""",
)

entry(
    index = 180,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(7.64255e+27,'s^-1'), n=-4.1103, w0=(301000,'J/mol'), E0=(83324,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.690997969616497, var=6.467170433494296, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R',), comment="""BM rule fitted to 16 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R
    Total Standard Deviation in ln(k): 6.834343801880023"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R
Total Standard Deviation in ln(k): 6.834343801880023""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R
Total Standard Deviation in ln(k): 6.834343801880023
""",
)

entry(
    index = 181,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.3639e+22,'s^-1'), n=-2.39448, w0=(301000,'J/mol'), E0=(74248.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08947314013609214, var=1.6441027510316233, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.7953297268265906"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.7953297268265906""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.7953297268265906
""",
)

entry(
    index = 182,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.05918e+15,'s^-1'), n=-0.560273, w0=(301000,'J/mol'), E0=(49044,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3563565371368125, var=4.1801437495254, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-2R!H-R
    Total Standard Deviation in ln(k): 7.506692022533551"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-2R!H-R
Total Standard Deviation in ln(k): 7.506692022533551""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-2R!H-R
Total Standard Deviation in ln(k): 7.506692022533551
""",
)

entry(
    index = 183,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_3R!H-inRing_Int-6R!H-1R!H",
    kinetics = ArrheniusBM(A=(4.2027e+12,'s^-1'), n=0.53843, w0=(301000,'J/mol'), E0=(56398,'J/mol'), Tmin=(500,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_3R!H-inRing_Int-6R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_3R!H-inRing_Int-6R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_3R!H-inRing_Int-6R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_3R!H-inRing_Int-6R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 184,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(9.25617e+26,'s^-1'), n=-3.65845, w0=(301000,'J/mol'), E0=(94300.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13194471089593346, var=4.666330241854961, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R
    Total Standard Deviation in ln(k): 4.662086003361224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R
Total Standard Deviation in ln(k): 4.662086003361224""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R
Total Standard Deviation in ln(k): 4.662086003361224
""",
)

entry(
    index = 185,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(6.846e+15,'s^-1'), n=-0.655635, w0=(301000,'J/mol'), E0=(61285.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03656095613468662, var=0.30694252120166926, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-3R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.2025329162151126"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.2025329162151126""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.2025329162151126
""",
)

entry(
    index = 186,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2.23464e+18,'s^-1'), n=-1.5045, w0=(301000,'J/mol'), E0=(69177.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.283707037551621, var=11.850161456104653, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-1R!H-R
    Total Standard Deviation in ln(k): 12.639070134745232"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-1R!H-R
Total Standard Deviation in ln(k): 12.639070134745232""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-1R!H-R
Total Standard Deviation in ln(k): 12.639070134745232
""",
)

entry(
    index = 187,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(9.87157e+08,'s^-1'), n=1.27497, w0=(301000,'J/mol'), E0=(38733.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 188,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-6R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5.46697e+08,'s^-1'), n=1.35885, w0=(301000,'J/mol'), E0=(43658.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-6R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-6R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-6R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 189,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.63069e+09,'s^-1'), n=1.21284, w0=(301000,'J/mol'), E0=(42388,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Int-6R!H-1R!H_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 190,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_3R!H-inRing_Ext-1R!H-R_Int-7R!H-6R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.56313e+10,'s^-1'), n=0.909091, w0=(301000,'J/mol'), E0=(127556,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_3R!H-inRing_Ext-1R!H-R_Int-7R!H-6R!H_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_3R!H-inRing_Ext-1R!H-R_Int-7R!H-6R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_3R!H-inRing_Ext-1R!H-R_Int-7R!H-6R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_3R!H-inRing_Ext-1R!H-R_Int-7R!H-6R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 191,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(5.45626e+14,'s^-1'), n=0.0647665, w0=(301000,'J/mol'), E0=(113099,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04141817837292049, var=3.505829457187664, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 24 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.857703733913083"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.857703733913083""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.857703733913083
""",
)

entry(
    index = 192,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.35506e+17,'s^-1'), n=-0.684859, w0=(301000,'J/mol'), E0=(113983,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0008438698927682013, var=11.334363435732213, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.751370917668205"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.751370917668205""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.751370917668205
""",
)

entry(
    index = 193,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(2.78356e+11,'s^-1'), n=0.825673, w0=(301000,'J/mol'), E0=(98497.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 194,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.57542e+11,'s^-1'), n=1.0304, w0=(301000,'J/mol'), E0=(97616.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 195,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(5.57031e+13,'s^-1'), n=0.237316, w0=(301000,'J/mol'), E0=(100694,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00461270234973664, var=1.5452924560006311, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.5036717231995977"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.5036717231995977""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.5036717231995977
""",
)

entry(
    index = 196,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(6.93688e+13,'s^-1'), n=0.434598, w0=(301000,'J/mol'), E0=(118511,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.012510848052986561, var=15.952645065015108, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 8.038499045277645"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 8.038499045277645""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 8.038499045277645
""",
)

entry(
    index = 197,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.78872e+12,'s^-1'), n=0.745276, w0=(301000,'J/mol'), E0=(93807,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 198,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-2R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(2.60769e+14,'s^-1'), n=-0.270463, w0=(301000,'J/mol'), E0=(109019,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.002063023286435602, var=1.5587168381597656, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-2R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-2R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 2.5080667888990598"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-2R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.5080667888990598""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-2R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.5080667888990598
""",
)

entry(
    index = 199,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(4.91157e+11,'s^-1'), n=0.837156, w0=(301000,'J/mol'), E0=(101552,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 200,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.06158e+12,'s^-1'), n=0.446259, w0=(301000,'J/mol'), E0=(127328,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 201,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.5238e+07,'s^-1'), n=1.69306, w0=(301000,'J/mol'), E0=(4784.18,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.003772848201756395, var=10.623495664562938, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.54365376920517"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.54365376920517""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.54365376920517
""",
)

entry(
    index = 202,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(4.06525e+14,'s^-1'), n=-0.449031, w0=(301000,'J/mol'), E0=(33127.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(2.2965e+14,'s^-1'), n=-0.244335, w0=(301000,'J/mol'), E0=(33913.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 204,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(6.74698e+13,'s^-1'), n=0.421648, w0=(301000,'J/mol'), E0=(7076.37,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.008336824537424565, var=10.390956867677444, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.48321175319575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.48321175319575""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.48321175319575
""",
)

entry(
    index = 205,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(5.36955e+16,'s^-1'), n=-0.559669, w0=(301000,'J/mol'), E0=(19486.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 206,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(3.05302e+16,'s^-1'), n=-0.354944, w0=(301000,'J/mol'), E0=(21740.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 207,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H",
    kinetics = ArrheniusBM(A=(1.56908e+12,'s^-1'), n=1.03583, w0=(301000,'J/mol'), E0=(33877.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 208,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H",
    kinetics = ArrheniusBM(A=(2.94208e+12,'s^-1'), n=0.847785, w0=(301000,'J/mol'), E0=(27883.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 209,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H",
    kinetics = ArrheniusBM(A=(1.64077e+14,'s^-1'), n=0.119497, w0=(301000,'J/mol'), E0=(39507.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 210,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H",
    kinetics = ArrheniusBM(A=(3.03633e+14,'s^-1'), n=-0.0669911, w0=(301000,'J/mol'), E0=(33460.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-3R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 211,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.88134e+20,'s^-1'), n=-1.4753, w0=(301000,'J/mol'), E0=(68338.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09471444207503227, var=1.634026956883531, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.8006100675376264"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.8006100675376264""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.8006100675376264
""",
)

entry(
    index = 212,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.17134e+16,'s^-1'), n=-0.378852, w0=(301000,'J/mol'), E0=(72616.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0007886354674401227, var=1.89169184476459, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 2.759269841927654"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.759269841927654""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.759269841927654
""",
)

entry(
    index = 213,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.31969e+12,'s^-1'), n=0.755635, w0=(301000,'J/mol'), E0=(53161.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 214,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.4174e+17,'s^-1'), n=-1.24765, w0=(301000,'J/mol'), E0=(77052.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06925665994210674, var=1.5650819863518526, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.6820001799375324"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.6820001799375324""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.6820001799375324
""",
)

entry(
    index = 215,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(2.58257e+16,'s^-1'), n=-0.366132, w0=(301000,'J/mol'), E0=(79880.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0033025690598680497, var=1.885078971221774, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 2.7607626493971167"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.7607626493971167""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.7607626493971167
""",
)

entry(
    index = 216,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.09262e+12,'s^-1'), n=0.959391, w0=(301000,'J/mol'), E0=(58118.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 217,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.62084e+20,'s^-1'), n=-1.30974, w0=(301000,'J/mol'), E0=(76340.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0002492671673462578, var=2.8119119786495776, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 3.3623177551763774"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.3623177551763774""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.3623177551763774
""",
)

entry(
    index = 218,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.17307e+18,'s^-1'), n=-1.10556, w0=(301000,'J/mol'), E0=(72810.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 219,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.29933e+21,'s^-1'), n=-1.96263, w0=(301000,'J/mol'), E0=(76606.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00018183956361884684, var=2.776290608551626, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 3.3407874784766753"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.3407874784766753""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.3407874784766753
""",
)

entry(
    index = 220,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.80047e+18,'s^-1'), n=-0.900859, w0=(301000,'J/mol'), E0=(72284.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 221,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.65981e+22,'s^-1'), n=-2.06474, w0=(301000,'J/mol'), E0=(81164.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07729425214541201, var=4.099616655048709, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R',), comment="""BM rule fitted to 14 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 4.253296037681868"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.253296037681868""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.253296037681868
""",
)

entry(
    index = 222,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(8.06743e+24,'s^-1'), n=-2.74573, w0=(301000,'J/mol'), E0=(97215.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06337250000451, var=2.451416334798664, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 3.2980409982614693"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 3.2980409982614693""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 3.2980409982614693
""",
)

entry(
    index = 223,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.29951e+16,'s^-1'), n=-0.647716, w0=(301000,'J/mol'), E0=(73729.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.009102064824380644, var=1.3511286054844016, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.353134625341714"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.353134625341714""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.353134625341714
""",
)

entry(
    index = 224,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.40861e+20,'s^-1'), n=-2.03669, w0=(301000,'J/mol'), E0=(91201.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06141157912551048, var=4.07743773557241, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R',), comment="""BM rule fitted to 14 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 4.202395100061841"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.202395100061841""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 4.202395100061841
""",
)

entry(
    index = 225,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(6.7595e+24,'s^-1'), n=-2.60805, w0=(301000,'J/mol'), E0=(104908,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04557442268221559, var=2.3893956209176452, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 3.213361927786928"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.213361927786928""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.213361927786928
""",
)

entry(
    index = 226,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(69277.6,'s^-1'), n=2.38386, w0=(301000,'J/mol'), E0=(44136,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 227,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.57815e+16,'s^-1'), n=-0.589969, w0=(301000,'J/mol'), E0=(81905.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.002202631918217346, var=1.3345456356949297, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.32145505540818"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.32145505540818""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.32145505540818
""",
)

entry(
    index = 228,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.76449e+29,'s^-1'), n=-3.92737, w0=(301000,'J/mol'), E0=(91938.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09186149813139446, var=1.6308739264655487, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.7909682340390534"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.7909682340390534""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.7909682340390534
""",
)

entry(
    index = 229,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(8.9146e+19,'s^-1'), n=-2.05152, w0=(301000,'J/mol'), E0=(55861.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.234774857494195, var=3.464328308741308, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 6.8338038845914895"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.8338038845914895""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.8338038845914895
""",
)

entry(
    index = 230,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.07803e+23,'s^-1'), n=-2.47886, w0=(301000,'J/mol'), E0=(74309.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06891691470379513, var=1.9847384174215192, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 2.9974437796684272"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.9974437796684272""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.9974437796684272
""",
)

entry(
    index = 231,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.10114e+19,'s^-1'), n=-1.23723, w0=(301000,'J/mol'), E0=(65831.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.002062301431935204, var=3.2309330453281757, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 3.608652141028271"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.608652141028271""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.608652141028271
""",
)

entry(
    index = 232,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(4.97172e+15,'s^-1'), n=-0.52909, w0=(301000,'J/mol'), E0=(60563,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 233,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(7.29458e+26,'s^-1'), n=-3.43865, w0=(301000,'J/mol'), E0=(93241.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03549380923082306, var=2.1728632515688644, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 3.044287263644485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 3.044287263644485""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 3.044287263644485
""",
)

entry(
    index = 234,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.32766e+20,'s^-1'), n=-2.00621, w0=(301000,'J/mol'), E0=(77581,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.006166109840807219, var=11.981355128126165, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.954701606834411"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.954701606834411""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.954701606834411
""",
)

entry(
    index = 235,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.36889e+11,'s^-1'), n=0.648844, w0=(301000,'J/mol'), E0=(51436.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 236,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(7.7695e+10,'s^-1'), n=0.853563, w0=(301000,'J/mol'), E0=(48721.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 237,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.7137e+18,'s^-1'), n=-1.45639, w0=(301000,'J/mol'), E0=(68486.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.9142202704983267, var=19.296930668970724, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 16.12861622846927"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 16.12861622846927""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 16.12861622846927
""",
)

entry(
    index = 238,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.19952e+17,'s^-1'), n=-0.69138, w0=(301000,'J/mol'), E0=(114297,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02908598358993157, var=1.6746512450294533, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.6673742802135485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.6673742802135485""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.6673742802135485
""",
)

entry(
    index = 239,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(8.82144e-30,'s^-1'), n=12.7446, w0=(301000,'J/mol'), E0=(-1887.94,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1474709012249327, var=1.8339188119089767, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 5.5979502370116325"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 5.5979502370116325""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 5.5979502370116325
""",
)

entry(
    index = 240,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.82644e+18,'s^-1'), n=-0.990842, w0=(301000,'J/mol'), E0=(112564,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0007124573966298415, var=11.32975822266313, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.7496694677238915"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.7496694677238915""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.7496694677238915
""",
)

entry(
    index = 241,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(4.46442e+13,'s^-1'), n=0.291051, w0=(301000,'J/mol'), E0=(101026,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 242,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(2.52796e+13,'s^-1'), n=0.495753, w0=(301000,'J/mol'), E0=(100218,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 243,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(6.44785e+10,'s^-1'), n=1.32596, w0=(301000,'J/mol'), E0=(98238.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 244,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(6.76829e+12,'s^-1'), n=0.409624, w0=(301000,'J/mol'), E0=(104262,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 245,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.06814e+14,'s^-1'), n=0.262343, w0=(301000,'J/mol'), E0=(101514,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0048462490646080285, var=1.2602770579604412, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.2627334420567817"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.2627334420567817""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.2627334420567817
""",
)

entry(
    index = 246,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(7.15905e+13,'s^-1'), n=0.14721, w0=(301000,'J/mol'), E0=(106367,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.002146353916199347, var=1.5583657219598064, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 2.507994247001181"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.507994247001181""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.507994247001181
""",
)

entry(
    index = 247,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(4.87286e+12,'s^-1'), n=0.925024, w0=(301000,'J/mol'), E0=(103903,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00021363315132660144, var=4.1138932265119825, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 4.066687717519018"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 4.066687717519018""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 4.066687717519018
""",
)

entry(
    index = 248,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.03895e+14,'s^-1'), n=0.223774, w0=(301000,'J/mol'), E0=(130619,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00018278289852354375, var=4.473944177869778, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 4.24081477037214"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 4.24081477037214""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 4.24081477037214
""",
)

entry(
    index = 249,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-2R!H-R_Ext-7R!H-R_Sp-9R!H=7R!H",
    kinetics = ArrheniusBM(A=(2.23824e+12,'s^-1'), n=0.414446, w0=(301000,'J/mol'), E0=(105242,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-2R!H-R_Ext-7R!H-R_Sp-9R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-2R!H-R_Ext-7R!H-R_Sp-9R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-2R!H-R_Ext-7R!H-R_Sp-9R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-2R!H-R_Ext-7R!H-R_Sp-9R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 250,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-2R!H-R_Ext-7R!H-R_N-Sp-9R!H=7R!H",
    kinetics = ArrheniusBM(A=(3.38227e+14,'s^-1'), n=-0.351906, w0=(301000,'J/mol'), E0=(110333,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-2R!H-R_Ext-7R!H-R_N-Sp-9R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-2R!H-R_Ext-7R!H-R_N-Sp-9R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-2R!H-R_Ext-7R!H-R_N-Sp-9R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-2R!H-R_Ext-2R!H-R_Ext-7R!H-R_N-Sp-9R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 251,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(9.44323e+13,'s^-1'), n=0.0512565, w0=(301000,'J/mol'), E0=(35367.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 252,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(9.87852e+15,'s^-1'), n=-0.865083, w0=(301000,'J/mol'), E0=(41162,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_Sp-9R!H=5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 253,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_Ext-3R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.24986e+16,'s^-1'), n=-0.0593803, w0=(301000,'J/mol'), E0=(23874.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_Ext-3R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 254,
    label = "Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.30979e+18,'s^-1'), n=-0.975665, w0=(301000,'J/mol'), E0=(30261.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Int-4R!H-1R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-6R!H-R_Ext-2R!H-R_Ext-5R!H-R_N-Sp-9R!H=5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 255,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.57081e+17,'s^-1'), n=-0.582178, w0=(301000,'J/mol'), E0=(64324.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-9.819297116927277e-06, var=1.8338835792608799, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 2.714856113364469"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 2.714856113364469""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 2.714856113364469
""",
)

entry(
    index = 256,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(9.87591e+15,'s^-1'), n=-0.151522, w0=(301000,'J/mol'), E0=(49204.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 257,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.42762e+16,'s^-1'), n=-0.476966, w0=(301000,'J/mol'), E0=(74671.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0005307494519622844, var=10.956474011712196, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.63711990853835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.63711990853835""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.63711990853835
""",
)

entry(
    index = 258,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(2.72793e+13,'s^-1'), n=0.30141, w0=(301000,'J/mol'), E0=(66024.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 259,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.52635e+13,'s^-1'), n=0.507892, w0=(301000,'J/mol'), E0=(65912.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 260,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(5.26579e+15,'s^-1'), n=-0.660714, w0=(301000,'J/mol'), E0=(75500.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.001121825018242827, var=1.8580168622537574, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 2.7354548412878517"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 2.7354548412878517""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 2.7354548412878517
""",
)

entry(
    index = 261,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.45164e+13,'s^-1'), n=-0.0408852, w0=(301000,'J/mol'), E0=(60326.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 262,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.01908e+16,'s^-1'), n=-0.454829, w0=(301000,'J/mol'), E0=(81898.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0006137164935577922, var=10.947677721711571, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.634664097919853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.634664097919853""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.634664097919853
""",
)

entry(
    index = 263,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.28717e+13,'s^-1'), n=0.505166, w0=(301000,'J/mol'), E0=(71319.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 264,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(7.29565e+12,'s^-1'), n=0.709876, w0=(301000,'J/mol'), E0=(71271,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 265,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(7.36057e+17,'s^-1'), n=-0.605267, w0=(301000,'J/mol'), E0=(73035.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 266,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(7.72011e+19,'s^-1'), n=-1.52161, w0=(301000,'J/mol'), E0=(78751.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 267,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(6.92862e+24,'s^-1'), n=-2.6107, w0=(301000,'J/mol'), E0=(89086.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0560344146696126, var=2.3399992343720717, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 3.207444468680412"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 3.207444468680412""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 3.207444468680412
""",
)

entry(
    index = 268,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.44981e+16,'s^-1'), n=-0.643643, w0=(301000,'J/mol'), E0=(66371.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01420604867188097, var=1.3273619699201382, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.3453728502694235"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.3453728502694235""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.3453728502694235
""",
)

entry(
    index = 269,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.9234e+23,'s^-1'), n=-2.3452, w0=(301000,'J/mol'), E0=(93971.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.023753391631946418, var=1.3555344792656274, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.393743274202598"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.393743274202598""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.393743274202598
""",
)

entry(
    index = 270,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(3.48375e+17,'s^-1'), n=-0.9783, w0=(301000,'J/mol'), E0=(77411.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.016350818607411974, var=2.0662191346408814, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 2.922758654230613"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 2.922758654230613""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 2.922758654230613
""",
)

entry(
    index = 271,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.63155e+10,'s^-1'), n=1.20189, w0=(301000,'J/mol'), E0=(56084.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 272,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.4756e+23,'s^-1'), n=-2.62995, w0=(301000,'J/mol'), E0=(99579.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.043875224171624407, var=2.3228564849233253, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 3.165639990051401"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 3.165639990051401""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 3.165639990051401
""",
)

entry(
    index = 273,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.58486e+15,'s^-1'), n=-0.702485, w0=(301000,'J/mol'), E0=(77141.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.007502320040109182, var=1.3220116718397823, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.323869711538385"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.323869711538385""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.323869711538385
""",
)

entry(
    index = 274,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(9.22699e+23,'s^-1'), n=-2.30727, w0=(301000,'J/mol'), E0=(102674,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.015651283059384864, var=1.3371586092939527, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.357511756014797"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.357511756014797""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.357511756014797
""",
)

entry(
    index = 275,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(6.83381e+17,'s^-1'), n=-0.949385, w0=(301000,'J/mol'), E0=(86072.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.010463684716072725, var=2.0530426345503, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 2.8987637863922577"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 2.8987637863922577""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 2.8987637863922577
""",
)

entry(
    index = 276,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.70376e+09,'s^-1'), n=1.40565, w0=(301000,'J/mol'), E0=(62219.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 277,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(5.75022e+29,'s^-1'), n=-4.0193, w0=(301000,'J/mol'), E0=(91826,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0727495587039281, var=1.9720391407475264, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 2.998023493894198"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 2.998023493894198""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 2.998023493894198
""",
)

entry(
    index = 278,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.23692e+26,'s^-1'), n=-2.86304, w0=(301000,'J/mol'), E0=(84604.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0011969443941186747, var=3.1594162146479934, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 3.56637322495906"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.56637322495906""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.56637322495906
""",
)

entry(
    index = 279,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(6.20502e+22,'s^-1'), n=-2.03421, w0=(301000,'J/mol'), E0=(87662,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 280,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.29705e+23,'s^-1'), n=-2.43227, w0=(301000,'J/mol'), E0=(75547.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08454548078835142, var=3.6881143124811877, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 4.062412060687941"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 4.062412060687941""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 4.062412060687941
""",
)

entry(
    index = 281,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(8.33802e+22,'s^-1'), n=-2.5167, w0=(301000,'J/mol'), E0=(72961.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.040124557295859085, var=2.017667225187021, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 2.9484336649170406"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 2.9484336649170406""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 2.9484336649170406
""",
)

entry(
    index = 282,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.89792e+15,'s^-1'), n=-0.20507, w0=(301000,'J/mol'), E0=(58071.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 283,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.36065e+27,'s^-1'), n=-3.59519, w0=(301000,'J/mol'), E0=(95526.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.862187631420674, var=8.836617679938765, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 15.66335452006777"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 15.66335452006777""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 15.66335452006777
""",
)

entry(
    index = 284,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.70536e+18,'s^-1'), n=-0.856274, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 285,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(9.6807e+17,'s^-1'), n=-0.65145, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 286,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(3.18811e+10,'s^-1'), n=1.14913, w0=(301000,'J/mol'), E0=(48865.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 287,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(3.33119e+12,'s^-1'), n=0.232795, w0=(301000,'J/mol'), E0=(57663.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 288,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.19799e+16,'s^-1'), n=-0.355719, w0=(301000,'J/mol'), E0=(118084,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.011865873265800709, var=1.4545832985923797, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 2.447646679464952"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 2.447646679464952""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 2.447646679464952
""",
)

entry(
    index = 289,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(9.31635e+17,'s^-1'), n=-1.01043, w0=(301000,'J/mol'), E0=(104496,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.000559583766845431, var=11.274287844829875, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.732746321102405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.732746321102405""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.732746321102405
""",
)

entry(
    index = 290,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(4.43732e+15,'s^-1'), n=-0.424245, w0=(301000,'J/mol'), E0=(100587,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 291,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(2.51385e+15,'s^-1'), n=-0.219549, w0=(301000,'J/mol'), E0=(99873.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 292,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(2.38703e+15,'s^-1'), n=0.186404, w0=(301000,'J/mol'), E0=(117027,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0015882467459529036, var=1.949799653610085, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 2.803306939805965"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 2.803306939805965""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 2.803306939805965
""",
)

entry(
    index = 293,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(5.75663e+16,'s^-1'), n=-0.538121, w0=(301000,'J/mol'), E0=(140517,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0008651388266666973, var=2.0192128598890293, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 2.8508824106345907"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 2.8508824106345907""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 2.8508824106345907
""",
)

entry(
    index = 294,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.03843e+13,'s^-1'), n=0.791339, w0=(301000,'J/mol'), E0=(100865,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 295,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.08637e+15,'s^-1'), n=-0.125, w0=(301000,'J/mol'), E0=(106814,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 296,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.21032e+14,'s^-1'), n=0.293805, w0=(301000,'J/mol'), E0=(107242,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0018531927242476979, var=1.5270258644031014, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 2.4819652946356903"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.4819652946356903""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 2.4819652946356903
""",
)

entry(
    index = 297,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-8R!H-R_Sp-10R!H=8R!H",
    kinetics = ArrheniusBM(A=(2.82238e+12,'s^-1'), n=0.620659, w0=(301000,'J/mol'), E0=(103165,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-8R!H-R_Sp-10R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-8R!H-R_Sp-10R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-8R!H-R_Sp-10R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-8R!H-R_Sp-10R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 298,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-8R!H-R_N-Sp-10R!H=8R!H",
    kinetics = ArrheniusBM(A=(4.27425e+14,'s^-1'), n=-0.145693, w0=(301000,'J/mol'), E0=(108274,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-8R!H-R_N-Sp-10R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-8R!H-R_N-Sp-10R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-8R!H-R_N-Sp-10R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-8R!H-R_N-Sp-10R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 299,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.35797e+11,'s^-1'), n=1.36739, w0=(301000,'J/mol'), E0=(98108.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 300,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.11701e+11,'s^-1'), n=0.976492, w0=(301000,'J/mol'), E0=(123434,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 301,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.2543e+17,'s^-1'), n=-0.636829, w0=(301000,'J/mol'), E0=(66162.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0010849254331593275, var=10.807656007387248, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.5932924362593335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.5932924362593335""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.5932924362593335
""",
)

entry(
    index = 302,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(1.16103e+17,'s^-1'), n=-0.605747, w0=(301000,'J/mol'), E0=(65073.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 303,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(6.56487e+16,'s^-1'), n=-0.400966, w0=(301000,'J/mol'), E0=(65197.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 304,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(6.34506e+12,'s^-1'), n=0.801699, w0=(301000,'J/mol'), E0=(66862.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 305,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(6.59091e+14,'s^-1'), n=-0.113648, w0=(301000,'J/mol'), E0=(72393.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 306,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.20152e+16,'s^-1'), n=-0.727486, w0=(301000,'J/mol'), E0=(77403.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0008356883851322521, var=10.875776934663024, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.613403839476542"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.613403839476542""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.613403839476542
""",
)

entry(
    index = 307,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(8.75457e+14,'s^-1'), n=-0.495111, w0=(301000,'J/mol'), E0=(74733.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 308,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(4.9716e+14,'s^-1'), n=-0.290415, w0=(301000,'J/mol'), E0=(74771.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 309,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(2.99234e+12,'s^-1'), n=1.00545, w0=(301000,'J/mol'), E0=(72244.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 310,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(3.1234e+14,'s^-1'), n=0.0891152, w0=(301000,'J/mol'), E0=(77769.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 311,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.09934e+24,'s^-1'), n=-2.32924, w0=(301000,'J/mol'), E0=(87039.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0294002109527691, var=1.331879419136236, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.387476098030387"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.387476098030387""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.387476098030387
""",
)

entry(
    index = 312,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(9.77271e+17,'s^-1'), n=-0.995808, w0=(301000,'J/mol'), E0=(70630.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.025514430550122712, var=2.0413435466461762, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 2.9283837667848176"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 2.9283837667848176""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 2.9283837667848176
""",
)

entry(
    index = 313,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(6.93044e+13,'s^-1'), n=0.294737, w0=(301000,'J/mol'), E0=(57907.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 314,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(5.08574e+24,'s^-1'), n=-2.63126, w0=(301000,'J/mol'), E0=(96885.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.027014097927145677, var=2.0729627415154823, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 2.9542495069225603"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 2.9542495069225603""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 2.9542495069225603
""",
)

entry(
    index = 315,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.02641e+17,'s^-1'), n=-0.303224, w0=(301000,'J/mol'), E0=(83207.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 316,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.51078e+18,'s^-1'), n=-1.1271, w0=(301000,'J/mol'), E0=(79585,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0020504093306339143, var=11.5044844254768, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.804864580584883"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.804864580584883""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.804864580584883
""",
)

entry(
    index = 317,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(1.92241e+11,'s^-1'), n=0.747669, w0=(301000,'J/mol'), E0=(61688.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 318,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(1.07946e+11,'s^-1'), n=0.953224, w0=(301000,'J/mol'), E0=(60459.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 319,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.26247e+22,'s^-1'), n=-2.38951, w0=(301000,'J/mol'), E0=(97936,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.020964916846735526, var=1.325545391265222, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 2.3607739190553776"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.3607739190553776""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 2.3607739190553776
""",
)

entry(
    index = 320,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(2.55583e+16,'s^-1'), n=-1.04136, w0=(301000,'J/mol'), E0=(81317.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.016410685364781172, var=2.031696564626386, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 2.8987340191810187"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 2.8987340191810187""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 2.8987340191810187
""",
)

entry(
    index = 321,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.23375e+11,'s^-1'), n=0.405374, w0=(301000,'J/mol'), E0=(67053.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 322,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(1.33537e+25,'s^-1'), n=-2.63532, w0=(301000,'J/mol'), E0=(106167,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.021444508594592824, var=2.0561277848331847, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 2.9285112487712768"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 2.9285112487712768""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 2.9285112487712768
""",
)

entry(
    index = 323,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(9.56071e+16,'s^-1'), n=-0.0994679, w0=(301000,'J/mol'), E0=(89488.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 324,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.77813e+18,'s^-1'), n=-1.08963, w0=(301000,'J/mol'), E0=(88211,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0014829163919686623, var=11.487973137324694, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.798557477603881"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.798557477603881""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.798557477603881
""",
)

entry(
    index = 325,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(9.0533e+10,'s^-1'), n=0.951426, w0=(301000,'J/mol'), E0=(68621.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 326,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(5.12981e+10,'s^-1'), n=1.15612, w0=(301000,'J/mol'), E0=(67536.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 327,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(6.15952e+29,'s^-1'), n=-3.95853, w0=(301000,'J/mol'), E0=(92912.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.087742805177679, var=3.6600418862153705, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 4.055765285928821"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 4.055765285928821""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 4.055765285928821
""",
)

entry(
    index = 328,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(5.32611e+29,'s^-1'), n=-4.07922, w0=(301000,'J/mol'), E0=(90716,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04793102153416596, var=2.005033584088962, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 2.9591187039680538"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 2.9591187039680538""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 2.9591187039680538
""",
)

entry(
    index = 329,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.36108e+22,'s^-1'), n=-1.71019, w0=(301000,'J/mol'), E0=(85260,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 330,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.32321e+22,'s^-1'), n=-2.05653, w0=(301000,'J/mol'), E0=(74206.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.004341089481420559, var=3.5761523957011194, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 3.8020051480874866"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.8020051480874866""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.8020051480874866
""",
)

entry(
    index = 331,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.23081e+16,'s^-1'), n=-0.659296, w0=(301000,'J/mol'), E0=(60998.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 332,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.28171e+23,'s^-1'), n=-2.66701, w0=(301000,'J/mol'), E0=(73392.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0030126504871066918, var=3.4582411245674387, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 3.735644337753276"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.735644337753276""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 3.735644337753276
""",
)

entry(
    index = 333,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.26167e+16,'s^-1'), n=-0.4546, w0=(301000,'J/mol'), E0=(59086.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 334,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(3.97593e+17,'s^-1'), n=-0.355987, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 335,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(4.13722e+19,'s^-1'), n=-1.27229, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-3R!H-R_N-3R!H-inRing_Ext-7R!H-R_Ext-1R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 336,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H",
    kinetics = ArrheniusBM(A=(2.29119e+15,'s^-1'), n=-0.0602093, w0=(301000,'J/mol'), E0=(118075,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.009810771313654135, var=1.9393012882887934, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H
    Total Standard Deviation in ln(k): 2.8164201555409343"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H
Total Standard Deviation in ln(k): 2.8164201555409343""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H
Total Standard Deviation in ln(k): 2.8164201555409343
""",
)

entry(
    index = 337,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H",
    kinetics = ArrheniusBM(A=(7.29633e+16,'s^-1'), n=-0.670209, w0=(301000,'J/mol'), E0=(118256,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.015561603635189117, var=1.9611483980008724, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H
    Total Standard Deviation in ln(k): 2.8465507209100953"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H
Total Standard Deviation in ln(k): 2.8465507209100953""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H
Total Standard Deviation in ln(k): 2.8465507209100953
""",
)

entry(
    index = 338,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.03208e+15,'s^-1'), n=0.0760431, w0=(301000,'J/mol'), E0=(100556,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 339,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.08046e+17,'s^-1'), n=-0.840296, w0=(301000,'J/mol'), E0=(106414,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 340,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.95755e+15,'s^-1'), n=0.0718856, w0=(301000,'J/mol'), E0=(119103,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.43775758304243e-05, var=11.138263984309047, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.690797301588019"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.690797301588019""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.690797301588019
""",
)

entry(
    index = 341,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(2.78045e+12,'s^-1'), n=0.913163, w0=(301000,'J/mol'), E0=(107679,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 342,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.57353e+12,'s^-1'), n=1.11786, w0=(301000,'J/mol'), E0=(107261,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 343,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.28045e+17,'s^-1'), n=-0.675098, w0=(301000,'J/mol'), E0=(142652,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0006640509199638254, var=11.338282734925793, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.752085918956684"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.752085918956684""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.752085918956684
""",
)

entry(
    index = 344,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(6.00853e+12,'s^-1'), n=0.522266, w0=(301000,'J/mol'), E0=(130366,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 345,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(3.40068e+12,'s^-1'), n=0.727115, w0=(301000,'J/mol'), E0=(129538,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 346,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-11R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.07466e+12,'s^-1'), n=0.944678, w0=(301000,'J/mol'), E0=(101817,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-11R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-11R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-11R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-11R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 347,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-11R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.62404e+14,'s^-1'), n=0.178327, w0=(301000,'J/mol'), E0=(106823,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-11R!H=8R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-11R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-11R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-11R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 348,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(2.69684e+16,'s^-1'), n=-0.10546, w0=(301000,'J/mol'), E0=(66285.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 349,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(2.8234e+18,'s^-1'), n=-1.02176, w0=(301000,'J/mol'), E0=(71810.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 350,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(2.03427e+14,'s^-1'), n=0.00517707, w0=(301000,'J/mol'), E0=(75814.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 351,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(2.13462e+16,'s^-1'), n=-0.911162, w0=(301000,'J/mol'), E0=(81377.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Int-5R!H-2R!H_Sp-5R!H-2R!H_N-Sp-5R!H=4R!H_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H#6R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 352,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(1.51884e+25,'s^-1'), n=-2.65274, w0=(301000,'J/mol'), E0=(90539.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.037922113350206905, var=2.0521014269302005, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 2.967096301817214"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 2.967096301817214""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 2.967096301817214
""",
)

entry(
    index = 353,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(8.63539e+20,'s^-1'), n=-1.21038, w0=(301000,'J/mol'), E0=(85516.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 354,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(3.86893e+18,'s^-1'), n=-1.13265, w0=(301000,'J/mol'), E0=(72744.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0011559595341792614, var=11.414066387782425, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.775843769283948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.775843769283948""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.775843769283948
""",
)

entry(
    index = 355,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(8.18652e+14,'s^-1'), n=-0.159488, w0=(301000,'J/mol'), E0=(65299.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 356,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(4.62101e+14,'s^-1'), n=0.045236, w0=(301000,'J/mol'), E0=(64390,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 357,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.10175e+25,'s^-1'), n=-2.77411, w0=(301000,'J/mol'), E0=(98998.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0013746334521603457, var=11.486610753320253, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.797882490959338"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.797882490959338""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.797882490959338
""",
)

entry(
    index = 358,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(2.38677e+18,'s^-1'), n=-0.757449, w0=(301000,'J/mol'), E0=(88785.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 359,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(1.33662e+18,'s^-1'), n=-0.55126, w0=(301000,'J/mol'), E0=(87627.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 360,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(4.45478e+10,'s^-1'), n=1.24796, w0=(301000,'J/mol'), E0=(60966.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 361,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(4.65769e+12,'s^-1'), n=0.332065, w0=(301000,'J/mol'), E0=(67391.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 362,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(4.5302e+23,'s^-1'), n=-2.71328, w0=(301000,'J/mol'), E0=(101518,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.028572636062182615, var=2.0443819357849, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 2.938198540154458"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 2.938198540154458""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 2.938198540154458
""",
)

entry(
    index = 363,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(6.51964e+18,'s^-1'), n=-1.09974, w0=(301000,'J/mol'), E0=(94653,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 364,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(9.80785e+16,'s^-1'), n=-1.17424, w0=(301000,'J/mol'), E0=(83410.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0009479676817935084, var=11.38502243766765, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.766698561267946"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.766698561267946""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.766698561267946
""",
)

entry(
    index = 365,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(6.17024e+12,'s^-1'), n=-0.0488511, w0=(301000,'J/mol'), E0=(74501.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 366,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(3.49177e+12,'s^-1'), n=0.155845, w0=(301000,'J/mol'), E0=(73630.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 367,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.21317e+25,'s^-1'), n=-2.77047, w0=(301000,'J/mol'), E0=(108249,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.001098231509860889, var=11.458677493170448, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.788921603765807"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.788921603765807""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.788921603765807
""",
)

entry(
    index = 368,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(1.12444e+18,'s^-1'), n=-0.553693, w0=(301000,'J/mol'), E0=(95618.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 369,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(6.37909e+17,'s^-1'), n=-0.348973, w0=(301000,'J/mol'), E0=(94594.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 370,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(2.10245e+10,'s^-1'), n=1.45171, w0=(301000,'J/mol'), E0=(68097.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 371,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H",
    kinetics = ArrheniusBM(A=(2.20145e+12,'s^-1'), n=0.535374, w0=(301000,'J/mol'), E0=(74340.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 372,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.96379e+29,'s^-1'), n=-3.65522, w0=(301000,'J/mol'), E0=(92254.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.47012617998688, var=3.220425865930785, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 14.829079175442843"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 14.829079175442843""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 14.829079175442843
""",
)

entry(
    index = 373,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.77579e+23,'s^-1'), n=-2.16441, w0=(301000,'J/mol'), E0=(88999.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 374,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(8.7255e+29,'s^-1'), n=-4.23703, w0=(301000,'J/mol'), E0=(91247.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.627082866528892, var=30.649268390692093, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 17.699281230593"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 17.699281230593""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 17.699281230593
""",
)

entry(
    index = 375,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.57477e+23,'s^-1'), n=-1.95972, w0=(301000,'J/mol'), E0=(87417.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 376,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(5.18859e+15,'s^-1'), n=-0.159008, w0=(301000,'J/mol'), E0=(59408.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_Sp-9R!H=8R!H_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 377,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(5.42947e+17,'s^-1'), n=-1.07535, w0=(301000,'J/mol'), E0=(66851.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-3R!H-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 378,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(7.40655e+15,'s^-1'), n=-0.170972, w0=(301000,'J/mol'), E0=(120130,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.6893931627925045e-05, var=11.088813489256335, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.675784214026999"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.675784214026999""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.675784214026999
""",
)

entry(
    index = 379,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.26628e+13,'s^-1'), n=0.490453, w0=(301000,'J/mol'), E0=(111600,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 380,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(7.17896e+12,'s^-1'), n=0.695149, w0=(301000,'J/mol'), E0=(111217,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 381,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(2.42048e+17,'s^-1'), n=-0.784503, w0=(301000,'J/mol'), E0=(120289,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00016566863256245584, var=11.152454598868927, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.695287378329075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.695287378329075""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.695287378329075
""",
)

entry(
    index = 382,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.91381e+15,'s^-1'), n=-0.275899, w0=(301000,'J/mol'), E0=(115891,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 383,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.08784e+15,'s^-1'), n=-0.0712026, w0=(301000,'J/mol'), E0=(115409,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 384,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(6.46468e+11,'s^-1'), n=1.41345, w0=(301000,'J/mol'), E0=(108063,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 385,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(6.75088e+13,'s^-1'), n=0.497112, w0=(301000,'J/mol'), E0=(113706,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 386,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.39722e+12,'s^-1'), n=1.02255, w0=(301000,'J/mol'), E0=(130185,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 387,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(1.46093e+14,'s^-1'), n=0.106254, w0=(301000,'J/mol'), E0=(136170,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 388,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.7996e+25,'s^-1'), n=-2.78541, w0=(301000,'J/mol'), E0=(92591.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0009156437966328335, var=11.41195086900182, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.774612272926218"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.774612272926218""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.774612272926218
""",
)

entry(
    index = 389,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H",
    kinetics = ArrheniusBM(A=(1.01588e+22,'s^-1'), n=-1.66461, w0=(301000,'J/mol'), E0=(92371.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 390,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H",
    kinetics = ArrheniusBM(A=(5.7533e+21,'s^-1'), n=-1.45977, w0=(301000,'J/mol'), E0=(91430.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 391,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(1.90153e+14,'s^-1'), n=0.3408, w0=(301000,'J/mol'), E0=(65009.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 392,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(1.98897e+16,'s^-1'), n=-0.575535, w0=(301000,'J/mol'), E0=(71060.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 393,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(5.55001e+17,'s^-1'), n=-0.257157, w0=(301000,'J/mol'), E0=(88166.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 394,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(5.77567e+19,'s^-1'), n=-1.17267, w0=(301000,'J/mol'), E0=(94498.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-1R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 395,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.67568e+24,'s^-1'), n=-2.84179, w0=(301000,'J/mol'), E0=(103553,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.000805747787417602, var=11.399158027453673, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.770539193973906"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.770539193973906""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.770539193973906
""",
)

entry(
    index = 396,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H",
    kinetics = ArrheniusBM(A=(7.66726e+19,'s^-1'), n=-1.55397, w0=(301000,'J/mol'), E0=(101606,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Sp-12R!H=11R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 397,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H",
    kinetics = ArrheniusBM(A=(4.35297e+19,'s^-1'), n=-1.34927, w0=(301000,'J/mol'), E0=(100699,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_N-Sp-12R!H=11R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 398,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(1.43322e+12,'s^-1'), n=0.451436, w0=(301000,'J/mol'), E0=(74265.6,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 399,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(1.50046e+14,'s^-1'), n=-0.464903, w0=(301000,'J/mol'), E0=(80276.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 400,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(2.62626e+17,'s^-1'), n=-0.0534056, w0=(301000,'J/mol'), E0=(95167.3,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 401,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H",
    kinetics = ArrheniusBM(A=(2.74094e+19,'s^-1'), n=-0.969741, w0=(301000,'J/mol'), E0=(101351,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-6R!H-R_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 402,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(6.47109e+22,'s^-1'), n=-1.66413, w0=(301000,'J/mol'), E0=(30100,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 403,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(6.77048e+24,'s^-1'), n=-2.58047, w0=(301000,'J/mol'), E0=(94775.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_N-3R!H-inRing_Ext-1R!H-R_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H_Ext-3R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 404,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-3R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(2.93835e+12,'s^-1'), n=0.99074, w0=(301000,'J/mol'), E0=(112036,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-3R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-3R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 405,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(3.07795e+14,'s^-1'), n=0.0744011, w0=(301000,'J/mol'), E0=(117660,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_Sp-11R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 406,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-3R!H-R_Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(4.44916e+14,'s^-1'), n=0.224389, w0=(301000,'J/mol'), E0=(116184,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-3R!H-R_Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-3R!H-R_Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-3R!H-R_Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 407,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=7R!H",
    kinetics = ArrheniusBM(A=(4.65585e+16,'s^-1'), n=-0.69195, w0=(301000,'J/mol'), E0=(121865,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=7R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=7R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_N-Sp-5R!H-4R!H_N-3R!H-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-2R!H-R_Ext-2R!H-R_Ext-9R!H-R_N-Sp-11R!H=9R!H_Ext-3R!H-R_N-Sp-8R!H=7R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 408,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R_Sp-12R!H=11R!H",
    kinetics = ArrheniusBM(A=(2.36098e+21,'s^-1'), n=-1.16432, w0=(301000,'J/mol'), E0=(92045.9,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R_Sp-12R!H=11R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R_Sp-12R!H=11R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R_Sp-12R!H=11R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R_Sp-12R!H=11R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 409,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R_N-Sp-12R!H=11R!H",
    kinetics = ArrheniusBM(A=(2.47204e+23,'s^-1'), n=-2.08061, w0=(301000,'J/mol'), E0=(98127.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R_N-Sp-12R!H=11R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R_N-Sp-12R!H=11R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R_N-Sp-12R!H=11R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R_N-Sp-12R!H=11R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 410,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R_Sp-12R!H=11R!H",
    kinetics = ArrheniusBM(A=(1.78333e+19,'s^-1'), n=-1.05368, w0=(301000,'J/mol'), E0=(101327,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R_Sp-12R!H=11R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R_Sp-12R!H=11R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R_Sp-12R!H=11R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R_Sp-12R!H=11R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 411,
    label = "Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R_N-Sp-12R!H=11R!H",
    kinetics = ArrheniusBM(A=(1.86694e+21,'s^-1'), n=-1.97002, w0=(301000,'J/mol'), E0=(107376,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R_N-Sp-12R!H=11R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R_N-Sp-12R!H=11R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R_N-Sp-12R!H=11R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-5R!H-=4R!H_Ext-5R!H-R_Sp-6R!H-5R!H_Sp-5R!H-4R!H_Sp-4R!H-2R!H_Ext-2R!H-R_Ext-7R!H-R_N-Sp-8R!H#7R!H_Ext-2R!H-R_Ext-1R!H-R_Ext-3R!H-R_Ext-11R!H-R_Ext-3R!H-R_N-Sp-12R!H=11R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

