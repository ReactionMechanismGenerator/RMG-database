#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_vdW/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = SurfaceArrheniusBM(A=(8390.78,'m^2/(mol*s)'), n=3.83932, w0=(415709,'J/mol'), E0=(91041.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21169174812920594, var=15.774803363451214, Tref=1000.0, N=54, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 54 training reactions at node Root
    Total Standard Deviation in ln(k): 8.494196695858765"""),
    rank = 11,
    shortDesc = """BM rule fitted to 54 training reactions at node Root
Total Standard Deviation in ln(k): 8.494196695858765""",
    longDesc = 
"""
BM rule fitted to 54 training reactions at node Root
Total Standard Deviation in ln(k): 8.494196695858765
""",
)

entry(
    index = 2,
    label = "Root_1R!H->N",
    kinetics = SurfaceArrheniusBM(A=(1.82992e-15,'m^2/(mol*s)'), n=9.30014, w0=(387621,'J/mol'), E0=(67796.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5107594847308008, var=11.699784369681064, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_1R!H->N',), comment="""BM rule fitted to 19 training reactions at node Root_1R!H->N
    Total Standard Deviation in ln(k): 8.140501105864207"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_1R!H->N
Total Standard Deviation in ln(k): 8.140501105864207""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_1R!H->N
Total Standard Deviation in ln(k): 8.140501105864207
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H->N",
    kinetics = SurfaceArrheniusBM(A=(4.91691e+27,'m^2/(mol*s)'), n=-3.14753, w0=(430957,'J/mol'), E0=(129223,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.16426979122802238, var=12.305602828188064, Tref=1000.0, N=35, data_mean=0.0, correlation='Root_N-1R!H->N',), comment="""BM rule fitted to 35 training reactions at node Root_N-1R!H->N
    Total Standard Deviation in ln(k): 7.445217045046951"""),
    rank = 11,
    shortDesc = """BM rule fitted to 35 training reactions at node Root_N-1R!H->N
Total Standard Deviation in ln(k): 7.445217045046951""",
    longDesc = 
"""
BM rule fitted to 35 training reactions at node Root_N-1R!H->N
Total Standard Deviation in ln(k): 7.445217045046951
""",
)

entry(
    index = 4,
    label = "Root_1R!H->N_facet111",
    kinetics = SurfaceArrheniusBM(A=(9.64737e+15,'m^2/(mol*s)'), n=0, w0=(406419,'J/mol'), E0=(122888,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->N_facet111',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->N_facet111
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->N_facet111
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->N_facet111
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_1R!H->N_facet211",
    kinetics = SurfaceArrheniusBM(A=(3.03488e-11,'m^2/(mol*s)'), n=8.07061, w0=(383309,'J/mol'), E0=(81577.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.44842274488481765, var=10.431604817928065, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R!H->N_facet211',), comment="""BM rule fitted to 16 training reactions at node Root_1R!H->N_facet211
    Total Standard Deviation in ln(k): 7.60158266677931"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R!H->N_facet211
Total Standard Deviation in ln(k): 7.60158266677931""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R!H->N_facet211
Total Standard Deviation in ln(k): 7.60158266677931
""",
)

entry(
    index = 6,
    label = "Root_1R!H->N_facet0001step",
    kinetics = SurfaceArrheniusBM(A=(9.64737e+15,'m^2/(mol*s)'), n=0, w0=(418225,'J/mol'), E0=(71402.5,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H->N_facet0001step',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H->N_facet0001step
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H->N_facet0001step
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H->N_facet0001step
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H->N_1BrCClFIOPSSi->C",
    kinetics = SurfaceArrheniusBM(A=(9.95505e+09,'m^2/(mol*s)'), n=2.1511, w0=(409330,'J/mol'), E0=(108328,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11232555165988092, var=9.579177635340328, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-1R!H->N_1BrCClFIOPSSi->C',), comment="""BM rule fitted to 23 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C
    Total Standard Deviation in ln(k): 6.486929502017495"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 6.486929502017495""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 6.486929502017495
""",
)

entry(
    index = 8,
    label = "Root_N-1R!H->N_N-1BrCClFIOPSSi->C",
    kinetics = SurfaceArrheniusBM(A=(1.56054e+27,'m^2/(mol*s)'), n=-3.13697, w0=(472408,'J/mol'), E0=(95884,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.17482269400462352, var=8.199156182539951, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R!H->N_N-1BrCClFIOPSSi->C',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R!H->N_N-1BrCClFIOPSSi->C
    Total Standard Deviation in ln(k): 6.1796452444021766"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R!H->N_N-1BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 6.1796452444021766""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R!H->N_N-1BrCClFIOPSSi->C
Total Standard Deviation in ln(k): 6.1796452444021766
""",
)

entry(
    index = 9,
    label = "Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R",
    kinetics = SurfaceArrheniusBM(A=(1.01406e+10,'m^2/(mol*s)'), n=2.14874, w0=(408794,'J/mol'), E0=(108363,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11236294914436086, var=9.56302917988487, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 6.481791353715072"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.481791353715072""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.481791353715072
""",
)

entry(
    index = 10,
    label = "Root_N-1R!H->N_N-1BrCClFIOPSSi->C_Ext-1O-R",
    kinetics = SurfaceArrheniusBM(A=(4.73304e+25,'m^2/(mol*s)'), n=-2.03627, w0=(470648,'J/mol'), E0=(159390,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02818984684847274, var=285.2305089925673, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->N_N-1BrCClFIOPSSi->C_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H->N_N-1BrCClFIOPSSi->C_Ext-1O-R
    Total Standard Deviation in ln(k): 33.928335834727086"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H->N_N-1BrCClFIOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 33.928335834727086""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H->N_N-1BrCClFIOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 33.928335834727086
""",
)

entry(
    index = 11,
    label = "Root_N-1R!H->N_N-1BrCClFIOPSSi->C_facet211",
    kinetics = SurfaceArrheniusBM(A=(1.2051e+16,'m^2/(mol*s)'), n=0, w0=(507137,'J/mol'), E0=(56737.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->N_N-1BrCClFIOPSSi->C_facet211',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->N_N-1BrCClFIOPSSi->C_facet211
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->N_N-1BrCClFIOPSSi->C_facet211
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->N_N-1BrCClFIOPSSi->C_facet211
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-1R!H->N_N-1BrCClFIOPSSi->C_facet111",
    kinetics = SurfaceArrheniusBM(A=(1.34376e+29,'m^2/(mol*s)'), n=-3.70783, w0=(468727,'J/mol'), E0=(101235,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.21606797370681774, var=9.357520795111974, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R!H->N_N-1BrCClFIOPSSi->C_facet111',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R!H->N_N-1BrCClFIOPSSi->C_facet111
    Total Standard Deviation in ln(k): 6.675381997771756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R!H->N_N-1BrCClFIOPSSi->C_facet111
Total Standard Deviation in ln(k): 6.675381997771756""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R!H->N_N-1BrCClFIOPSSi->C_facet111
Total Standard Deviation in ln(k): 6.675381997771756
""",
)

entry(
    index = 13,
    label = "Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O",
    kinetics = SurfaceArrheniusBM(A=(6.53337e+19,'m^2/(mol*s)'), n=-0.699672, w0=(392344,'J/mol'), E0=(150057,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.631647194435182, var=28.756905625929836, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O
    Total Standard Deviation in ln(k): 12.337538448661025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 12.337538448661025""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 12.337538448661025
""",
)

entry(
    index = 14,
    label = "Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_N-5R!H->O",
    kinetics = SurfaceArrheniusBM(A=(1.74932e+16,'m^2/(mol*s)'), n=0.282275, w0=(422503,'J/mol'), E0=(110702,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01081884463478998, var=3.5509078733565715, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_N-5R!H->O',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 3.804876291476394"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_N-5R!H->O
Total Standard Deviation in ln(k): 3.804876291476394""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_N-5R!H->O
Total Standard Deviation in ln(k): 3.804876291476394
""",
)

entry(
    index = 15,
    label = "Root_N-1R!H->N_N-1BrCClFIOPSSi->C_Ext-1O-R_Ext-5R!H-R",
    kinetics = SurfaceArrheniusBM(A=(5.65505e+11,'m^2/(mol*s)'), n=2.56481, w0=(470648,'J/mol'), E0=(107770,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->N_N-1BrCClFIOPSSi->C_Ext-1O-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->N_N-1BrCClFIOPSSi->C_Ext-1O-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->N_N-1BrCClFIOPSSi->C_Ext-1O-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->N_N-1BrCClFIOPSSi->C_Ext-1O-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H",
    kinetics = SurfaceArrheniusBM(A=(6.03748e+19,'m^2/(mol*s)'), n=-0.689662, w0=(396098,'J/mol'), E0=(150010,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6307956882797259, var=28.773726713379645, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H
    Total Standard Deviation in ln(k): 12.338542725018938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H
Total Standard Deviation in ln(k): 12.338542725018938""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H
Total Standard Deviation in ln(k): 12.338542725018938
""",
)

entry(
    index = 17,
    label = "Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_N-2R->H",
    kinetics = SurfaceArrheniusBM(A=(1.781e+17,'m^2/(mol*s)'), n=0, w0=(358555,'J/mol'), E0=(101107,'J/mol'), Tmin=(298,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_N-2R->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_N-2R->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_N-2R->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_N-2R->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_N-5R!H->O_Ext-1C-R",
    kinetics = SurfaceArrheniusBM(A=(6.0298e+15,'m^2/(mol*s)'), n=0.477857, w0=(422503,'J/mol'), E0=(110391,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.015752584906008893, var=4.755471164086196, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_N-5R!H->O_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_N-5R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 4.411313725944223"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_N-5R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 4.411313725944223""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_N-5R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 4.411313725944223
""",
)

entry(
    index = 19,
    label = "Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_Ext-1C-R",
    kinetics = SurfaceArrheniusBM(A=(7.35336e+19,'m^2/(mol*s)'), n=-0.714107, w0=(399529,'J/mol'), E0=(150343,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.38113402029795895, var=24.320045408424175, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_Ext-1C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_Ext-1C-R
    Total Standard Deviation in ln(k): 10.844045982812311"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_Ext-1C-R
Total Standard Deviation in ln(k): 10.844045982812311""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_Ext-1C-R
Total Standard Deviation in ln(k): 10.844045982812311
""",
)

entry(
    index = 20,
    label = "Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_Sp-5O-1C",
    kinetics = SurfaceArrheniusBM(A=(2.75289e+09,'m^2/(mol*s)'), n=1.91983, w0=(384090,'J/mol'), E0=(38504.4,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_Sp-5O-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_Sp-5O-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_Sp-5O-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_Sp-5O-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_N-Sp-5O-1C",
    kinetics = SurfaceArrheniusBM(A=(5.34079e+08,'m^2/(mol*s)'), n=1.79538, w0=(384090,'J/mol'), E0=(23445.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_N-Sp-5O-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_N-Sp-5O-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_N-Sp-5O-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_N-Sp-5O-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_Ext-1C-R_Sp-5O=1C",
    kinetics = SurfaceArrheniusBM(A=(7.30126e+12,'m^2/(mol*s)'), n=2.04438, w0=(384090,'J/mol'), E0=(96857.7,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_Ext-1C-R_Sp-5O=1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_Ext-1C-R_Sp-5O=1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_Ext-1C-R_Sp-5O=1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_Ext-1C-R_Sp-5O=1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_Ext-1C-R_N-Sp-5O=1C",
    kinetics = SurfaceArrheniusBM(A=(6.419e+19,'m^2/(mol*s)'), n=-0.69741, w0=(402102,'J/mol'), E0=(150242,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5470045234534795, var=27.156236446747684, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_Ext-1C-R_N-Sp-5O=1C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_Ext-1C-R_N-Sp-5O=1C
    Total Standard Deviation in ln(k): 11.821387684460785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_Ext-1C-R_N-Sp-5O=1C
Total Standard Deviation in ln(k): 11.821387684460785""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H->N_1BrCClFIOPSSi->C_Ext-1C-R_5R!H->O_2R->H_Ext-1C-R_N-Sp-5O=1C
Total Standard Deviation in ln(k): 11.821387684460785
""",
)

