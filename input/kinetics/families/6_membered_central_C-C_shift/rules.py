#!/usr/bin/env python
# encoding: utf-8

name = "6_membered_central_C-C_shift/rules"
shortDesc = "Concerted shift of the central C-C bond in an 1,5-unsaturated hexane to between the end atoms"
longDesc = """
Taken from:

Miller, J. A.; Klippenstein, S. J., The Recombination of Propargyl Radicals and Other Reactions on a C6H6 Potential.
J. Phys. Chem. A 2003, 107, 7783-7799.
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.13773e+22,'s^-1'), n=-3.02809, w0=(842667,'J/mol'), E0=(163347,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1825953895891476, var=2.60951657451414, Tref=1000.0, N=12, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 12 training reactions at node Root
    Total Standard Deviation in ln(k): 3.697231066626578"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root
Total Standard Deviation in ln(k): 3.697231066626578""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root
Total Standard Deviation in ln(k): 3.697231066626578
""",
)

entry(
    index = 2,
    label = "Root_1C-inRing",
    kinetics = ArrheniusBM(A=(7.58009e+10,'s^-1'), n=0.238027, w0=(846500,'J/mol'), E0=(131218,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.694537898310487e-06, var=0.32888118814627954, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1C-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_1C-inRing
    Total Standard Deviation in ln(k): 1.1496930621167525"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1C-inRing
Total Standard Deviation in ln(k): 1.1496930621167525""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1C-inRing
Total Standard Deviation in ln(k): 1.1496930621167525
""",
)

entry(
    index = 3,
    label = "Root_N-1C-inRing",
    kinetics = ArrheniusBM(A=(2.45311e+23,'s^-1'), n=-3.40381, w0=(840750,'J/mol'), E0=(170054,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.19825376744628276, var=3.859701772032733, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1C-inRing',), comment="""BM rule fitted to 8 training reactions at node Root_N-1C-inRing
    Total Standard Deviation in ln(k): 4.436652379372542"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1C-inRing
Total Standard Deviation in ln(k): 4.436652379372542""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1C-inRing
Total Standard Deviation in ln(k): 4.436652379372542
""",
)

entry(
    index = 4,
    label = "Root_1C-inRing_Sp-4C-2C",
    kinetics = ArrheniusBM(A=(2.62657e+11,'s^-1'), n=0.120233, w0=(846500,'J/mol'), E0=(133795,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.8451975003243754e-15, var=1.7660153933651777, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1C-inRing_Sp-4C-2C',), comment="""BM rule fitted to 2 training reactions at node Root_1C-inRing_Sp-4C-2C
    Total Standard Deviation in ln(k): 2.664122753831894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1C-inRing_Sp-4C-2C
Total Standard Deviation in ln(k): 2.664122753831894""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1C-inRing_Sp-4C-2C
Total Standard Deviation in ln(k): 2.664122753831894
""",
)

entry(
    index = 5,
    label = "Root_1C-inRing_N-Sp-4C-2C",
    kinetics = ArrheniusBM(A=(2.31536e+10,'s^-1'), n=0.348564, w0=(846500,'J/mol'), E0=(128689,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.054398571613929e-15, var=0.14590362365658285, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1C-inRing_N-Sp-4C-2C',), comment="""BM rule fitted to 2 training reactions at node Root_1C-inRing_N-Sp-4C-2C
    Total Standard Deviation in ln(k): 0.7657553301974053"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1C-inRing_N-Sp-4C-2C
Total Standard Deviation in ln(k): 0.7657553301974053""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1C-inRing_N-Sp-4C-2C
Total Standard Deviation in ln(k): 0.7657553301974053
""",
)

entry(
    index = 6,
    label = "Root_N-1C-inRing_3C-inRing",
    kinetics = ArrheniusBM(A=(4.32278e+11,'s^-1'), n=0.113137, w0=(846500,'J/mol'), E0=(134018,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0025473768222647234, var=0.6073119847948238, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1C-inRing_3C-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_N-1C-inRing_3C-inRing
    Total Standard Deviation in ln(k): 1.568694985231892"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1C-inRing_3C-inRing
Total Standard Deviation in ln(k): 1.568694985231892""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1C-inRing_3C-inRing
Total Standard Deviation in ln(k): 1.568694985231892
""",
)

entry(
    index = 7,
    label = "Root_N-1C-inRing_N-3C-inRing",
    kinetics = ArrheniusBM(A=(1.30611e+11,'s^-1'), n=0.178888, w0=(835000,'J/mol'), E0=(155330,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0016457408915626127, var=0.24587185375674625, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1C-inRing_N-3C-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_N-1C-inRing_N-3C-inRing
    Total Standard Deviation in ln(k): 0.9981922775962153"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1C-inRing_N-3C-inRing
Total Standard Deviation in ln(k): 0.9981922775962153""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1C-inRing_N-3C-inRing
Total Standard Deviation in ln(k): 0.9981922775962153
""",
)

entry(
    index = 8,
    label = "Root_N-1C-inRing_3C-inRing_Sp-4C-2C",
    kinetics = ArrheniusBM(A=(7.10742e+10,'s^-1'), n=0.373744, w0=(846500,'J/mol'), E0=(130704,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.3933273817247035e-17, var=0.14590362365660145, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1C-inRing_3C-inRing_Sp-4C-2C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1C-inRing_3C-inRing_Sp-4C-2C
    Total Standard Deviation in ln(k): 0.7657553301974516"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1C-inRing_3C-inRing_Sp-4C-2C
Total Standard Deviation in ln(k): 0.7657553301974516""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1C-inRing_3C-inRing_Sp-4C-2C
Total Standard Deviation in ln(k): 0.7657553301974516
""",
)

entry(
    index = 9,
    label = "Root_N-1C-inRing_3C-inRing_N-Sp-4C-2C",
    kinetics = ArrheniusBM(A=(2.20493e+12,'s^-1'), n=-0.124849, w0=(846500,'J/mol'), E0=(137157,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.602528453014257e-15, var=1.7660153933655387, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1C-inRing_3C-inRing_N-Sp-4C-2C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1C-inRing_3C-inRing_N-Sp-4C-2C
    Total Standard Deviation in ln(k): 2.664122753832171"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1C-inRing_3C-inRing_N-Sp-4C-2C
Total Standard Deviation in ln(k): 2.664122753832171""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1C-inRing_3C-inRing_N-Sp-4C-2C
Total Standard Deviation in ln(k): 2.664122753832171
""",
)

entry(
    index = 10,
    label = "Root_N-1C-inRing_N-3C-inRing_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(1.38831e+11,'s^-1'), n=0.154516, w0=(835000,'J/mol'), E0=(157098,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.7573309526898815e-15, var=0.08030901615460162, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1C-inRing_N-3C-inRing_Sp-3C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1C-inRing_N-3C-inRing_Sp-3C-1C
    Total Standard Deviation in ln(k): 0.5681187753025234"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1C-inRing_N-3C-inRing_Sp-3C-1C
Total Standard Deviation in ln(k): 0.5681187753025234""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1C-inRing_N-3C-inRing_Sp-3C-1C
Total Standard Deviation in ln(k): 0.5681187753025234
""",
)

entry(
    index = 11,
    label = "Root_N-1C-inRing_N-3C-inRing_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(1.22879e+11,'s^-1'), n=0.203258, w0=(835000,'J/mol'), E0=(153562,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=8.786654763449407e-17, var=0.0803090161545758, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1C-inRing_N-3C-inRing_N-Sp-3C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1C-inRing_N-3C-inRing_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 0.5681187753024279"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1C-inRing_N-3C-inRing_N-Sp-3C-1C
Total Standard Deviation in ln(k): 0.5681187753024279""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1C-inRing_N-3C-inRing_N-Sp-3C-1C
Total Standard Deviation in ln(k): 0.5681187753024279
""",
)

