#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/rules"
shortDesc = u""
longDesc = u"""
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
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->C",
    kinetics = ArrheniusBM(A=(2.8686e+06,'m^3/(mol*s)'), n=0.425846, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_N-3R!H->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 2,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.25e+08,'m^3/(mol*s)'), n=-0.7, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 3,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.76637e+07,'m^3/(mol*s)'), n=0.153073, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00248871722291, var=1.13870876508, Tref=1000.0, N=5, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R
    Total Standard Deviation in ln(k): 2.14551182899"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R
Total Standard Deviation in ln(k): 2.14551182899""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R
Total Standard Deviation in ln(k): 2.14551182899
""",
)

entry(
    index = 4,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing",
    kinetics = ArrheniusBM(A=(2.5021e+10,'m^3/(mol*s)'), n=-0.72284, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21796197679, var=0.116043798991, Tref=1000.0, N=2, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing
    Total Standard Deviation in ln(k): 1.23056021221"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing
Total Standard Deviation in ln(k): 1.23056021221""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing
Total Standard Deviation in ln(k): 1.23056021221
""",
)

entry(
    index = 5,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_4R!H->O",
    kinetics = ArrheniusBM(A=(1.505e+06,'m^3/(mol*s)'), n=1.79841e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_4R!H->O
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_4R!H->O
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_4R!H->O
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 6,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O",
    kinetics = ArrheniusBM(A=(4.52905e+07,'m^3/(mol*s)'), n=-0.17, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.93790333559e-10, var=0.843006791659, Tref=1000.0, N=5, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O
    Total Standard Deviation in ln(k): 1.84065555863"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O
Total Standard Deviation in ln(k): 1.84065555863""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O
Total Standard Deviation in ln(k): 1.84065555863
""",
)

entry(
    index = 7,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O",
    kinetics = ArrheniusBM(A=(1.54072e+07,'m^3/(mol*s)'), n=-6.19948e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.142131114327, var=0.0599978326704, Tref=1000.0, N=3, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O
    Total Standard Deviation in ln(k): 0.848162284374"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O
Total Standard Deviation in ln(k): 0.848162284374""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O
Total Standard Deviation in ln(k): 0.848162284374
""",
)

entry(
    index = 8,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C",
    kinetics = ArrheniusBM(A=(7.84783e+07,'m^3/(mol*s)'), n=0.0629272, w0=(201667,'J/mol'), E0=(20166.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0177834035034, var=0.220663363462, Tref=1000.0, N=9, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C
    Total Standard Deviation in ln(k): 0.986402595487"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C
Total Standard Deviation in ln(k): 0.986402595487""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C
Total Standard Deviation in ln(k): 0.986402595487
""",
)

entry(
    index = 9,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(2.13947e+08,'m^3/(mol*s)'), n=-0.514474, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.000121059371351, var=1.09982367998, Tref=1000.0, N=21, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 2.10271953737"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 2.10271953737""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 2.10271953737
""",
)

entry(
    index = 10,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_2R->C",
    kinetics = ArrheniusBM(A=(3.7586e+07,'m^3/(mol*s)'), n=-0.395795, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00722098163323, var=0.0433403113763, Tref=1000.0, N=2, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_2R->C
    Total Standard Deviation in ln(k): 0.435495654232"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_2R->C
Total Standard Deviation in ln(k): 0.435495654232""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_2R->C
Total Standard Deviation in ln(k): 0.435495654232
""",
)

entry(
    index = 11,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(45504,'m^3/(mol*s)'), n=0.740315, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0441547038934, var=0.0, Tref=1000.0, N=2, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.110941467069"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.110941467069""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.110941467069
""",
)

entry(
    index = 12,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(3.10427e+07,'m^3/(mol*s)'), n=-0.214439, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_N-5R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_N-5R!H-inRing
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_N-5R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_N-5R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 13,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.95927e+08,'m^3/(mol*s)'), n=-0.639165, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0851650107975, var=0.528125578779, Tref=1000.0, N=11, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 1.67086850823"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.67086850823""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 1.67086850823
""",
)

entry(
    index = 14,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.63105e+07,'m^3/(mol*s)'), n=-0.118135, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00652285405283, var=0.794920323305, Tref=1000.0, N=2, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R
    Total Standard Deviation in ln(k): 1.80377688208"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R
Total Standard Deviation in ln(k): 1.80377688208""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R
Total Standard Deviation in ln(k): 1.80377688208
""",
)

entry(
    index = 15,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(5.04559e+09,'m^3/(mol*s)'), n=-0.682225, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0359763322856, var=2.58798417273, Tref=1000.0, N=7, correlation='Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 3.31545278443"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 3.31545278443""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 3.31545278443
""",
)

entry(
    index = 16,
    label = "Root_1R->H_N-2R-inRing_N-2R->H",
    kinetics = ArrheniusBM(A=(1.27835e+08,'m^3/(mol*s)'), n=0.0610269, w0=(181283,'J/mol'), E0=(18128.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.133043932478, var=9.40764000037, Tref=1000.0, N=30, correlation='Root_1R->H_N-2R-inRing_N-2R->H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H
    Total Standard Deviation in ln(k): 6.48317988216"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H
Total Standard Deviation in ln(k): 6.48317988216""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H
Total Standard Deviation in ln(k): 6.48317988216
""",
)

entry(
    index = 17,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(129687,'m^3/(mol*s)'), n=0.801692, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 18,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-2R-R_N-Sp-3R!H-=2R",
    kinetics = ArrheniusBM(A=(4.01625e+07,'m^3/(mol*s)'), n=0.214672, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-2R-R_N-Sp-3R!H-=2R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-2R-R_N-Sp-3R!H-=2R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-2R-R_N-Sp-3R!H-=2R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-2R-R_N-Sp-3R!H-=2R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 19,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(9.33146e+06,'m^3/(mol*s)'), n=0.409212, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 20,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_3R!H->N",
    kinetics = ArrheniusBM(A=(1.32408e+08,'m^3/(mol*s)'), n=-0.361164, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_3R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_3R!H->N
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_3R!H->N
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_3R!H->N
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 21,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(1.36745e+07,'m^3/(mol*s)'), n=-0.263863, w0=(139000,'J/mol'), E0=(13900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00481396807501, var=0.0768145972539, Tref=1000.0, N=3, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R
    Total Standard Deviation in ln(k): 0.567716674236"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R
Total Standard Deviation in ln(k): 0.567716674236""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R
Total Standard Deviation in ln(k): 0.567716674236
""",
)

entry(
    index = 22,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(8.65419e+10,'m^3/(mol*s)'), n=-1.4012, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.218338226454, var=0.11719079963, Tref=1000.0, N=2, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C
    Total Standard Deviation in ln(k): 1.23487231009"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 1.23487231009""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 1.23487231009
""",
)

entry(
    index = 23,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-4R!H-=3R!H_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.02858e+06,'m^3/(mol*s)'), n=0.504886, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-4R!H-=3R!H_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-4R!H-=3R!H_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-4R!H-=3R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-4R!H-=3R!H_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 24,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(7.04085e+06,'m^3/(mol*s)'), n=-0.0872803, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 25,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0",
    kinetics = ArrheniusBM(A=(1.03124e+31,'m^3/(mol*s)'), n=-7.48856, w0=(79333.3,'J/mol'), E0=(7933.33,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.354218852058, var=34.8187486739, Tref=1000.0, N=6, correlation='Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0
    Total Standard Deviation in ln(k): 12.7194203157"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0
Total Standard Deviation in ln(k): 12.7194203157""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0
Total Standard Deviation in ln(k): 12.7194203157
""",
)

entry(
    index = 26,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.4834e+08,'m^3/(mol*s)'), n=-0.557189, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00108714239892, var=1.14816174436, Tref=1000.0, N=4, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 2.15085144951"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 2.15085144951""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 2.15085144951
""",
)

entry(
    index = 27,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.23e+07,'m^3/(mol*s)'), n=-8.53421e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R_Ext-1C-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R_Ext-1C-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 28,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R",
    kinetics = ArrheniusBM(A=(2.14111e+08,'m^3/(mol*s)'), n=-0.500739, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.279825822694, var=1.16058598837, Tref=1000.0, N=6, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R
    Total Standard Deviation in ln(k): 2.86279100961"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R
Total Standard Deviation in ln(k): 2.86279100961""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R
Total Standard Deviation in ln(k): 2.86279100961
""",
)

entry(
    index = 29,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C",
    kinetics = ArrheniusBM(A=(6.75488e+06,'m^3/(mol*s)'), n=0.301153, w0=(110375,'J/mol'), E0=(11037.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0699102737434, var=2.77744018627, Tref=1000.0, N=4, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C
    Total Standard Deviation in ln(k): 3.51667604249"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C
Total Standard Deviation in ln(k): 3.51667604249""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C
Total Standard Deviation in ln(k): 3.51667604249
""",
)

entry(
    index = 30,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_N-3R!H->C",
    kinetics = ArrheniusBM(A=(3.77e+06,'m^3/(mol*s)'), n=-2.20284e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_N-3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_N-3R!H->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_N-3R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_N-3R!H->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 31,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C",
    kinetics = ArrheniusBM(A=(1.72215e+10,'m^3/(mol*s)'), n=-0.966317, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.100863834071, var=0.318288919583, Tref=1000.0, N=4, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C
    Total Standard Deviation in ln(k): 1.38444011628"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C
Total Standard Deviation in ln(k): 1.38444011628""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C
Total Standard Deviation in ln(k): 1.38444011628
""",
)

entry(
    index = 32,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_2R-inRing",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=-1.21605e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_2R-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_2R-inRing
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_2R-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_2R-inRing
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 33,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C",
    kinetics = ArrheniusBM(A=(91220.9,'m^3/(mol*s)'), n=0.645371, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0563208528418, var=0.081353830223, Tref=1000.0, N=8, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C
    Total Standard Deviation in ln(k): 0.713312104122"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C
Total Standard Deviation in ln(k): 0.713312104122""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C
Total Standard Deviation in ln(k): 0.713312104122
""",
)

entry(
    index = 34,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=-1.42812e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_4R!H->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 35,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Sp-4R!H-=3R!H",
    kinetics = ArrheniusBM(A=(4.64055e+29,'m^3/(mol*s)'), n=-6.98707, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Sp-4R!H-=3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Sp-4R!H-=3R!H
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Sp-4R!H-=3R!H
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_Sp-4R!H-=3R!H
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 36,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_2R->C_3R!H->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=-1.37127e-07, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_2R->C_3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_2R->C_3R!H->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_2R->C_3R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_2R->C_3R!H->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 37,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(9.99999e+06,'m^3/(mol*s)'), n=9.65418e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_Sp-4R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_Sp-4R!H-2R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_Sp-4R!H-2R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_Sp-4R!H-2R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 38,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_N-2NO->N_N-3R!H->C",
    kinetics = ArrheniusBM(A=(5250.69,'m^3/(mol*s)'), n=1.27262, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_N-2NO->N_N-3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_N-2NO->N_N-3R!H->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_N-2NO->N_N-3R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_N-2NO->N_N-3R!H->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 39,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_N-Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(578146,'m^3/(mol*s)'), n=0.175759, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.614494871354, var=0.864366397977, Tref=1000.0, N=2, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_N-Sp-5R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_N-Sp-5R!H-1C
    Total Standard Deviation in ln(k): 3.40778537242"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 3.40778537242""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 3.40778537242
""",
)

entry(
    index = 40,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C",
    kinetics = ArrheniusBM(A=(45504,'m^3/(mol*s)'), n=0.740315, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0441547025686, var=0.0, Tref=1000.0, N=3, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C
    Total Standard Deviation in ln(k): 0.11094146374"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C
Total Standard Deviation in ln(k): 0.11094146374""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C
Total Standard Deviation in ln(k): 0.11094146374
""",
)

entry(
    index = 41,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(308.407,'m^3/(mol*s)'), n=0.967216, w0=(139000,'J/mol'), E0=(13900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0049236047651, var=0.0302625193734, Tref=1000.0, N=3, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R
    Total Standard Deviation in ln(k): 0.361117102774"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R
Total Standard Deviation in ln(k): 0.361117102774""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R
Total Standard Deviation in ln(k): 0.361117102774
""",
)

entry(
    index = 42,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-4R!H-=3R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.95338e+06,'m^3/(mol*s)'), n=0.346862, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-4R!H-=3R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-4R!H-=3R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-4R!H-=3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-4R!H-=3R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 43,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(4.50099e+08,'m^3/(mol*s)'), n=-0.701965, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0017319911826, var=1.36934858384, Tref=1000.0, N=9, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 2.35027605843"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 2.35027605843""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 2.35027605843
""",
)

entry(
    index = 44,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_2R->C_N-3R!H->C",
    kinetics = ArrheniusBM(A=(10935.8,'m^3/(mol*s)'), n=0.77776, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0184655330759, var=0.0205899691821, Tref=1000.0, N=2, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_2R->C_N-3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_2R->C_N-3R!H->C
    Total Standard Deviation in ln(k): 0.334059363082"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_2R->C_N-3R!H->C
Total Standard Deviation in ln(k): 0.334059363082""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_2R->C_N-3R!H->C
Total Standard Deviation in ln(k): 0.334059363082
""",
)

entry(
    index = 45,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(45504,'m^3/(mol*s)'), n=0.740315, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_N-2R->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 46,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_2OS->S",
    kinetics = ArrheniusBM(A=(2.85887e+07,'m^3/(mol*s)'), n=0.338251, w0=(71000,'J/mol'), E0=(24020.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_2OS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_2OS->S
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_2OS->S
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_2OS->S
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 47,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C",
    kinetics = ArrheniusBM(A=(7.82867e+07,'m^3/(mol*s)'), n=0.0631113, w0=(205250,'J/mol'), E0=(20525,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0175378549852, var=0.221368827459, Tref=1000.0, N=8, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C
    Total Standard Deviation in ln(k): 0.987289785558"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C
Total Standard Deviation in ln(k): 0.987289785558""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C
Total Standard Deviation in ln(k): 0.987289785558
""",
)

entry(
    index = 48,
    label = "Root_N-1R->H",
    kinetics = ArrheniusBM(A=(4.12325e+06,'m^3/(mol*s)'), n=0.220072, w0=(146681,'J/mol'), E0=(1439.78,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0578190218441, var=4.89406232774, Tref=1000.0, N=102, correlation='Root_N-1R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H
    Total Standard Deviation in ln(k): 4.58025465656"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 4.58025465656""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 4.58025465656
""",
)

entry(
    index = 49,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_N-3R!H->C",
    kinetics = ArrheniusBM(A=(7.05e+06,'m^3/(mol*s)'), n=8.99479e-09, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_N-3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_N-3R!H->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_N-3R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_N-3R!H->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 50,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C",
    kinetics = ArrheniusBM(A=(7.88213e+06,'m^3/(mol*s)'), n=0.314663, w0=(193067,'J/mol'), E0=(19306.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.379272271586, var=0.88677526262, Tref=1000.0, N=15, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C
    Total Standard Deviation in ln(k): 2.84077927867"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C
Total Standard Deviation in ln(k): 2.84077927867""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C
Total Standard Deviation in ln(k): 2.84077927867
""",
)

entry(
    index = 51,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C",
    kinetics = ArrheniusBM(A=(1.64483e+26,'m^3/(mol*s)'), n=-5.36567, w0=(201667,'J/mol'), E0=(20166.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.38384058707, var=325.386444698, Tref=1000.0, N=6, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C
    Total Standard Deviation in ln(k): 47.1770308805"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C
Total Standard Deviation in ln(k): 47.1770308805""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C
Total Standard Deviation in ln(k): 47.1770308805
""",
)

entry(
    index = 52,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R",
    kinetics = ArrheniusBM(A=(7.98328e+06,'m^3/(mol*s)'), n=-8.3375e-07, w0=(122000,'J/mol'), E0=(12200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.6119682562e-08, var=0.123635288982, Tref=1000.0, N=2, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R
    Total Standard Deviation in ln(k): 0.704901181513"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R
Total Standard Deviation in ln(k): 0.704901181513""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R
Total Standard Deviation in ln(k): 0.704901181513
""",
)

entry(
    index = 53,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.76793e+10,'m^3/(mol*s)'), n=-1.00291, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing_Ext-2R-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing_Ext-2R-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing_Ext-2R-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 54,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_2CNOS->S",
    kinetics = ArrheniusBM(A=(1.33939e+07,'m^3/(mol*s)'), n=0.524764, w0=(181667,'J/mol'), E0=(18166.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.33916110237, var=17.7318816581, Tref=1000.0, N=3, correlation='Root_1R->H_N-2R-inRing_N-2R->H_2CNOS->S',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_2CNOS->S
    Total Standard Deviation in ln(k): 14.3190764254"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_2CNOS->S
Total Standard Deviation in ln(k): 14.3190764254""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_2CNOS->S
Total Standard Deviation in ln(k): 14.3190764254
""",
)

entry(
    index = 55,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_N-2NO->N",
    kinetics = ArrheniusBM(A=(2.61215e+06,'m^3/(mol*s)'), n=0.325758, w0=(143500,'J/mol'), E0=(14350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.336871845639, var=0.241325868577, Tref=1000.0, N=2, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_N-2NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_N-2NO->N
    Total Standard Deviation in ln(k): 1.83123636332"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_N-2NO->N
Total Standard Deviation in ln(k): 1.83123636332""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_N-2NO->N
Total Standard Deviation in ln(k): 1.83123636332
""",
)

entry(
    index = 56,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C",
    kinetics = ArrheniusBM(A=(9.37627e+08,'m^3/(mol*s)'), n=-0.294429, w0=(193565,'J/mol'), E0=(19356.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.802829446258, var=19.2997675727, Tref=1000.0, N=23, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C
    Total Standard Deviation in ln(k): 10.8242614663"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C
Total Standard Deviation in ln(k): 10.8242614663""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C
Total Standard Deviation in ln(k): 10.8242614663
""",
)

entry(
    index = 57,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C",
    kinetics = ArrheniusBM(A=(9.18826e+09,'m^3/(mol*s)'), n=-0.839049, w0=(78500,'J/mol'), E0=(7850,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0465430889647, var=0.673853817501, Tref=1000.0, N=5, correlation='Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C
    Total Standard Deviation in ln(k): 1.76260138417"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C
Total Standard Deviation in ln(k): 1.76260138417""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C
Total Standard Deviation in ln(k): 1.76260138417
""",
)

entry(
    index = 58,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C",
    kinetics = ArrheniusBM(A=(9.3042e+08,'m^3/(mol*s)'), n=-0.614675, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0056097018252, var=3.01068616167, Tref=1000.0, N=5, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C
    Total Standard Deviation in ln(k): 3.4925765058"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C
Total Standard Deviation in ln(k): 3.4925765058""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C
Total Standard Deviation in ln(k): 3.4925765058
""",
)

entry(
    index = 59,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N",
    kinetics = ArrheniusBM(A=(403.078,'m^3/(mol*s)'), n=1.76559, w0=(71000,'J/mol'), E0=(13653.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.726705389742, var=5.98513001094, Tref=1000.0, N=2, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N
    Total Standard Deviation in ln(k): 6.73038215317"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N
Total Standard Deviation in ln(k): 6.73038215317""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N
Total Standard Deviation in ln(k): 6.73038215317
""",
)

entry(
    index = 60,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(6.16957e+06,'m^3/(mol*s)'), n=-1.87134e-07, w0=(122000,'J/mol'), E0=(12200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.52051667475e-07, var=0.241111252513, Tref=1000.0, N=4, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O
    Total Standard Deviation in ln(k): 0.984387063055"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O
Total Standard Deviation in ln(k): 0.984387063055""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O
Total Standard Deviation in ln(k): 0.984387063055
""",
)

entry(
    index = 61,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(7.75e+08,'m^3/(mol*s)'), n=-0.75, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 62,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(9.17499e+07,'m^3/(mol*s)'), n=0.115342, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_Sp-4R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 63,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.62598e+07,'m^3/(mol*s)'), n=0.255122, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-2C-R_Ext-5R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 64,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.40832e+09,'m^3/(mol*s)'), n=-1.11667, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.14473363032e-10, var=3.4189890868, Tref=1000.0, N=3, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.70685712135"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.70685712135""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.70685712135
""",
)

entry(
    index = 65,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_2R->C",
    kinetics = ArrheniusBM(A=(6.81404e+07,'m^3/(mol*s)'), n=-2.32247e-07, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.00612506154e-08, var=0.119534414219, Tref=1000.0, N=2, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_2R->C
    Total Standard Deviation in ln(k): 0.69311210551"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_2R->C
Total Standard Deviation in ln(k): 0.69311210551""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_2R->C
Total Standard Deviation in ln(k): 0.69311210551
""",
)

entry(
    index = 66,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(3.00842e+07,'m^3/(mol*s)'), n=0.263537, w0=(205250,'J/mol'), E0=(20525,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0585000762605, var=0.199349423787, Tref=1000.0, N=4, correlation='Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 1.04207053369"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 1.04207053369""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 1.04207053369
""",
)

entry(
    index = 67,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(3.24036e+06,'m^3/(mol*s)'), n=3.5707e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.50055194392e-09, var=0.0475248579916, Tref=1000.0, N=2, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R
    Total Standard Deviation in ln(k): 0.437036213272"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 0.437036213272""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 0.437036213272
""",
)

entry(
    index = 68,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O",
    kinetics = ArrheniusBM(A=(37804.6,'m^3/(mol*s)'), n=0.550145, w0=(125643,'J/mol'), E0=(-16673.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0547341013006, var=4.25993866024, Tref=1000.0, N=28, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O
    Total Standard Deviation in ln(k): 4.27521965564"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O
Total Standard Deviation in ln(k): 4.27521965564""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O
Total Standard Deviation in ln(k): 4.27521965564
""",
)

entry(
    index = 69,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(5.69413e+09,'m^3/(mol*s)'), n=-0.523824, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16007161633, var=0.288590491554, Tref=1000.0, N=3, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 1.47914608549"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 1.47914608549""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 1.47914608549
""",
)

entry(
    index = 70,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_N-2OS->S",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=1.78837e-07, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_N-2OS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_N-2OS->S
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_N-2OS->S
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C_N-3R!H->N_N-2OS->S
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 71,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_2R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.7e+07,'m^3/(mol*s)'), n=4.95181e-08, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_2R->C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_2R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 72,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing",
    kinetics = ArrheniusBM(A=(9.99999e+06,'m^3/(mol*s)'), n=1.28714e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.49162334898e-09, var=0.0, Tref=1000.0, N=2, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing
    Total Standard Deviation in ln(k): 6.26036017332e-09"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing
Total Standard Deviation in ln(k): 6.26036017332e-09""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing
Total Standard Deviation in ln(k): 6.26036017332e-09
""",
)

entry(
    index = 73,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-1N-R_Ext-1N-R_2R->C",
    kinetics = ArrheniusBM(A=(2.33137e+11,'m^3/(mol*s)'), n=-1.13781, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_1CClNOSSi->N_Ext-1N-R_Ext-1N-R_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-1N-R_Ext-1N-R_2R->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-1N-R_Ext-1N-R_2R->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-1N-R_Ext-1N-R_2R->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 74,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_N-3R!H-u0",
    kinetics = ArrheniusBM(A=(6.60235e+128,'m^3/(mol*s)'), n=-37.2419, w0=(71000,'J/mol'), E0=(271802,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.394167378209, var=243.949911149, Tref=1000.0, N=2, correlation='Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_N-3R!H-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_N-3R!H-u0
    Total Standard Deviation in ln(k): 32.3021189072"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_N-3R!H-u0
Total Standard Deviation in ln(k): 32.3021189072""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_N-3R!H-u0
Total Standard Deviation in ln(k): 32.3021189072
""",
)

entry(
    index = 75,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R",
    kinetics = ArrheniusBM(A=(3.18795e+10,'m^3/(mol*s)'), n=-1.17734, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.298025015457, var=0.3094099417, Tref=1000.0, N=5, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R
    Total Standard Deviation in ln(k): 1.86393303255"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R
Total Standard Deviation in ln(k): 1.86393303255""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R
Total Standard Deviation in ln(k): 1.86393303255
""",
)

entry(
    index = 76,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C",
    kinetics = ArrheniusBM(A=(15.724,'m^3/(mol*s)'), n=2.04268, w0=(71000,'J/mol'), E0=(-696.447,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.461512523709, var=5.42084271959, Tref=1000.0, N=3, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C
    Total Standard Deviation in ln(k): 5.82714440121"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C
Total Standard Deviation in ln(k): 5.82714440121""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_N-2R->C
Total Standard Deviation in ln(k): 5.82714440121
""",
)

entry(
    index = 77,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(4.12e+09,'m^3/(mol*s)'), n=-1.1, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 78,
    label = "Root_1R->H_N-2R-inRing_2R->H",
    kinetics = ArrheniusBM(A=(30255.8,'m^3/(mol*s)'), n=0.454367, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0250878995306, var=56.1568697784, Tref=1000.0, N=2, correlation='Root_1R->H_N-2R-inRing_2R->H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_2R->H
    Total Standard Deviation in ln(k): 15.0860960863"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_2R->H
Total Standard Deviation in ln(k): 15.0860960863""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_2R->H
Total Standard Deviation in ln(k): 15.0860960863
""",
)

entry(
    index = 79,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C",
    kinetics = ArrheniusBM(A=(9.98828e+07,'m^3/(mol*s)'), n=0.00561861, w0=(201667,'J/mol'), E0=(20166.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.07954496089, var=4.22925582891, Tref=1000.0, N=3, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C
    Total Standard Deviation in ln(k): 6.83519320067"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C
Total Standard Deviation in ln(k): 6.83519320067""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C
Total Standard Deviation in ln(k): 6.83519320067
""",
)

entry(
    index = 80,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R",
    kinetics = ArrheniusBM(A=(4.63831e+07,'m^3/(mol*s)'), n=-6.58468e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0123271345724, var=1.99454645199, Tref=1000.0, N=6, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R
    Total Standard Deviation in ln(k): 2.86222822617"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R
Total Standard Deviation in ln(k): 2.86222822617""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R
Total Standard Deviation in ln(k): 2.86222822617
""",
)

entry(
    index = 81,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.24e+10,'m^3/(mol*s)'), n=-1.5, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 82,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.52619e+07,'m^3/(mol*s)'), n=-6.53409e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.159897533582, var=0.0656793251983, Tref=1000.0, N=2, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 0.915525659817"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 0.915525659817""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 0.915525659817
""",
)

entry(
    index = 83,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.22275e+29,'m^3/(mol*s)'), n=-6.20388, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=10.070721229, var=800.140618875, Tref=1000.0, N=2, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_Ext-2C-R
    Total Standard Deviation in ln(k): 82.0107735588"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_Ext-2C-R
Total Standard Deviation in ln(k): 82.0107735588""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_Ext-2C-R
Total Standard Deviation in ln(k): 82.0107735588
""",
)

entry(
    index = 84,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing",
    kinetics = ArrheniusBM(A=(199626,'m^3/(mol*s)'), n=0.610916, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0324341459036, var=0.917134149564, Tref=1000.0, N=50, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing
    Total Standard Deviation in ln(k): 2.00136989945"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing
Total Standard Deviation in ln(k): 2.00136989945""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing
Total Standard Deviation in ln(k): 2.00136989945
""",
)

entry(
    index = 85,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(7.82306e+07,'m^3/(mol*s)'), n=0.0632962, w0=(209857,'J/mol'), E0=(20985.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0177752274534, var=0.222667283872, Tref=1000.0, N=7, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R
    Total Standard Deviation in ln(k): 0.990648434191"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 0.990648434191""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 0.990648434191
""",
)

entry(
    index = 86,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(9.74233e+08,'m^3/(mol*s)'), n=-0.300434, w0=(195524,'J/mol'), E0=(19552.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.837794104455, var=19.9890275553, Tref=1000.0, N=21, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.0679984731"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.0679984731""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.0679984731
""",
)

entry(
    index = 87,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_N-2NO->N",
    kinetics = ArrheniusBM(A=(122000,'m^3/(mol*s)'), n=0.2, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_N-2NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_N-2NO->N
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_N-2NO->N
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_N-2NO->N
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 88,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(3.56381e+06,'m^3/(mol*s)'), n=-0.0535546, w0=(152600,'J/mol'), E0=(15260,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0261245836817, var=0.43760691139, Tref=1000.0, N=5, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R
    Total Standard Deviation in ln(k): 1.39180927994"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R
Total Standard Deviation in ln(k): 1.39180927994""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R
Total Standard Deviation in ln(k): 1.39180927994
""",
)

entry(
    index = 89,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_2R-inRing",
    kinetics = ArrheniusBM(A=(5.7e+06,'m^3/(mol*s)'), n=1.36803e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_2R-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_2R-inRing
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_2R-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_2R-inRing
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 90,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-1N-R_Ext-1N-R",
    kinetics = ArrheniusBM(A=(1.08281e+07,'m^3/(mol*s)'), n=0.100375, w0=(75166.7,'J/mol'), E0=(7516.67,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.09139294411, var=4.01089233273, Tref=1000.0, N=3, correlation='Root_N-1R->H_1CClNOSSi->N_Ext-1N-R_Ext-1N-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-1N-R_Ext-1N-R
    Total Standard Deviation in ln(k): 6.75711883075"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-1N-R_Ext-1N-R
Total Standard Deviation in ln(k): 6.75711883075""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-1N-R_Ext-1N-R
Total Standard Deviation in ln(k): 6.75711883075
""",
)

entry(
    index = 91,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_N-2R-inRing",
    kinetics = ArrheniusBM(A=(6.08474e+07,'m^3/(mol*s)'), n=-0.428622, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_N-2R-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_N-2R-inRing
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_N-2R-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_N-2R-inRing
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 92,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.51e+07,'m^3/(mol*s)'), n=2.42855e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_3R!H->O_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 93,
    label = "Root_N-1R->H_1CClNOSSi->N",
    kinetics = ArrheniusBM(A=(398.587,'m^3/(mol*s)'), n=1.63922, w0=(77730.8,'J/mol'), E0=(49953.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.524765286603, var=8.83723212856, Tref=1000.0, N=13, correlation='Root_N-1R->H_1CClNOSSi->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N
    Total Standard Deviation in ln(k): 7.27807842839"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N
Total Standard Deviation in ln(k): 7.27807842839""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N
Total Standard Deviation in ln(k): 7.27807842839
""",
)

entry(
    index = 94,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C",
    kinetics = ArrheniusBM(A=(1.03468e+10,'m^3/(mol*s)'), n=-0.848331, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00516292776992, var=0.173847691771, Tref=1000.0, N=2, correlation='Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C
    Total Standard Deviation in ln(k): 0.848847406671"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C
Total Standard Deviation in ln(k): 0.848847406671""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C
Total Standard Deviation in ln(k): 0.848847406671
""",
)

entry(
    index = 95,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(4.65276e+06,'m^3/(mol*s)'), n=-1.19345e-07, w0=(132200,'J/mol'), E0=(13220,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.53321347418e-07, var=0.780952341849, Tref=1000.0, N=5, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 1.77161500365"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 1.77161500365""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 1.77161500365
""",
)

entry(
    index = 96,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.08049e+08,'m^3/(mol*s)'), n=-0.685207, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.691788023649, var=1.05747121089, Tref=1000.0, N=3, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.79969848986"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.79969848986""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.79969848986
""",
)

entry(
    index = 97,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_N-2NO->N_3R!H->C",
    kinetics = ArrheniusBM(A=(2.80515e+06,'m^3/(mol*s)'), n=0.314888, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_N-2NO->N_3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_N-2NO->N_3R!H->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_N-2NO->N_3R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_N-2NO->N_3R!H->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 98,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_Sp-3CCSS#2R",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=-1.34483e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_Sp-3CCSS#2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_Sp-3CCSS#2R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_Sp-3CCSS#2R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_Sp-3CCSS#2R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 99,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.61526e+07,'m^3/(mol*s)'), n=-0.2125, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.11811042808e-10, var=0.384383286643, Tref=1000.0, N=4, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 1.24290872788"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 1.24290872788""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 1.24290872788
""",
)

entry(
    index = 100,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C",
    kinetics = ArrheniusBM(A=(9.10287e+13,'m^3/(mol*s)'), n=-2.74437, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_N-3R!H->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 101,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.6895e+08,'m^3/(mol*s)'), n=-0.811251, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.000621224287992, var=1.52046208061, Tref=1000.0, N=7, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R
    Total Standard Deviation in ln(k): 2.47353991738"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.47353991738""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.47353991738
""",
)

entry(
    index = 102,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O",
    kinetics = ArrheniusBM(A=(590543,'m^3/(mol*s)'), n=0.538327, w0=(171033,'J/mol'), E0=(17103.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0201293645259, var=3.62478427822, Tref=1000.0, N=61, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O
    Total Standard Deviation in ln(k): 3.86736459191"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O
Total Standard Deviation in ln(k): 3.86736459191""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O
Total Standard Deviation in ln(k): 3.86736459191
""",
)

entry(
    index = 103,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_2R->C",
    kinetics = ArrheniusBM(A=(113109,'m^3/(mol*s)'), n=0.518507, w0=(139000,'J/mol'), E0=(13900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0123104015705, var=1.98462212699, Tref=1000.0, N=3, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_2R->C
    Total Standard Deviation in ln(k): 2.8551336178"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_2R->C
Total Standard Deviation in ln(k): 2.8551336178""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_2R->C
Total Standard Deviation in ln(k): 2.8551336178
""",
)

entry(
    index = 104,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-2R-R",
    kinetics = ArrheniusBM(A=(2.99147e+07,'m^3/(mol*s)'), n=0.155577, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-2R-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-2R-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-2R-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 105,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_N-1CS->C",
    kinetics = ArrheniusBM(A=(1.74988e+07,'m^3/(mol*s)'), n=0.493661, w0=(113000,'J/mol'), E0=(11300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.78036942243, var=24.8279862009, Tref=1000.0, N=2, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_N-1CS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_N-1CS->C
    Total Standard Deviation in ln(k): 16.9749844749"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_N-1CS->C
Total Standard Deviation in ln(k): 16.9749844749""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_N-1CS->C
Total Standard Deviation in ln(k): 16.9749844749
""",
)

entry(
    index = 106,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.42839e+09,'m^3/(mol*s)'), n=-0.858081, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.283695694404, var=1.87999745198, Tref=1000.0, N=4, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R
    Total Standard Deviation in ln(k): 3.46155564072"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R
Total Standard Deviation in ln(k): 3.46155564072""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R
Total Standard Deviation in ln(k): 3.46155564072
""",
)

entry(
    index = 107,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_N-2R->C",
    kinetics = ArrheniusBM(A=(1.57e+07,'m^3/(mol*s)'), n=1.44035e-07, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_N-2R->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_N-2R->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_N-2R->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 108,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-2R-R",
    kinetics = ArrheniusBM(A=(5.22915e+07,'m^3/(mol*s)'), n=0.181361, w0=(194500,'J/mol'), E0=(19450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.150824113586, var=0.0951888293469, Tref=1000.0, N=2, correlation='Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-2R-R
    Total Standard Deviation in ln(k): 0.997469697333"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-2R-R
Total Standard Deviation in ln(k): 0.997469697333""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-2R-R
Total Standard Deviation in ln(k): 0.997469697333
""",
)

entry(
    index = 109,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing",
    kinetics = ArrheniusBM(A=(7.49725e+08,'m^3/(mol*s)'), n=-0.546607, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0173097986373, var=0.452291225768, Tref=1000.0, N=9, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing
    Total Standard Deviation in ln(k): 1.39172842662"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing
Total Standard Deviation in ln(k): 1.39172842662""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing
Total Standard Deviation in ln(k): 1.39172842662
""",
)

entry(
    index = 110,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=-1.37127e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 111,
    label = "Root_1R->H",
    kinetics = ArrheniusBM(A=(1.6326e+08,'m^3/(mol*s)'), n=0.00413565, w0=(190779,'J/mol'), E0=(19077.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0619105688366, var=7.34417314112, Tref=1000.0, N=43, correlation='Root_1R->H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H
    Total Standard Deviation in ln(k): 5.58841330597"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 5.58841330597""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 5.58841330597
""",
)

entry(
    index = 112,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.48129e+07,'m^3/(mol*s)'), n=-0.157514, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 113,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R",
    kinetics = ArrheniusBM(A=(104369,'m^3/(mol*s)'), n=0.705194, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0346096610536, var=0.973963688559, Tref=1000.0, N=10, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R
    Total Standard Deviation in ln(k): 2.06542394964"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R
Total Standard Deviation in ln(k): 2.06542394964""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R
Total Standard Deviation in ln(k): 2.06542394964
""",
)

entry(
    index = 114,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_4R!H-inRing",
    kinetics = ArrheniusBM(A=(601.137,'m^3/(mol*s)'), n=0.87177, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_4R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_4R!H-inRing
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_4R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_4R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 115,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_Ext-2C-R_Ext-3R!H-R",
    kinetics = Arrhenius(
         A = (1.00000e+7,"m^3/(mol*s)"),
        n = (0.00000,""),
        Ea = (0,"J/mol"),
        T0 = (1,"K"),
    ),
    rank = 11,
    shortDesc = u"""Approximately the collision limit""",
    longDesc = 
u"""
To address issue https://github.com/ReactionMechanismGenerator/RMG-database/issues/353
in which it is suggested this rule was auto-generated using poor thermochemistry,
and ended up much too fast, we have replaced it with the previous value for this reaction,
https://rmg.mit.edu/database/kinetics/families/R_Recombination/training/40/
Apparently taken from entry: C9H7_19 + H_15 <=> indene_25
from kinetics library: kislovB
This is pretty much the collision limit. (10^13 cm3/mol/s)
""",
)

entry(
    index = 116,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_2NO->N",
    kinetics = ArrheniusBM(A=(2.63e+08,'m^3/(mol*s)'), n=-1.1, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_2NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_2NO->N
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_2NO->N
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_2NO->N
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 117,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_2R-inRing",
    kinetics = ArrheniusBM(A=(1.77136e+06,'m^3/(mol*s)'), n=0.0494766, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0355540882513, var=0.00255574629843, Tref=1000.0, N=2, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_2R-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_2R-inRing
    Total Standard Deviation in ln(k): 0.190680037989"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_2R-inRing
Total Standard Deviation in ln(k): 0.190680037989""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_2R-inRing
Total Standard Deviation in ln(k): 0.190680037989
""",
)

entry(
    index = 118,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.62598e+07,'m^3/(mol*s)'), n=0.255122, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00414786628487, var=0.0, Tref=1000.0, N=2, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 0.0104217745851"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 0.0104217745851""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 0.0104217745851
""",
)

entry(
    index = 119,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_3C-inRing",
    kinetics = ArrheniusBM(A=(8.89521e+07,'m^3/(mol*s)'), n=0.0353438, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_3C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_3C-inRing
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_3C-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_3C-inRing
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 120,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_5R!H-inRing",
    kinetics = ArrheniusBM(A=(1.11452e+11,'m^3/(mol*s)'), n=-1.43904, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_5R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_5R!H-inRing
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_5R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_Sp-3R!H=2R_Ext-1C-R_Sp-5R!H-1C_5R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 121,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_2R->C",
    kinetics = ArrheniusBM(A=(6.89518e+73,'m^3/(mol*s)'), n=-21.0166, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_2R->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_2R->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_2R->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 122,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-4R!H-=3R!H",
    kinetics = ArrheniusBM(A=(4.97333e+06,'m^3/(mol*s)'), n=0.298336, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00838141925469, var=0.779307072033, Tref=1000.0, N=3, correlation='Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-4R!H-=3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-4R!H-=3R!H
    Total Standard Deviation in ln(k): 1.79080630403"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-4R!H-=3R!H
Total Standard Deviation in ln(k): 1.79080630403""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R_N-Sp-4R!H-=3R!H
Total Standard Deviation in ln(k): 1.79080630403
""",
)

entry(
    index = 123,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-3R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=1.78837e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-3R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-3R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-3R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 124,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_N-Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(3.45106e-07,'m^3/(mol*s)'), n=3.72998, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_N-Sp-4R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_N-Sp-4R!H-2R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 125,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(106477,'m^3/(mol*s)'), n=0.348287, w0=(140789,'J/mol'), E0=(14078.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0108230153501, var=2.70964383578, Tref=1000.0, N=19, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R
    Total Standard Deviation in ln(k): 3.32718707999"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R
Total Standard Deviation in ln(k): 3.32718707999""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R
Total Standard Deviation in ln(k): 3.32718707999
""",
)

entry(
    index = 126,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C",
    kinetics = ArrheniusBM(A=(129687,'m^3/(mol*s)'), n=0.801692, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0247533941213, var=0.0, Tref=1000.0, N=2, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C
    Total Standard Deviation in ln(k): 0.0621944575911"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C
Total Standard Deviation in ln(k): 0.0621944575911""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_N-3R!H->C
Total Standard Deviation in ln(k): 0.0621944575911
""",
)

entry(
    index = 127,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R",
    kinetics = ArrheniusBM(A=(5.3914e+06,'m^3/(mol*s)'), n=0.320354, w0=(123500,'J/mol'), E0=(12350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00769442559707, var=3.73743573387, Tref=1000.0, N=3, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R
    Total Standard Deviation in ln(k): 3.89497653508"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R
Total Standard Deviation in ln(k): 3.89497653508""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R
Total Standard Deviation in ln(k): 3.89497653508
""",
)

entry(
    index = 128,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S",
    kinetics = ArrheniusBM(A=(4.95222e+08,'m^3/(mol*s)'), n=-0.217361, w0=(181241,'J/mol'), E0=(18124.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.456330193395, var=13.8732277567, Tref=1000.0, N=27, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S
    Total Standard Deviation in ln(k): 8.61355133141"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S
Total Standard Deviation in ln(k): 8.61355133141""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S
Total Standard Deviation in ln(k): 8.61355133141
""",
)

entry(
    index = 129,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(2.41364e+09,'m^3/(mol*s)'), n=-0.390932, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00603156000563, var=0.104335976043, Tref=1000.0, N=4, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C
    Total Standard Deviation in ln(k): 0.662705751806"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 0.662705751806""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 0.662705751806
""",
)

entry(
    index = 130,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-1N-R",
    kinetics = ArrheniusBM(A=(6.74236e+06,'m^3/(mol*s)'), n=0.142499, w0=(77250,'J/mol'), E0=(7725,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0607054911525, var=1.94482475529, Tref=1000.0, N=4, correlation='Root_N-1R->H_1CClNOSSi->N_Ext-1N-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-1N-R
    Total Standard Deviation in ln(k): 2.94826923214"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-1N-R
Total Standard Deviation in ln(k): 2.94826923214""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-1N-R
Total Standard Deviation in ln(k): 2.94826923214
""",
)

entry(
    index = 131,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.48129e+07,'m^3/(mol*s)'), n=-0.157514, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 132,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_N-Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(9.99999e+06,'m^3/(mol*s)'), n=9.65418e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_N-Sp-4R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_N-Sp-4R!H-2R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R_N-2R-inRing_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 133,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.78708e+06,'m^3/(mol*s)'), n=-0.129357, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Ext-2R-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 134,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H",
    kinetics = ArrheniusBM(A=(6.28654e+07,'m^3/(mol*s)'), n=-0.211676, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00579809229276, var=0.287312654976, Tref=1000.0, N=3, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H
    Total Standard Deviation in ln(k): 1.0891372184"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H
Total Standard Deviation in ln(k): 1.0891372184""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_Sp-4R!H=3R!H
Total Standard Deviation in ln(k): 1.0891372184
""",
)

entry(
    index = 135,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R",
    kinetics = ArrheniusBM(A=(164141,'m^3/(mol*s)'), n=0.637502, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0311760265022, var=0.946024688451, Tref=1000.0, N=48, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R
    Total Standard Deviation in ln(k): 2.02821325078"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R
Total Standard Deviation in ln(k): 2.02821325078""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R
Total Standard Deviation in ln(k): 2.02821325078
""",
)

entry(
    index = 136,
    label = "Root_1R->H_2R-inRing",
    kinetics = ArrheniusBM(A=(5.62514e+08,'m^3/(mol*s)'), n=-0.277158, w0=(212091,'J/mol'), E0=(21209.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0171165426824, var=1.95021798231, Tref=1000.0, N=11, correlation='Root_1R->H_2R-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing
    Total Standard Deviation in ln(k): 2.84262303871"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing
Total Standard Deviation in ln(k): 2.84262303871""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing
Total Standard Deviation in ln(k): 2.84262303871
""",
)

entry(
    index = 137,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.67503e+10,'m^3/(mol*s)'), n=-0.732092, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_N-Sp-4R!H=3C_N-Sp-4R!H-3C_N-3C-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 138,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.7487e+12,'m^3/(mol*s)'), n=-1.52302, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0804082824434, var=2.76117179731, Tref=1000.0, N=4, correlation='Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 3.53325384094"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.53325384094""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.53325384094
""",
)

entry(
    index = 139,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(5.15801e+06,'m^3/(mol*s)'), n=0.423463, w0=(201667,'J/mol'), E0=(20166.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00140340965819, var=0.294742016181, Tref=1000.0, N=3, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C
    Total Standard Deviation in ln(k): 1.09189979396"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 1.09189979396""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 1.09189979396
""",
)

entry(
    index = 140,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R",
    kinetics = ArrheniusBM(A=(37016,'m^3/(mol*s)'), n=0.5518, w0=(132200,'J/mol'), E0=(-16592.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0638405962927, var=4.31215946294, Tref=1000.0, N=25, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R
    Total Standard Deviation in ln(k): 4.32338419159"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R
Total Standard Deviation in ln(k): 4.32338419159""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R
Total Standard Deviation in ln(k): 4.32338419159
""",
)

entry(
    index = 141,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=-1.42812e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 142,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1374.05,'m^3/(mol*s)'), n=1.72073, w0=(77250,'J/mol'), E0=(43534.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.152210486783, var=35.9417334497, Tref=1000.0, N=8, correlation='Root_N-1R->H_1CClNOSSi->N_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R
    Total Standard Deviation in ln(k): 12.4011108484"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R
Total Standard Deviation in ln(k): 12.4011108484""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R
Total Standard Deviation in ln(k): 12.4011108484
""",
)

entry(
    index = 143,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(3.63222,'m^3/(mol*s)'), n=1.59841, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_N-4R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_N-4R!H-inRing
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 144,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-2R-R_Sp-3R!H-=2R",
    kinetics = ArrheniusBM(A=(2.2e+08,'m^3/(mol*s)'), n=1.30791e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-2R-R_Sp-3R!H-=2R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-2R-R_Sp-3R!H-=2R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-2R-R_Sp-3R!H-=2R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-2R-R_Sp-3R!H-=2R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 145,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.1534e+07,'m^3/(mol*s)'), n=0.0505704, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00289490297729, var=9.94451676066, Tref=1000.0, N=2, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 6.32919123293"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 6.32919123293""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_Sp-3R!H=2C_3R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 6.32919123293
""",
)

entry(
    index = 146,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_N-2R->C",
    kinetics = ArrheniusBM(A=(1.81e+06,'m^3/(mol*s)'), n=-5.80997e-08, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_N-2R->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_N-2R->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Sp-4R!H-2R_N-2R->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 147,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(1.48138e+06,'m^3/(mol*s)'), n=-0.119415, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 148,
    label = "Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(4.43763e+07,'m^3/(mol*s)'), n=-0.328516, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_2R-inRing_Ext-2R-R_Ext-3R!H-R_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 149,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_4R!H->C",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=1.10623e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_4R!H->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_4R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_4R!H->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 150,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.53609e+09,'m^3/(mol*s)'), n=-0.946459, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.000724761308015, var=1.22133425516, Tref=1000.0, N=6, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 2.2173337826"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 2.2173337826""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 2.2173337826
""",
)

entry(
    index = 151,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.80332e+07,'m^3/(mol*s)'), n=0.127561, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00207394171242, var=4.85073603852, Tref=1000.0, N=2, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-3R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 4.42051694063"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.42051694063""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_Ext-2C-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 4.42051694063
""",
)

entry(
    index = 152,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R",
    kinetics = ArrheniusBM(A=(5.66445e+06,'m^3/(mol*s)'), n=-0.45, w0=(77250,'J/mol'), E0=(7725,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.16655300091e-16, var=3.401841873, Tref=1000.0, N=2, correlation='Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R
    Total Standard Deviation in ln(k): 3.69754995947"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R
Total Standard Deviation in ln(k): 3.69754995947""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R
Total Standard Deviation in ln(k): 3.69754995947
""",
)

entry(
    index = 153,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R",
    kinetics = ArrheniusBM(A=(1.1146e+21,'m^3/(mol*s)'), n=-4.68812, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 154,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H",
    kinetics = ArrheniusBM(A=(5.67927e+10,'m^3/(mol*s)'), n=-1.26686, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.103891372706, var=0.0257351059192, Tref=1000.0, N=2, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H
    Total Standard Deviation in ln(k): 0.582636509508"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H
Total Standard Deviation in ln(k): 0.582636509508""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H
Total Standard Deviation in ln(k): 0.582636509508
""",
)

entry(
    index = 155,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C",
    kinetics = ArrheniusBM(A=(3.65367e+06,'m^3/(mol*s)'), n=0.2352, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.470950179139, var=0.481323982295, Tref=1000.0, N=2, correlation='Root_N-1R->H_1CClNOSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C
    Total Standard Deviation in ln(k): 2.57412732042"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C
Total Standard Deviation in ln(k): 2.57412732042""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C
Total Standard Deviation in ln(k): 2.57412732042
""",
)

entry(
    index = 156,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_3R!H->C",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=-5.81278e-09, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_3R!H->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_3R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_3R!H->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 157,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(6.30526e+07,'m^3/(mol*s)'), n=-0.283333, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-6.50053689359e-11, var=0.305422193575, Tref=1000.0, N=3, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 1.10791715097"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 1.10791715097""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 1.10791715097
""",
)

entry(
    index = 158,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.8345e+07,'m^3/(mol*s)'), n=-0.175, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.38215142465e-09, var=1.02308715893, Tref=1000.0, N=2, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.02774485734"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.02774485734""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.02774485734
""",
)

entry(
    index = 159,
    label = "Root_N-1R->H_N-1CClNOSSi->N",
    kinetics = ArrheniusBM(A=(388820,'m^3/(mol*s)'), n=0.540123, w0=(156753,'J/mol'), E0=(-102376,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0275389427923, var=4.36991544586, Tref=1000.0, N=89, correlation='Root_N-1R->H_N-1CClNOSSi->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N
    Total Standard Deviation in ln(k): 4.25996023581"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N
Total Standard Deviation in ln(k): 4.25996023581""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N
Total Standard Deviation in ln(k): 4.25996023581
""",
)

entry(
    index = 160,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(8.43648e+08,'m^3/(mol*s)'), n=-0.692983, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.486034813833, var=0.494552119499, Tref=1000.0, N=2, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_4R!H->C
    Total Standard Deviation in ln(k): 2.63101090859"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 2.63101090859""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 2.63101090859
""",
)

entry(
    index = 161,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C",
    kinetics = ArrheniusBM(A=(2.58432e+07,'m^3/(mol*s)'), n=-0.0956355, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0184614839253, var=0.814135090552, Tref=1000.0, N=5, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C
    Total Standard Deviation in ln(k): 1.85524676771"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C
Total Standard Deviation in ln(k): 1.85524676771""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C
Total Standard Deviation in ln(k): 1.85524676771
""",
)

entry(
    index = 162,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(6.64e+07,'m^3/(mol*s)'), n=-0.35, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 163,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_3C-inRing",
    kinetics = ArrheniusBM(A=(4.64183e+06,'m^3/(mol*s)'), n=0.438923, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.000133802134542, var=0.433753886377, Tref=1000.0, N=2, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_3C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_3C-inRing
    Total Standard Deviation in ln(k): 1.32065459619"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_3C-inRing
Total Standard Deviation in ln(k): 1.32065459619""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_3C-inRing
Total Standard Deviation in ln(k): 1.32065459619
""",
)

entry(
    index = 164,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_3R!H->C",
    kinetics = ArrheniusBM(A=(9.04e+06,'m^3/(mol*s)'), n=-5.64022e-08, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_3R!H->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_3R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-2R-R_N-4R!H->O_Ext-2R-R_3R!H->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 165,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=-1.37127e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_3R!H->O_Ext-1C-R_5R!H->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 166,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(3.17094e+06,'m^3/(mol*s)'), n=0.460394, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 167,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(3.5e+06,'m^3/(mol*s)'), n=1.0712e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 168,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-6C-R",
    kinetics = ArrheniusBM(A=(1.33755e+09,'m^3/(mol*s)'), n=-0.828757, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-6C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-6C-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-6C-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_Ext-2R-R_Ext-1C-R_6R!H->C_Ext-6C-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 169,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_2NO->N",
    kinetics = ArrheniusBM(A=(1.12206e+07,'m^3/(mol*s)'), n=0.314888, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_2NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_2NO->N
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_2NO->N
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_N-2CNO->C_Ext-2NO-R_2NO->N
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 170,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_N-3C-inRing",
    kinetics = ArrheniusBM(A=(1.62598e+07,'m^3/(mol*s)'), n=0.255122, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_N-3C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_N-3C-inRing
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_N-3C-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_N-3C-inRing
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 171,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R",
    kinetics = ArrheniusBM(A=(7.23001e+07,'m^3/(mol*s)'), n=-9.93442e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.23272519859e-11, var=0.0, Tref=1000.0, N=2, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R
    Total Standard Deviation in ln(k): 8.12242512209e-11"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R
Total Standard Deviation in ln(k): 8.12242512209e-11""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O_N-Sp-3CCSS#2R
Total Standard Deviation in ln(k): 8.12242512209e-11
""",
)

entry(
    index = 172,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C",
    kinetics = ArrheniusBM(A=(315400,'m^3/(mol*s)'), n=0.546593, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0328000692469, var=0.856170432709, Tref=1000.0, N=59, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C
    Total Standard Deviation in ln(k): 1.93738313973"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C
Total Standard Deviation in ln(k): 1.93738313973""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C
Total Standard Deviation in ln(k): 1.93738313973
""",
)

entry(
    index = 173,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_2CNOS->S_Ext-2S-R",
    kinetics = ArrheniusBM(A=(6.69928e+07,'m^3/(mol*s)'), n=0.692369, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_N-2R-inRing_N-2R->H_2CNOS->S_Ext-2S-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_2CNOS->S_Ext-2S-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_2CNOS->S_Ext-2S-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_2CNOS->S_Ext-2S-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 174,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(8.92033e+06,'m^3/(mol*s)'), n=1.17885e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0370545850026, var=0.142813102216, Tref=1000.0, N=3, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R
    Total Standard Deviation in ln(k): 0.850703803965"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R
Total Standard Deviation in ln(k): 0.850703803965""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_N-Sp-3R!H-1C_Ext-2R-R
Total Standard Deviation in ln(k): 0.850703803965
""",
)

entry(
    index = 175,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(101631,'m^3/(mol*s)'), n=0.35323, w0=(139000,'J/mol'), E0=(13900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0148472730165, var=2.75207767881, Tref=1000.0, N=9, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 3.36303735057"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.36303735057""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.36303735057
""",
)

entry(
    index = 176,
    label = "Root_1R->H_N-2R-inRing",
    kinetics = ArrheniusBM(A=(1.26936e+08,'m^3/(mol*s)'), n=0.0613599, w0=(183453,'J/mol'), E0=(18345.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.131160529267, var=9.43217642564, Tref=1000.0, N=32, correlation='Root_1R->H_N-2R-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing
    Total Standard Deviation in ln(k): 6.48646108043"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing
Total Standard Deviation in ln(k): 6.48646108043""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing
Total Standard Deviation in ln(k): 6.48646108043
""",
)

entry(
    index = 177,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C",
    kinetics = ArrheniusBM(A=(9.29149e+06,'m^3/(mol*s)'), n=-0.3, w0=(75166.7,'J/mol'), E0=(7516.67,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.40309720458e-11, var=16.7795781874, Tref=1000.0, N=3, correlation='Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C
    Total Standard Deviation in ln(k): 8.21197292804"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C
Total Standard Deviation in ln(k): 8.21197292804""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C
Total Standard Deviation in ln(k): 8.21197292804
""",
)

entry(
    index = 178,
    label = "Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C_Ext-1N-R",
    kinetics = ArrheniusBM(A=(2.57593e+11,'m^3/(mol*s)'), n=-1.2919, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C_Ext-1N-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C_Ext-1N-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C_Ext-1N-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1CClNOSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C_Ext-1N-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 179,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.12408e+07,'m^3/(mol*s)'), n=0.159297, w0=(159759,'J/mol'), E0=(8347.73,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0296844859348, var=6.10981833732, Tref=1000.0, N=145, correlation='Root',), comment="""BM rule fitted to 2 training reactions at node Root
    Total Standard Deviation in ln(k): 5.02989766626"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 5.02989766626""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root
Total Standard Deviation in ln(k): 5.02989766626
""",
)

entry(
    index = 180,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(6.79503e+06,'m^3/(mol*s)'), n=0.417452, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_Sp-3C-2C_Ext-3C-R_Sp-4R!H=3C_3C-inRing_Ext-4R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 181,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O",
    kinetics = ArrheniusBM(A=(8.46129e+07,'m^3/(mol*s)'), n=-5.23396e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00433609697246, var=0.183327166906, Tref=1000.0, N=3, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O
    Total Standard Deviation in ln(k): 0.869256557712"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O
Total Standard Deviation in ln(k): 0.869256557712""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_N-Sp-3R!H-2R_N-3R!H->O
Total Standard Deviation in ln(k): 0.869256557712
""",
)

entry(
    index = 182,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(2.46571e+08,'m^3/(mol*s)'), n=-0.461716, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_N-3R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_N-3R!H-inRing
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_N-3R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_N-3R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 183,
    label = "Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_N-Sp-3C-2C",
    kinetics = ArrheniusBM(A=(1.81e+08,'m^3/(mol*s)'), n=-8.9089e-10, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_N-Sp-3C-2C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_N-Sp-3C-2C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R-inRing_N-2R->H_N-2CNOS->S_2CNO->C_Ext-2C-R_N-Sp-3R!H=2C_3R!H->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 184,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.12455e+08,'m^3/(mol*s)'), n=-0.428757, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 185,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_3R!H-inRing",
    kinetics = ArrheniusBM(A=(6.75496e+10,'m^3/(mol*s)'), n=-1.29253, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_3R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_3R!H-inRing
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_3R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-3R!H-R_N-Sp-3R!H=2R_N-Sp-4R!H=3R!H_3R!H-inRing
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 186,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O",
    kinetics = ArrheniusBM(A=(2.49263e+08,'m^3/(mol*s)'), n=-0.519467, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00186367249776, var=0.658318197044, Tref=1000.0, N=7, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O
    Total Standard Deviation in ln(k): 1.6312606891"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O
Total Standard Deviation in ln(k): 1.6312606891""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Ext-2R-R_N-3R!H->O
Total Standard Deviation in ln(k): 1.6312606891
""",
)

entry(
    index = 187,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing",
    kinetics = ArrheniusBM(A=(1.79861e+10,'m^3/(mol*s)'), n=-0.973503, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0958344498313, var=0.310258299277, Tref=1000.0, N=3, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing
    Total Standard Deviation in ln(k): 1.35744424775"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing
Total Standard Deviation in ln(k): 1.35744424775""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_1C-inRing_Ext-1C-R_Sp-3R!H-1C_N-2R-inRing
Total Standard Deviation in ln(k): 1.35744424775
""",
)

entry(
    index = 188,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=-1.42812e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_1CS->C_N-1C-inRing_Ext-2R-R_Sp-3R!H-2R_3R!H->C_2R->C_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 189,
    label = "Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_N-1CS->C_Ext-1S-R",
    kinetics = ArrheniusBM(A=(9.40412e+06,'m^3/(mol*s)'), n=0.634469, w0=(113000,'J/mol'), E0=(11300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.1368631905, Tref=1000.0, N=1, correlation='Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_N-1CS->C_Ext-1S-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_N-1CS->C_Ext-1S-R
    Total Standard Deviation in ln(k): 11.5401827615"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_N-1CS->C_Ext-1S-R
Total Standard Deviation in ln(k): 11.5401827615""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_N-1COS->O_N-1CS->C_Ext-1S-R
Total Standard Deviation in ln(k): 11.5401827615
""",
)

entry(
    index = 190,
    label = "Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(297.12,'m^3/(mol*s)'), n=0.971996, w0=(122000,'J/mol'), E0=(12200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0290918489436, var=0.0160072644778, Tref=1000.0, N=2, correlation='Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 0.326733816017"""),
    rank = 11,
    shortDesc = u"""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 0.326733816017""",
    longDesc = 
u"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1CClNOSSi->N_1COS->O_Ext-1O-R_Ext-2R-R_Ext-4R!H-R_Sp-4R!H-2R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 0.326733816017
""",
)

