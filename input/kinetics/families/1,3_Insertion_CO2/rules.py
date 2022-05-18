#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_CO2/rules"
shortDesc = ""
longDesc = """
572 - 575 Some of the tortional motions in the alkyl part of the 
transition states are treated as free rotations as they are relatively loose TSs. 

The dictionary defines CO2 in two ways, allowing the R-R' to insert either way
around. However, there are only rates for one of these ways. The other is
presumably matching the top level node.
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.59515e-07,'m^3/(mol*s)'), n=3.81416, w0=(803500,'J/mol'), E0=(295238,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1623246572352582, var=27.089230696923906, Tref=1000.0, N=8, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 8 training reactions at node Root
    Total Standard Deviation in ln(k): 10.841958840749095"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root
Total Standard Deviation in ln(k): 10.841958840749095""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root
Total Standard Deviation in ln(k): 10.841958840749095
""",
)

entry(
    index = 2,
    label = "Root_5CbCdCsHN->Cs",
    kinetics = ArrheniusBM(A=(4.03893e-10,'m^3/(mol*s)'), n=4.09744, w0=(725000,'J/mol'), E0=(303009,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-12.41552760724517, var=320.71014689362426, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5CbCdCsHN->Cs',), comment="""BM rule fitted to 2 training reactions at node Root_5CbCdCsHN->Cs
    Total Standard Deviation in ln(k): 67.09635461577197"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5CbCdCsHN->Cs
Total Standard Deviation in ln(k): 67.09635461577197""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5CbCdCsHN->Cs
Total Standard Deviation in ln(k): 67.09635461577197
""",
)

entry(
    index = 3,
    label = "Root_N-5CbCdCsHN->Cs",
    kinetics = ArrheniusBM(A=(1.32592e-07,'m^3/(mol*s)'), n=4.05114, w0=(829667,'J/mol'), E0=(290192,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0852817481199456, var=16.704684453181038, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-5CbCdCsHN->Cs',), comment="""BM rule fitted to 6 training reactions at node Root_N-5CbCdCsHN->Cs
    Total Standard Deviation in ln(k): 8.407901579083527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-5CbCdCsHN->Cs
Total Standard Deviation in ln(k): 8.407901579083527""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-5CbCdCsHN->Cs
Total Standard Deviation in ln(k): 8.407901579083527
""",
)

entry(
    index = 4,
    label = "Root_5CbCdCsHN->Cs_4CbCdCsHN->Cs",
    kinetics = ArrheniusBM(A=(7.3e-05,'m^3/(mol*s)'), n=3.13, w0=(745500,'J/mol'), E0=(452454,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5CbCdCsHN->Cs_4CbCdCsHN->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_5CbCdCsHN->Cs_4CbCdCsHN->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5CbCdCsHN->Cs_4CbCdCsHN->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5CbCdCsHN->Cs_4CbCdCsHN->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_5CbCdCsHN->Cs_N-4CbCdCsHN->Cs",
    kinetics = ArrheniusBM(A=(3.99078e-08,'m^3/(mol*s)'), n=3.39053, w0=(704500,'J/mol'), E0=(299332,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5CbCdCsHN->Cs_N-4CbCdCsHN->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_5CbCdCsHN->Cs_N-4CbCdCsHN->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5CbCdCsHN->Cs_N-4CbCdCsHN->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5CbCdCsHN->Cs_N-4CbCdCsHN->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H",
    kinetics = ArrheniusBM(A=(2.09592e-09,'m^3/(mol*s)'), n=4.52829, w0=(830833,'J/mol'), E0=(281703,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.26419894212477385, var=45.86391189281504, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H',), comment="""BM rule fitted to 3 training reactions at node Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H
    Total Standard Deviation in ln(k): 14.24046376199527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H
Total Standard Deviation in ln(k): 14.24046376199527""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H
Total Standard Deviation in ln(k): 14.24046376199527
""",
)

entry(
    index = 7,
    label = "Root_N-5CbCdCsHN->Cs_N-4CbCdCsHN->H",
    kinetics = ArrheniusBM(A=(0.000632778,'m^3/(mol*s)'), n=3.08238, w0=(828500,'J/mol'), E0=(308073,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.009489328295250576, var=1.1130688182633763, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5CbCdCsHN->Cs_N-4CbCdCsHN->H',), comment="""BM rule fitted to 3 training reactions at node Root_N-5CbCdCsHN->Cs_N-4CbCdCsHN->H
    Total Standard Deviation in ln(k): 2.1388796718782688"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5CbCdCsHN->Cs_N-4CbCdCsHN->H
Total Standard Deviation in ln(k): 2.1388796718782688""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5CbCdCsHN->Cs_N-4CbCdCsHN->H
Total Standard Deviation in ln(k): 2.1388796718782688
""",
)

entry(
    index = 8,
    label = "Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H_5CbCdHN->Cd",
    kinetics = ArrheniusBM(A=(9.9052e-11,'m^3/(mol*s)'), n=4.86959, w0=(810500,'J/mol'), E0=(279564,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0004649474097141082, var=84.16755128353569, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H_5CbCdHN->Cd',), comment="""BM rule fitted to 2 training reactions at node Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H_5CbCdHN->Cd
    Total Standard Deviation in ln(k): 18.39318418740552"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H_5CbCdHN->Cd
Total Standard Deviation in ln(k): 18.39318418740552""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H_5CbCdHN->Cd
Total Standard Deviation in ln(k): 18.39318418740552
""",
)

entry(
    index = 9,
    label = "Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H_N-5CbCdHN->Cd",
    kinetics = ArrheniusBM(A=(1510,'m^3/(mol*s)'), n=1.23, w0=(871500,'J/mol'), E0=(302238,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H_N-5CbCdHN->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H_N-5CbCdHN->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H_N-5CbCdHN->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H_N-5CbCdHN->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_N-5CbCdCsHN->Cs_N-4CbCdCsHN->H_Ext-4CsN-R",
    kinetics = ArrheniusBM(A=(0.00204667,'m^3/(mol*s)'), n=2.86279, w0=(828500,'J/mol'), E0=(307252,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.3453611489250746e-05, var=2.530939774000289, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5CbCdCsHN->Cs_N-4CbCdCsHN->H_Ext-4CsN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-5CbCdCsHN->Cs_N-4CbCdCsHN->H_Ext-4CsN-R
    Total Standard Deviation in ln(k): 3.189452826014204"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5CbCdCsHN->Cs_N-4CbCdCsHN->H_Ext-4CsN-R
Total Standard Deviation in ln(k): 3.189452826014204""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5CbCdCsHN->Cs_N-4CbCdCsHN->H_Ext-4CsN-R
Total Standard Deviation in ln(k): 3.189452826014204
""",
)

entry(
    index = 11,
    label = "Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H_5CbCdHN->Cd_Ext-5Cd-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.15601e-09,'m^3/(mol*s)'), n=4.43694, w0=(810500,'J/mol'), E0=(247946,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H_5CbCdHN->Cd_Ext-5Cd-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H_5CbCdHN->Cd_Ext-5Cd-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H_5CbCdHN->Cd_Ext-5Cd-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5CbCdCsHN->Cs_4CbCdCsHN->H_5CbCdHN->Cd_Ext-5Cd-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-5CbCdCsHN->Cs_N-4CbCdCsHN->H_Ext-4CsN-R_Ext-4CsN-R",
    kinetics = ArrheniusBM(A=(0.106,'m^3/(mol*s)'), n=2.13, w0=(828500,'J/mol'), E0=(302587,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5CbCdCsHN->Cs_N-4CbCdCsHN->H_Ext-4CsN-R_Ext-4CsN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-5CbCdCsHN->Cs_N-4CbCdCsHN->H_Ext-4CsN-R_Ext-4CsN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5CbCdCsHN->Cs_N-4CbCdCsHN->H_Ext-4CsN-R_Ext-4CsN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5CbCdCsHN->Cs_N-4CbCdCsHN->H_Ext-4CsN-R_Ext-4CsN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

