#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/rules"
shortDesc = ""
longDesc = """
For some reason the definition of Cs_rad::

 Cs_rad
 1 * C 1 

which is not mutually exclusive from its L2 siblings such as::

 Cd_rad
 1 * C 1 {2,D}, {3,S}
 2   C 0 {1,D}
 3   R 0 {1,S}

is apparently not causing a problem
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.19781e+07,'m^3/(mol*s)'), n=0.0114452, w0=(176.88,'kJ/mol'), E0=(68.5339,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03159666528300197, var=4.280875854033208, Tref=1000.0, N=271, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 271 training reactions at node Root
    Total Standard Deviation in ln(k): 4.227241124277926"""),
    rank = 11,
    shortDesc = """BM rule fitted to 271 training reactions at node Root
Total Standard Deviation in ln(k): 4.227241124277926""",
    longDesc = 
"""
BM rule fitted to 271 training reactions at node Root
Total Standard Deviation in ln(k): 4.227241124277926
""",
)

entry(
    index = 2,
    label = "Root_1R->H",
    kinetics = ArrheniusBM(A=(1.87153e+07,'m^3/(mol*s)'), n=0.267642, w0=(206.149,'kJ/mol'), E0=(94.4569,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01588828971812187, var=4.099619818353831, Tref=1000.0, N=87, data_mean=0.0, correlation='Root_1R->H',), comment="""BM rule fitted to 87 training reactions at node Root_1R->H
    Total Standard Deviation in ln(k): 4.099011265941489"""),
    rank = 11,
    shortDesc = """BM rule fitted to 87 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 4.099011265941489""",
    longDesc = 
"""
BM rule fitted to 87 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 4.099011265941489
""",
)

entry(
    index = 3,
    label = "Root_1R->H_2R->S",
    kinetics = ArrheniusBM(A=(9.71437e+06,'m^3/(mol*s)'), n=0.570447, w0=(181.5,'kJ/mol'), E0=(63.8083,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.2425089050590827, var=19.920377804880065, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_2R->S',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_2R->S
    Total Standard Deviation in ln(k): 14.5820282916646"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_2R->S
Total Standard Deviation in ln(k): 14.5820282916646""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_2R->S
Total Standard Deviation in ln(k): 14.5820282916646
""",
)

entry(
    index = 4,
    label = "Root_1R->H_2R->S_Ext-2S-R",
    kinetics = ArrheniusBM(A=(4.27677e+06,'m^3/(mol*s)'), n=1.0812, w0=(181.5,'kJ/mol'), E0=(67.7603,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_2R->S_Ext-2S-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_2R->S_Ext-2S-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_2R->S_Ext-2S-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_2R->S_Ext-2S-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_1R->H_N-2R->S",
    kinetics = ArrheniusBM(A=(1.84222e+08,'m^3/(mol*s)'), n=-0.0881505, w0=(207.03,'kJ/mol'), E0=(117.018,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.16529117185993783, var=3.2470767751065326, Tref=1000.0, N=84, data_mean=0.0, correlation='Root_1R->H_N-2R->S',), comment="""BM rule fitted to 84 training reactions at node Root_1R->H_N-2R->S
    Total Standard Deviation in ln(k): 4.027766291477692"""),
    rank = 11,
    shortDesc = """BM rule fitted to 84 training reactions at node Root_1R->H_N-2R->S
Total Standard Deviation in ln(k): 4.027766291477692""",
    longDesc = 
"""
BM rule fitted to 84 training reactions at node Root_1R->H_N-2R->S
Total Standard Deviation in ln(k): 4.027766291477692
""",
)

entry(
    index = 6,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing",
    kinetics = ArrheniusBM(A=(6.18581e+08,'m^3/(mol*s)'), n=-0.227063, w0=(205.5,'kJ/mol'), E0=(114.909,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005542906064395105, var=5.543577102614576, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing',), comment="""BM rule fitted to 14 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing
    Total Standard Deviation in ln(k): 4.734035984124622"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing
Total Standard Deviation in ln(k): 4.734035984124622""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing
Total Standard Deviation in ln(k): 4.734035984124622
""",
)

entry(
    index = 7,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(5.83557e+10,'m^3/(mol*s)'), n=-0.84119, w0=(205.5,'kJ/mol'), E0=(147.906,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7481061299473746, var=21.71274817033935, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H
    Total Standard Deviation in ln(k): 11.22111565409768"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 11.22111565409768""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 11.22111565409768
""",
)

entry(
    index = 8,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(353416,'m^3/(mol*s)'), n=0.0261687, w0=(205.5,'kJ/mol'), E0=(20.55,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.051990533709137074, var=36.4083102723705, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 12.227060445663648"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 12.227060445663648""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 12.227060445663648
""",
)

entry(
    index = 9,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(176351,'m^3/(mol*s)'), n=-0.549379, w0=(205.5,'kJ/mol'), E0=(76.9995,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(6.03232e+06,'m^3/(mol*s)'), n=-0.00929868, w0=(205.5,'kJ/mol'), E0=(89.8042,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(8.77012e+06,'m^3/(mol*s)'), n=-0.0289636, w0=(205.5,'kJ/mol'), E0=(118.876,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO",
    kinetics = ArrheniusBM(A=(4.44193e+07,'m^3/(mol*s)'), n=0.0790884, w0=(205.5,'kJ/mol'), E0=(82.069,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4321989925295231, var=9.818254810490107, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO
    Total Standard Deviation in ln(k): 7.367582962483659"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 7.367582962483659""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 7.367582962483659
""",
)

entry(
    index = 13,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_4R!H-inRing",
    kinetics = ArrheniusBM(A=(3.70386e+06,'m^3/(mol*s)'), n=0.19941, w0=(205.5,'kJ/mol'), E0=(50.3456,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.8120480258864409, var=13.318773824843154, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_4R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_4R!H-inRing
    Total Standard Deviation in ln(k): 11.869144161224577"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_4R!H-inRing
Total Standard Deviation in ln(k): 11.869144161224577""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_4R!H-inRing
Total Standard Deviation in ln(k): 11.869144161224577
""",
)

entry(
    index = 14,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_4R!H-inRing_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.37186e+06,'m^3/(mol*s)'), n=0.39882, w0=(205.5,'kJ/mol'), E0=(58.2267,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_4R!H-inRing_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_4R!H-inRing_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_4R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_4R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(9.3466e+06,'m^3/(mol*s)'), n=0.408973, w0=(205.5,'kJ/mol'), E0=(73.9218,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_N-4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_N-4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-Sp-3R!H-2BrCClFHNO",
    kinetics = ArrheniusBM(A=(7.92127e+07,'m^3/(mol*s)'), n=0.261109, w0=(205.5,'kJ/mol'), E0=(122.333,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-Sp-3R!H-2BrCClFHNO',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-Sp-3R!H-2BrCClFHNO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(4.42591e+07,'m^3/(mol*s)'), n=0.134893, w0=(205.5,'kJ/mol'), E0=(81.9077,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08996105998184312, var=0.2504706643421616, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
    Total Standard Deviation in ln(k): 1.2293434663569764"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 1.2293434663569764""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 1.2293434663569764
""",
)

entry(
    index = 18,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.70417e+07,'m^3/(mol*s)'), n=0.13817, w0=(205.5,'kJ/mol'), E0=(78.7152,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.016363460614647846, var=0.010255354138943597, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.24413118271194525"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.24413118271194525""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.24413118271194525
""",
)

entry(
    index = 19,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Sp-3R!H-2BrCClFHNO",
    kinetics = ArrheniusBM(A=(1.19687e+08,'m^3/(mol*s)'), n=-0.0437944, w0=(205.5,'kJ/mol'), E0=(76.6063,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6660752472298344, var=0.03338195309685563, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Sp-3R!H-2BrCClFHNO',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Sp-3R!H-2BrCClFHNO
    Total Standard Deviation in ln(k): 2.039835606758406"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 2.039835606758406""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 2.039835606758406
""",
)

entry(
    index = 20,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Sp-3R!H-2BrCClFHNO_Ext-2BrCClFHNO-R",
    kinetics = ArrheniusBM(A=(2.36997e+07,'m^3/(mol*s)'), n=0.0829452, w0=(205.5,'kJ/mol'), E0=(62.8092,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Sp-3R!H-2BrCClFHNO_Ext-2BrCClFHNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Sp-3R!H-2BrCClFHNO_Ext-2BrCClFHNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Sp-3R!H-2BrCClFHNO_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Sp-3R!H-2BrCClFHNO_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_N-Sp-3R!H-2BrCClFHNO",
    kinetics = ArrheniusBM(A=(2.45117e+07,'m^3/(mol*s)'), n=0.200434, w0=(205.5,'kJ/mol'), E0=(122.733,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0032279228172590476, var=0.0013491684535557648, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_N-Sp-3R!H-2BrCClFHNO',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_N-Sp-3R!H-2BrCClFHNO
    Total Standard Deviation in ln(k): 0.08174634006970083"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_N-Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 0.08174634006970083""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_N-Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 0.08174634006970083
""",
)

entry(
    index = 22,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_N-Sp-3R!H-2BrCClFHNO_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.29183e+07,'m^3/(mol*s)'), n=0.208569, w0=(205.5,'kJ/mol'), E0=(122.114,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_N-Sp-3R!H-2BrCClFHNO_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_N-Sp-3R!H-2BrCClFHNO_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_N-Sp-3R!H-2BrCClFHNO_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_N-Sp-3R!H-2BrCClFHNO_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5.15096e+07,'m^3/(mol*s)'), n=0.183576, w0=(205.5,'kJ/mol'), E0=(88.2201,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4398789556040558, var=0.03463880789404014, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.4783348544757335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.4783348544757335""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.4783348544757335
""",
)

entry(
    index = 24,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2BrCClFHNO",
    kinetics = ArrheniusBM(A=(3.94526e+07,'m^3/(mol*s)'), n=0.217294, w0=(205.5,'kJ/mol'), E0=(89.2907,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2BrCClFHNO',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2BrCClFHNO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2BrCClFHNO",
    kinetics = ArrheniusBM(A=(2.2e+08,'m^3/(mol*s)'), n=0, w0=(205.5,'kJ/mol'), E0=(118.308,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2BrCClFHNO',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2BrCClFHNO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing",
    kinetics = ArrheniusBM(A=(1.21289e+08,'m^3/(mol*s)'), n=-0.043635, w0=(207.336,'kJ/mol'), E0=(123.588,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.32949696452019295, var=2.990278128710778, Tref=1000.0, N=70, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing',), comment="""BM rule fitted to 70 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing
    Total Standard Deviation in ln(k): 4.2945540508305395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 70 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing
Total Standard Deviation in ln(k): 4.2945540508305395""",
    longDesc = 
"""
BM rule fitted to 70 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing
Total Standard Deviation in ln(k): 4.2945540508305395
""",
)

entry(
    index = 27,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O",
    kinetics = ArrheniusBM(A=(4.36942e+06,'m^3/(mol*s)'), n=0.260159, w0=(229.5,'kJ/mol'), E0=(50.1,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.18747662062982248, var=11.444138350979815, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O
    Total Standard Deviation in ln(k): 7.2529023955595395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O
Total Standard Deviation in ln(k): 7.2529023955595395""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O
Total Standard Deviation in ln(k): 7.2529023955595395
""",
)

entry(
    index = 28,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R",
    kinetics = ArrheniusBM(A=(2.55303e+06,'m^3/(mol*s)'), n=0.293392, w0=(229.5,'kJ/mol'), E0=(47.7213,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-6.898954322861617, var=122.33739474515733, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R
    Total Standard Deviation in ln(k): 39.50767622575325"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R
Total Standard Deviation in ln(k): 39.50767622575325""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R
Total Standard Deviation in ln(k): 39.50767622575325
""",
)

entry(
    index = 29,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_3R!H->Cl",
    kinetics = ArrheniusBM(A=(2.49746e+10,'m^3/(mol*s)'), n=-2.63174, w0=(229.5,'kJ/mol'), E0=(91.7404,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09052057931515818, var=1.2163223125035128e-05, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_3R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_3R!H->Cl
    Total Standard Deviation in ln(k): 0.23443031800553002"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_3R!H->Cl
Total Standard Deviation in ln(k): 0.23443031800553002""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_3R!H->Cl
Total Standard Deviation in ln(k): 0.23443031800553002
""",
)

entry(
    index = 30,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl",
    kinetics = ArrheniusBM(A=(2.07243e+06,'m^3/(mol*s)'), n=0.359788, w0=(229.5,'kJ/mol'), E0=(47.4183,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5519444187120015, var=4.570454558554161, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl
    Total Standard Deviation in ln(k): 5.67264225813464"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl
Total Standard Deviation in ln(k): 5.67264225813464""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl
Total Standard Deviation in ln(k): 5.67264225813464
""",
)

entry(
    index = 31,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl_3BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.21037e+06,'m^3/(mol*s)'), n=0.349925, w0=(229.5,'kJ/mol'), E0=(88.1187,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl_3BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl_3BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl_3BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl_3BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl_N-3BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(43950,'m^3/(mol*s)'), n=1, w0=(229.5,'kJ/mol'), E0=(53.9246,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl_N-3BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl_N-3BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl_N-3BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl_N-3BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O",
    kinetics = ArrheniusBM(A=(7.53096e+07,'m^3/(mol*s)'), n=0.0230384, w0=(205.631,'kJ/mol'), E0=(124.121,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.34650456385344414, var=2.982766656268015, Tref=1000.0, N=65, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O',), comment="""BM rule fitted to 65 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O
    Total Standard Deviation in ln(k): 4.332929895957191"""),
    rank = 11,
    shortDesc = """BM rule fitted to 65 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O
Total Standard Deviation in ln(k): 4.332929895957191""",
    longDesc = 
"""
BM rule fitted to 65 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O
Total Standard Deviation in ln(k): 4.332929895957191
""",
)

entry(
    index = 34,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_2CHN->N",
    kinetics = ArrheniusBM(A=(8.84147e+06,'m^3/(mol*s)'), n=0.349925, w0=(193,'kJ/mol'), E0=(113.913,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_2CHN->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_2CHN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_2CHN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_2CHN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N",
    kinetics = ArrheniusBM(A=(8.5478e+07,'m^3/(mol*s)'), n=0.00375573, w0=(205.828,'kJ/mol'), E0=(123.654,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.39175180662234177, var=3.321199756901395, Tref=1000.0, N=64, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N',), comment="""BM rule fitted to 64 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N
    Total Standard Deviation in ln(k): 4.637762126376641"""),
    rank = 11,
    shortDesc = """BM rule fitted to 64 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N
Total Standard Deviation in ln(k): 4.637762126376641""",
    longDesc = 
"""
BM rule fitted to 64 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N
Total Standard Deviation in ln(k): 4.637762126376641
""",
)

entry(
    index = 36,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C",
    kinetics = ArrheniusBM(A=(8.4062e+07,'m^3/(mol*s)'), n=0.00657626, w0=(205.5,'kJ/mol'), E0=(124.071,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3987253077174363, var=3.289907111258809, Tref=1000.0, N=62, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C',), comment="""BM rule fitted to 62 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C
    Total Standard Deviation in ln(k): 4.638031130304823"""),
    rank = 11,
    shortDesc = """BM rule fitted to 62 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C
Total Standard Deviation in ln(k): 4.638031130304823""",
    longDesc = 
"""
BM rule fitted to 62 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C
Total Standard Deviation in ln(k): 4.638031130304823
""",
)

entry(
    index = 37,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(8.24769e+07,'m^3/(mol*s)'), n=0.00794181, w0=(205.5,'kJ/mol'), E0=(123.739,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.40388498780815635, var=3.3523550915267966, Tref=1000.0, N=60, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R',), comment="""BM rule fitted to 60 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R
    Total Standard Deviation in ln(k): 4.68534360342036"""),
    rank = 11,
    shortDesc = """BM rule fitted to 60 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R
Total Standard Deviation in ln(k): 4.68534360342036""",
    longDesc = 
"""
BM rule fitted to 60 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R
Total Standard Deviation in ln(k): 4.68534360342036
""",
)

entry(
    index = 38,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F",
    kinetics = ArrheniusBM(A=(2.23995e+19,'m^3/(mol*s)'), n=-4.71736, w0=(205.5,'kJ/mol'), E0=(131.923,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.25751318094629677, var=35.011553852326195, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F',), comment="""BM rule fitted to 16 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F
    Total Standard Deviation in ln(k): 12.50914812408589"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F
Total Standard Deviation in ln(k): 12.50914812408589""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F
Total Standard Deviation in ln(k): 12.50914812408589
""",
)

entry(
    index = 39,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R",
    kinetics = ArrheniusBM(A=(9.99888e+19,'m^3/(mol*s)'), n=-4.91877, w0=(205.5,'kJ/mol'), E0=(132.719,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.26404397768419113, var=37.60956396899984, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R',), comment="""BM rule fitted to 15 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R
    Total Standard Deviation in ln(k): 12.95779310242817"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 12.95779310242817""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 12.95779310242817
""",
)

entry(
    index = 40,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.00014e+24,'m^3/(mol*s)'), n=-6.08812, w0=(205.5,'kJ/mol'), E0=(133.129,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.263235212374115, var=12.871443056165813, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C',), comment="""BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C
    Total Standard Deviation in ln(k): 7.853741627960401"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 7.853741627960401""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 7.853741627960401
""",
)

entry(
    index = 41,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(8.75187e+24,'m^3/(mol*s)'), n=-6.27391, w0=(205.5,'kJ/mol'), E0=(132.369,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2518700973192663, var=11.384895334210652, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 10 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 7.397118414584184"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 7.397118414584184""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 7.397118414584184
""",
)

entry(
    index = 42,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.21692e+34,'m^3/(mol*s)'), n=-8.80473, w0=(205.5,'kJ/mol'), E0=(123.144,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(8.43711e+23,'m^3/(mol*s)'), n=-5.99271, w0=(205.5,'kJ/mol'), E0=(133.394,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.25884854535692575, var=10.966526674850428, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl',), comment="""BM rule fitted to 9 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 7.289203095535672"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 7.289203095535672""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 7.289203095535672
""",
)

entry(
    index = 44,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(1.21692e+34,'m^3/(mol*s)'), n=-8.80473, w0=(205.5,'kJ/mol'), E0=(122.494,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(4.53221e+22,'m^3/(mol*s)'), n=-5.64121, w0=(205.5,'kJ/mol'), E0=(134.756,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.267571626393173, var=9.741478293666106, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br',), comment="""BM rule fitted to 8 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 6.929337601869539"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 6.929337601869539""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 6.929337601869539
""",
)

entry(
    index = 46,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(205.5,'kJ/mol'), E0=(117.474,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C",
    kinetics = ArrheniusBM(A=(7.81494e+24,'m^3/(mol*s)'), n=-6.44709, w0=(205.5,'kJ/mol'), E0=(137.225,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.30579614707389685, var=9.983013711910235, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C
    Total Standard Deviation in ln(k): 7.102474435962612"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C
Total Standard Deviation in ln(k): 7.102474435962612""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C
Total Standard Deviation in ln(k): 7.102474435962612
""",
)

entry(
    index = 48,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C",
    kinetics = ArrheniusBM(A=(8.36064e+26,'m^3/(mol*s)'), n=-7.16302, w0=(205.5,'kJ/mol'), E0=(135.775,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3351504735852967, var=16.804457517960397, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C
    Total Standard Deviation in ln(k): 9.060145297268072"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C
Total Standard Deviation in ln(k): 9.060145297268072""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C
Total Standard Deviation in ln(k): 9.060145297268072
""",
)

entry(
    index = 49,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.7313e+28,'m^3/(mol*s)'), n=-7.39166, w0=(205.5,'kJ/mol'), E0=(134.959,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3166437201132897, var=29.409938925631906, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.667452230541292"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R
Total Standard Deviation in ln(k): 11.667452230541292""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R
Total Standard Deviation in ln(k): 11.667452230541292
""",
)

entry(
    index = 50,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(5.06317e+29,'m^3/(mol*s)'), n=-7.6173, w0=(205.5,'kJ/mol'), E0=(134.184,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.30158007722040336, var=26.748226087879157, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.125965532151271"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.125965532151271""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.125965532151271
""",
)

entry(
    index = 51,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R_Ext-2C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.21692e+34,'m^3/(mol*s)'), n=-8.80473, w0=(205.5,'kJ/mol'), E0=(123.739,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R_Ext-2C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R_Ext-2C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R_Ext-2C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R_Ext-2C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.57075e+24,'m^3/(mol*s)'), n=-6.76739, w0=(205.5,'kJ/mol'), E0=(137.077,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_N-Sp-4C-2C",
    kinetics = ArrheniusBM(A=(6.6015e+19,'m^3/(mol*s)'), n=-4.65728, w0=(205.5,'kJ/mol'), E0=(140.851,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23241034472971045, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_N-Sp-4C-2C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_N-Sp-4C-2C
    Total Standard Deviation in ln(k): 0.5839455897731418"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_N-Sp-4C-2C
Total Standard Deviation in ln(k): 0.5839455897731418""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_N-Sp-4C-2C
Total Standard Deviation in ln(k): 0.5839455897731418
""",
)

entry(
    index = 54,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_N-Sp-4C-2C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(6.6015e+19,'m^3/(mol*s)'), n=-4.65728, w0=(205.5,'kJ/mol'), E0=(143.265,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_N-Sp-4C-2C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_N-Sp-4C-2C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_N-Sp-4C-2C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_N-Sp-4C-2C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C",
    kinetics = ArrheniusBM(A=(2.39918e+21,'m^3/(mol*s)'), n=-5.87461, w0=(205.5,'kJ/mol'), E0=(134.469,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3354732596135791, var=2.658413076695544, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C
    Total Standard Deviation in ln(k): 4.111546146559168"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C
Total Standard Deviation in ln(k): 4.111546146559168""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C
Total Standard Deviation in ln(k): 4.111546146559168
""",
)

entry(
    index = 56,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.90705e+22,'m^3/(mol*s)'), n=-6.09098, w0=(205.5,'kJ/mol'), E0=(134.892,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_N-Sp-4C-2C",
    kinetics = ArrheniusBM(A=(6.6015e+19,'m^3/(mol*s)'), n=-4.65728, w0=(205.5,'kJ/mol'), E0=(138.048,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_N-Sp-4C-2C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_N-Sp-4C-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_N-Sp-4C-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_N-Sp-4C-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(9.98266e-07,'m^3/(mol*s)'), n=2.68204, w0=(205.5,'kJ/mol'), E0=(130.058,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2693008724972855, var=814.5040851448289, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 57.890808095783754"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 57.890808095783754""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 57.890808095783754
""",
)

entry(
    index = 59,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(4.1766,'m^3/(mol*s)'), n=1.94174, w0=(205.5,'kJ/mol'), E0=(122.15,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F",
    kinetics = ArrheniusBM(A=(7.91533e+07,'m^3/(mol*s)'), n=0.0289698, w0=(205.5,'kJ/mol'), E0=(127.426,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5070918032355857, var=2.5662051033541067, Tref=1000.0, N=44, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F',), comment="""BM rule fitted to 44 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F
    Total Standard Deviation in ln(k): 4.4855611505517805"""),
    rank = 11,
    shortDesc = """BM rule fitted to 44 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F
Total Standard Deviation in ln(k): 4.4855611505517805""",
    longDesc = 
"""
BM rule fitted to 44 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F
Total Standard Deviation in ln(k): 4.4855611505517805
""",
)

entry(
    index = 61,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.44904e+09,'m^3/(mol*s)'), n=-0.378839, w0=(205.5,'kJ/mol'), E0=(137.589,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22908454048506927, var=2.3685443576061265, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C',), comment="""BM rule fitted to 38 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 3.660891794837678"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 3.660891794837678""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 3.660891794837678
""",
)

entry(
    index = 62,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.82538e+08,'m^3/(mol*s)'), n=-0.0522651, w0=(205.5,'kJ/mol'), E0=(159.942,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.495816097854588, var=2.3611745675100306, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R',), comment="""BM rule fitted to 18 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R
    Total Standard Deviation in ln(k): 4.326267846312695"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R
Total Standard Deviation in ln(k): 4.326267846312695""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R
Total Standard Deviation in ln(k): 4.326267846312695
""",
)

entry(
    index = 63,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_3C-inRing",
    kinetics = ArrheniusBM(A=(1.25109e+08,'m^3/(mol*s)'), n=-0.247784, w0=(205.5,'kJ/mol'), E0=(139.279,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_3C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing",
    kinetics = ArrheniusBM(A=(3.0032e+07,'m^3/(mol*s)'), n=0.204237, w0=(205.5,'kJ/mol'), E0=(106.645,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.015586503275756534, var=0.07356775305347633, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing',), comment="""BM rule fitted to 17 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing
    Total Standard Deviation in ln(k): 0.5829139031874249"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing
Total Standard Deviation in ln(k): 0.5829139031874249""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing
Total Standard Deviation in ln(k): 0.5829139031874249
""",
)

entry(
    index = 65,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.01164e+07,'m^3/(mol*s)'), n=0.204963, w0=(205.5,'kJ/mol'), E0=(106.914,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.013398046494463411, var=0.0571037910146848, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R',), comment="""BM rule fitted to 16 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R
    Total Standard Deviation in ln(k): 0.5127229368682941"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 0.5127229368682941""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 0.5127229368682941
""",
)

entry(
    index = 66,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.88633e+07,'m^3/(mol*s)'), n=0.213913, w0=(205.5,'kJ/mol'), E0=(102.98,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.197906922440378e-05, var=0.01210657880115639, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R',), comment="""BM rule fitted to 9 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.22078677680714184"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.22078677680714184""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.22078677680714184
""",
)

entry(
    index = 67,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(2.85197e+07,'m^3/(mol*s)'), n=0.213787, w0=(205.5,'kJ/mol'), E0=(102.976,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00012681105802580086, var=0.012046587691161825, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 0.22035222491166043"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.22035222491166043""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.22035222491166043
""",
)

entry(
    index = 68,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(2.83155e+07,'m^3/(mol*s)'), n=0.213711, w0=(205.5,'kJ/mol'), E0=(102.973,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00015371010021244128, var=0.013218501330287211, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 0.23087408926051417"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 0.23087408926051417""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 0.23087408926051417
""",
)

entry(
    index = 69,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.79114e+07,'m^3/(mol*s)'), n=0.21356, w0=(205.5,'kJ/mol'), E0=(102.968,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00020750917090565628, var=0.01529032030782134, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.2484149607337448"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.2484149607337448""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.2484149607337448
""",
)

entry(
    index = 70,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(2.67335e+07,'m^3/(mol*s)'), n=0.213107, w0=(205.5,'kJ/mol'), E0=(102.953,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00036890525002828464, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 0.0009268976131363935"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.0009268976131363935""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.0009268976131363935
""",
)

entry(
    index = 71,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(2.67335e+07,'m^3/(mol*s)'), n=0.213107, w0=(205.5,'kJ/mol'), E0=(102.953,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(2.67335e+07,'m^3/(mol*s)'), n=0.213107, w0=(205.5,'kJ/mol'), E0=(102.953,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(2.67335e+07,'m^3/(mol*s)'), n=0.213107, w0=(205.5,'kJ/mol'), E0=(102.953,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(2.67335e+07,'m^3/(mol*s)'), n=0.213107, w0=(205.5,'kJ/mol'), E0=(102.953,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Sp-3C=2C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(205.5,'kJ/mol'), E0=(120.874,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Sp-3C=2C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Sp-3C=2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Sp-3C=2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Sp-3C=2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C",
    kinetics = ArrheniusBM(A=(3.25274e+07,'m^3/(mol*s)'), n=0.19337, w0=(205.5,'kJ/mol'), E0=(106.781,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7164792645658096, var=0.6748704888446296, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C
    Total Standard Deviation in ln(k): 3.4470990760189535"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C
Total Standard Deviation in ln(k): 3.4470990760189535""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C
Total Standard Deviation in ln(k): 3.4470990760189535
""",
)

entry(
    index = 77,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.43549e+07,'m^3/(mol*s)'), n=0.0910533, w0=(205.5,'kJ/mol'), E0=(82.6821,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0028590110630623746, var=4.845846562261507, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 4.420263631284479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.420263631284479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.420263631284479
""",
)

entry(
    index = 78,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.7979e+07,'m^3/(mol*s)'), n=0.240345, w0=(205.5,'kJ/mol'), E0=(72.6386,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.21692e+34,'m^3/(mol*s)'), n=-8.80473, w0=(205.5,'kJ/mol'), E0=(20.55,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(1.7979e+07,'m^3/(mol*s)'), n=0.240345, w0=(205.5,'kJ/mol'), E0=(73.5184,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.005718031428005246, var=3.3763365973602174e-18, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C
    Total Standard Deviation in ln(k): 0.014366916819354281"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C
Total Standard Deviation in ln(k): 0.014366916819354281""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C
Total Standard Deviation in ln(k): 0.014366916819354281
""",
)

entry(
    index = 81,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.7979e+07,'m^3/(mol*s)'), n=0.240345, w0=(205.5,'kJ/mol'), E0=(76.741,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_N-Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(1.21037e+07,'m^3/(mol*s)'), n=0.336111, w0=(205.5,'kJ/mol'), E0=(110.697,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_N-Sp-4R!H-2C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_N-Sp-4R!H-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing",
    kinetics = ArrheniusBM(A=(3.31088e+08,'m^3/(mol*s)'), n=-0.0885348, w0=(205.5,'kJ/mol'), E0=(107.175,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02797848705983826, var=0.07920232407078374, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing
    Total Standard Deviation in ln(k): 0.634488443974192"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing
Total Standard Deviation in ln(k): 0.634488443974192""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing
Total Standard Deviation in ln(k): 0.634488443974192
""",
)

entry(
    index = 84,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(1.69017e+08,'m^3/(mol*s)'), n=0.0270731, w0=(205.5,'kJ/mol'), E0=(117.751,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10012748921436605, var=0.32132622559030904, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 1.3879735987544362"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.3879735987544362""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.3879735987544362
""",
)

entry(
    index = 85,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(4.79728e+07,'m^3/(mol*s)'), n=0.210679, w0=(205.5,'kJ/mol'), E0=(102.403,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(6.84478e+06,'m^3/(mol*s)'), n=0.41638, w0=(205.5,'kJ/mol'), E0=(78.1607,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 87,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(5.24876e+07,'m^3/(mol*s)'), n=0.108701, w0=(205.5,'kJ/mol'), E0=(88.3079,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10087784772476338, var=0.08078892568683867, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 0.8232756541119596"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 0.8232756541119596""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 0.8232756541119596
""",
)

entry(
    index = 88,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(3.16837e+06,'m^3/(mol*s)'), n=0.460513, w0=(205.5,'kJ/mol'), E0=(84.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(8.58356e+07,'m^3/(mol*s)'), n=0.0405873, w0=(205.5,'kJ/mol'), E0=(94.4402,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing",
    kinetics = ArrheniusBM(A=(1.99782e+09,'m^3/(mol*s)'), n=-0.419678, w0=(205.5,'kJ/mol'), E0=(28.7159,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2680272198418019, var=4.692251029733155, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing',), comment="""BM rule fitted to 16 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing
    Total Standard Deviation in ln(k): 5.016013032843771"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing
Total Standard Deviation in ln(k): 5.016013032843771""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing
Total Standard Deviation in ln(k): 5.016013032843771
""",
)

entry(
    index = 91,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.83153e+09,'m^3/(mol*s)'), n=-0.472098, w0=(205.5,'kJ/mol'), E0=(8.96091,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.41963027123128643, var=6.185483720472112, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R',), comment="""BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R
    Total Standard Deviation in ln(k): 6.0402503968519925"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 6.0402503968519925""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 6.0402503968519925
""",
)

entry(
    index = 92,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.21132e+09,'m^3/(mol*s)'), n=-0.304271, w0=(205.5,'kJ/mol'), E0=(84.9277,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11001570284037318, var=0.2703467101703673, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 1.3187808760358657"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 1.3187808760358657""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 1.3187808760358657
""",
)

entry(
    index = 93,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C",
    kinetics = ArrheniusBM(A=(1.31702e+09,'m^3/(mol*s)'), n=-0.311872, w0=(205.5,'kJ/mol'), E0=(85.0263,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08752712652122276, var=0.1390014693965761, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C
    Total Standard Deviation in ln(k): 0.9673407940389758"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C
Total Standard Deviation in ln(k): 0.9673407940389758""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C
Total Standard Deviation in ln(k): 0.9673407940389758
""",
)

entry(
    index = 94,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_Sp-4C=3C",
    kinetics = ArrheniusBM(A=(1.7979e+07,'m^3/(mol*s)'), n=0.240345, w0=(205.5,'kJ/mol'), E0=(81.2352,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_Sp-4C=3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_Sp-4C=3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_Sp-4C=3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_Sp-4C=3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C",
    kinetics = ArrheniusBM(A=(2.33349e+09,'m^3/(mol*s)'), n=-0.385433, w0=(205.5,'kJ/mol'), E0=(62.7437,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06986973055216424, var=0.05124357621262757, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C
    Total Standard Deviation in ln(k): 0.6293648488406877"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C
Total Standard Deviation in ln(k): 0.6293648488406877""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C
Total Standard Deviation in ln(k): 0.6293648488406877
""",
)

entry(
    index = 96,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C",
    kinetics = ArrheniusBM(A=(3.1711e+07,'m^3/(mol*s)'), n=0.21519, w0=(205.5,'kJ/mol'), E0=(105.778,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0002075092942954368, var=8.990172124599921e-08, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C
    Total Standard Deviation in ln(k): 0.0011224721985031766"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C
Total Standard Deviation in ln(k): 0.0011224721985031766""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C
Total Standard Deviation in ln(k): 0.0011224721985031766
""",
)

entry(
    index = 97,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(3.16564e+07,'m^3/(mol*s)'), n=0.21546, w0=(205.5,'kJ/mol'), E0=(105.772,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C",
    kinetics = ArrheniusBM(A=(1.11169e+10,'m^3/(mol*s)'), n=-0.603566, w0=(205.5,'kJ/mol'), E0=(93.9262,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21742595252866823, var=0.12210407896034299, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C
    Total Standard Deviation in ln(k): 1.2468188414261385"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 1.2468188414261385""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 1.2468188414261385
""",
)

entry(
    index = 99,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.17785e+10,'m^3/(mol*s)'), n=-0.611491, w0=(205.5,'kJ/mol'), E0=(91.732,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 100,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C",
    kinetics = ArrheniusBM(A=(2.83712e+08,'m^3/(mol*s)'), n=-0.251115, w0=(205.5,'kJ/mol'), E0=(121.492,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04900385874705703, var=3.2086570313419123, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C
    Total Standard Deviation in ln(k): 3.7141520099806296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 3.7141520099806296""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 3.7141520099806296
""",
)

entry(
    index = 101,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(205.5,'kJ/mol'), E0=(119.224,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 102,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(5.15008e+19,'m^3/(mol*s)'), n=-5.14141, w0=(205.5,'kJ/mol'), E0=(140.589,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3019489816516087, var=33.39144235156441, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 12.343093361898859"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 12.343093361898859""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 12.343093361898859
""",
)

entry(
    index = 103,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C",
    kinetics = ArrheniusBM(A=(4.36443e+19,'m^3/(mol*s)'), n=-5.46416, w0=(205.5,'kJ/mol'), E0=(139.804,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.34830808530593727, var=49.292539217588185, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C
    Total Standard Deviation in ln(k): 14.950119406858647"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C
Total Standard Deviation in ln(k): 14.950119406858647""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C
Total Standard Deviation in ln(k): 14.950119406858647
""",
)

entry(
    index = 104,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.84097e+21,'m^3/(mol*s)'), n=-5.92191, w0=(205.5,'kJ/mol'), E0=(139.268,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3347815616900648, var=90.07385025150133, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R
    Total Standard Deviation in ln(k): 19.86754788222595"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 19.86754788222595""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 19.86754788222595
""",
)

entry(
    index = 105,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.29291e+24,'m^3/(mol*s)'), n=-6.27825, w0=(205.5,'kJ/mol'), E0=(140.107,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 106,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C",
    kinetics = ArrheniusBM(A=(6.6015e+19,'m^3/(mol*s)'), n=-4.65728, w0=(205.5,'kJ/mol'), E0=(141.766,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23241034472971045, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C
    Total Standard Deviation in ln(k): 0.5839455897731418"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 0.5839455897731418""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 0.5839455897731418
""",
)

entry(
    index = 107,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.6015e+19,'m^3/(mol*s)'), n=-4.65728, w0=(205.5,'kJ/mol'), E0=(143.176,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 108,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Sp-3C#2C",
    kinetics = ArrheniusBM(A=(1.81e+08,'m^3/(mol*s)'), n=0, w0=(205.5,'kJ/mol'), E0=(139.288,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Sp-3C#2C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Sp-3C#2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Sp-3C#2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Sp-3C#2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 109,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C",
    kinetics = ArrheniusBM(A=(1.19651e+08,'m^3/(mol*s)'), n=1.7095e-11, w0=(205.5,'kJ/mol'), E0=(110.794,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16819443494880706, var=0.07267224299466107, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C
    Total Standard Deviation in ln(k): 0.9630313506418621"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C
Total Standard Deviation in ln(k): 0.9630313506418621""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C
Total Standard Deviation in ln(k): 0.9630313506418621
""",
)

entry(
    index = 110,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_Sp-3C-2C",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(205.5,'kJ/mol'), E0=(105.714,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_Sp-3C-2C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_Sp-3C-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_Sp-3C-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_Sp-3C-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 111,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_N-Sp-3C-2C",
    kinetics = ArrheniusBM(A=(1.21e+08,'m^3/(mol*s)'), n=0, w0=(205.5,'kJ/mol'), E0=(115.874,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_N-Sp-3C-2C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_N-Sp-3C-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 112,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.3625e+06,'m^3/(mol*s)'), n=0.449623, w0=(205.5,'kJ/mol'), E0=(84.5781,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.364302582884085, var=58.955157624898376, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 28.870956594557356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 28.870956594557356""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 28.870956594557356
""",
)

entry(
    index = 113,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3ClOS->S",
    kinetics = ArrheniusBM(A=(2.12532e+06,'m^3/(mol*s)'), n=0.469939, w0=(205.5,'kJ/mol'), E0=(98.4527,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3ClOS->S',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3ClOS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3ClOS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3ClOS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 114,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S",
    kinetics = ArrheniusBM(A=(3.7835e+13,'m^3/(mol*s)'), n=-2.73588, w0=(205.5,'kJ/mol'), E0=(7.17874,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09287195291663569, var=0.210498487689372, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S
    Total Standard Deviation in ln(k): 1.1531213578230466"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S
Total Standard Deviation in ln(k): 1.1531213578230466""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S
Total Standard Deviation in ln(k): 1.1531213578230466
""",
)

entry(
    index = 115,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_3ClO->O",
    kinetics = ArrheniusBM(A=(2.31504e+12,'m^3/(mol*s)'), n=-2.20453, w0=(205.5,'kJ/mol'), E0=(73.5422,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_3ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_3ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_3ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_3ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 116,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O",
    kinetics = ArrheniusBM(A=(7.60724e+13,'m^3/(mol*s)'), n=-2.86872, w0=(205.5,'kJ/mol'), E0=(70.6013,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16831304554632454, var=0.020241279232878672, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O
    Total Standard Deviation in ln(k): 0.7081144670934144"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O
Total Standard Deviation in ln(k): 0.7081144670934144""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O
Total Standard Deviation in ln(k): 0.7081144670934144
""",
)

entry(
    index = 117,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.62297e+14,'m^3/(mol*s)'), n=-2.96586, w0=(205.5,'kJ/mol'), E0=(20.55,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1756911488172365, var=8.662493862641411e-06, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O_Ext-2C-R
    Total Standard Deviation in ln(k): 0.4473354065895171"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O_Ext-2C-R
Total Standard Deviation in ln(k): 0.4473354065895171""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O_Ext-2C-R
Total Standard Deviation in ln(k): 0.4473354065895171
""",
)

entry(
    index = 118,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_N-2CH->C",
    kinetics = ArrheniusBM(A=(55567.3,'m^3/(mol*s)'), n=0.364988, w0=(216,'kJ/mol'), E0=(112.137,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03458487191910846, var=56.35834449117743, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_N-2CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_N-2CH->C
    Total Standard Deviation in ln(k): 15.136882911102552"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_N-2CH->C
Total Standard Deviation in ln(k): 15.136882911102552""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_N-2CH->C
Total Standard Deviation in ln(k): 15.136882911102552
""",
)

entry(
    index = 119,
    label = "Root_N-1R->H",
    kinetics = ArrheniusBM(A=(2.28856e+07,'m^3/(mol*s)'), n=0.0145805, w0=(163.041,'kJ/mol'), E0=(60.0257,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1261133691358666, var=4.555627884255527, Tref=1000.0, N=184, data_mean=0.0, correlation='Root_N-1R->H',), comment="""BM rule fitted to 184 training reactions at node Root_N-1R->H
    Total Standard Deviation in ln(k): 4.595757650510032"""),
    rank = 11,
    shortDesc = """BM rule fitted to 184 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 4.595757650510032""",
    longDesc = 
"""
BM rule fitted to 184 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 4.595757650510032
""",
)

entry(
    index = 120,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(1.28908e+12,'m^3/(mol*s)'), n=-1.44734, w0=(108.577,'kJ/mol'), E0=(90.5088,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6803343082570938, var=9.266948773022817, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N
    Total Standard Deviation in ln(k): 7.8121297494878315"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N
Total Standard Deviation in ln(k): 7.8121297494878315""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N
Total Standard Deviation in ln(k): 7.8121297494878315
""",
)

entry(
    index = 121,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R",
    kinetics = ArrheniusBM(A=(9.29993e+30,'m^3/(mol*s)'), n=-7.27836, w0=(128.438,'kJ/mol'), E0=(101.995,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12728370502763736, var=33.234134534564305, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R
    Total Standard Deviation in ln(k): 11.87691642316424"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R
Total Standard Deviation in ln(k): 11.87691642316424""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R
Total Standard Deviation in ln(k): 11.87691642316424
""",
)

entry(
    index = 122,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0",
    kinetics = ArrheniusBM(A=(1.41118e+27,'m^3/(mol*s)'), n=-6.1779, w0=(103.5,'kJ/mol'), E0=(10.35,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.006370659830096921, var=30.8883433868944, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0
    Total Standard Deviation in ln(k): 11.15777947190845"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0
Total Standard Deviation in ln(k): 11.15777947190845""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0
Total Standard Deviation in ln(k): 11.15777947190845
""",
)

entry(
    index = 123,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_2R->C",
    kinetics = ArrheniusBM(A=(4.23489e+61,'m^3/(mol*s)'), n=-16.8824, w0=(152.5,'kJ/mol'), E0=(1.525,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 124,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C",
    kinetics = ArrheniusBM(A=(4.60585e+10,'m^3/(mol*s)'), n=-1.0482, w0=(93.7,'kJ/mol'), E0=(61.1327,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21860200069121408, var=0.9652198726683298, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C
    Total Standard Deviation in ln(k): 2.518815345582996"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C
Total Standard Deviation in ln(k): 2.518815345582996""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C
Total Standard Deviation in ln(k): 2.518815345582996
""",
)

entry(
    index = 125,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C",
    kinetics = ArrheniusBM(A=(1.81328e+10,'m^3/(mol*s)'), n=-0.926861, w0=(92,'kJ/mol'), E0=(38.1802,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.023092714384428795, var=0.1979032497345805, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C
    Total Standard Deviation in ln(k): 0.949854718861428"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C
Total Standard Deviation in ln(k): 0.949854718861428""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C
Total Standard Deviation in ln(k): 0.949854718861428
""",
)

entry(
    index = 126,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C_Ext-1N-R",
    kinetics = ArrheniusBM(A=(7.65893e+11,'m^3/(mol*s)'), n=-1.44419, w0=(100.5,'kJ/mol'), E0=(40.1586,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C_Ext-1N-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C_Ext-1N-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C_Ext-1N-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C_Ext-1N-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 127,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C",
    kinetics = ArrheniusBM(A=(9.42742e+16,'m^3/(mol*s)'), n=-3.16695, w0=(94.8333,'kJ/mol'), E0=(69.7205,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8482384528447815, var=2.8535549893045737, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C
    Total Standard Deviation in ln(k): 5.517744849639554"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C
Total Standard Deviation in ln(k): 5.517744849639554""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C
Total Standard Deviation in ln(k): 5.517744849639554
""",
)

entry(
    index = 128,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R",
    kinetics = ArrheniusBM(A=(2.55463e+12,'m^3/(mol*s)'), n=-2.07, w0=(92,'kJ/mol'), E0=(41.4606,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2073116437415204, var=2.406300035478217, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R
    Total Standard Deviation in ln(k): 3.6306793661188173"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R
Total Standard Deviation in ln(k): 3.6306793661188173""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R
Total Standard Deviation in ln(k): 3.6306793661188173
""",
)

entry(
    index = 129,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_2NO->O",
    kinetics = ArrheniusBM(A=(122000,'m^3/(mol*s)'), n=0.2, w0=(100.5,'kJ/mol'), E0=(20.1213,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 130,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_N-2NO->O",
    kinetics = ArrheniusBM(A=(2.63e+08,'m^3/(mol*s)'), n=-1.1, w0=(83.5,'kJ/mol'), E0=(13.7525,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_N-2NO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_N-2NO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0",
    kinetics = ArrheniusBM(A=(2.33856e+31,'m^3/(mol*s)'), n=-8.22442, w0=(100.5,'kJ/mol'), E0=(58.8122,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1670620681254752, var=233.88139069458302, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0
    Total Standard Deviation in ln(k): 31.078530702420622"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0
Total Standard Deviation in ln(k): 31.078530702420622""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0
Total Standard Deviation in ln(k): 31.078530702420622
""",
)

entry(
    index = 132,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R",
    kinetics = ArrheniusBM(A=(1.22632e+19,'m^3/(mol*s)'), n=-4.10329, w0=(100.5,'kJ/mol'), E0=(1.21995,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R",
    kinetics = ArrheniusBM(A=(1.02626e+07,'m^3/(mol*s)'), n=0.0868089, w0=(126.5,'kJ/mol'), E0=(45.967,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1919442187735095, var=4.547212141637392, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R
    Total Standard Deviation in ln(k): 4.757207710086374"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R
Total Standard Deviation in ln(k): 4.757207710086374""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R
Total Standard Deviation in ln(k): 4.757207710086374
""",
)

entry(
    index = 134,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R",
    kinetics = ArrheniusBM(A=(7.93988e+11,'m^3/(mol*s)'), n=-1.2959, w0=(117.833,'kJ/mol'), E0=(116.074,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3470375777548632, var=2.8582163193257277, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R
    Total Standard Deviation in ln(k): 4.261210986039267"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R
Total Standard Deviation in ln(k): 4.261210986039267""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R
Total Standard Deviation in ln(k): 4.261210986039267
""",
)

entry(
    index = 135,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_2R->C",
    kinetics = ArrheniusBM(A=(1.33461e+13,'m^3/(mol*s)'), n=-1.66494, w0=(152.5,'kJ/mol'), E0=(63.1547,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 136,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C",
    kinetics = ArrheniusBM(A=(3.65367e+06,'m^3/(mol*s)'), n=0.2352, w0=(100.5,'kJ/mol'), E0=(52.3217,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.47095022036263345, var=0.4813240235668661, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C
    Total Standard Deviation in ln(k): 2.574127483627416"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C
Total Standard Deviation in ln(k): 2.574127483627416""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C
Total Standard Deviation in ln(k): 2.574127483627416
""",
)

entry(
    index = 137,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(2.93721e+06,'m^3/(mol*s)'), n=0.288859, w0=(167.181,'kJ/mol'), E0=(60.3825,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12020360967739878, var=4.711449572538075, Tref=1000.0, N=171, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N',), comment="""BM rule fitted to 171 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N
    Total Standard Deviation in ln(k): 4.653471778252971"""),
    rank = 11,
    shortDesc = """BM rule fitted to 171 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N
Total Standard Deviation in ln(k): 4.653471778252971""",
    longDesc = 
"""
BM rule fitted to 171 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N
Total Standard Deviation in ln(k): 4.653471778252971
""",
)

entry(
    index = 138,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl",
    kinetics = ArrheniusBM(A=(3.77965e+12,'m^3/(mol*s)'), n=-1.89404, w0=(162.442,'kJ/mol'), E0=(16.2442,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15648417958656624, var=13.849946630363993, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl',), comment="""BM rule fitted to 26 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl
    Total Standard Deviation in ln(k): 7.853901451365102"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl
Total Standard Deviation in ln(k): 7.853901451365102""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl
Total Standard Deviation in ln(k): 7.853901451365102
""",
)

entry(
    index = 139,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C",
    kinetics = ArrheniusBM(A=(3.27007e+13,'m^3/(mol*s)'), n=-2.12465, w0=(163.5,'kJ/mol'), E0=(124.399,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.012957707495321292, var=13.73369341993895, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C
    Total Standard Deviation in ln(k): 7.461904401341154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C
Total Standard Deviation in ln(k): 7.461904401341154""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C
Total Standard Deviation in ln(k): 7.461904401341154
""",
)

entry(
    index = 140,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.74322e+13,'m^3/(mol*s)'), n=-2.09051, w0=(163.5,'kJ/mol'), E0=(127.609,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0011055911007469387, var=14.347479877596948, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R',), comment="""BM rule fitted to 24 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 7.596326899335355"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 7.596326899335355""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 7.596326899335355
""",
)

entry(
    index = 141,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F",
    kinetics = ArrheniusBM(A=(1.45492e+14,'m^3/(mol*s)'), n=-1.95635, w0=(163.5,'kJ/mol'), E0=(62.5786,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22403213467765656, var=44.10639172454973, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F
    Total Standard Deviation in ln(k): 13.876870344724166"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F
Total Standard Deviation in ln(k): 13.876870344724166""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F
Total Standard Deviation in ln(k): 13.876870344724166
""",
)

entry(
    index = 142,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.55598e+15,'m^3/(mol*s)'), n=-2.44544, w0=(163.5,'kJ/mol'), E0=(57.1957,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2809355785089933, var=64.03755998098522, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R
    Total Standard Deviation in ln(k): 16.748454329803657"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 16.748454329803657""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 16.748454329803657
""",
)

entry(
    index = 143,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.85364e+42,'m^3/(mol*s)'), n=-9.9178, w0=(163.5,'kJ/mol'), E0=(1.635,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 144,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.20701e+07,'m^3/(mol*s)'), n=0.0453429, w0=(163.5,'kJ/mol'), E0=(81.7588,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.058886864375418395, var=9.360080764723941, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 6.2812933744157595"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 6.2812933744157595""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 6.2812933744157595
""",
)

entry(
    index = 145,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_4BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.46348e+06,'m^3/(mol*s)'), n=0.110251, w0=(163.5,'kJ/mol'), E0=(81.5572,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_4BrCFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_4BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(3.46638e+07,'m^3/(mol*s)'), n=0.0128888, w0=(163.5,'kJ/mol'), E0=(81.8596,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05069508969883262, var=16.30368745872988, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 8.222058795330017"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 8.222058795330017""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 8.222058795330017
""",
)

entry(
    index = 147,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.80246e+06,'m^3/(mol*s)'), n=0.0257777, w0=(163.5,'kJ/mol'), E0=(74.5352,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F",
    kinetics = ArrheniusBM(A=(3.48972e+13,'m^3/(mol*s)'), n=-2.21039, w0=(163.5,'kJ/mol'), E0=(145.241,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.019339439580997302, var=7.8289083206571455, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F
    Total Standard Deviation in ln(k): 5.657877675440784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F
Total Standard Deviation in ln(k): 5.657877675440784""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F
Total Standard Deviation in ln(k): 5.657877675440784
""",
)

entry(
    index = 149,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.13891e+12,'m^3/(mol*s)'), n=-1.66575, w0=(163.5,'kJ/mol'), E0=(16.35,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04609020162126216, var=5.730545793899475, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 4.914851304048008"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 4.914851304048008""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 4.914851304048008
""",
)

entry(
    index = 150,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C",
    kinetics = ArrheniusBM(A=(2.2655e+10,'m^3/(mol*s)'), n=-1.17544, w0=(163.5,'kJ/mol'), E0=(118.468,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09538662893606398, var=9.159880637656538, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C
    Total Standard Deviation in ln(k): 6.30705468971594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C
Total Standard Deviation in ln(k): 6.30705468971594""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C
Total Standard Deviation in ln(k): 6.30705468971594
""",
)

entry(
    index = 151,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.46812e+08,'m^3/(mol*s)'), n=-0.724216, w0=(163.5,'kJ/mol'), E0=(37.7578,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.26559035564746014, var=12.14702562549829, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R
    Total Standard Deviation in ln(k): 7.654332078922364"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R
Total Standard Deviation in ln(k): 7.654332078922364""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R
Total Standard Deviation in ln(k): 7.654332078922364
""",
)

entry(
    index = 152,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.93132e+10,'m^3/(mol*s)'), n=-1.22628, w0=(163.5,'kJ/mol'), E0=(62.6353,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13970672475364135, var=10.687591922547561, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 6.90487831417212"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.90487831417212""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.90487831417212
""",
)

entry(
    index = 153,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(228516,'m^3/(mol*s)'), n=0.317874, w0=(163.5,'kJ/mol'), E0=(69.7597,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04499257574084583, var=20.619355759337463, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 9.216256124574329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 9.216256124574329""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 9.216256124574329
""",
)

entry(
    index = 154,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=2.48906e-08, w0=(163.5,'kJ/mol'), E0=(60.9633,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 155,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(5221.95,'m^3/(mol*s)'), n=0.635748, w0=(163.5,'kJ/mol'), E0=(65.7136,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 156,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.13552e+14,'m^3/(mol*s)'), n=-2.31938, w0=(163.5,'kJ/mol'), E0=(68.0308,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 157,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(0.0029093,'m^3/(mol*s)'), n=2.14648, w0=(163.5,'kJ/mol'), E0=(16.35,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 158,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(3.38331e+10,'m^3/(mol*s)'), n=-1.44396, w0=(163.5,'kJ/mol'), E0=(137.524,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 159,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(4.95357e+08,'m^3/(mol*s)'), n=-0.866913, w0=(163.5,'kJ/mol'), E0=(139.111,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 160,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.65838e+13,'m^3/(mol*s)'), n=-1.74873, w0=(163.5,'kJ/mol'), E0=(64.663,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 161,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C",
    kinetics = ArrheniusBM(A=(6.30746e+17,'m^3/(mol*s)'), n=-3.317, w0=(163.5,'kJ/mol'), E0=(87.541,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09093972422750127, var=1.5234337678964684, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C
    Total Standard Deviation in ln(k): 2.702885338679541"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 2.702885338679541""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 2.702885338679541
""",
)

entry(
    index = 162,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.84656e+14,'m^3/(mol*s)'), n=-2.20814, w0=(163.5,'kJ/mol'), E0=(83.7345,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10977590784692547, var=2.4938126900982676, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R
    Total Standard Deviation in ln(k): 3.4416584458550132"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R
Total Standard Deviation in ln(k): 3.4416584458550132""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R
Total Standard Deviation in ln(k): 3.4416584458550132
""",
)

entry(
    index = 163,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(8.1925e+11,'m^3/(mol*s)'), n=-1.52514, w0=(163.5,'kJ/mol'), E0=(97.8768,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04656700350726976, var=0.3699213630204074, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 1.33630567121414"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.33630567121414""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.33630567121414
""",
)

entry(
    index = 164,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.09626e+13,'m^3/(mol*s)'), n=-2.05815, w0=(163.5,'kJ/mol'), E0=(95.3094,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 165,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.27064e+20,'m^3/(mol*s)'), n=-4.11807, w0=(163.5,'kJ/mol'), E0=(80.933,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 166,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.32222e+12,'m^3/(mol*s)'), n=-2.2486, w0=(163.5,'kJ/mol'), E0=(2.48328,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19554063196991378, var=6.967896071248746, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 5.783161729669141"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 5.783161729669141""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 5.783161729669141
""",
)

entry(
    index = 167,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3BrClO->O",
    kinetics = ArrheniusBM(A=(5593.5,'m^3/(mol*s)'), n=0.141043, w0=(163.5,'kJ/mol'), E0=(127.231,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3BrClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3BrClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3BrClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3BrClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 168,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O",
    kinetics = ArrheniusBM(A=(8.17544e+14,'m^3/(mol*s)'), n=-3.04515, w0=(163.5,'kJ/mol'), E0=(32.1895,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11357896036203688, var=3.090768340203733, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O
    Total Standard Deviation in ln(k): 3.8098150460622713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O
Total Standard Deviation in ln(k): 3.8098150460622713""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O
Total Standard Deviation in ln(k): 3.8098150460622713
""",
)

entry(
    index = 169,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(9.5271e+11,'m^3/(mol*s)'), n=-2.09678, w0=(163.5,'kJ/mol'), E0=(3.44407,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7272315810012803, var=16.99112902181845, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R
    Total Standard Deviation in ln(k): 10.090792599637137"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R
Total Standard Deviation in ln(k): 10.090792599637137""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R
Total Standard Deviation in ln(k): 10.090792599637137
""",
)

entry(
    index = 170,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.98116e+19,'m^3/(mol*s)'), n=-4.24465, w0=(163.5,'kJ/mol'), E0=(158.462,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_N-2R->C",
    kinetics = ArrheniusBM(A=(3.24625e+12,'m^3/(mol*s)'), n=-2.82209, w0=(136,'kJ/mol'), E0=(81.9052,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl",
    kinetics = ArrheniusBM(A=(2.79887e+06,'m^3/(mol*s)'), n=0.29645, w0=(168.031,'kJ/mol'), E0=(60.4236,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12137033811528962, var=4.676159199737414, Tref=1000.0, N=145, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl',), comment="""BM rule fitted to 145 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl
    Total Standard Deviation in ln(k): 4.6400756882615175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 145 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl
Total Standard Deviation in ln(k): 4.6400756882615175""",
    longDesc = 
"""
BM rule fitted to 145 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl
Total Standard Deviation in ln(k): 4.6400756882615175
""",
)

entry(
    index = 173,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O",
    kinetics = ArrheniusBM(A=(12673.2,'m^3/(mol*s)'), n=0.690283, w0=(161.911,'kJ/mol'), E0=(-0.622409,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3812446254077848, var=7.83911918926562, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O',), comment="""BM rule fitted to 28 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O
    Total Standard Deviation in ln(k): 6.570843956679056"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O
Total Standard Deviation in ln(k): 6.570843956679056""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O
Total Standard Deviation in ln(k): 6.570843956679056
""",
)

entry(
    index = 174,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R",
    kinetics = ArrheniusBM(A=(22168.4,'m^3/(mol*s)'), n=0.619748, w0=(164.18,'kJ/mol'), E0=(1.07368,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.38247444085384447, var=7.8122814551813935, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R
    Total Standard Deviation in ln(k): 6.564317570201389"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R
Total Standard Deviation in ln(k): 6.564317570201389""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R
Total Standard Deviation in ln(k): 6.564317570201389
""",
)

entry(
    index = 175,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O",
    kinetics = ArrheniusBM(A=(9113.57,'m^3/(mol*s)'), n=0.726393, w0=(176.553,'kJ/mol'), E0=(-0.620585,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4505290767586665, var=8.864077938153839, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O
    Total Standard Deviation in ln(k): 7.100600441070029"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O
Total Standard Deviation in ln(k): 7.100600441070029""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O
Total Standard Deviation in ln(k): 7.100600441070029
""",
)

entry(
    index = 176,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C",
    kinetics = ArrheniusBM(A=(3.93796e+08,'m^3/(mol*s)'), n=-0.660794, w0=(179,'kJ/mol'), E0=(55.7639,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0648808092294275, var=0.4017020872719151, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C',), comment="""BM rule fitted to 18 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C
    Total Standard Deviation in ln(k): 1.4336176428223202"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C
Total Standard Deviation in ln(k): 1.4336176428223202""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C
Total Standard Deviation in ln(k): 1.4336176428223202
""",
)

entry(
    index = 177,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing",
    kinetics = ArrheniusBM(A=(1.90891e+06,'m^3/(mol*s)'), n=0.0381637, w0=(179,'kJ/mol'), E0=(45.7926,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.004883806222350359, var=0.5005705380914729, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing
    Total Standard Deviation in ln(k): 1.4306411800124683"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing
Total Standard Deviation in ln(k): 1.4306411800124683""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing
Total Standard Deviation in ln(k): 1.4306411800124683
""",
)

entry(
    index = 178,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing_Ext-2C-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.6229e+06,'m^3/(mol*s)'), n=-0.00476945, w0=(179,'kJ/mol'), E0=(41.7602,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing_Ext-2C-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing_Ext-2C-R_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing_Ext-2C-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing_Ext-2C-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 179,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.97515e+06,'m^3/(mol*s)'), n=-0.00323035, w0=(179,'kJ/mol'), E0=(42.8817,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 180,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing",
    kinetics = ArrheniusBM(A=(284464,'m^3/(mol*s)'), n=0.158989, w0=(179,'kJ/mol'), E0=(41.2069,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07307342555193728, var=1.039002618272806, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing
    Total Standard Deviation in ln(k): 2.227057663697973"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing
Total Standard Deviation in ln(k): 2.227057663697973""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing
Total Standard Deviation in ln(k): 2.227057663697973
""",
)

entry(
    index = 181,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R",
    kinetics = ArrheniusBM(A=(99063.5,'m^3/(mol*s)'), n=0.290298, w0=(179,'kJ/mol'), E0=(39.7644,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10559855350330952, var=1.0655351314124175, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R
    Total Standard Deviation in ln(k): 2.334705994048373"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R
Total Standard Deviation in ln(k): 2.334705994048373""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R
Total Standard Deviation in ln(k): 2.334705994048373
""",
)

entry(
    index = 182,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(413.576,'m^3/(mol*s)'), n=0.967607, w0=(179,'kJ/mol'), E0=(30.477,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2630652819878215, var=1.1878858578990525, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 2.84593234490966"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.84593234490966""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.84593234490966
""",
)

entry(
    index = 183,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(8.14976e+13,'m^3/(mol*s)'), n=-2.27223, w0=(179,'kJ/mol'), E0=(68.3469,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03642541003782715, var=3.51219038874387, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 3.8485628226786726"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 3.8485628226786726""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 3.8485628226786726
""",
)

entry(
    index = 184,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.8422e+07,'m^3/(mol*s)'), n=-0.361029, w0=(179,'kJ/mol'), E0=(37.3913,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 185,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(49.5695,'m^3/(mol*s)'), n=1.23161, w0=(179,'kJ/mol'), E0=(25.7763,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3233266493524891, var=1.2527084791405165, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 3.056167429805253"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 3.056167429805253""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 3.056167429805253
""",
)

entry(
    index = 186,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(124.902,'m^3/(mol*s)'), n=1.09941, w0=(179,'kJ/mol'), E0=(18.757,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01560833182403432, var=0.016020860987762845, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C
    Total Standard Deviation in ln(k): 0.2929633293189987"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C
Total Standard Deviation in ln(k): 0.2929633293189987""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C
Total Standard Deviation in ln(k): 0.2929633293189987
""",
)

entry(
    index = 187,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C_4R!H-inRing",
    kinetics = ArrheniusBM(A=(252.533,'m^3/(mol*s)'), n=0.999283, w0=(179,'kJ/mol'), E0=(17.1319,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C_4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C_4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 188,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(1.53331,'m^3/(mol*s)'), n=1.7252, w0=(179,'kJ/mol'), E0=(20.382,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C_N-4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C_N-4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 189,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(0.004135,'m^3/(mol*s)'), n=2.525, w0=(179,'kJ/mol'), E0=(37.3872,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-2C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 190,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(1.01905e+07,'m^3/(mol*s)'), n=-0.198371, w0=(179,'kJ/mol'), E0=(38.2273,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.054859309462099146, var=1.178102591472186, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C
    Total Standard Deviation in ln(k): 2.3137856239163224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C
Total Standard Deviation in ln(k): 2.3137856239163224""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C
Total Standard Deviation in ln(k): 2.3137856239163224
""",
)

entry(
    index = 191,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.44254e+06,'m^3/(mol*s)'), n=0.00088922, w0=(179,'kJ/mol'), E0=(38.2273,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17523027882982423, var=1.332721973881736, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R
    Total Standard Deviation in ln(k): 2.754614988497054"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R
Total Standard Deviation in ln(k): 2.754614988497054""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R
Total Standard Deviation in ln(k): 2.754614988497054
""",
)

entry(
    index = 192,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(5.17579e+06,'m^3/(mol*s)'), n=0.00053286, w0=(179,'kJ/mol'), E0=(38.2273,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2362166361863198e-10, var=0.783633349042906, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C
    Total Standard Deviation in ln(k): 1.7746529872935115"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C
Total Standard Deviation in ln(k): 1.7746529872935115""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C
Total Standard Deviation in ln(k): 1.7746529872935115
""",
)

entry(
    index = 193,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.05e+06,'m^3/(mol*s)'), n=6.30826e-09, w0=(179,'kJ/mol'), E0=(34.6022,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 194,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.505e+06,'m^3/(mol*s)'), n=-1.3397e-08, w0=(179,'kJ/mol'), E0=(33.4345,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 195,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(3.24037e+06,'m^3/(mol*s)'), n=-7.05147e-08, w0=(179,'kJ/mol'), E0=(31.8977,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13894437474460805, var=0.17180942216559375, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C
    Total Standard Deviation in ln(k): 1.180067156868643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 1.180067156868643""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 1.180067156868643
""",
)

entry(
    index = 196,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C_4R!H->C",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=-6.55423e-09, w0=(179,'kJ/mol'), E0=(40.5994,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 197,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(3.5e+06,'m^3/(mol*s)'), n=-4.57487e-10, w0=(179,'kJ/mol'), E0=(33.5686,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 198,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_N-2R->C",
    kinetics = ArrheniusBM(A=(2.49151e+08,'m^3/(mol*s)'), n=0.0472428, w0=(132.5,'kJ/mol'), E0=(27.384,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 199,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O",
    kinetics = ArrheniusBM(A=(7.75903e+07,'m^3/(mol*s)'), n=-0.290943, w0=(125,'kJ/mol'), E0=(14.137,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.583252385011253, var=5.759706844490362, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O
    Total Standard Deviation in ln(k): 11.301825628806402"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O
Total Standard Deviation in ln(k): 11.301825628806402""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O
Total Standard Deviation in ln(k): 11.301825628806402
""",
)

entry(
    index = 200,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.50084e+08,'m^3/(mol*s)'), n=-0.433098, w0=(143,'kJ/mol'), E0=(64.3351,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13208035018416822, var=0.20161860433449766, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R
    Total Standard Deviation in ln(k): 1.232025525932261"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R
Total Standard Deviation in ln(k): 1.232025525932261""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R
Total Standard Deviation in ln(k): 1.232025525932261
""",
)

entry(
    index = 201,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C",
    kinetics = ArrheniusBM(A=(7.38316e+06,'m^3/(mol*s)'), n=1.31229e-07, w0=(179,'kJ/mol'), E0=(58.9141,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.016021952005170214, var=0.3543710496450803, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C
    Total Standard Deviation in ln(k): 1.2336563624693968"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C
Total Standard Deviation in ln(k): 1.2336563624693968""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C
Total Standard Deviation in ln(k): 1.2336563624693968
""",
)

entry(
    index = 202,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(9.04e+06,'m^3/(mol*s)'), n=2.17087e-08, w0=(179,'kJ/mol'), E0=(72.7054,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_N-2R->C",
    kinetics = ArrheniusBM(A=(1.81e+06,'m^3/(mol*s)'), n=0, w0=(71,'kJ/mol'), E0=(40.702,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 204,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(1.55564e+07,'m^3/(mol*s)'), n=-5.63145e-08, w0=(125,'kJ/mol'), E0=(35.2414,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7121440562946592, var=2.9508506800589083, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 5.233048665971416"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C
Total Standard Deviation in ln(k): 5.233048665971416""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C
Total Standard Deviation in ln(k): 5.233048665971416
""",
)

entry(
    index = 205,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C_2R->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=-8.5357e-08, w0=(179,'kJ/mol'), E0=(71.5824,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 206,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C_N-2R->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(71,'kJ/mol'), E0=(46.5188,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 207,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_N-3BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(1.12593e+08,'m^3/(mol*s)'), n=-0.33733, w0=(71,'kJ/mol'), E0=(19.907,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_N-3BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_N-3BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_N-3BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_N-3BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 208,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C",
    kinetics = ArrheniusBM(A=(6.81403e+07,'m^3/(mol*s)'), n=-1.87063e-10, w0=(179,'kJ/mol'), E0=(97.5317,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.951279959203741e-16, var=0.1195344065457376, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C
    Total Standard Deviation in ln(k): 0.6931120579847649"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C
Total Standard Deviation in ln(k): 0.6931120579847649""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C
Total Standard Deviation in ln(k): 0.6931120579847649
""",
)

entry(
    index = 209,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.7e+07,'m^3/(mol*s)'), n=0, w0=(179,'kJ/mol'), E0=(98.5531,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 210,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_N-2R->C",
    kinetics = ArrheniusBM(A=(1.57e+07,'m^3/(mol*s)'), n=0, w0=(71,'kJ/mol'), E0=(52.1149,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 211,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O",
    kinetics = ArrheniusBM(A=(506530,'m^3/(mol*s)'), n=0.554816, w0=(169.496,'kJ/mol'), E0=(13.9414,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02648174565896206, var=3.6079392316977894, Tref=1000.0, N=117, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O',), comment="""BM rule fitted to 117 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O
    Total Standard Deviation in ln(k): 3.874446358480738"""),
    rank = 11,
    shortDesc = """BM rule fitted to 117 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O
Total Standard Deviation in ln(k): 3.874446358480738""",
    longDesc = 
"""
BM rule fitted to 117 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O
Total Standard Deviation in ln(k): 3.874446358480738
""",
)

entry(
    index = 212,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing",
    kinetics = ArrheniusBM(A=(1.26173e+09,'m^3/(mol*s)'), n=-0.614843, w0=(173,'kJ/mol'), E0=(21.5217,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.011388155870254303, var=0.2640727834609356, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing
    Total Standard Deviation in ln(k): 1.0588069702762606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing
Total Standard Deviation in ln(k): 1.0588069702762606""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing
Total Standard Deviation in ln(k): 1.0588069702762606
""",
)

entry(
    index = 213,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS",
    kinetics = ArrheniusBM(A=(1.64652e+10,'m^3/(mol*s)'), n=-0.959714, w0=(173,'kJ/mol'), E0=(34.6868,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09357740147613781, var=0.36787669337185147, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS
    Total Standard Deviation in ln(k): 1.4510478471372923"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS
Total Standard Deviation in ln(k): 1.4510478471372923""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS
Total Standard Deviation in ln(k): 1.4510478471372923
""",
)

entry(
    index = 214,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_2R-inRing",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=2.59562e-08, w0=(173,'kJ/mol'), E0=(46.0647,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_2R-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_2R-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_2R-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_2R-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 215,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_N-2R-inRing",
    kinetics = ArrheniusBM(A=(1.71905e+10,'m^3/(mol*s)'), n=-0.966851, w0=(173,'kJ/mol'), E0=(73.0943,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07464897564796032, var=0.299509236916578, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_N-2R-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_N-2R-inRing
    Total Standard Deviation in ln(k): 1.2847003683901814"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_N-2R-inRing
Total Standard Deviation in ln(k): 1.2847003683901814""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_N-2R-inRing
Total Standard Deviation in ln(k): 1.2847003683901814
""",
)

entry(
    index = 216,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_N-2R-inRing_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.17885e+10,'m^3/(mol*s)'), n=-0.943326, w0=(173,'kJ/mol'), E0=(71.8334,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_N-2R-inRing_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_N-2R-inRing_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_N-2R-inRing_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_N-2R-inRing_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 217,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS",
    kinetics = ArrheniusBM(A=(4.28281e+08,'m^3/(mol*s)'), n=-0.469786, w0=(173,'kJ/mol'), E0=(110.538,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11347341788092068, var=0.43400451681228536, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS
    Total Standard Deviation in ln(k): 1.605808896298352"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS
Total Standard Deviation in ln(k): 1.605808896298352""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS
Total Standard Deviation in ln(k): 1.605808896298352
""",
)

entry(
    index = 218,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R",
    kinetics = ArrheniusBM(A=(5.20355e+08,'m^3/(mol*s)'), n=-0.509162, w0=(173,'kJ/mol'), E0=(111.454,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.35721850280207135, var=0.8400903028694655, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R
    Total Standard Deviation in ln(k): 2.735002733860902"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R
Total Standard Deviation in ln(k): 2.735002733860902""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R
Total Standard Deviation in ln(k): 2.735002733860902
""",
)

entry(
    index = 219,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_2R-inRing",
    kinetics = ArrheniusBM(A=(1.6752e+09,'m^3/(mol*s)'), n=-0.659797, w0=(173,'kJ/mol'), E0=(124.605,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0101763682895386, var=2.902598485050662, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_2R-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_2R-inRing
    Total Standard Deviation in ln(k): 5.9536015511279485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_2R-inRing
Total Standard Deviation in ln(k): 5.9536015511279485""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_2R-inRing
Total Standard Deviation in ln(k): 5.9536015511279485
""",
)

entry(
    index = 220,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(173,'kJ/mol'), E0=(98.302,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.440892098500625e-16, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing
    Total Standard Deviation in ln(k): 1.115802034799152e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing
Total Standard Deviation in ln(k): 1.115802034799152e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing
Total Standard Deviation in ln(k): 1.115802034799152e-15
""",
)

entry(
    index = 221,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing_Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(173,'kJ/mol'), E0=(95.9587,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing_Sp-4R!H-2R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing_Sp-4R!H-2R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing_Sp-4R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing_Sp-4R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 222,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing_N-Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(173,'kJ/mol'), E0=(100.645,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing_N-Sp-4R!H-2R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing_N-Sp-4R!H-2R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 223,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing",
    kinetics = ArrheniusBM(A=(268174,'m^3/(mol*s)'), n=0.649932, w0=(169.168,'kJ/mol'), E0=(8.25568,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.022274522756211453, var=4.036084053586106, Tref=1000.0, N=107, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing',), comment="""BM rule fitted to 107 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing
    Total Standard Deviation in ln(k): 4.08348043161476"""),
    rank = 11,
    shortDesc = """BM rule fitted to 107 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing
Total Standard Deviation in ln(k): 4.08348043161476""",
    longDesc = 
"""
BM rule fitted to 107 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing
Total Standard Deviation in ln(k): 4.08348043161476
""",
)

entry(
    index = 224,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C",
    kinetics = ArrheniusBM(A=(165155,'m^3/(mol*s)'), n=0.640329, w0=(170.238,'kJ/mol'), E0=(30.5502,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04475704216221732, var=1.347424601814671, Tref=1000.0, N=105, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C',), comment="""BM rule fitted to 105 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C
    Total Standard Deviation in ln(k): 2.439523692044205"""),
    rank = 11,
    shortDesc = """BM rule fitted to 105 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C
Total Standard Deviation in ln(k): 2.439523692044205""",
    longDesc = 
"""
BM rule fitted to 105 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C
Total Standard Deviation in ln(k): 2.439523692044205
""",
)

entry(
    index = 225,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S",
    kinetics = ArrheniusBM(A=(28641.6,'m^3/(mol*s)'), n=0.894523, w0=(136,'kJ/mol'), E0=(48.5387,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05017112034754546, var=1.0341867674379976, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S
    Total Standard Deviation in ln(k): 2.1647729008918577"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S
Total Standard Deviation in ln(k): 2.1647729008918577""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S
Total Standard Deviation in ln(k): 2.1647729008918577
""",
)

entry(
    index = 226,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C",
    kinetics = ArrheniusBM(A=(15609.6,'m^3/(mol*s)'), n=0.89762, w0=(136,'kJ/mol'), E0=(70.8376,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06086937253965734, var=0.0, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C
    Total Standard Deviation in ln(k): 0.15293812195893802"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C
Total Standard Deviation in ln(k): 0.15293812195893802""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C
Total Standard Deviation in ln(k): 0.15293812195893802
""",
)

entry(
    index = 227,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(15609.6,'m^3/(mol*s)'), n=0.89762, w0=(136,'kJ/mol'), E0=(70.3142,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06086936834917852, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.15293811143009678"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.15293811143009678""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.15293811143009678
""",
)

entry(
    index = 228,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(15609.6,'m^3/(mol*s)'), n=0.89762, w0=(136,'kJ/mol'), E0=(69.559,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 229,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_N-3R!H->C",
    kinetics = ArrheniusBM(A=(71187.7,'m^3/(mol*s)'), n=0.889878, w0=(136,'kJ/mol'), E0=(61.8411,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03412373816711143, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_N-3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_N-3R!H->C
    Total Standard Deviation in ln(k): 0.08573803559575735"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_N-3R!H->C
Total Standard Deviation in ln(k): 0.08573803559575735""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_N-3R!H->C
Total Standard Deviation in ln(k): 0.08573803559575735
""",
)

entry(
    index = 230,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_N-3R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(71187.7,'m^3/(mol*s)'), n=0.889878, w0=(136,'kJ/mol'), E0=(62.5403,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_N-3R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_N-3R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_N-3R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_N-3R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 231,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S",
    kinetics = ArrheniusBM(A=(1.41662e+09,'m^3/(mol*s)'), n=-0.656414, w0=(171.95,'kJ/mol'), E0=(95.2985,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03737901574361908, var=3.3762881385160988, Tref=1000.0, N=100, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S',), comment="""BM rule fitted to 100 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S
    Total Standard Deviation in ln(k): 3.777553398592124"""),
    rank = 11,
    shortDesc = """BM rule fitted to 100 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S
Total Standard Deviation in ln(k): 3.777553398592124""",
    longDesc = 
"""
BM rule fitted to 100 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S
Total Standard Deviation in ln(k): 3.777553398592124
""",
)

entry(
    index = 232,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br",
    kinetics = ArrheniusBM(A=(72680.1,'m^3/(mol*s)'), n=0.611725, w0=(142.5,'kJ/mol'), E0=(65.2635,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.017037293925430675, var=10.418254157447697, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br
    Total Standard Deviation in ln(k): 6.513554923181364"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br
Total Standard Deviation in ln(k): 6.513554923181364""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br
Total Standard Deviation in ln(k): 6.513554923181364
""",
)

entry(
    index = 233,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(197869,'m^3/(mol*s)'), n=0.545011, w0=(142.5,'kJ/mol'), E0=(61.7168,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03667693851495551, var=9.189186040759944, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 6.169240919486213"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 6.169240919486213""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 6.169240919486213
""",
)

entry(
    index = 234,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.87561e-13,'m^3/(mol*s)'), n=5.64166, w0=(142.5,'kJ/mol'), E0=(87.5689,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 235,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C",
    kinetics = ArrheniusBM(A=(3.08187e+08,'m^3/(mol*s)'), n=-0.456645, w0=(142.5,'kJ/mol'), E0=(61.9838,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14803576582112554, var=2.853572976908944, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C
    Total Standard Deviation in ln(k): 3.7584522894033894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C
Total Standard Deviation in ln(k): 3.7584522894033894""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C
Total Standard Deviation in ln(k): 3.7584522894033894
""",
)

entry(
    index = 236,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.66906e+08,'m^3/(mol*s)'), n=-0.60886, w0=(142.5,'kJ/mol'), E0=(57.9815,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1417378548032923, var=4.459560672209686, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.589659027943717"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 4.589659027943717""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 4.589659027943717
""",
)

entry(
    index = 237,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.59501e+09,'m^3/(mol*s)'), n=-0.91329, w0=(142.5,'kJ/mol'), E0=(50.8537,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2126067872307201, var=6.81087616907107, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 5.766076427621965"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.766076427621965""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.766076427621965
""",
)

entry(
    index = 238,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R_3R!H->Cl",
    kinetics = ArrheniusBM(A=(4.77213e+06,'m^3/(mol*s)'), n=0.171878, w0=(142.5,'kJ/mol'), E0=(57.719,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R_3R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R_3R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R_3R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R_3R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 239,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R_N-3R!H->Cl",
    kinetics = ArrheniusBM(A=(2.70825e+12,'m^3/(mol*s)'), n=-1.99846, w0=(142.5,'kJ/mol'), E0=(43.9883,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R_N-3R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R_N-3R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R_N-3R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R_N-3R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 240,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_N-Sp-3R!H-1C",
    kinetics = ArrheniusBM(A=(5.19615e+07,'m^3/(mol*s)'), n=0, w0=(142.5,'kJ/mol'), E0=(84.0884,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.166553000908251e-16, var=2.4138979216251584, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_N-Sp-3R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_N-Sp-3R!H-1C
    Total Standard Deviation in ln(k): 3.1147015559000386"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_N-Sp-3R!H-1C
Total Standard Deviation in ln(k): 3.1147015559000386""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_N-Sp-3R!H-1C
Total Standard Deviation in ln(k): 3.1147015559000386
""",
)

entry(
    index = 241,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br",
    kinetics = ArrheniusBM(A=(1.61393e+09,'m^3/(mol*s)'), n=-0.673018, w0=(174.511,'kJ/mol'), E0=(94.86,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03443850225349541, var=3.3530031119056956, Tref=1000.0, N=92, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br',), comment="""BM rule fitted to 92 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br
    Total Standard Deviation in ln(k): 3.7574408497887566"""),
    rank = 11,
    shortDesc = """BM rule fitted to 92 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br
Total Standard Deviation in ln(k): 3.7574408497887566""",
    longDesc = 
"""
BM rule fitted to 92 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br
Total Standard Deviation in ln(k): 3.7574408497887566
""",
)

entry(
    index = 242,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.58438e+09,'m^3/(mol*s)'), n=-0.680032, w0=(174.544,'kJ/mol'), E0=(92.3052,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.044985497533730524, var=3.83376159366093, Tref=1000.0, N=90, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R',), comment="""BM rule fitted to 90 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 4.038298937925498"""),
    rank = 11,
    shortDesc = """BM rule fitted to 90 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 4.038298937925498""",
    longDesc = 
"""
BM rule fitted to 90 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 4.038298937925498
""",
)

entry(
    index = 243,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F",
    kinetics = ArrheniusBM(A=(7.45098e+06,'m^3/(mol*s)'), n=-0.832298, w0=(176.31,'kJ/mol'), E0=(-21.1919,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2384146369919076, var=14.914477840909992, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F',), comment="""BM rule fitted to 21 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F
    Total Standard Deviation in ln(k): 10.853734488350794"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F
Total Standard Deviation in ln(k): 10.853734488350794""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F
Total Standard Deviation in ln(k): 10.853734488350794
""",
)

entry(
    index = 244,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(2.03454e+08,'m^3/(mol*s)'), n=-0.589199, w0=(173,'kJ/mol'), E0=(3.9581,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19963538331842393, var=7.210172744911929, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R
    Total Standard Deviation in ln(k): 5.884663924983251"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R
Total Standard Deviation in ln(k): 5.884663924983251""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R
Total Standard Deviation in ln(k): 5.884663924983251
""",
)

entry(
    index = 245,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.63131e-11,'m^3/(mol*s)'), n=4.71246, w0=(173,'kJ/mol'), E0=(139.101,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 246,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_4R!H->O",
    kinetics = ArrheniusBM(A=(4e+07,'m^3/(mol*s)'), n=0, w0=(173,'kJ/mol'), E0=(88.2769,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 247,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(5.10609e+09,'m^3/(mol*s)'), n=-1.00997, w0=(173,'kJ/mol'), E0=(0.182894,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2030752232360106, var=3.690099749926623, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O
    Total Standard Deviation in ln(k): 4.361261633796893"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O
Total Standard Deviation in ln(k): 4.361261633796893""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O
Total Standard Deviation in ln(k): 4.361261633796893
""",
)

entry(
    index = 248,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F",
    kinetics = ArrheniusBM(A=(5.31635e+11,'m^3/(mol*s)'), n=-1.64268, w0=(173,'kJ/mol'), E0=(1.83333,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.26642151855962876, var=3.25028187885375, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F
    Total Standard Deviation in ln(k): 4.283645083075501"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F
Total Standard Deviation in ln(k): 4.283645083075501""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F
Total Standard Deviation in ln(k): 4.283645083075501
""",
)

entry(
    index = 249,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.80704e+11,'m^3/(mol*s)'), n=-1.71043, w0=(173,'kJ/mol'), E0=(103.211,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09418869825718985, var=0.952038110964405, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R
    Total Standard Deviation in ln(k): 2.1927239576746422"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R
Total Standard Deviation in ln(k): 2.1927239576746422""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R
Total Standard Deviation in ln(k): 2.1927239576746422
""",
)

entry(
    index = 250,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(4.80829e+08,'m^3/(mol*s)'), n=-0.721577, w0=(173,'kJ/mol'), E0=(97.2206,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06302132047686594, var=2.3121660947075444, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 3.2067067767456465"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.2067067767456465""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.2067067767456465
""",
)

entry(
    index = 251,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(1.9799e+06,'m^3/(mol*s)'), n=0, w0=(173,'kJ/mol'), E0=(89.8135,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.5832765004541253e-16, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R
    Total Standard Deviation in ln(k): 1.9651578851126486"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R
Total Standard Deviation in ln(k): 1.9651578851126486""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R
Total Standard Deviation in ln(k): 1.9651578851126486
""",
)

entry(
    index = 252,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R_6R!H->Cl",
    kinetics = ArrheniusBM(A=(2.8e+06,'m^3/(mol*s)'), n=0, w0=(173,'kJ/mol'), E0=(90.1406,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R_6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R_6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 253,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(1.4e+06,'m^3/(mol*s)'), n=0, w0=(173,'kJ/mol'), E0=(89.4864,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R_N-6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R_N-6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 254,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(2.56119e+13,'m^3/(mol*s)'), n=-2.20486, w0=(173,'kJ/mol'), E0=(106.206,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10977238202470588, var=0.8543561534149596, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 2.128814467892811"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.128814467892811""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.128814467892811
""",
)

entry(
    index = 255,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(3.16153e+11,'m^3/(mol*s)'), n=-1.54858, w0=(173,'kJ/mol'), E0=(106.863,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1332670390480019, var=0.8642583207865906, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R
    Total Standard Deviation in ln(k): 2.19855368910603"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R
Total Standard Deviation in ln(k): 2.19855368910603""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R
Total Standard Deviation in ln(k): 2.19855368910603
""",
)

entry(
    index = 256,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_5BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(8.91091e+09,'m^3/(mol*s)'), n=-1.08237, w0=(173,'kJ/mol'), E0=(100.156,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09453198057832876, var=3.2356139136116546, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_5BrCFINOPSSi->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_5BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 3.8435973675984645"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 3.8435973675984645""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 3.8435973675984645
""",
)

entry(
    index = 257,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_5BrCFINOPSSi->Br_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(2.8e+06,'m^3/(mol*s)'), n=0, w0=(173,'kJ/mol'), E0=(88.8321,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_5BrCFINOPSSi->Br_Ext-2CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_5BrCFINOPSSi->Br_Ext-2CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_5BrCFINOPSSi->Br_Ext-2CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_5BrCFINOPSSi->Br_Ext-2CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 258,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_N-5BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(1.12169e+13,'m^3/(mol*s)'), n=-2.01479, w0=(173,'kJ/mol'), E0=(113.571,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1720020915738618, var=0.07952613920554234, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_N-5BrCFINOPSSi->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_N-5BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 0.9975089547998341"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_N-5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 0.9975089547998341""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_N-5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 0.9975089547998341
""",
)

entry(
    index = 259,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_N-5BrCFINOPSSi->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.83587e+13,'m^3/(mol*s)'), n=-2.16473, w0=(173,'kJ/mol'), E0=(116.106,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_N-5BrCFINOPSSi->Br_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_N-5BrCFINOPSSi->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_N-5BrCFINOPSSi->Br_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_N-5BrCFINOPSSi->Br_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 260,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.80345e+13,'m^3/(mol*s)'), n=-2.05221, w0=(173,'kJ/mol'), E0=(83.473,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 261,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F",
    kinetics = ArrheniusBM(A=(204.407,'m^3/(mol*s)'), n=1.30994, w0=(173,'kJ/mol'), E0=(97.708,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.006495679117668562, var=10.327386067777251, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F
    Total Standard Deviation in ln(k): 6.458787698127734"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F
Total Standard Deviation in ln(k): 6.458787698127734""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F
Total Standard Deviation in ln(k): 6.458787698127734
""",
)

entry(
    index = 262,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(925.476,'m^3/(mol*s)'), n=1.08429, w0=(173,'kJ/mol'), E0=(89.9152,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.009601989312046661, var=36.603399325259446, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F_Ext-2CF-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F_Ext-2CF-R
    Total Standard Deviation in ln(k): 12.15292181934084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F_Ext-2CF-R
Total Standard Deviation in ln(k): 12.15292181934084""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F_Ext-2CF-R
Total Standard Deviation in ln(k): 12.15292181934084
""",
)

entry(
    index = 263,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F_Ext-2CF-R_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(1.4e+07,'m^3/(mol*s)'), n=0, w0=(173,'kJ/mol'), E0=(89.1053,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F_Ext-2CF-R_Ext-2CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F_Ext-2CF-R_Ext-2CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F_Ext-2CF-R_Ext-2CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F_Ext-2CF-R_Ext-2CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 264,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C",
    kinetics = ArrheniusBM(A=(1.22533e+19,'m^3/(mol*s)'), n=-4.65414, w0=(173,'kJ/mol'), E0=(107.156,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0291123599725194, var=3.1432128143077245, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C
    Total Standard Deviation in ln(k): 6.139925978955974"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C
Total Standard Deviation in ln(k): 6.139925978955974""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C
Total Standard Deviation in ln(k): 6.139925978955974
""",
)

entry(
    index = 265,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.35279e+19,'m^3/(mol*s)'), n=-4.67047, w0=(173,'kJ/mol'), E0=(104.469,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1952341712979282, var=4.188869180028304, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C_Ext-1C-R
    Total Standard Deviation in ln(k): 7.106137505695212"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.106137505695212""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.106137505695212
""",
)

entry(
    index = 266,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.29446e+18,'m^3/(mol*s)'), n=-4.19701, w0=(173,'kJ/mol'), E0=(127.795,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 267,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_N-2CF->C",
    kinetics = ArrheniusBM(A=(1e+06,'m^3/(mol*s)'), n=0, w0=(242.5,'kJ/mol'), E0=(126.651,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_N-2CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_N-2CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_N-2CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_N-2CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 268,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F",
    kinetics = ArrheniusBM(A=(9.4996e+08,'m^3/(mol*s)'), n=-0.553872, w0=(174.007,'kJ/mol'), E0=(107.36,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04533143464417339, var=2.379338637808372, Tref=1000.0, N=69, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F',), comment="""BM rule fitted to 69 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F
    Total Standard Deviation in ln(k): 3.2062229804737767"""),
    rank = 11,
    shortDesc = """BM rule fitted to 69 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F
Total Standard Deviation in ln(k): 3.2062229804737767""",
    longDesc = 
"""
BM rule fitted to 69 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F
Total Standard Deviation in ln(k): 3.2062229804737767
""",
)

entry(
    index = 269,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(2.94724e+14,'m^3/(mol*s)'), n=-2.79674, w0=(173,'kJ/mol'), E0=(15.7501,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4059670944461193, var=4.3929068346112015, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 5.221794693069276"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 5.221794693069276""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 5.221794693069276
""",
)

entry(
    index = 270,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(6.91206e+12,'m^3/(mol*s)'), n=-2.31041, w0=(173,'kJ/mol'), E0=(0.652496,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.34802699206835497, var=6.911221000028625, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R
    Total Standard Deviation in ln(k): 6.144728059819724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R
Total Standard Deviation in ln(k): 6.144728059819724""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R
Total Standard Deviation in ln(k): 6.144728059819724
""",
)

entry(
    index = 271,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.84829e+11,'m^3/(mol*s)'), n=-2.01038, w0=(173,'kJ/mol'), E0=(1.67777,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.29635477484669037, var=8.489684130166493, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R
    Total Standard Deviation in ln(k): 6.585819118143684"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R
Total Standard Deviation in ln(k): 6.585819118143684""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R
Total Standard Deviation in ln(k): 6.585819118143684
""",
)

entry(
    index = 272,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.95004e+08,'m^3/(mol*s)'), n=-0.654592, w0=(173,'kJ/mol'), E0=(32.6618,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3571663206925548, var=1.4158740863498107, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 3.2828472574542653"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 3.2828472574542653""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 3.2828472574542653
""",
)

entry(
    index = 273,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(92.2154,'m^3/(mol*s)'), n=1.49683, w0=(173,'kJ/mol'), E0=(67.4291,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.056910805468668384, var=2.6324205120309845, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R_Ext-2CF-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R_Ext-2CF-R
    Total Standard Deviation in ln(k): 3.3956216679477214"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R_Ext-2CF-R
Total Standard Deviation in ln(k): 3.3956216679477214""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R_Ext-2CF-R
Total Standard Deviation in ln(k): 3.3956216679477214
""",
)

entry(
    index = 274,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R_Ext-2CF-R_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(25018.3,'m^3/(mol*s)'), n=0.762967, w0=(173,'kJ/mol'), E0=(57.3292,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R_Ext-2CF-R_Ext-2CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R_Ext-2CF-R_Ext-2CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R_Ext-2CF-R_Ext-2CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R_Ext-2CF-R_Ext-2CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 275,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(7.75415e+17,'m^3/(mol*s)'), n=-4.1508, w0=(173,'kJ/mol'), E0=(17.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-2CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-2CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-2CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-2CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 276,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.13778e+18,'m^3/(mol*s)'), n=-3.98591, w0=(173,'kJ/mol'), E0=(140.214,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5386017501249244, var=1.268075927437603, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 3.610780394907533"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 3.610780394907533""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 3.610780394907533
""",
)

entry(
    index = 277,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.0936e+21,'m^3/(mol*s)'), n=-4.94671, w0=(173,'kJ/mol'), E0=(139.63,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 278,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(8.13595e+08,'m^3/(mol*s)'), n=-0.525518, w0=(174.158,'kJ/mol'), E0=(108.009,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.056450919358685785, var=2.309837575337569, Tref=1000.0, N=60, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl',), comment="""BM rule fitted to 60 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 3.188662883612303"""),
    rank = 11,
    shortDesc = """BM rule fitted to 60 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 3.188662883612303""",
    longDesc = 
"""
BM rule fitted to 60 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 3.188662883612303
""",
)

entry(
    index = 279,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.78164e+10,'m^3/(mol*s)'), n=-0.796684, w0=(175.673,'kJ/mol'), E0=(148.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.33575524242363664, var=5.342524857041936, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R',), comment="""BM rule fitted to 26 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 5.4773312351280685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 5.4773312351280685""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 5.4773312351280685
""",
)

entry(
    index = 280,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R",
    kinetics = ArrheniusBM(A=(1.35887e+12,'m^3/(mol*s)'), n=-1.00236, w0=(190.375,'kJ/mol'), E0=(122.548,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14719265409132679, var=2.390745340641604, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R
    Total Standard Deviation in ln(k): 3.4695592324797513"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R
Total Standard Deviation in ln(k): 3.4695592324797513""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R
Total Standard Deviation in ln(k): 3.4695592324797513
""",
)

entry(
    index = 281,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.52887e+10,'m^3/(mol*s)'), n=-0.421056, w0=(173,'kJ/mol'), E0=(86.0342,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.030895812897821735, var=3.1393582276389975, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 3.629664229344913"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.629664229344913""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.629664229344913
""",
)

entry(
    index = 282,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_Ext-5R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.13992e+08,'m^3/(mol*s)'), n=-0.108893, w0=(173,'kJ/mol'), E0=(90.7227,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_Ext-5R!H-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_Ext-5R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 283,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_2CF->C",
    kinetics = ArrheniusBM(A=(2.81979e+07,'m^3/(mol*s)'), n=-0.126529, w0=(173,'kJ/mol'), E0=(52.4656,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_2CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_2CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_2CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_2CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 284,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_N-2CF->C",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(242.5,'kJ/mol'), E0=(126.976,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_N-2CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_N-2CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_N-2CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_N-2CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 285,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O",
    kinetics = ArrheniusBM(A=(7.27036e+07,'m^3/(mol*s)'), n=-0.266667, w0=(173,'kJ/mol'), E0=(40.1462,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03623134627034809, var=1.003233389522121, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O
    Total Standard Deviation in ln(k): 2.0990070397706857"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O
Total Standard Deviation in ln(k): 2.0990070397706857""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O
Total Standard Deviation in ln(k): 2.0990070397706857
""",
)

entry(
    index = 286,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(8.11368e+07,'m^3/(mol*s)'), n=-0.32, w0=(173,'kJ/mol'), E0=(9.82378,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.5226095922391282e-07, var=0.5020281929604099, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R
    Total Standard Deviation in ln(k): 1.4204343293524204"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R
Total Standard Deviation in ln(k): 1.4204343293524204""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R
Total Standard Deviation in ln(k): 1.4204343293524204
""",
)

entry(
    index = 287,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_5R!H->O",
    kinetics = ArrheniusBM(A=(1.4799e+07,'m^3/(mol*s)'), n=3.11304e-08, w0=(173,'kJ/mol'), E0=(37.7974,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=9.193463220142285e-09, var=0.3243450103025167, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_5R!H->O
    Total Standard Deviation in ln(k): 1.1417226287440765"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_5R!H->O
Total Standard Deviation in ln(k): 1.1417226287440765""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_5R!H->O
Total Standard Deviation in ln(k): 1.1417226287440765
""",
)

entry(
    index = 288,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_5R!H->O_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=-7.90496e-08, w0=(173,'kJ/mol'), E0=(64.2298,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_5R!H->O_Ext-2CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_5R!H->O_Ext-2CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_5R!H->O_Ext-2CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_5R!H->O_Ext-2CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 289,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(2.52275e+08,'m^3/(mol*s)'), n=-0.533333, w0=(173,'kJ/mol'), E0=(17.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09789675142796564, var=0.2171391628300253, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O
    Total Standard Deviation in ln(k): 1.1801420658116069"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O
Total Standard Deviation in ln(k): 1.1801420658116069""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O
Total Standard Deviation in ln(k): 1.1801420658116069
""",
)

entry(
    index = 290,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(2.88995e+09,'m^3/(mol*s)'), n=-0.866642, w0=(173,'kJ/mol'), E0=(150.11,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.73600691749923e-16, var=0.18719384195212546, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O_Ext-2CF-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O_Ext-2CF-R
    Total Standard Deviation in ln(k): 0.8673667472246981"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O_Ext-2CF-R
Total Standard Deviation in ln(k): 0.8673667472246981""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O_Ext-2CF-R
Total Standard Deviation in ln(k): 0.8673667472246981
""",
)

entry(
    index = 291,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O_Ext-2CF-R_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(7.75e+08,'m^3/(mol*s)'), n=-0.75, w0=(173,'kJ/mol'), E0=(68.4604,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O_Ext-2CF-R_Ext-2CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O_Ext-2CF-R_Ext-2CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O_Ext-2CF-R_Ext-2CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O_Ext-2CF-R_Ext-2CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 292,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O",
    kinetics = ArrheniusBM(A=(3.40267e+10,'m^3/(mol*s)'), n=-0.792692, w0=(173,'kJ/mol'), E0=(17.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.48117816467576935, var=10.00110388920631, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O
    Total Standard Deviation in ln(k): 7.548869210529466"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O
Total Standard Deviation in ln(k): 7.548869210529466""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O
Total Standard Deviation in ln(k): 7.548869210529466
""",
)

entry(
    index = 293,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(5.44763e+10,'m^3/(mol*s)'), n=-0.821521, w0=(173,'kJ/mol'), E0=(17.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.49637622761910133, var=9.904855231996942, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R
    Total Standard Deviation in ln(k): 7.556474671291582"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R
Total Standard Deviation in ln(k): 7.556474671291582""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R
Total Standard Deviation in ln(k): 7.556474671291582
""",
)

entry(
    index = 294,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.65983e+11,'m^3/(mol*s)'), n=-0.84129, w0=(173,'kJ/mol'), E0=(17.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1366575604485066, var=2.914302663837648, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 3.7657098673484954"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.7657098673484954""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.7657098673484954
""",
)

entry(
    index = 295,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.39195e+11,'m^3/(mol*s)'), n=-0.855542, w0=(173,'kJ/mol'), E0=(80.2691,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08362621578487493, var=0.7494705113280606, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.9456546683702245"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.9456546683702245""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.9456546683702245
""",
)

entry(
    index = 296,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.1576e+11,'m^3/(mol*s)'), n=-0.948728, w0=(173,'kJ/mol'), E0=(81.2369,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 297,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.20378e+09,'m^3/(mol*s)'), n=-0.813265, w0=(173,'kJ/mol'), E0=(76.4155,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 298,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(2.55114e+09,'m^3/(mol*s)'), n=-1.1, w0=(173,'kJ/mol'), E0=(17.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07902162017928036, var=1.9839185473777685, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R
    Total Standard Deviation in ln(k): 3.0222490884962006"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R
Total Standard Deviation in ln(k): 3.0222490884962006""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R
Total Standard Deviation in ln(k): 3.0222490884962006
""",
)

entry(
    index = 299,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.14759e+09,'m^3/(mol*s)'), n=-1.3, w0=(173,'kJ/mol'), E0=(17.3,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11500109114045273, var=4.7818258189085325, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R_Ext-1C-R
    Total Standard Deviation in ln(k): 4.672779094026469"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.672779094026469""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.672779094026469
""",
)

entry(
    index = 300,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R_Ext-1C-R_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(1.24e+10,'m^3/(mol*s)'), n=-1.5, w0=(173,'kJ/mol'), E0=(69.3328,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R_Ext-1C-R_Ext-2CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R_Ext-1C-R_Ext-2CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R_Ext-1C-R_Ext-2CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R_Ext-1C-R_Ext-2CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 301,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_5R!H->C",
    kinetics = ArrheniusBM(A=(3.41902e+08,'m^3/(mol*s)'), n=-0.65, w0=(173,'kJ/mol'), E0=(90.3754,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.007291370132393764, var=0.8826412212865885, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_5R!H->C
    Total Standard Deviation in ln(k): 1.9017483285227228"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_5R!H->C
Total Standard Deviation in ln(k): 1.9017483285227228""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_5R!H->C
Total Standard Deviation in ln(k): 1.9017483285227228
""",
)

entry(
    index = 302,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.98065e+08,'m^3/(mol*s)'), n=-0.75, w0=(173,'kJ/mol'), E0=(89.8378,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.014034090117568947, var=0.8575717470917587, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.8917498551199692"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.8917498551199692""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.8917498551199692
""",
)

entry(
    index = 303,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(173,'kJ/mol'), E0=(86.6078,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 304,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.79314e+07,'m^3/(mol*s)'), n=-0.354978, w0=(173,'kJ/mol'), E0=(93.5762,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.013741703414530529, var=1.5926133177271242, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-1C-R
    Total Standard Deviation in ln(k): 2.5644781905756875"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-1C-R
Total Standard Deviation in ln(k): 2.5644781905756875""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-1C-R
Total Standard Deviation in ln(k): 2.5644781905756875
""",
)

entry(
    index = 305,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R",
    kinetics = ArrheniusBM(A=(9.27205e+07,'m^3/(mol*s)'), n=-0.310628, w0=(173,'kJ/mol'), E0=(89.3776,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03456587760583898, var=0.32744995998498544, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R
    Total Standard Deviation in ln(k): 1.2340233741340056"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R
Total Standard Deviation in ln(k): 1.2340233741340056""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R
Total Standard Deviation in ln(k): 1.2340233741340056
""",
)

entry(
    index = 306,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C",
    kinetics = ArrheniusBM(A=(1.11549e+09,'m^3/(mol*s)'), n=-0.68237, w0=(173,'kJ/mol'), E0=(98.3239,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.29431919638206655, var=1.0853977775937997, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C
    Total Standard Deviation in ln(k): 2.8280770960896398"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C
Total Standard Deviation in ln(k): 2.8280770960896398""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C
Total Standard Deviation in ln(k): 2.8280770960896398
""",
)

entry(
    index = 307,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(1.9609e+09,'m^3/(mol*s)'), n=-0.904668, w0=(173,'kJ/mol'), E0=(22.3689,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.28018604745082587, var=1.8325624862869876, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R
    Total Standard Deviation in ln(k): 3.417838454361126"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R
Total Standard Deviation in ln(k): 3.417838454361126""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R
Total Standard Deviation in ln(k): 3.417838454361126
""",
)

entry(
    index = 308,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF",
    kinetics = ArrheniusBM(A=(2.14313e+13,'m^3/(mol*s)'), n=-2.10789, w0=(173,'kJ/mol'), E0=(86.4833,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2292210902170985, var=0.08276968483892665, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF
    Total Standard Deviation in ln(k): 1.152689076722439"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF
Total Standard Deviation in ln(k): 1.152689076722439""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF
Total Standard Deviation in ln(k): 1.152689076722439
""",
)

entry(
    index = 309,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF_5R!H-inRing",
    kinetics = ArrheniusBM(A=(3.144e+13,'m^3/(mol*s)'), n=-2.163, w0=(173,'kJ/mol'), E0=(86.8507,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF_5R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF_5R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF_5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 310,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(1.80218e+07,'m^3/(mol*s)'), n=-0.134489, w0=(173,'kJ/mol'), E0=(68.6955,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF_N-5R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF_N-5R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF_N-5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF_N-5R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 311,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-5R!H-2CF",
    kinetics = ArrheniusBM(A=(250896,'m^3/(mol*s)'), n=0.298496, w0=(173,'kJ/mol'), E0=(73.0117,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6275205214902675, var=0.8643428515802953, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-5R!H-2CF',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-5R!H-2CF
    Total Standard Deviation in ln(k): 3.4404877499228292"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-5R!H-2CF
Total Standard Deviation in ln(k): 3.4404877499228292""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-5R!H-2CF
Total Standard Deviation in ln(k): 3.4404877499228292
""",
)

entry(
    index = 312,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C",
    kinetics = ArrheniusBM(A=(1.92539e+07,'m^3/(mol*s)'), n=-0.0745672, w0=(173,'kJ/mol'), E0=(74.964,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04600587343232903, var=0.20801607180280726, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C
    Total Standard Deviation in ln(k): 1.0299278369545217"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C
Total Standard Deviation in ln(k): 1.0299278369545217""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C
Total Standard Deviation in ln(k): 1.0299278369545217
""",
)

entry(
    index = 313,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(1.51229e+07,'m^3/(mol*s)'), n=-0.0676006, w0=(173,'kJ/mol'), E0=(49.7923,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.003749406214745409, var=0.08299210480849455, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R
    Total Standard Deviation in ln(k): 0.5869517226875783"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R
Total Standard Deviation in ln(k): 0.5869517226875783""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R
Total Standard Deviation in ln(k): 0.5869517226875783
""",
)

entry(
    index = 314,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-4R!H=3BrBrCCOO",
    kinetics = ArrheniusBM(A=(3.11826e+08,'m^3/(mol*s)'), n=-0.382134, w0=(173,'kJ/mol'), E0=(75.8922,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3183737345414065, var=0.1827168304887792, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-4R!H=3BrBrCCOO',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-4R!H=3BrBrCCOO
    Total Standard Deviation in ln(k): 1.656865819294608"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-4R!H=3BrBrCCOO
Total Standard Deviation in ln(k): 1.656865819294608""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-4R!H=3BrBrCCOO
Total Standard Deviation in ln(k): 1.656865819294608
""",
)

entry(
    index = 315,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-4R!H=3BrBrCCOO_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.81979e+07,'m^3/(mol*s)'), n=-0.126529, w0=(173,'kJ/mol'), E0=(63.0351,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-4R!H=3BrBrCCOO_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-4R!H=3BrBrCCOO_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-4R!H=3BrBrCCOO_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-4R!H=3BrBrCCOO_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 316,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO",
    kinetics = ArrheniusBM(A=(1.93043e+07,'m^3/(mol*s)'), n=-0.098048, w0=(173,'kJ/mol'), E0=(70.9984,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02730475287940057, var=0.08728452577365406, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO
    Total Standard Deviation in ln(k): 0.6608829293167341"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO
Total Standard Deviation in ln(k): 0.6608829293167341""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO
Total Standard Deviation in ln(k): 0.6608829293167341
""",
)

entry(
    index = 317,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO",
    kinetics = ArrheniusBM(A=(2.17712e+06,'m^3/(mol*s)'), n=0.213828, w0=(173,'kJ/mol'), E0=(91.8286,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00017420561540792457, var=0.0990966364878013, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO
    Total Standard Deviation in ln(k): 0.6315206517471764"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO
Total Standard Deviation in ln(k): 0.6315206517471764""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO
Total Standard Deviation in ln(k): 0.6315206517471764
""",
)

entry(
    index = 318,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(2.04234e+06,'m^3/(mol*s)'), n=0.213743, w0=(173,'kJ/mol'), E0=(91.8711,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00019021684654209193, var=0.06095973870725716, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 0.4954475449108113"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 0.4954475449108113""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 0.4954475449108113
""",
)

entry(
    index = 319,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.91473e+06,'m^3/(mol*s)'), n=0.213499, w0=(173,'kJ/mol'), E0=(91.8934,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0002843644781612201, var=0.01520205540628923, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 0.24789153373219883"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.24789153373219883""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.24789153373219883
""",
)

entry(
    index = 320,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.83408e+06,'m^3/(mol*s)'), n=0.21354, w0=(173,'kJ/mol'), E0=(91.946,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00013833959390359632, var=0.009545124775307553, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.19620850882636154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.19620850882636154""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.19620850882636154
""",
)

entry(
    index = 321,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(1.7321e+06,'m^3/(mol*s)'), n=0.213053, w0=(173,'kJ/mol'), E0=(91.7789,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00018445277657968474, var=0.0036396741799292346, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 0.12140853954009201"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.12140853954009201""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.12140853954009201
""",
)

entry(
    index = 322,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.76821e+06,'m^3/(mol*s)'), n=0.213187, w0=(173,'kJ/mol'), E0=(92.0401,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 323,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.91186e+06,'m^3/(mol*s)'), n=0.213947, w0=(173,'kJ/mol'), E0=(92.1381,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 324,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(1.92552e+06,'m^3/(mol*s)'), n=0.212513, w0=(173,'kJ/mol'), E0=(91.8365,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 325,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(3.31402e+06,'m^3/(mol*s)'), n=0.214407, w0=(173,'kJ/mol'), E0=(91.5219,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 326,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO",
    kinetics = ArrheniusBM(A=(8.05579e+10,'m^3/(mol*s)'), n=-1.31825, w0=(173,'kJ/mol'), E0=(70.2335,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11515356162216174, var=8.862062190663219e-05, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO
    Total Standard Deviation in ln(k): 0.30820283748078453"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO
Total Standard Deviation in ln(k): 0.30820283748078453""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO
Total Standard Deviation in ln(k): 0.30820283748078453
""",
)

entry(
    index = 327,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO_3BrCO-inRing",
    kinetics = ArrheniusBM(A=(5.781e+11,'m^3/(mol*s)'), n=-1.568, w0=(173,'kJ/mol'), E0=(71.1639,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO_3BrCO-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO_3BrCO-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO_3BrCO-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO_3BrCO-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 328,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO_N-3BrCO-inRing",
    kinetics = ArrheniusBM(A=(1.92839e+08,'m^3/(mol*s)'), n=-0.425577, w0=(173,'kJ/mol'), E0=(70.7985,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO_N-3BrCO-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO_N-3BrCO-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO_N-3BrCO-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO_N-3BrCO-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 329,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(5.38619e+06,'m^3/(mol*s)'), n=0.213797, w0=(173,'kJ/mol'), E0=(93.1835,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00016139601674549603, var=0.035561666158317407, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.37845447071147176"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.37845447071147176""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.37845447071147176
""",
)

entry(
    index = 330,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(5.749e+06,'m^3/(mol*s)'), n=0.214, w0=(173,'kJ/mol'), E0=(93.1981,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 331,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_3BrCO->Br",
    kinetics = ArrheniusBM(A=(6.23766e+12,'m^3/(mol*s)'), n=-2.0926, w0=(173,'kJ/mol'), E0=(76.0373,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_3BrCO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_3BrCO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_3BrCO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_3BrCO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 332,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br",
    kinetics = ArrheniusBM(A=(5.1212e+08,'m^3/(mol*s)'), n=-0.486282, w0=(173,'kJ/mol'), E0=(74.5286,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09174528502411183, var=2.2086913598763154, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br
    Total Standard Deviation in ln(k): 3.2098862382056246"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br
Total Standard Deviation in ln(k): 3.2098862382056246""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br
Total Standard Deviation in ln(k): 3.2098862382056246
""",
)

entry(
    index = 333,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O",
    kinetics = ArrheniusBM(A=(1.55383e+07,'m^3/(mol*s)'), n=7.91731e-08, w0=(173,'kJ/mol'), E0=(74.2358,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4106194988574241, var=0.041321879286125504, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O
    Total Standard Deviation in ln(k): 1.4392254951870347"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O
Total Standard Deviation in ln(k): 1.4392254951870347""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O
Total Standard Deviation in ln(k): 1.4392254951870347
""",
)

entry(
    index = 334,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(1.54071e+07,'m^3/(mol*s)'), n=2.87541e-08, w0=(173,'kJ/mol'), E0=(73.8976,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4702287212190456, var=0.055106343110206374, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R
    Total Standard Deviation in ln(k): 1.6520855517155943"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R
Total Standard Deviation in ln(k): 1.6520855517155943""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R
Total Standard Deviation in ln(k): 1.6520855517155943
""",
)

entry(
    index = 335,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(173,'kJ/mol'), E0=(94.6468,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-6.661338147750941e-16, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C
    Total Standard Deviation in ln(k): 1.6737030521987289e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C
Total Standard Deviation in ln(k): 1.6737030521987289e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C
Total Standard Deviation in ln(k): 1.6737030521987289e-15
""",
)

entry(
    index = 336,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C_Sp-4C-2CF",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(173,'kJ/mol'), E0=(88.0115,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C_Sp-4C-2CF',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C_Sp-4C-2CF
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C_Sp-4C-2CF
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C_Sp-4C-2CF
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 337,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C_N-Sp-4C-2CF",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(173,'kJ/mol'), E0=(101.282,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C_N-Sp-4C-2CF',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C_N-Sp-4C-2CF
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C_N-Sp-4C-2CF
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C_N-Sp-4C-2CF
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 338,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.51e+07,'m^3/(mol*s)'), n=-4.41403e-09, w0=(173,'kJ/mol'), E0=(62.0036,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 339,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O",
    kinetics = ArrheniusBM(A=(6.53371e+08,'m^3/(mol*s)'), n=-0.521521, w0=(173,'kJ/mol'), E0=(106.067,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1558722777664984, var=2.5591229813264165, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O
    Total Standard Deviation in ln(k): 3.5986655312202775"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O
Total Standard Deviation in ln(k): 3.5986655312202775""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O
Total Standard Deviation in ln(k): 3.5986655312202775
""",
)

entry(
    index = 340,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(9.58073e+08,'m^3/(mol*s)'), n=-0.619182, w0=(173,'kJ/mol'), E0=(92.6958,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.003931094435416637, var=3.092035168239547, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_Sp-3C-1C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_Sp-3C-1C
    Total Standard Deviation in ln(k): 3.5350401112134833"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_Sp-3C-1C
Total Standard Deviation in ln(k): 3.5350401112134833""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_Sp-3C-1C
Total Standard Deviation in ln(k): 3.5350401112134833
""",
)

entry(
    index = 341,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_Sp-3C-1C_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(8.41487e+08,'m^3/(mol*s)'), n=-0.692606, w0=(173,'kJ/mol'), E0=(91.9409,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.48603527133186847, var=0.49451181887314966, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_Sp-3C-1C_Ext-2CF-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_Sp-3C-1C_Ext-2CF-R
    Total Standard Deviation in ln(k): 2.630954614494615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_Sp-3C-1C_Ext-2CF-R
Total Standard Deviation in ln(k): 2.630954614494615""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_Sp-3C-1C_Ext-2CF-R
Total Standard Deviation in ln(k): 2.630954614494615
""",
)

entry(
    index = 342,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(8.46126e+07,'m^3/(mol*s)'), n=4.50611e-11, w0=(173,'kJ/mol'), E0=(123.895,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004336177281116738, var=0.18332710585750625, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 0.869256616574999"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C
Total Standard Deviation in ln(k): 0.869256616574999""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C
Total Standard Deviation in ln(k): 0.869256616574999
""",
)

entry(
    index = 343,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_Sp-3C#1C",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(173,'kJ/mol'), E0=(144.168,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_Sp-3C#1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_Sp-3C#1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_Sp-3C#1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_Sp-3C#1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 344,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_N-Sp-3C#1C",
    kinetics = ArrheniusBM(A=(7.23e+07,'m^3/(mol*s)'), n=0, w0=(173,'kJ/mol'), E0=(113.759,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.110223024625156e-15, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_N-Sp-3C#1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_N-Sp-3C#1C
    Total Standard Deviation in ln(k): 2.789505086997879e-15"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_N-Sp-3C#1C
Total Standard Deviation in ln(k): 2.789505086997879e-15""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_N-Sp-3C#1C
Total Standard Deviation in ln(k): 2.789505086997879e-15
""",
)

entry(
    index = 345,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(7.23e+07,'m^3/(mol*s)'), n=0, w0=(173,'kJ/mol'), E0=(121.132,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 346,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_N-1BrCFS->C",
    kinetics = ArrheniusBM(A=(3.78184e+06,'m^3/(mol*s)'), n=0.702356, w0=(113,'kJ/mol'), E0=(66.2824,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.5951715169634566, var=40.609964819214646, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_N-1BrCFS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_N-1BrCFS->C
    Total Standard Deviation in ln(k): 21.808458645878552"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_N-1BrCFS->C
Total Standard Deviation in ln(k): 21.808458645878552""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_N-1BrCFS->C
Total Standard Deviation in ln(k): 21.808458645878552
""",
)

entry(
    index = 347,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_N-1BrCFS->C_Ext-1BrFS-R",
    kinetics = ArrheniusBM(A=(4.35417e+06,'m^3/(mol*s)'), n=0.747681, w0=(113,'kJ/mol'), E0=(64.5591,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_N-1BrCFS->C_Ext-1BrFS-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_N-1BrCFS->C_Ext-1BrFS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_N-1BrCFS->C_Ext-1BrFS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_N-1BrCFS->C_Ext-1BrFS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

