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
    kinetics = ArrheniusBM(A=(3.89319e+06,'m^3/(mol*s)'), n=0.30384, w0=(176880,'J/mol'), E0=(8236.22,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.027520853528482176, var=5.061994643747491, Tref=1000.0, N=271, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 271 training reactions at node Root
    Total Standard Deviation in ln(k): 4.579576657170572"""),
    rank = 11,
    shortDesc = """BM rule fitted to 271 training reactions at node Root
Total Standard Deviation in ln(k): 4.579576657170572""",
    longDesc = 
"""
BM rule fitted to 271 training reactions at node Root
Total Standard Deviation in ln(k): 4.579576657170572
""",
)

entry(
    index = 2,
    label = "Root_1R->H",
    kinetics = ArrheniusBM(A=(9.70327e+06,'m^3/(mol*s)'), n=0.349364, w0=(206149,'J/mol'), E0=(20614.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03289962861125776, var=3.9659335711689367, Tref=1000.0, N=87, data_mean=0.0, correlation='Root_1R->H',), comment="""BM rule fitted to 87 training reactions at node Root_1R->H
    Total Standard Deviation in ln(k): 4.075022489235355"""),
    rank = 11,
    shortDesc = """BM rule fitted to 87 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 4.075022489235355""",
    longDesc = 
"""
BM rule fitted to 87 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 4.075022489235355
""",
)

entry(
    index = 3,
    label = "Root_N-1R->H",
    kinetics = ArrheniusBM(A=(2.52018e+06,'m^3/(mol*s)'), n=0.289112, w0=(163041,'J/mol'), E0=(556.855,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04372322248524533, var=4.804893539068511, Tref=1000.0, N=184, data_mean=0.0, correlation='Root_N-1R->H',), comment="""BM rule fitted to 184 training reactions at node Root_N-1R->H
    Total Standard Deviation in ln(k): 4.504250140311958"""),
    rank = 11,
    shortDesc = """BM rule fitted to 184 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 4.504250140311958""",
    longDesc = 
"""
BM rule fitted to 184 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 4.504250140311958
""",
)

entry(
    index = 4,
    label = "Root_1R->H_2R->S",
    kinetics = ArrheniusBM(A=(9.71437e+06,'m^3/(mol*s)'), n=0.570447, w0=(181500,'J/mol'), E0=(18150,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.297428653350114, var=16.999244251708323, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_2R->S',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_2R->S
    Total Standard Deviation in ln(k): 14.037984545977633"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_2R->S
Total Standard Deviation in ln(k): 14.037984545977633""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_2R->S
Total Standard Deviation in ln(k): 14.037984545977633
""",
)

entry(
    index = 5,
    label = "Root_1R->H_N-2R->S",
    kinetics = ArrheniusBM(A=(9.69971e+06,'m^3/(mol*s)'), n=0.278181, w0=(207030,'J/mol'), E0=(20703,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005527548660432436, var=3.446935345201928, Tref=1000.0, N=84, data_mean=0.0, correlation='Root_1R->H_N-2R->S',), comment="""BM rule fitted to 84 training reactions at node Root_1R->H_N-2R->S
    Total Standard Deviation in ln(k): 3.735864224870612"""),
    rank = 11,
    shortDesc = """BM rule fitted to 84 training reactions at node Root_1R->H_N-2R->S
Total Standard Deviation in ln(k): 3.735864224870612""",
    longDesc = 
"""
BM rule fitted to 84 training reactions at node Root_1R->H_N-2R->S
Total Standard Deviation in ln(k): 3.735864224870612
""",
)

entry(
    index = 6,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(1.13747e+11,'m^3/(mol*s)'), n=-1.13197, w0=(108577,'J/mol'), E0=(66470.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2279573730560091, var=7.4217446498918465, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N
    Total Standard Deviation in ln(k): 6.034232765091002"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N
Total Standard Deviation in ln(k): 6.034232765091002""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N
Total Standard Deviation in ln(k): 6.034232765091002
""",
)

entry(
    index = 7,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(346714,'m^3/(mol*s)'), n=0.554734, w0=(167181,'J/mol'), E0=(-944.984,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08364014858477295, var=4.95083431976501, Tref=1000.0, N=171, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N',), comment="""BM rule fitted to 171 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N
    Total Standard Deviation in ln(k): 4.670780972330772"""),
    rank = 11,
    shortDesc = """BM rule fitted to 171 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N
Total Standard Deviation in ln(k): 4.670780972330772""",
    longDesc = 
"""
BM rule fitted to 171 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N
Total Standard Deviation in ln(k): 4.670780972330772
""",
)

entry(
    index = 8,
    label = "Root_1R->H_2R->S_Ext-2S-R",
    kinetics = ArrheniusBM(A=(6.94752e+06,'m^3/(mol*s)'), n=1.02083, w0=(181500,'J/mol'), E0=(18150,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_2R->S_Ext-2S-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_2R->S_Ext-2S-R
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
    index = 9,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing",
    kinetics = ArrheniusBM(A=(1.97574e+07,'m^3/(mol*s)'), n=0.201466, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08214281580881276, var=5.587460475686786, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing',), comment="""BM rule fitted to 14 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing
    Total Standard Deviation in ln(k): 4.945143610938387"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing
Total Standard Deviation in ln(k): 4.945143610938387""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing
Total Standard Deviation in ln(k): 4.945143610938387
""",
)

entry(
    index = 10,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing",
    kinetics = ArrheniusBM(A=(6.17641e+06,'m^3/(mol*s)'), n=0.326852, w0=(207336,'J/mol'), E0=(20733.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.023124123861458658, var=2.7675581495161676, Tref=1000.0, N=70, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing',), comment="""BM rule fitted to 70 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing
    Total Standard Deviation in ln(k): 3.393173984957397"""),
    rank = 11,
    shortDesc = """BM rule fitted to 70 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing
Total Standard Deviation in ln(k): 3.393173984957397""",
    longDesc = 
"""
BM rule fitted to 70 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing
Total Standard Deviation in ln(k): 3.393173984957397
""",
)

entry(
    index = 11,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R",
    kinetics = ArrheniusBM(A=(4.44019e+07,'m^3/(mol*s)'), n=0.099952, w0=(102750,'J/mol'), E0=(62857.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.44712125795983465, var=42.880470218871515, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R
    Total Standard Deviation in ln(k): 14.251063282008296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R
Total Standard Deviation in ln(k): 14.251063282008296""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R
Total Standard Deviation in ln(k): 14.251063282008296
""",
)

entry(
    index = 12,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R",
    kinetics = ArrheniusBM(A=(1.02626e+07,'m^3/(mol*s)'), n=0.0868089, w0=(126500,'J/mol'), E0=(12650,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05623872139052022, var=2.373836264200777, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R
    Total Standard Deviation in ln(k): 3.2300505538616187"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R
Total Standard Deviation in ln(k): 3.2300505538616187""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R
Total Standard Deviation in ln(k): 3.2300505538616187
""",
)

entry(
    index = 13,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl",
    kinetics = ArrheniusBM(A=(3.77965e+12,'m^3/(mol*s)'), n=-1.89404, w0=(162442,'J/mol'), E0=(16244.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04585810079750562, var=15.280811642889606, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl',), comment="""BM rule fitted to 26 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl
    Total Standard Deviation in ln(k): 7.9518668455435275"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl
Total Standard Deviation in ln(k): 7.9518668455435275""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl
Total Standard Deviation in ln(k): 7.9518668455435275
""",
)

entry(
    index = 14,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl",
    kinetics = ArrheniusBM(A=(326696,'m^3/(mol*s)'), n=0.563721, w0=(168031,'J/mol'), E0=(-751.077,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08723059354127995, var=4.969814487486747, Tref=1000.0, N=145, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl',), comment="""BM rule fitted to 145 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl
    Total Standard Deviation in ln(k): 4.688344439255668"""),
    rank = 11,
    shortDesc = """BM rule fitted to 145 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl
Total Standard Deviation in ln(k): 4.688344439255668""",
    longDesc = 
"""
BM rule fitted to 145 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl
Total Standard Deviation in ln(k): 4.688344439255668
""",
)

entry(
    index = 15,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(1.05361e+07,'m^3/(mol*s)'), n=0.231347, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7524292976797862, var=21.37814119662213, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H
    Total Standard Deviation in ln(k): 11.159719620454235"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 11.159719620454235""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 11.159719620454235
""",
)

entry(
    index = 16,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(3.06565e+07,'m^3/(mol*s)'), n=0.180587, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.021385446216783472, var=0.25147658313897314, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
    Total Standard Deviation in ln(k): 1.0590556155782338"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 1.0590556155782338""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 1.0590556155782338
""",
)

entry(
    index = 17,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O",
    kinetics = ArrheniusBM(A=(4.36942e+06,'m^3/(mol*s)'), n=0.260159, w0=(229500,'J/mol'), E0=(22950,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19827754566927608, var=10.563566902886153, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O
    Total Standard Deviation in ln(k): 7.013902836357316"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O
Total Standard Deviation in ln(k): 7.013902836357316""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O
Total Standard Deviation in ln(k): 7.013902836357316
""",
)

entry(
    index = 18,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O",
    kinetics = ArrheniusBM(A=(6.32169e+06,'m^3/(mol*s)'), n=0.331332, w0=(205631,'J/mol'), E0=(20563.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05274739189212409, var=2.757447652455107, Tref=1000.0, N=65, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O',), comment="""BM rule fitted to 65 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O
    Total Standard Deviation in ln(k): 3.4615068557478885"""),
    rank = 11,
    shortDesc = """BM rule fitted to 65 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O
Total Standard Deviation in ln(k): 3.4615068557478885""",
    longDesc = 
"""
BM rule fitted to 65 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O
Total Standard Deviation in ln(k): 3.4615068557478885
""",
)

entry(
    index = 19,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0",
    kinetics = ArrheniusBM(A=(1.41118e+27,'m^3/(mol*s)'), n=-6.1779, w0=(103500,'J/mol'), E0=(7060,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.241990514763132, var=45.75734468547163, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0
    Total Standard Deviation in ln(k): 16.681444307847325"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0
Total Standard Deviation in ln(k): 16.681444307847325""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0
Total Standard Deviation in ln(k): 16.681444307847325
""",
)

entry(
    index = 20,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0",
    kinetics = ArrheniusBM(A=(2.45793e+37,'m^3/(mol*s)'), n=-9.90145, w0=(100500,'J/mol'), E0=(75869.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.195003934534635, var=143.43167501029603, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0
    Total Standard Deviation in ln(k): 29.52438671530587"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0
Total Standard Deviation in ln(k): 29.52438671530587""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0
Total Standard Deviation in ln(k): 29.52438671530587
""",
)

entry(
    index = 21,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R",
    kinetics = ArrheniusBM(A=(1.61122e+07,'m^3/(mol*s)'), n=0.0486133, w0=(117833,'J/mol'), E0=(11783.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3590452419025245, var=6.1008567309137565, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R
    Total Standard Deviation in ln(k): 8.366364619253039"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R
Total Standard Deviation in ln(k): 8.366364619253039""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R
Total Standard Deviation in ln(k): 8.366364619253039
""",
)

entry(
    index = 22,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C",
    kinetics = ArrheniusBM(A=(4.7264e+12,'m^3/(mol*s)'), n=-1.88398, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04512858974000704, var=13.460340823243623, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C
    Total Standard Deviation in ln(k): 7.468428056631796"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C
Total Standard Deviation in ln(k): 7.468428056631796""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C
Total Standard Deviation in ln(k): 7.468428056631796
""",
)

entry(
    index = 23,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_N-2R->C",
    kinetics = ArrheniusBM(A=(3.24625e+12,'m^3/(mol*s)'), n=-2.82209, w0=(136000,'J/mol'), E0=(13600,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_N-2R->C
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
    index = 24,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O",
    kinetics = ArrheniusBM(A=(25691.7,'m^3/(mol*s)'), n=0.582409, w0=(161911,'J/mol'), E0=(-17770,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23312804888296784, var=3.7575899546532385, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O',), comment="""BM rule fitted to 28 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O
    Total Standard Deviation in ln(k): 4.471828379929168"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O
Total Standard Deviation in ln(k): 4.471828379929168""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O
Total Standard Deviation in ln(k): 4.471828379929168
""",
)

entry(
    index = 25,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O",
    kinetics = ArrheniusBM(A=(506530,'m^3/(mol*s)'), n=0.554816, w0=(169496,'J/mol'), E0=(16949.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02648174275194381, var=3.6079391996218293, Tref=1000.0, N=117, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O',), comment="""BM rule fitted to 117 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O
    Total Standard Deviation in ln(k): 3.874446334249786"""),
    rank = 11,
    shortDesc = """BM rule fitted to 117 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O
Total Standard Deviation in ln(k): 3.874446334249786""",
    longDesc = 
"""
BM rule fitted to 117 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O
Total Standard Deviation in ln(k): 3.874446334249786
""",
)

entry(
    index = 26,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(353416,'m^3/(mol*s)'), n=0.0261687, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0002677079444786214, var=37.506987303396876, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 12.278261325720894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 12.278261325720894""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 12.278261325720894
""",
)

entry(
    index = 27,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO",
    kinetics = ArrheniusBM(A=(6.34417e+06,'m^3/(mol*s)'), n=0.321249, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6451615619770243, var=7.387095572639518, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO
    Total Standard Deviation in ln(k): 7.069720888611477"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 7.069720888611477""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 7.069720888611477
""",
)

entry(
    index = 28,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-Sp-3R!H-2BrCClFHNO",
    kinetics = ArrheniusBM(A=(4.27e+07,'m^3/(mol*s)'), n=0.338, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-Sp-3R!H-2BrCClFHNO',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-Sp-3R!H-2BrCClFHNO
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
    index = 29,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.52929e+07,'m^3/(mol*s)'), n=0.185643, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02592286849721949, var=0.07894813951634323, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.6284175150992781"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.6284175150992781""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.6284175150992781
""",
)

entry(
    index = 30,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5.15096e+07,'m^3/(mol*s)'), n=0.183576, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1489920501984019, var=0.10041008290210698, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.0096033162086009"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.0096033162086009""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.0096033162086009
""",
)

entry(
    index = 31,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R",
    kinetics = ArrheniusBM(A=(2.55303e+06,'m^3/(mol*s)'), n=0.293392, w0=(229500,'J/mol'), E0=(22950,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-6.898784700718085, var=122.37018022197243, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R
    Total Standard Deviation in ln(k): 39.51022101988649"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R
Total Standard Deviation in ln(k): 39.51022101988649""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R
Total Standard Deviation in ln(k): 39.51022101988649
""",
)

entry(
    index = 32,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_2CHN->N",
    kinetics = ArrheniusBM(A=(2.8e+06,'m^3/(mol*s)'), n=0.493, w0=(193000,'J/mol'), E0=(19300,'J/mol'), Tmin=(200,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_2CHN->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_2CHN->N
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
    index = 33,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N",
    kinetics = ArrheniusBM(A=(6.19912e+06,'m^3/(mol*s)'), n=0.330247, w0=(205828,'J/mol'), E0=(20582.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04835763485928428, var=3.012056213379905, Tref=1000.0, N=64, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N',), comment="""BM rule fitted to 64 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N
    Total Standard Deviation in ln(k): 3.6007747467818887"""),
    rank = 11,
    shortDesc = """BM rule fitted to 64 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N
Total Standard Deviation in ln(k): 3.6007747467818887""",
    longDesc = 
"""
BM rule fitted to 64 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N
Total Standard Deviation in ln(k): 3.6007747467818887
""",
)

entry(
    index = 34,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_2R->C",
    kinetics = ArrheniusBM(A=(505,'m^3/(mol*s)'), n=0, w0=(152500,'J/mol'), E0=(15250,'J/mol'), Tmin=(2000,'K'), Tmax=(4000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_2R->C
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
    index = 35,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C",
    kinetics = ArrheniusBM(A=(1.59502e+10,'m^3/(mol*s)'), n=-0.916249, w0=(93700,'J/mol'), E0=(7892.71,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0859446315507169, var=5.442076615510027, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C
    Total Standard Deviation in ln(k): 7.4052019829714375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C
Total Standard Deviation in ln(k): 7.4052019829714375""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C
Total Standard Deviation in ln(k): 7.4052019829714375
""",
)

entry(
    index = 36,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R",
    kinetics = ArrheniusBM(A=(58500,'m^3/(mol*s)'), n=0, w0=(100500,'J/mol'), E0=(10050,'J/mol'), Tmin=(473,'K'), Tmax=(703,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R
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
    index = 37,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_2R->C",
    kinetics = ArrheniusBM(A=(1.75326e+12,'m^3/(mol*s)'), n=-1.41237, w0=(152500,'J/mol'), E0=(15250,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_2R->C
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
    index = 38,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C",
    kinetics = ArrheniusBM(A=(3.65367e+06,'m^3/(mol*s)'), n=0.2352, w0=(100500,'J/mol'), E0=(10050,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4709502203626317, var=0.4813240235668652, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C
    Total Standard Deviation in ln(k): 2.5741274836274104"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C
Total Standard Deviation in ln(k): 2.5741274836274104""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C
Total Standard Deviation in ln(k): 2.5741274836274104
""",
)

entry(
    index = 39,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.20711e+12,'m^3/(mol*s)'), n=-1.82343, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03326924556394403, var=14.088165865967738, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R',), comment="""BM rule fitted to 24 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 7.608204916950396"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 7.608204916950396""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 7.608204916950396
""",
)

entry(
    index = 40,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R",
    kinetics = ArrheniusBM(A=(25126.5,'m^3/(mol*s)'), n=0.584161, w0=(164180,'J/mol'), E0=(-17855.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2603862582677316, var=3.8363952457056487, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R
    Total Standard Deviation in ln(k): 4.5808549054772465"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R
Total Standard Deviation in ln(k): 4.5808549054772465""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R
Total Standard Deviation in ln(k): 4.5808549054772465
""",
)

entry(
    index = 41,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C",
    kinetics = ArrheniusBM(A=(6.81408e+07,'m^3/(mol*s)'), n=-1.05806e-06, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.305460834090209e-17, var=0.1195344065457376, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C
    Total Standard Deviation in ln(k): 0.6931120579847638"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C
Total Standard Deviation in ln(k): 0.6931120579847638""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C
Total Standard Deviation in ln(k): 0.6931120579847638
""",
)

entry(
    index = 42,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_N-2R->C",
    kinetics = ArrheniusBM(A=(1.57e+07,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(200,'K'), Tmax=(400,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_N-2R->C
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
    index = 43,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing",
    kinetics = ArrheniusBM(A=(1.26173e+09,'m^3/(mol*s)'), n=-0.614843, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.010144846432645734, var=0.2598237760344, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing
    Total Standard Deviation in ln(k): 1.0473614112425502"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing
Total Standard Deviation in ln(k): 1.0473614112425502""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing
Total Standard Deviation in ln(k): 1.0473614112425502
""",
)

entry(
    index = 44,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing",
    kinetics = ArrheniusBM(A=(268174,'m^3/(mol*s)'), n=0.649932, w0=(169168,'J/mol'), E0=(16916.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02863081421054907, var=4.030334530286578, Tref=1000.0, N=107, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing',), comment="""BM rule fitted to 107 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing
    Total Standard Deviation in ln(k): 4.0965813330982135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 107 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing
Total Standard Deviation in ln(k): 4.0965813330982135""",
    longDesc = 
"""
BM rule fitted to 107 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing
Total Standard Deviation in ln(k): 4.0965813330982135
""",
)

entry(
    index = 45,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1785.64,'m^3/(mol*s)'), n=0.0220967, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Ext-3R!H-R
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
    index = 46,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(2.63315e+06,'m^3/(mol*s)'), n=0.0938491, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
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
    index = 47,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(8.77012e+06,'m^3/(mol*s)'), n=-0.0289636, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
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
    index = 48,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_4R!H-inRing",
    kinetics = ArrheniusBM(A=(3.70386e+06,'m^3/(mol*s)'), n=0.19941, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1097017345178382, var=0.8159359144189625, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_4R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_4R!H-inRing
    Total Standard Deviation in ln(k): 2.086493076125835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_4R!H-inRing
Total Standard Deviation in ln(k): 2.086493076125835""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_4R!H-inRing
Total Standard Deviation in ln(k): 2.086493076125835
""",
)

entry(
    index = 49,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(9.42e+06,'m^3/(mol*s)'), n=0.408, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_N-4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_N-4R!H-inRing
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
    index = 50,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Sp-3R!H-2BrCClFHNO",
    kinetics = ArrheniusBM(A=(2.80593e+07,'m^3/(mol*s)'), n=0.136701, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.47660747185827573, var=1.386468955460086, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Sp-3R!H-2BrCClFHNO',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Sp-3R!H-2BrCClFHNO
    Total Standard Deviation in ln(k): 3.5580500164857103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 3.5580500164857103""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 3.5580500164857103
""",
)

entry(
    index = 51,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_N-Sp-3R!H-2BrCClFHNO",
    kinetics = ArrheniusBM(A=(2.45117e+07,'m^3/(mol*s)'), n=0.200434, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.035225327597470955, var=0.01056069269555372, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_N-Sp-3R!H-2BrCClFHNO',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_N-Sp-3R!H-2BrCClFHNO
    Total Standard Deviation in ln(k): 0.2945229114894713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_N-Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 0.2945229114894713""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_N-Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 0.2945229114894713
""",
)

entry(
    index = 52,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2BrCClFHNO",
    kinetics = ArrheniusBM(A=(3.62e+07,'m^3/(mol*s)'), n=0.228, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2BrCClFHNO',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2BrCClFHNO
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
    index = 53,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2BrCClFHNO",
    kinetics = ArrheniusBM(A=(2.2e+08,'m^3/(mol*s)'), n=0, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1200,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2BrCClFHNO',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2BrCClFHNO
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
    index = 54,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_3R!H->Cl",
    kinetics = ArrheniusBM(A=(2.49746e+10,'m^3/(mol*s)'), n=-2.63174, w0=(229500,'J/mol'), E0=(22950,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9878236278062851, var=1.2163224389639997e-05, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_3R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_3R!H->Cl
    Total Standard Deviation in ln(k): 2.4889605909597616"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_3R!H->Cl
Total Standard Deviation in ln(k): 2.4889605909597616""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_3R!H->Cl
Total Standard Deviation in ln(k): 2.4889605909597616
""",
)

entry(
    index = 55,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl",
    kinetics = ArrheniusBM(A=(2.07243e+06,'m^3/(mol*s)'), n=0.359788, w0=(229500,'J/mol'), E0=(22950,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.573841544937113, var=0.5984327916266005, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl
    Total Standard Deviation in ln(k): 2.992644667134224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl
Total Standard Deviation in ln(k): 2.992644667134224""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl
Total Standard Deviation in ln(k): 2.992644667134224
""",
)

entry(
    index = 56,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C",
    kinetics = ArrheniusBM(A=(6.23846e+06,'m^3/(mol*s)'), n=0.3302, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05223573700039762, var=2.971511532414158, Tref=1000.0, N=62, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C',), comment="""BM rule fitted to 62 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C
    Total Standard Deviation in ln(k): 3.5870224876502066"""),
    rank = 11,
    shortDesc = """BM rule fitted to 62 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C
Total Standard Deviation in ln(k): 3.5870224876502066""",
    longDesc = 
"""
BM rule fitted to 62 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C
Total Standard Deviation in ln(k): 3.5870224876502066
""",
)

entry(
    index = 57,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_N-2CH->C",
    kinetics = ArrheniusBM(A=(55567.3,'m^3/(mol*s)'), n=0.364988, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3774142242586176, var=47.94959741791935, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_N-2CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_N-2CH->C
    Total Standard Deviation in ln(k): 14.830194859219086"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_N-2CH->C
Total Standard Deviation in ln(k): 14.830194859219086""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_N-2CH->C
Total Standard Deviation in ln(k): 14.830194859219086
""",
)

entry(
    index = 58,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C",
    kinetics = ArrheniusBM(A=(1.81328e+10,'m^3/(mol*s)'), n=-0.926861, w0=(92000,'J/mol'), E0=(9200,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.252003776439555, var=0.000612219778486719, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C
    Total Standard Deviation in ln(k): 0.6827786287928762"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C
Total Standard Deviation in ln(k): 0.6827786287928762""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C
Total Standard Deviation in ln(k): 0.6827786287928762
""",
)

entry(
    index = 59,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C",
    kinetics = ArrheniusBM(A=(9.29149e+06,'m^3/(mol*s)'), n=-0.3, w0=(94833.3,'J/mol'), E0=(-2275.97,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03461470783786757, var=17.26014472327979, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C
    Total Standard Deviation in ln(k): 8.415709729420323"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C
Total Standard Deviation in ln(k): 8.415709729420323""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C
Total Standard Deviation in ln(k): 8.415709729420323
""",
)

entry(
    index = 60,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F",
    kinetics = ArrheniusBM(A=(1.45492e+14,'m^3/(mol*s)'), n=-1.95635, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2445884555307146, var=43.52115347577087, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F
    Total Standard Deviation in ln(k): 13.83989428103599"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F
Total Standard Deviation in ln(k): 13.83989428103599""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F
Total Standard Deviation in ln(k): 13.83989428103599
""",
)

entry(
    index = 61,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F",
    kinetics = ArrheniusBM(A=(1.17526e+12,'m^3/(mol*s)'), n=-1.78845, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10638969230944832, var=9.008754515245393, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F
    Total Standard Deviation in ln(k): 6.284440386534291"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F
Total Standard Deviation in ln(k): 6.284440386534291""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F
Total Standard Deviation in ln(k): 6.284440386534291
""",
)

entry(
    index = 62,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O",
    kinetics = ArrheniusBM(A=(7389.39,'m^3/(mol*s)'), n=0.755616, w0=(176553,'J/mol'), E0=(-18318.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3184856740191667, var=4.675075494823225, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O',), comment="""BM rule fitted to 19 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O
    Total Standard Deviation in ln(k): 5.134837987282462"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O
Total Standard Deviation in ln(k): 5.134837987282462""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O
Total Standard Deviation in ln(k): 5.134837987282462
""",
)

entry(
    index = 63,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O",
    kinetics = ArrheniusBM(A=(7.75903e+07,'m^3/(mol*s)'), n=-0.290943, w0=(125000,'J/mol'), E0=(12500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27156013880001, var=0.6119123121345926, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O
    Total Standard Deviation in ln(k): 2.250512396528818"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O
Total Standard Deviation in ln(k): 2.250512396528818""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O
Total Standard Deviation in ln(k): 2.250512396528818
""",
)

entry(
    index = 64,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.7e+07,'m^3/(mol*s)'), n=0, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(200,'K'), Tmax=(400,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C_Ext-2C-R
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
    index = 65,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS",
    kinetics = ArrheniusBM(A=(1.64652e+10,'m^3/(mol*s)'), n=-0.959714, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10212608903374547, var=0.31794223547158906, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS
    Total Standard Deviation in ln(k): 1.3869954866602756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS
Total Standard Deviation in ln(k): 1.3869954866602756""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS
Total Standard Deviation in ln(k): 1.3869954866602756
""",
)

entry(
    index = 66,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS",
    kinetics = ArrheniusBM(A=(4.28281e+08,'m^3/(mol*s)'), n=-0.469786, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11347341781219641, var=0.43400451988942185, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS
    Total Standard Deviation in ln(k): 1.6058089008076266"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS
Total Standard Deviation in ln(k): 1.6058089008076266""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS
Total Standard Deviation in ln(k): 1.6058089008076266
""",
)

entry(
    index = 67,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C",
    kinetics = ArrheniusBM(A=(165155,'m^3/(mol*s)'), n=0.640329, w0=(170238,'J/mol'), E0=(17023.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04475704518575621, var=1.3474245931457252, Tref=1000.0, N=105, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C',), comment="""BM rule fitted to 105 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C
    Total Standard Deviation in ln(k): 2.4395236921551873"""),
    rank = 11,
    shortDesc = """BM rule fitted to 105 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C
Total Standard Deviation in ln(k): 2.4395236921551873""",
    longDesc = 
"""
BM rule fitted to 105 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C
Total Standard Deviation in ln(k): 2.4395236921551873
""",
)

entry(
    index = 68,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_N-1BrCFS->C",
    kinetics = ArrheniusBM(A=(3.78184e+06,'m^3/(mol*s)'), n=0.702356, w0=(113000,'J/mol'), E0=(11300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.385942648067958, var=33.619040003930174, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_N-1BrCFS->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_N-1BrCFS->C
    Total Standard Deviation in ln(k): 20.131234124359324"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_N-1BrCFS->C
Total Standard Deviation in ln(k): 20.131234124359324""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_N-1BrCFS->C
Total Standard Deviation in ln(k): 20.131234124359324
""",
)

entry(
    index = 69,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_4R!H-inRing_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(249317,'m^3/(mol*s)'), n=0.611, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_4R!H-inRing_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Sp-3R!H-2BrCClFHNO_4R!H-inRing_Ext-3R!H-R
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
    index = 70,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Sp-3R!H-2BrCClFHNO_Ext-2BrCClFHNO-R",
    kinetics = ArrheniusBM(A=(6.44369e+06,'m^3/(mol*s)'), n=0.245, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Sp-3R!H-2BrCClFHNO_Ext-2BrCClFHNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Sp-3R!H-2BrCClFHNO_Ext-2BrCClFHNO-R
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
    index = 71,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_N-Sp-3R!H-2BrCClFHNO_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.25e+07,'m^3/(mol*s)'), n=0.284, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_N-Sp-3R!H-2BrCClFHNO_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_N-Sp-3R!H-2BrCClFHNO_Ext-4R!H-R
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
    index = 72,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl_3BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(700000,'m^3/(mol*s)'), n=0.493, w0=(229500,'J/mol'), E0=(22950,'J/mol'), Tmin=(200,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl_3BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl_3BrCFINOPSSi->C
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
    index = 73,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl_N-3BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(43950,'m^3/(mol*s)'), n=1, w0=(229500,'J/mol'), E0=(22950,'J/mol'), Tmin=(298,'K'), Tmax=(6000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl_N-3BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl_N-3BrCFINOPSSi->C
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
    index = 74,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(6.07099e+06,'m^3/(mol*s)'), n=0.332583, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04791227976020315, var=3.0149725677560166, Tref=1000.0, N=60, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R',), comment="""BM rule fitted to 60 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R
    Total Standard Deviation in ln(k): 3.6013397198393586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 60 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R
Total Standard Deviation in ln(k): 3.6013397198393586""",
    longDesc = 
"""
BM rule fitted to 60 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R
Total Standard Deviation in ln(k): 3.6013397198393586
""",
)

entry(
    index = 75,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C_Ext-1N-R",
    kinetics = ArrheniusBM(A=(1.30329e+10,'m^3/(mol*s)'), n=-0.937308, w0=(100500,'J/mol'), E0=(10050,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C_Ext-1N-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->C_Ext-1N-R
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
    index = 76,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R",
    kinetics = ArrheniusBM(A=(4.36478e+09,'m^3/(mol*s)'), n=-1.4273, w0=(92000,'J/mol'), E0=(-10340.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=3.401841872999714, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R
    Total Standard Deviation in ln(k): 3.697549959467405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R
Total Standard Deviation in ln(k): 3.697549959467405""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R
Total Standard Deviation in ln(k): 3.697549959467405
""",
)

entry(
    index = 77,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.55598e+15,'m^3/(mol*s)'), n=-2.44544, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.30573553449130975, var=63.277478777611705, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R
    Total Standard Deviation in ln(k): 16.715274419810346"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 16.715274419810346""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 16.715274419810346
""",
)

entry(
    index = 78,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.13891e+12,'m^3/(mol*s)'), n=-1.66575, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08261610721337945, var=7.325998628073099, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 5.633710800974514"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 5.633710800974514""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 5.633710800974514
""",
)

entry(
    index = 79,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.32222e+12,'m^3/(mol*s)'), n=-2.2486, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19554062431509478, var=6.967896087778388, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 5.783161716712744"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 5.783161716712744""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 5.783161716712744
""",
)

entry(
    index = 80,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C",
    kinetics = ArrheniusBM(A=(57395.9,'m^3/(mol*s)'), n=0.438385, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0033991330825936267, var=2.7059432770952125, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C',), comment="""BM rule fitted to 18 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C
    Total Standard Deviation in ln(k): 3.306279940125072"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C
Total Standard Deviation in ln(k): 3.306279940125072""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C
Total Standard Deviation in ln(k): 3.306279940125072
""",
)

entry(
    index = 81,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_N-2R->C",
    kinetics = ArrheniusBM(A=(2.49151e+08,'m^3/(mol*s)'), n=0.0472428, w0=(132500,'J/mol'), E0=(27449.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_N-2R->C
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
    index = 82,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R",
    kinetics = ArrheniusBM(A=(4.62085e+06,'m^3/(mol*s)'), n=-2.20952e-08, w0=(143000,'J/mol'), E0=(14300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.1029743876190133e-09, var=1.5745902317994485, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R
    Total Standard Deviation in ln(k): 2.515595254417866"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R
Total Standard Deviation in ln(k): 2.515595254417866""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R
Total Standard Deviation in ln(k): 2.515595254417866
""",
)

entry(
    index = 83,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(1.55564e+07,'m^3/(mol*s)'), n=-1.42144e-07, w0=(125000,'J/mol'), E0=(12500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.5050664115508311, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 1.4247256172567304"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C
Total Standard Deviation in ln(k): 1.4247256172567304""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C
Total Standard Deviation in ln(k): 1.4247256172567304
""",
)

entry(
    index = 84,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_N-3BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(5.15e+07,'m^3/(mol*s)'), n=-0.24, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(200,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_N-3BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_N-3BrCClFINPSSi->C
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
    index = 85,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_2R-inRing",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_2R-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_2R-inRing
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
    index = 86,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_N-2R-inRing",
    kinetics = ArrheniusBM(A=(1.71905e+10,'m^3/(mol*s)'), n=-0.966851, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09712774283837174, var=0.3098801559086371, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_N-2R-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_N-2R-inRing
    Total Standard Deviation in ln(k): 1.3600130301505053"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_N-2R-inRing
Total Standard Deviation in ln(k): 1.3600130301505053""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_N-2R-inRing
Total Standard Deviation in ln(k): 1.3600130301505053
""",
)

entry(
    index = 87,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R",
    kinetics = ArrheniusBM(A=(5.20355e+08,'m^3/(mol*s)'), n=-0.509162, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.35721846065088814, var=0.8400902286142375, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R
    Total Standard Deviation in ln(k): 2.7350025467468573"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R
Total Standard Deviation in ln(k): 2.7350025467468573""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R
Total Standard Deviation in ln(k): 2.7350025467468573
""",
)

entry(
    index = 88,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S",
    kinetics = ArrheniusBM(A=(28641.6,'m^3/(mol*s)'), n=0.894523, w0=(136000,'J/mol'), E0=(13600,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.050171120393623474, var=1.0341867544346448, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S
    Total Standard Deviation in ln(k): 2.1647728881907358"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S
Total Standard Deviation in ln(k): 2.1647728881907358""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S
Total Standard Deviation in ln(k): 2.1647728881907358
""",
)

entry(
    index = 89,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S",
    kinetics = ArrheniusBM(A=(6.13423e+08,'m^3/(mol*s)'), n=-0.552269, w0=(171950,'J/mol'), E0=(17195,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.024334211463546394, var=3.3703619654870898, Tref=1000.0, N=100, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S',), comment="""BM rule fitted to 100 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S
    Total Standard Deviation in ln(k): 3.7415432682668106"""),
    rank = 11,
    shortDesc = """BM rule fitted to 100 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S
Total Standard Deviation in ln(k): 3.7415432682668106""",
    longDesc = 
"""
BM rule fitted to 100 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S
Total Standard Deviation in ln(k): 3.7415432682668106
""",
)

entry(
    index = 90,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_N-1BrCFS->C_Ext-1BrFS-R",
    kinetics = ArrheniusBM(A=(106000,'m^3/(mol*s)'), n=1.21, w0=(113000,'J/mol'), E0=(11300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_N-1BrCFS->C_Ext-1BrFS-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_N-1BrCFS->C_Ext-1BrFS-R
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

entry(
    index = 91,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F",
    kinetics = ArrheniusBM(A=(2.23995e+19,'m^3/(mol*s)'), n=-4.71736, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.257513190549315, var=35.011554013247, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F',), comment="""BM rule fitted to 16 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F
    Total Standard Deviation in ln(k): 12.509148175474557"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F
Total Standard Deviation in ln(k): 12.509148175474557""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F
Total Standard Deviation in ln(k): 12.509148175474557
""",
)

entry(
    index = 92,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F",
    kinetics = ArrheniusBM(A=(4.41881e+06,'m^3/(mol*s)'), n=0.388019, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09464422275169895, var=2.1415112871761504, Tref=1000.0, N=44, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F',), comment="""BM rule fitted to 44 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F
    Total Standard Deviation in ln(k): 3.171509501150261"""),
    rank = 11,
    shortDesc = """BM rule fitted to 44 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F
Total Standard Deviation in ln(k): 3.171509501150261""",
    longDesc = 
"""
BM rule fitted to 44 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F
Total Standard Deviation in ln(k): 3.171509501150261
""",
)

entry(
    index = 93,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_2NO->O",
    kinetics = ArrheniusBM(A=(122000,'m^3/(mol*s)'), n=0.2, w0=(100500,'J/mol'), E0=(10050,'J/mol'), Tmin=(300,'K'), Tmax=(400,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_2NO->O
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
    index = 94,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_N-2NO->O",
    kinetics = ArrheniusBM(A=(2.63e+08,'m^3/(mol*s)'), n=-1.1, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(300,'K'), Tmax=(600,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_N-2NO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->C_Ext-1N-R_N-2NO->O
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
    index = 95,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(5363.42,'m^3/(mol*s)'), n=1.12404, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->Cl
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
    index = 96,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(1.20701e+07,'m^3/(mol*s)'), n=0.0453429, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.058886752814273205, var=9.360079713854214, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 6.281292749812114"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 6.281292749812114""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 6.281292749812114
""",
)

entry(
    index = 97,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C",
    kinetics = ArrheniusBM(A=(1.5304e+09,'m^3/(mol*s)'), n=-0.840119, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16939402075968962, var=8.985160681582101, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C
    Total Standard Deviation in ln(k): 6.434858153857042"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C
Total Standard Deviation in ln(k): 6.434858153857042""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C
Total Standard Deviation in ln(k): 6.434858153857042
""",
)

entry(
    index = 98,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C",
    kinetics = ArrheniusBM(A=(6.30746e+17,'m^3/(mol*s)'), n=-3.317, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0909397244197589, var=1.5234337631355757, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C
    Total Standard Deviation in ln(k): 2.702885335296229"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 2.702885335296229""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 2.702885335296229
""",
)

entry(
    index = 99,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3BrClO->O",
    kinetics = ArrheniusBM(A=(1.01646e+20,'m^3/(mol*s)'), n=-4.5175, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3BrClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3BrClO->O
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
    index = 100,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O",
    kinetics = ArrheniusBM(A=(8.17544e+14,'m^3/(mol*s)'), n=-3.04515, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11357895801889693, var=3.0907683435189086, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O
    Total Standard Deviation in ln(k): 3.8098150420651526"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O
Total Standard Deviation in ln(k): 3.8098150420651526""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O
Total Standard Deviation in ln(k): 3.8098150420651526
""",
)

entry(
    index = 101,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing",
    kinetics = ArrheniusBM(A=(1.90891e+06,'m^3/(mol*s)'), n=0.0381639, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03546199309361285, var=0.43816276119659187, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing
    Total Standard Deviation in ln(k): 1.4161120929301536"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing
Total Standard Deviation in ln(k): 1.4161120929301536""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing
Total Standard Deviation in ln(k): 1.4161120929301536
""",
)

entry(
    index = 102,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing",
    kinetics = ArrheniusBM(A=(22.4279,'m^3/(mol*s)'), n=1.33462, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15031622818067827, var=1.3032394374490985, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing
    Total Standard Deviation in ln(k): 2.6662747635943003"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing
Total Standard Deviation in ln(k): 2.6662747635943003""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing
Total Standard Deviation in ln(k): 2.6662747635943003
""",
)

entry(
    index = 103,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C",
    kinetics = ArrheniusBM(A=(7.38318e+06,'m^3/(mol*s)'), n=-1.1548e-07, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.3279077205677291, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C
    Total Standard Deviation in ln(k): 1.1479760049827752"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C
Total Standard Deviation in ln(k): 1.1479760049827752""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C
Total Standard Deviation in ln(k): 1.1479760049827752
""",
)

entry(
    index = 104,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_N-2R->C",
    kinetics = ArrheniusBM(A=(1.81e+06,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_N-2R->C
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
    index = 105,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C_2R->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C_2R->C
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
    index = 106,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C_N-2R->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C_N-2R->C
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
    index = 107,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_N-2R-inRing_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.668e+09,'m^3/(mol*s)'), n=-0.7, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_N-2R-inRing_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_Sp-3R!H-1BrCFS_N-2R-inRing_Ext-2R-R
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
    index = 108,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_2R-inRing",
    kinetics = ArrheniusBM(A=(1.6752e+09,'m^3/(mol*s)'), n=-0.659797, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0329788338602979, var=2.2202828217281576, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_2R-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_2R-inRing
    Total Standard Deviation in ln(k): 5.582602458105895"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_2R-inRing
Total Standard Deviation in ln(k): 5.582602458105895""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_2R-inRing
Total Standard Deviation in ln(k): 5.582602458105895
""",
)

entry(
    index = 109,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing",
    kinetics = ArrheniusBM(A=(9.99999e+06,'m^3/(mol*s)'), n=1.02685e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 110,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C",
    kinetics = ArrheniusBM(A=(15609.6,'m^3/(mol*s)'), n=0.89762, w0=(136000,'J/mol'), E0=(13600,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06086937252594513, var=0.0, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C
    Total Standard Deviation in ln(k): 0.15293812192448525"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C
Total Standard Deviation in ln(k): 0.15293812192448525""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C
Total Standard Deviation in ln(k): 0.15293812192448525
""",
)

entry(
    index = 111,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_N-3R!H->C",
    kinetics = ArrheniusBM(A=(71187.7,'m^3/(mol*s)'), n=0.889878, w0=(136000,'J/mol'), E0=(13600,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3723820346018363, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_N-3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_N-3R!H->C
    Total Standard Deviation in ln(k): 0.9356332527684328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_N-3R!H->C
Total Standard Deviation in ln(k): 0.9356332527684328""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_N-3R!H->C
Total Standard Deviation in ln(k): 0.9356332527684328
""",
)

entry(
    index = 112,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br",
    kinetics = ArrheniusBM(A=(72680,'m^3/(mol*s)'), n=0.611725, w0=(142500,'J/mol'), E0=(14250,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03616093258231267, var=10.361316207409716, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br
    Total Standard Deviation in ln(k): 6.543898042945132"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br
Total Standard Deviation in ln(k): 6.543898042945132""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br
Total Standard Deviation in ln(k): 6.543898042945132
""",
)

entry(
    index = 113,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br",
    kinetics = ArrheniusBM(A=(6.6945e+08,'m^3/(mol*s)'), n=-0.563521, w0=(174511,'J/mol'), E0=(17451.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.024824515165402728, var=3.3268899684153306, Tref=1000.0, N=92, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br',), comment="""BM rule fitted to 92 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br
    Total Standard Deviation in ln(k): 3.7189626564358416"""),
    rank = 11,
    shortDesc = """BM rule fitted to 92 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br
Total Standard Deviation in ln(k): 3.7189626564358416""",
    longDesc = 
"""
BM rule fitted to 92 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br
Total Standard Deviation in ln(k): 3.7189626564358416
""",
)

entry(
    index = 114,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R",
    kinetics = ArrheniusBM(A=(9.99888e+19,'m^3/(mol*s)'), n=-4.91877, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2640439695114029, var=37.60956406999751, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R',), comment="""BM rule fitted to 15 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R
    Total Standard Deviation in ln(k): 12.957793098401323"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 12.957793098401323""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 12.957793098401323
""",
)

entry(
    index = 115,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(9.25218e+06,'m^3/(mol*s)'), n=0.315312, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.041783203653284015, var=3.179156366776864, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C',), comment="""BM rule fitted to 38 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 3.679463438822317"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 3.679463438822317""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 3.679463438822317
""",
)

entry(
    index = 116,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(2.3625e+06,'m^3/(mol*s)'), n=0.449623, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-5.36495209471228, var=57.817184372985146, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 28.723305928413293"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 28.723305928413293""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C
Total Standard Deviation in ln(k): 28.723305928413293
""",
)

entry(
    index = 117,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_4BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(2471.06,'m^3/(mol*s)'), n=0.904611, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_4BrCFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_4BrCFINOPSSi->O
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
    index = 118,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(3.46635e+07,'m^3/(mol*s)'), n=0.01289, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.553220035741629, var=23.930171509944543, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 11.196858273429726"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 11.196858273429726""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 11.196858273429726
""",
)

entry(
    index = 119,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.46812e+08,'m^3/(mol*s)'), n=-0.724217, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20342395975073702, var=11.793107737006444, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R
    Total Standard Deviation in ln(k): 7.395595157332486"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R
Total Standard Deviation in ln(k): 7.395595157332486""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R
Total Standard Deviation in ln(k): 7.395595157332486
""",
)

entry(
    index = 120,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(13966.5,'m^3/(mol*s)'), n=0.851267, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-3C-R
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
    index = 121,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.84656e+14,'m^3/(mol*s)'), n=-2.20814, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10977590386192605, var=2.493812679363622, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R
    Total Standard Deviation in ln(k): 3.441658429028756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R
Total Standard Deviation in ln(k): 3.441658429028756""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R
Total Standard Deviation in ln(k): 3.441658429028756
""",
)

entry(
    index = 122,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.16447e+13,'m^3/(mol*s)'), n=-2.06111, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-3C-R
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
    index = 123,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(9.5271e+11,'m^3/(mol*s)'), n=-2.09678, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5685971363586413, var=30.87199035050881, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R
    Total Standard Deviation in ln(k): 12.56745905739619"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R
Total Standard Deviation in ln(k): 12.56745905739619""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R
Total Standard Deviation in ln(k): 12.56745905739619
""",
)

entry(
    index = 124,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing_Ext-2C-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(27200,'m^3/(mol*s)'), n=0.504, w0=(179000,'J/mol'), E0=(17900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing_Ext-2C-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing_Ext-2C-R_Ext-4R!H-R_Ext-4R!H-R
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
    index = 125,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(252000,'m^3/(mol*s)'), n=0.34, w0=(179000,'J/mol'), E0=(17900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_2C-inRing_Ext-2C-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5R!H-R
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
    index = 126,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R",
    kinetics = ArrheniusBM(A=(21.4016,'m^3/(mol*s)'), n=1.33893, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1914441397512343, var=1.2934718347708287, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R
    Total Standard Deviation in ln(k): 2.7610187372406902"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R
Total Standard Deviation in ln(k): 2.7610187372406902""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R
Total Standard Deviation in ln(k): 2.7610187372406902
""",
)

entry(
    index = 127,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(9.04e+06,'m^3/(mol*s)'), n=0, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C_Ext-2C-R_Ext-2C-R
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
    index = 128,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing_Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing_Sp-4R!H-2R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing_Sp-4R!H-2R
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
    index = 129,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing_N-Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing_N-Sp-4R!H-2R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_1BrCFS-inRing_Ext-1BrCFS-R_N-Sp-3R!H-1BrCFS_Ext-2R-R_N-2R-inRing_N-Sp-4R!H-2R
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
    index = 130,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(15609.6,'m^3/(mol*s)'), n=0.89762, w0=(136000,'J/mol'), E0=(13600,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6642490346951677, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.6689674238572052"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.6689674238572052""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.6689674238572052
""",
)

entry(
    index = 131,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_N-3R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3940,'m^3/(mol*s)'), n=1.25, w0=(136000,'J/mol'), E0=(13600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_N-3R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_N-3R!H->C_Ext-1C-R
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
    index = 132,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(197869,'m^3/(mol*s)'), n=0.545011, w0=(142500,'J/mol'), E0=(14250,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05075129033823847, var=9.056438078790713, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 6.160548799148447"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 6.160548799148447""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 6.160548799148447
""",
)

entry(
    index = 133,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.37599e+08,'m^3/(mol*s)'), n=-0.56677, w0=(174544,'J/mol'), E0=(17454.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03369078968137468, var=3.776565491727085, Tref=1000.0, N=90, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R',), comment="""BM rule fitted to 90 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 3.9805295818648503"""),
    rank = 11,
    shortDesc = """BM rule fitted to 90 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 3.9805295818648503""",
    longDesc = 
"""
BM rule fitted to 90 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R
Total Standard Deviation in ln(k): 3.9805295818648503
""",
)

entry(
    index = 134,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.00014e+24,'m^3/(mol*s)'), n=-6.08812, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.26323521490291324, var=12.871443063766044, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C',), comment="""BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C
    Total Standard Deviation in ln(k): 7.853741636437606"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 7.853741636437606""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 7.853741636437606
""",
)

entry(
    index = 135,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(9.98263e-07,'m^3/(mol*s)'), n=2.68204, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.9387987595604397, var=734.5348286596737, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 61.71685401152726"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 61.71685401152726""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 61.71685401152726
""",
)

entry(
    index = 136,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(362196,'m^3/(mol*s)'), n=0.722013, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1319968959991974, var=7.210745687028978, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R',), comment="""BM rule fitted to 18 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R
    Total Standard Deviation in ln(k): 5.7149318501018955"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R
Total Standard Deviation in ln(k): 5.7149318501018955""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R
Total Standard Deviation in ln(k): 5.7149318501018955
""",
)

entry(
    index = 137,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing",
    kinetics = ArrheniusBM(A=(9.32523e+06,'m^3/(mol*s)'), n=0.355643, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04360754403647797, var=0.2732975096407379, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing
    Total Standard Deviation in ln(k): 1.1575993770159558"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing
Total Standard Deviation in ln(k): 1.1575993770159558""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing
Total Standard Deviation in ln(k): 1.1575993770159558
""",
)

entry(
    index = 138,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing",
    kinetics = ArrheniusBM(A=(1.99782e+09,'m^3/(mol*s)'), n=-0.419678, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2680272364593517, var=4.692251060830319, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing',), comment="""BM rule fitted to 16 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing
    Total Standard Deviation in ln(k): 5.016013088986289"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing
Total Standard Deviation in ln(k): 5.016013088986289""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing
Total Standard Deviation in ln(k): 5.016013088986289
""",
)

entry(
    index = 139,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3ClOS->S",
    kinetics = ArrheniusBM(A=(500000,'m^3/(mol*s)'), n=0.65, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3ClOS->S',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_3ClOS->S
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
    index = 140,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S",
    kinetics = ArrheniusBM(A=(3.7835e+13,'m^3/(mol*s)'), n=-2.73588, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09287195407279597, var=0.21049848868108362, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S
    Total Standard Deviation in ln(k): 1.1531213628946178"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S
Total Standard Deviation in ln(k): 1.1531213628946178""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S
Total Standard Deviation in ln(k): 1.1531213628946178
""",
)

entry(
    index = 141,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1437.61,'m^3/(mol*s)'), n=1.09579, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-2C-R
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
    index = 142,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.93132e+10,'m^3/(mol*s)'), n=-1.22628, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13970672124315614, var=10.687591904721073, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 6.9048782998860165"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.9048782998860165""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R
Total Standard Deviation in ln(k): 6.9048782998860165
""",
)

entry(
    index = 143,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(9.05803e+27,'m^3/(mol*s)'), n=-6.59025, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-2C-R
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
    index = 144,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.81048e+30,'m^3/(mol*s)'), n=-7.09644, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_4R!H->C
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
    index = 145,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(3.21509e+31,'m^3/(mol*s)'), n=-7.40295, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_N-4R!H->C
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
    index = 146,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(8.1925e+11,'m^3/(mol*s)'), n=-1.52514, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5081716130487814, var=0.010089181152055388, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 1.478178544581669"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.478178544581669""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R
Total Standard Deviation in ln(k): 1.478178544581669
""",
)

entry(
    index = 147,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.98116e+19,'m^3/(mol*s)'), n=-4.24465, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3BrClO->O_Ext-2C-R_Ext-2C-R
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
    index = 148,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(15.5065,'m^3/(mol*s)'), n=1.37619, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3722131797793585, var=1.3105540315178243, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 3.2302183209858235"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.2302183209858235""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.2302183209858235
""",
)

entry(
    index = 149,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(3.58931e+06,'m^3/(mol*s)'), n=-0.0683945, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.012309496992156803, var=1.2758196654656362, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C
    Total Standard Deviation in ln(k): 2.2953205073328253"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C
Total Standard Deviation in ln(k): 2.2953205073328253""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C
Total Standard Deviation in ln(k): 2.2953205073328253
""",
)

entry(
    index = 150,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(3.24037e+06,'m^3/(mol*s)'), n=2.67936e-07, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=6.458191251135313e-17, var=0.04752486418241179, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C
    Total Standard Deviation in ln(k): 0.43703622037861506"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 0.43703622037861506""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C
Total Standard Deviation in ln(k): 0.43703622037861506
""",
)

entry(
    index = 151,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(89.4,'m^3/(mol*s)'), n=1.54, w0=(136000,'J/mol'), E0=(13600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_2R->S_Ext-2S-R_3R!H->C_Ext-1C-R_Ext-1C-R
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
    index = 152,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.83961e-10,'m^3/(mol*s)'), n=4.9034, w0=(142500,'J/mol'), E0=(14250,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Ext-3R!H-R
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
    index = 153,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C",
    kinetics = ArrheniusBM(A=(3.08187e+08,'m^3/(mol*s)'), n=-0.456645, w0=(142500,'J/mol'), E0=(14250,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10630339243394078, var=2.5905328905235434, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C
    Total Standard Deviation in ln(k): 3.493741613543768"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C
Total Standard Deviation in ln(k): 3.493741613543768""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C
Total Standard Deviation in ln(k): 3.493741613543768
""",
)

entry(
    index = 154,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_N-Sp-3R!H-1C",
    kinetics = ArrheniusBM(A=(5.19615e+07,'m^3/(mol*s)'), n=4.80037e-08, w0=(142500,'J/mol'), E0=(14250,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=2.413897921625164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_N-Sp-3R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_N-Sp-3R!H-1C
    Total Standard Deviation in ln(k): 3.1147015559000413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_N-Sp-3R!H-1C
Total Standard Deviation in ln(k): 3.1147015559000413""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_N-Sp-3R!H-1C
Total Standard Deviation in ln(k): 3.1147015559000413
""",
)

entry(
    index = 155,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F",
    kinetics = ArrheniusBM(A=(2.98696e+15,'m^3/(mol*s)'), n=-3.29718, w0=(176310,'J/mol'), E0=(17631,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.2941719719397358, var=13.674895902465439, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F',), comment="""BM rule fitted to 21 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F
    Total Standard Deviation in ln(k): 10.6651151755515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F
Total Standard Deviation in ln(k): 10.6651151755515""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F
Total Standard Deviation in ln(k): 10.6651151755515
""",
)

entry(
    index = 156,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F",
    kinetics = ArrheniusBM(A=(1.97476e+08,'m^3/(mol*s)'), n=-0.358415, w0=(174007,'J/mol'), E0=(17400.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.028034203869938407, var=2.4148279590666055, Tref=1000.0, N=69, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F',), comment="""BM rule fitted to 69 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F
    Total Standard Deviation in ln(k): 3.18573921938979"""),
    rank = 11,
    shortDesc = """BM rule fitted to 69 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F
Total Standard Deviation in ln(k): 3.18573921938979""",
    longDesc = 
"""
BM rule fitted to 69 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F
Total Standard Deviation in ln(k): 3.18573921938979
""",
)

entry(
    index = 157,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(8.75187e+24,'m^3/(mol*s)'), n=-6.27391, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.25187009427351104, var=11.384895347359857, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 10 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 7.3971184108378"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 7.3971184108378""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 7.3971184108378
""",
)

entry(
    index = 158,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C",
    kinetics = ArrheniusBM(A=(2.39918e+21,'m^3/(mol*s)'), n=-5.87461, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.6609179753085948, var=2.4474408242787957, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C
    Total Standard Deviation in ln(k): 12.334553810562252"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C
Total Standard Deviation in ln(k): 12.334553810562252""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C
Total Standard Deviation in ln(k): 12.334553810562252
""",
)

entry(
    index = 159,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_N-Sp-4C-2C",
    kinetics = ArrheniusBM(A=(2.4e+28,'m^3/(mol*s)'), n=-7.11, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_N-Sp-4C-2C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_N-Sp-4C-2C
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
    index = 160,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.5e+07,'m^3/(mol*s)'), n=0, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->C_Ext-2C-R
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
    index = 161,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_3C-inRing",
    kinetics = ArrheniusBM(A=(1.25109e+08,'m^3/(mol*s)'), n=-0.247784, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_3C-inRing
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
    index = 162,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing",
    kinetics = ArrheniusBM(A=(2.68054e+07,'m^3/(mol*s)'), n=0.21838, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.023310567665240308, var=0.07965262646958993, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing',), comment="""BM rule fitted to 17 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing
    Total Standard Deviation in ln(k): 0.624361574708755"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing
Total Standard Deviation in ln(k): 0.624361574708755""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing
Total Standard Deviation in ln(k): 0.624361574708755
""",
)

entry(
    index = 163,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(1.14605e+07,'m^3/(mol*s)'), n=0.36193, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06473678945074876, var=0.16285884646625434, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 0.971681599438312"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 0.971681599438312""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 0.971681599438312
""",
)

entry(
    index = 164,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(7.58778e+06,'m^3/(mol*s)'), n=0.349356, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17016890191634104, var=0.2974812683061607, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 1.520979521855843"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.520979521855843""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.520979521855843
""",
)

entry(
    index = 165,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.83153e+09,'m^3/(mol*s)'), n=-0.472098, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4131319918281209, var=6.191315770002749, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R',), comment="""BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R
    Total Standard Deviation in ln(k): 6.026273013875103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 6.026273013875103""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 6.026273013875103
""",
)

entry(
    index = 166,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Sp-3C#2C",
    kinetics = ArrheniusBM(A=(1.81e+08,'m^3/(mol*s)'), n=0, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Sp-3C#2C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Sp-3C#2C
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
    index = 167,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C",
    kinetics = ArrheniusBM(A=(1.19651e+08,'m^3/(mol*s)'), n=3.04541e-07, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16819443494880856, var=0.07267224299466185, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C
    Total Standard Deviation in ln(k): 0.9630313506418686"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C
Total Standard Deviation in ln(k): 0.9630313506418686""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C
Total Standard Deviation in ln(k): 0.9630313506418686
""",
)

entry(
    index = 168,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_3ClO->O",
    kinetics = ArrheniusBM(A=(46800,'m^3/(mol*s)'), n=0, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(1500,'K'), Tmax=(1900,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_3ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_3ClO->O
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
    index = 169,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O",
    kinetics = ArrheniusBM(A=(7.60724e+13,'m^3/(mol*s)'), n=-2.86872, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1683130451926711, var=0.020241278793041436, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O
    Total Standard Deviation in ln(k): 0.7081144631059917"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O
Total Standard Deviation in ln(k): 0.7081144631059917""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O
Total Standard Deviation in ln(k): 0.7081144631059917
""",
)

entry(
    index = 170,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(228516,'m^3/(mol*s)'), n=0.317874, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.49099035658628687, var=28.07779457238084, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.85643140830555"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.85643140830555""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.85643140830555
""",
)

entry(
    index = 171,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.17037e+12,'m^3/(mol*s)'), n=-1.62373, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-2C-R
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
    index = 172,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.64994e+14,'m^3/(mol*s)'), n=-2.23152, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R
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
    index = 173,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(1.59931e+07,'m^3/(mol*s)'), n=-0.350524, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3243923006376555, var=1.570809053220402, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 3.3276290240615687"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 3.3276290240615687""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 3.3276290240615687
""",
)

entry(
    index = 174,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(13.9325,'m^3/(mol*s)'), n=1.38954, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4238861397169194, var=1.3763793023443802, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 3.4169795646974666"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 3.4169795646974666""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 3.4169795646974666
""",
)

entry(
    index = 175,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.41998e+06,'m^3/(mol*s)'), n=-4.72547e-07, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.4894960932194606e-07, var=1.3573950188437058, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R
    Total Standard Deviation in ln(k): 2.3356630192661396"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R
Total Standard Deviation in ln(k): 2.3356630192661396""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R
Total Standard Deviation in ln(k): 2.3356630192661396
""",
)

entry(
    index = 176,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C_4R!H->C",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=0, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C_4R!H->C
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
    index = 177,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(3.5e+06,'m^3/(mol*s)'), n=0, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_N-Sp-4R!H-2C_N-4R!H->C
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
    index = 178,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.66906e+08,'m^3/(mol*s)'), n=-0.60886, w0=(142500,'J/mol'), E0=(14250,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14173786022890533, var=4.459560686439948, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.589659048330421"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 4.589659048330421""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 4.589659048330421
""",
)

entry(
    index = 179,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(2.03454e+08,'m^3/(mol*s)'), n=-0.589199, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07532915873795223, var=6.0325521090133, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R
    Total Standard Deviation in ln(k): 5.11315003935608"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R
Total Standard Deviation in ln(k): 5.11315003935608""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R
Total Standard Deviation in ln(k): 5.11315003935608
""",
)

entry(
    index = 180,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C",
    kinetics = ArrheniusBM(A=(1.22533e+19,'m^3/(mol*s)'), n=-4.65414, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.029112360120668, var=3.143212838601613, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C
    Total Standard Deviation in ln(k): 6.139925993063474"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C
Total Standard Deviation in ln(k): 6.139925993063474""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C
Total Standard Deviation in ln(k): 6.139925993063474
""",
)

entry(
    index = 181,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_N-2CF->C",
    kinetics = ArrheniusBM(A=(1e+06,'m^3/(mol*s)'), n=0, w0=(242500,'J/mol'), E0=(24250,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_N-2CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_N-2CF->C
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
    index = 182,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(2.94723e+14,'m^3/(mol*s)'), n=-2.79674, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4059670961657003, var=4.392906822891536, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 5.221794691784953"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 5.221794691784953""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 5.221794691784953
""",
)

entry(
    index = 183,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(1.62869e+08,'m^3/(mol*s)'), n=-0.325368, w0=(174158,'J/mol'), E0=(17415.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0368174694162729, var=2.340513891536735, Tref=1000.0, N=60, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl',), comment="""BM rule fitted to 60 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl
    Total Standard Deviation in ln(k): 3.1594979066038427"""),
    rank = 11,
    shortDesc = """BM rule fitted to 60 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 3.1594979066038427""",
    longDesc = 
"""
BM rule fitted to 60 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl
Total Standard Deviation in ln(k): 3.1594979066038427
""",
)

entry(
    index = 184,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.12e+41,'m^3/(mol*s)'), n=-10.8, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_5R!H->Cl
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
    index = 185,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(8.43711e+23,'m^3/(mol*s)'), n=-5.99271, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2588485530224486, var=10.966526638171555, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl',), comment="""BM rule fitted to 9 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 7.289203103693596"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 7.289203103693596""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 7.289203103693596
""",
)

entry(
    index = 186,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.11e+34,'m^3/(mol*s)'), n=-9.59, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C_Ext-2C-R
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
    index = 187,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.68385e+07,'m^3/(mol*s)'), n=0.219301, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.021519060178803617, var=0.06270356135707832, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R',), comment="""BM rule fitted to 16 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R
    Total Standard Deviation in ln(k): 0.5560672694481664"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 0.5560672694481664""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R
Total Standard Deviation in ln(k): 0.5560672694481664
""",
)

entry(
    index = 188,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(2.09978e+06,'m^3/(mol*s)'), n=0.6, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C
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
    index = 189,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(7.09e+06,'m^3/(mol*s)'), n=0.412, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C
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
    index = 190,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(3.156e+06,'m^3/(mol*s)'), n=0.461, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C
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
    index = 191,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(7.22657e+07,'m^3/(mol*s)'), n=0.062, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C
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
    index = 192,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.21132e+09,'m^3/(mol*s)'), n=-0.304271, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12269472272695502, var=0.28081469210070564, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 1.370626437198403"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 1.370626437198403""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 1.370626437198403
""",
)

entry(
    index = 193,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(5.15007e+19,'m^3/(mol*s)'), n=-5.14141, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3019489866697833, var=33.391442226143326, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 12.343093352751294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 12.343093352751294""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 12.343093352751294
""",
)

entry(
    index = 194,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_Sp-3C-2C",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_Sp-3C-2C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_Sp-3C-2C
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
    index = 195,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_N-Sp-3C-2C",
    kinetics = ArrheniusBM(A=(1.21e+08,'m^3/(mol*s)'), n=0, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_N-Sp-3C-2C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_N-Sp-3C#2C_N-Sp-3C-2C
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
    index = 196,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.62297e+14,'m^3/(mol*s)'), n=-2.96586, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.9172642592337796, var=8.66250553588887e-06, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O_Ext-2C-R
    Total Standard Deviation in ln(k): 4.82314724578251"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O_Ext-2C-R
Total Standard Deviation in ln(k): 4.82314724578251""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->C_N-3ClOS->S_N-3ClO->O_Ext-2C-R
Total Standard Deviation in ln(k): 4.82314724578251
""",
)

entry(
    index = 197,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(163500,'J/mol'), E0=(16350,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_5R!H->F
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
    index = 198,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(2.53123,'m^3/(mol*s)'), n=1.5854, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Sp-3C-2C_Ext-2C-R_Ext-3C-R_Ext-3C-R_Ext-3C-R_N-5R!H->F
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
    index = 199,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-2C-R",
    kinetics = ArrheniusBM(A=(4.18e+06,'m^3/(mol*s)'), n=-0.085, w0=(179000,'J/mol'), E0=(17900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-2C-R
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
    index = 200,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(124.902,'m^3/(mol*s)'), n=1.09941, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6005523355889325, var=0.015436303854962363, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C
    Total Standard Deviation in ln(k): 1.757999611670846"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C
Total Standard Deviation in ln(k): 1.757999611670846""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C
Total Standard Deviation in ln(k): 1.757999611670846
""",
)

entry(
    index = 201,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(0.004135,'m^3/(mol*s)'), n=2.525, w0=(179000,'J/mol'), E0=(17900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-2C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-2C
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
    index = 202,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(5.15546e+06,'m^3/(mol*s)'), n=-6.35516e-07, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.305460834090209e-17, var=0.7836333533627092, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C
    Total Standard Deviation in ln(k): 1.7746529918743192"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C
Total Standard Deviation in ln(k): 1.7746529918743192""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C
Total Standard Deviation in ln(k): 1.7746529918743192
""",
)

entry(
    index = 203,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.505e+06,'m^3/(mol*s)'), n=0, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(200,'K'), Tmax=(300,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_N-5R!H->C
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
    index = 204,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.59501e+09,'m^3/(mol*s)'), n=-0.91329, w0=(142500,'J/mol'), E0=(14250,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.3201134058007704, var=18.768935493398782, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 14.514570404182463"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 14.514570404182463""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 14.514570404182463
""",
)

entry(
    index = 205,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.262388,'m^3/(mol*s)'), n=1.84767, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_Ext-4R!H-R
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
    index = 206,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_4R!H->O",
    kinetics = ArrheniusBM(A=(4e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_4R!H->O
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
    index = 207,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(5.10609e+09,'m^3/(mol*s)'), n=-1.00997, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06670074303734959, var=2.4865436886022945, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O
    Total Standard Deviation in ln(k): 3.3288121038302823"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O
Total Standard Deviation in ln(k): 3.3288121038302823""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O
Total Standard Deviation in ln(k): 3.3288121038302823
""",
)

entry(
    index = 208,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.35279e+19,'m^3/(mol*s)'), n=-4.67047, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1952341741101709, var=4.18886917553156, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C_Ext-1C-R
    Total Standard Deviation in ln(k): 7.106137510558848"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.106137510558848""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.106137510558848
""",
)

entry(
    index = 209,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(6.91206e+12,'m^3/(mol*s)'), n=-2.31041, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.34802700444812823, var=6.9112209340447635, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R
    Total Standard Deviation in ln(k): 6.1447280657660315"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R
Total Standard Deviation in ln(k): 6.1447280657660315""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R
Total Standard Deviation in ln(k): 6.1447280657660315
""",
)

entry(
    index = 210,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.13778e+18,'m^3/(mol*s)'), n=-3.98591, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.877597519120878, var=1.1652692990436386, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 16.931897167737752"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 16.931897167737752""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 16.931897167737752
""",
)

entry(
    index = 211,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.40432e+10,'m^3/(mol*s)'), n=-0.600746, w0=(175673,'J/mol'), E0=(17567.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15114643148377926, var=6.101398069345152, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R',), comment="""BM rule fitted to 26 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R
    Total Standard Deviation in ln(k): 5.3316626651803904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 5.3316626651803904""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R
Total Standard Deviation in ln(k): 5.3316626651803904
""",
)

entry(
    index = 212,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R",
    kinetics = ArrheniusBM(A=(2.60145e+07,'m^3/(mol*s)'), n=-0.152484, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.020296918617266256, var=0.32136534358908186, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R
    Total Standard Deviation in ln(k): 1.1874634455734214"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R
Total Standard Deviation in ln(k): 1.1874634455734214""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R
Total Standard Deviation in ln(k): 1.1874634455734214
""",
)

entry(
    index = 213,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_3BrCO->Br",
    kinetics = ArrheniusBM(A=(310000,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_3BrCO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_3BrCO->Br
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
    index = 214,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br",
    kinetics = ArrheniusBM(A=(4.78607e+08,'m^3/(mol*s)'), n=-0.478103, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1181355971138859, var=1.9914919479626447, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br
    Total Standard Deviation in ln(k): 3.1259098721109693"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br
Total Standard Deviation in ln(k): 3.1259098721109693""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br
Total Standard Deviation in ln(k): 3.1259098721109693
""",
)

entry(
    index = 215,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(1.12e+41,'m^3/(mol*s)'), n=-10.8, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->Br
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
    index = 216,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(4.53221e+22,'m^3/(mol*s)'), n=-5.64121, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2675716278866836, var=9.741478351930377, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br',), comment="""BM rule fitted to 8 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 6.929337624333936"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 6.929337624333936""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 6.929337624333936
""",
)

entry(
    index = 217,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.88633e+07,'m^3/(mol*s)'), n=0.213913, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.197897857500688e-05, var=0.012106578839213466, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R',), comment="""BM rule fitted to 9 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.22078677692607784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.22078677692607784""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.22078677692607784
""",
)

entry(
    index = 218,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Sp-3C=2C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Sp-3C=2C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Sp-3C=2C
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
    index = 219,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C",
    kinetics = ArrheniusBM(A=(2.42121e+07,'m^3/(mol*s)'), n=0.230106, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6867675649490259, var=1.162208815439692, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C
    Total Standard Deviation in ln(k): 3.8867671143058615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C
Total Standard Deviation in ln(k): 3.8867671143058615""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C
Total Standard Deviation in ln(k): 3.8867671143058615
""",
)

entry(
    index = 220,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C",
    kinetics = ArrheniusBM(A=(1.31702e+09,'m^3/(mol*s)'), n=-0.311872, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09855729141736821, var=0.14657211529301606, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C
    Total Standard Deviation in ln(k): 1.0151389546179668"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C
Total Standard Deviation in ln(k): 1.0151389546179668""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C
Total Standard Deviation in ln(k): 1.0151389546179668
""",
)

entry(
    index = 221,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C",
    kinetics = ArrheniusBM(A=(2.72123e+07,'m^3/(mol*s)'), n=0.0405888, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0026605099486425566, var=2.9797993750572114, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C
    Total Standard Deviation in ln(k): 3.4672775135939036"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 3.4672775135939036""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 3.4672775135939036
""",
)

entry(
    index = 222,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C",
    kinetics = ArrheniusBM(A=(4.36443e+19,'m^3/(mol*s)'), n=-5.46416, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.348308094578755, var=49.29253916270169, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C
    Total Standard Deviation in ln(k): 14.95011942232105"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C
Total Standard Deviation in ln(k): 14.95011942232105""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C
Total Standard Deviation in ln(k): 14.95011942232105
""",
)

entry(
    index = 223,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C",
    kinetics = ArrheniusBM(A=(6.6015e+19,'m^3/(mol*s)'), n=-4.65728, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.536223587017913, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C
    Total Standard Deviation in ln(k): 6.372421072909329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 6.372421072909329""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C
Total Standard Deviation in ln(k): 6.372421072909329
""",
)

entry(
    index = 224,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C_4R!H-inRing",
    kinetics = ArrheniusBM(A=(3.845,'m^3/(mol*s)'), n=1.52, w0=(179000,'J/mol'), E0=(17900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C_4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C_4R!H-inRing
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
    index = 225,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(0.0239,'m^3/(mol*s)'), n=2.243, w0=(179000,'J/mol'), E0=(17900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C_N-4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2C_N-4R!H-inRing
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
    index = 226,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.05e+06,'m^3/(mol*s)'), n=0, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_3R!H->O_2R->C_N-2C-inRing_Ext-2C-R_Sp-4R!H-2C_Ext-2C-R_5R!H->C_Ext-2C-R
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
    index = 227,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R_3R!H->Cl",
    kinetics = ArrheniusBM(A=(410.863,'m^3/(mol*s)'), n=1.33656, w0=(142500,'J/mol'), E0=(14250,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R_3R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R_3R!H->Cl
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
    index = 228,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R_N-3R!H->Cl",
    kinetics = ArrheniusBM(A=(6.84618,'m^3/(mol*s)'), n=1.32431, w0=(142500,'J/mol'), E0=(14250,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R_N-3R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_2BrCF->Br_Ext-1C-R_Sp-3R!H-1C_Ext-1C-R_Ext-1C-R_N-3R!H->Cl
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
    index = 229,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F",
    kinetics = ArrheniusBM(A=(5.31635e+11,'m^3/(mol*s)'), n=-1.64268, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08666340067968399, var=1.7246968931301185, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F
    Total Standard Deviation in ln(k): 2.8505200224180225"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F
Total Standard Deviation in ln(k): 2.8505200224180225""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F
Total Standard Deviation in ln(k): 2.8505200224180225
""",
)

entry(
    index = 230,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F",
    kinetics = ArrheniusBM(A=(204.407,'m^3/(mol*s)'), n=1.30994, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.006495666341019505, var=10.327386200937552, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F
    Total Standard Deviation in ln(k): 6.4587877075598685"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F
Total Standard Deviation in ln(k): 6.4587877075598685""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F
Total Standard Deviation in ln(k): 6.4587877075598685
""",
)

entry(
    index = 231,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.78e+27,'m^3/(mol*s)'), n=-6.64, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C_Ext-1C-R_Ext-1C-R
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
    index = 232,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.84829e+11,'m^3/(mol*s)'), n=-2.01038, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2963547859085115, var=8.489684066704982, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R
    Total Standard Deviation in ln(k): 6.5858191241053"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R
Total Standard Deviation in ln(k): 6.5858191241053""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R
Total Standard Deviation in ln(k): 6.5858191241053
""",
)

entry(
    index = 233,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.54e+40,'m^3/(mol*s)'), n=-10.66, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-1C-R_Ext-1C-R
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
    index = 234,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R",
    kinetics = ArrheniusBM(A=(1.07363e+10,'m^3/(mol*s)'), n=-0.40001, w0=(190375,'J/mol'), E0=(19037.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13873041190497074, var=3.85582083288152, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R
    Total Standard Deviation in ln(k): 4.285115612451995"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R
Total Standard Deviation in ln(k): 4.285115612451995""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R
Total Standard Deviation in ln(k): 4.285115612451995
""",
)

entry(
    index = 235,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O",
    kinetics = ArrheniusBM(A=(7.27037e+07,'m^3/(mol*s)'), n=-0.266667, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2929156463716392e-09, var=0.9482355690112468, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O
    Total Standard Deviation in ln(k): 1.9521586575651686"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O
Total Standard Deviation in ln(k): 1.9521586575651686""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O
Total Standard Deviation in ln(k): 1.9521586575651686
""",
)

entry(
    index = 236,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O",
    kinetics = ArrheniusBM(A=(3.40266e+10,'m^3/(mol*s)'), n=-0.792692, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4811781641962043, var=10.001103914652795, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O
    Total Standard Deviation in ln(k): 7.54886921739002"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O
Total Standard Deviation in ln(k): 7.54886921739002""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O
Total Standard Deviation in ln(k): 7.54886921739002
""",
)

entry(
    index = 237,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C",
    kinetics = ArrheniusBM(A=(7.48426e+07,'m^3/(mol*s)'), n=-0.346198, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27470422837724523, var=1.1926687938300655, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C
    Total Standard Deviation in ln(k): 2.8795703096784964"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C
Total Standard Deviation in ln(k): 2.8795703096784964""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C
Total Standard Deviation in ln(k): 2.8795703096784964
""",
)

entry(
    index = 238,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C",
    kinetics = ArrheniusBM(A=(1.30834e+07,'m^3/(mol*s)'), n=-0.0264904, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00027487107226433134, var=0.20277814970297373, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C
    Total Standard Deviation in ln(k): 0.903440776901281"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C
Total Standard Deviation in ln(k): 0.903440776901281""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C
Total Standard Deviation in ln(k): 0.903440776901281
""",
)

entry(
    index = 239,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O",
    kinetics = ArrheniusBM(A=(1.55384e+07,'m^3/(mol*s)'), n=-7.59459e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12716993381876504, var=0.05513829209243009, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O
    Total Standard Deviation in ln(k): 0.790265201313268"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O
Total Standard Deviation in ln(k): 0.790265201313268""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O
Total Standard Deviation in ln(k): 0.790265201313268
""",
)

entry(
    index = 240,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O",
    kinetics = ArrheniusBM(A=(6.53371e+08,'m^3/(mol*s)'), n=-0.521521, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15587227381418983, var=2.559122993418375, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O
    Total Standard Deviation in ln(k): 3.598665528866518"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O
Total Standard Deviation in ln(k): 3.598665528866518""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O
Total Standard Deviation in ln(k): 3.598665528866518
""",
)

entry(
    index = 241,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->C
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
    index = 242,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C",
    kinetics = ArrheniusBM(A=(7.81494e+24,'m^3/(mol*s)'), n=-6.44709, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.305796145688144, var=9.983013716132552, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C
    Total Standard Deviation in ln(k): 7.102474433820333"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C
Total Standard Deviation in ln(k): 7.102474433820333""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C
Total Standard Deviation in ln(k): 7.102474433820333
""",
)

entry(
    index = 243,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(2.85197e+07,'m^3/(mol*s)'), n=0.213787, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.000126811292081254, var=0.012046587663541186, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 0.22035222524749093"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.22035222524749093""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.22035222524749093
""",
)

entry(
    index = 244,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(1.89626e+07,'m^3/(mol*s)'), n=0.120172, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03119957587204572, var=5.060225472910453, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 4.58803141017077"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.58803141017077""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R
Total Standard Deviation in ln(k): 4.58803141017077
""",
)

entry(
    index = 245,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.12e+41,'m^3/(mol*s)'), n=-10.8, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-3C-R
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
    index = 246,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(1.7979e+07,'m^3/(mol*s)'), n=0.240345, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06239915174409146, var=9.629649721936181e-35, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C
    Total Standard Deviation in ln(k): 0.15678178830173736"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C
Total Standard Deviation in ln(k): 0.15678178830173736""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C
Total Standard Deviation in ln(k): 0.15678178830173736
""",
)

entry(
    index = 247,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_N-Sp-4R!H-2C",
    kinetics = ArrheniusBM(A=(6.117e+08,'m^3/(mol*s)'), n=-0.152, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_N-Sp-4R!H-2C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_N-Sp-4R!H-2C
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
    index = 248,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_Sp-4C=3C",
    kinetics = ArrheniusBM(A=(2.92e+07,'m^3/(mol*s)'), n=0.18, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(200,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_Sp-4C=3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_Sp-4C=3C
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
    index = 249,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C",
    kinetics = ArrheniusBM(A=(2.33349e+09,'m^3/(mol*s)'), n=-0.385433, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06986973032483731, var=0.05124357648151392, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C
    Total Standard Deviation in ln(k): 0.6293648494601423"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C
Total Standard Deviation in ln(k): 0.6293648494601423""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C
Total Standard Deviation in ln(k): 0.6293648494601423
""",
)

entry(
    index = 250,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_N-Sp-3C-2C_Ext-3C-R
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
    index = 251,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.84096e+21,'m^3/(mol*s)'), n=-5.92191, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.653369690823422, var=91.55450293110613, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R
    Total Standard Deviation in ln(k): 28.361451450432188"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 28.361451450432188""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R
Total Standard Deviation in ln(k): 28.361451450432188
""",
)

entry(
    index = 252,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.4e+28,'m^3/(mol*s)'), n=-7.11, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_N-Sp-3C-2C_Ext-3C-R
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
    index = 253,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.80704e+11,'m^3/(mol*s)'), n=-1.71043, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09418869616164992, var=0.9520381096174071, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R
    Total Standard Deviation in ln(k): 2.1927239510256875"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R
Total Standard Deviation in ln(k): 2.1927239510256875""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R
Total Standard Deviation in ln(k): 2.1927239510256875
""",
)

entry(
    index = 254,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(925.476,'m^3/(mol*s)'), n=1.08429, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10478361023988274, var=38.58695606349498, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F_Ext-2CF-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F_Ext-2CF-R
    Total Standard Deviation in ln(k): 12.71636892606939"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F_Ext-2CF-R
Total Standard Deviation in ln(k): 12.71636892606939""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F_Ext-2CF-R
Total Standard Deviation in ln(k): 12.71636892606939
""",
)

entry(
    index = 255,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.95004e+08,'m^3/(mol*s)'), n=-0.654592, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09304754614240092, var=0.9355080249062689, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 2.1728009261009507"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.1728009261009507""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.1728009261009507
""",
)

entry(
    index = 256,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(1.816e+40,'m^3/(mol*s)'), n=-10.56, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-2CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-2CF-R
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
    index = 257,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.52887e+10,'m^3/(mol*s)'), n=-0.421056, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.33715670700436484, var=0.3811706868322634, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 2.084831240009212"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.084831240009212""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.084831240009212
""",
)

entry(
    index = 258,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_2CF->C",
    kinetics = ArrheniusBM(A=(1.02e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_2CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_2CF->C
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
    index = 259,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_N-2CF->C",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(242500,'J/mol'), E0=(24250,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_N-2CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_N-2CF->C
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
    index = 260,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(8.11368e+07,'m^3/(mol*s)'), n=-0.32, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.836831953640066e-10, var=0.5020281415876423, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R
    Total Standard Deviation in ln(k): 1.4204338763306865"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R
Total Standard Deviation in ln(k): 1.4204338763306865""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R
Total Standard Deviation in ln(k): 1.4204338763306865
""",
)

entry(
    index = 261,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(5.44763e+10,'m^3/(mol*s)'), n=-0.821521, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4963762271127419, var=9.904855254581296, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R
    Total Standard Deviation in ln(k): 7.556474677212332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R
Total Standard Deviation in ln(k): 7.556474677212332""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R
Total Standard Deviation in ln(k): 7.556474677212332
""",
)

entry(
    index = 262,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8.79314e+07,'m^3/(mol*s)'), n=-0.354978, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14995901122765223, var=2.2305291506772655, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-1C-R
    Total Standard Deviation in ln(k): 3.3708444816661607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-1C-R
Total Standard Deviation in ln(k): 3.3708444816661607""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-1C-R
Total Standard Deviation in ln(k): 3.3708444816661607
""",
)

entry(
    index = 263,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(1.9609e+09,'m^3/(mol*s)'), n=-0.904668, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2801860435942295, var=1.832562471894275, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R
    Total Standard Deviation in ln(k): 3.417838434014057"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R
Total Standard Deviation in ln(k): 3.417838434014057""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R
Total Standard Deviation in ln(k): 3.417838434014057
""",
)

entry(
    index = 264,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(1.51229e+07,'m^3/(mol*s)'), n=-0.0676006, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0015083346805988627, var=0.08098025792921044, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R
    Total Standard Deviation in ln(k): 0.5742778560803471"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R
Total Standard Deviation in ln(k): 0.5742778560803471""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R
Total Standard Deviation in ln(k): 0.5742778560803471
""",
)

entry(
    index = 265,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(5.38619e+06,'m^3/(mol*s)'), n=0.213797, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0017612663798735474, var=0.03659456747547423, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-4R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.38792523090451425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.38792523090451425""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.38792523090451425
""",
)

entry(
    index = 266,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(1.5407e+07,'m^3/(mol*s)'), n=7.49647e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14213107497021946, var=0.059997829985618166, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R
    Total Standard Deviation in ln(k): 0.8481621745004314"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R
Total Standard Deviation in ln(k): 0.8481621745004314""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R
Total Standard Deviation in ln(k): 0.8481621745004314
""",
)

entry(
    index = 267,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_Sp-3C-1C",
    kinetics = ArrheniusBM(A=(9.58073e+08,'m^3/(mol*s)'), n=-0.619183, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.003931094337186852, var=3.0920351691010954, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_Sp-3C-1C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_Sp-3C-1C
    Total Standard Deviation in ln(k): 3.535040111457791"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_Sp-3C-1C
Total Standard Deviation in ln(k): 3.535040111457791""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_Sp-3C-1C
Total Standard Deviation in ln(k): 3.535040111457791
""",
)

entry(
    index = 268,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C",
    kinetics = ArrheniusBM(A=(8.46134e+07,'m^3/(mol*s)'), n=-1.34299e-06, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004336172346831628, var=0.18332713064265185, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C
    Total Standard Deviation in ln(k): 0.8692566622009568"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C
Total Standard Deviation in ln(k): 0.8692566622009568""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C
Total Standard Deviation in ln(k): 0.8692566622009568
""",
)

entry(
    index = 269,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C",
    kinetics = ArrheniusBM(A=(8.36064e+26,'m^3/(mol*s)'), n=-7.16302, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.335150463723986, var=16.804457621129963, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C
    Total Standard Deviation in ln(k): 9.060145297717952"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C
Total Standard Deviation in ln(k): 9.060145297717952""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C
Total Standard Deviation in ln(k): 9.060145297717952
""",
)

entry(
    index = 270,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_N-Sp-4C-2C",
    kinetics = ArrheniusBM(A=(6.6015e+19,'m^3/(mol*s)'), n=-4.65728, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.536223587017913, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_N-Sp-4C-2C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_N-Sp-4C-2C
    Total Standard Deviation in ln(k): 6.372421072909329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_N-Sp-4C-2C
Total Standard Deviation in ln(k): 6.372421072909329""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_N-Sp-4C-2C
Total Standard Deviation in ln(k): 6.372421072909329
""",
)

entry(
    index = 271,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(2.83155e+07,'m^3/(mol*s)'), n=0.213711, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00015371060567378, var=0.01321850147114157, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 0.23087409175853962"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 0.23087409175853962""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 0.23087409175853962
""",
)

entry(
    index = 272,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.92e+07,'m^3/(mol*s)'), n=0.18, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(200,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Ext-4R!H-R_Ext-2C-R
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
    index = 273,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.92e+07,'m^3/(mol*s)'), n=0.18, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(200,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_N-Sp-3C=2C_Sp-4R!H-2C_Ext-2C-R
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
    index = 274,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C",
    kinetics = ArrheniusBM(A=(3.1711e+07,'m^3/(mol*s)'), n=0.21519, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0022644853455516876, var=7.490440640908408e-07, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C
    Total Standard Deviation in ln(k): 0.007424706391292111"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C
Total Standard Deviation in ln(k): 0.007424706391292111""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C
Total Standard Deviation in ln(k): 0.007424706391292111
""",
)

entry(
    index = 275,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C",
    kinetics = ArrheniusBM(A=(1.11169e+10,'m^3/(mol*s)'), n=-0.603566, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2406798463897532, var=0.000995063531188551, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C
    Total Standard Deviation in ln(k): 0.6679618536124499"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 0.6679618536124499""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C
Total Standard Deviation in ln(k): 0.6679618536124499
""",
)

entry(
    index = 276,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(7.27e+36,'m^3/(mol*s)'), n=-9.86, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R_Ext-3C-R
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
    index = 277,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(4.80829e+08,'m^3/(mol*s)'), n=-0.721577, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06302136044247904, var=2.3121662723299528, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 3.206706994250524"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.206706994250524""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl
Total Standard Deviation in ln(k): 3.206706994250524
""",
)

entry(
    index = 278,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(2.56119e+13,'m^3/(mol*s)'), n=-2.20486, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10977238313035541, var=0.8543561589632981, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 2.128814476687692"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.128814476687692""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.128814476687692
""",
)

entry(
    index = 279,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F_Ext-2CF-R_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(1.4e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F_Ext-2CF-R_Ext-2CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_N-4BrCClF->F_Ext-2CF-R_Ext-2CF-R
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
    index = 280,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(92.2154,'m^3/(mol*s)'), n=1.49683, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1615737753239117, var=0.0004855564388348445, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R_Ext-2CF-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R_Ext-2CF-R
    Total Standard Deviation in ln(k): 2.962702103177292"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R_Ext-2CF-R
Total Standard Deviation in ln(k): 2.962702103177292""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R_Ext-2CF-R
Total Standard Deviation in ln(k): 2.962702103177292
""",
)

entry(
    index = 281,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_Ext-5R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.223e+10,'m^3/(mol*s)'), n=-0.506, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_Ext-5R!H-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_Ext-5R!H-R_Ext-1C-R
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
    index = 282,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_5R!H->O",
    kinetics = ArrheniusBM(A=(1.47989e+07,'m^3/(mol*s)'), n=5.29939e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.32434502719988945, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_5R!H->O
    Total Standard Deviation in ln(k): 1.141722635385032"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_5R!H->O
Total Standard Deviation in ln(k): 1.141722635385032""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_5R!H->O
Total Standard Deviation in ln(k): 1.141722635385032
""",
)

entry(
    index = 283,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(2.52275e+08,'m^3/(mol*s)'), n=-0.533333, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.937185935018646e-11, var=0.3834307425082525, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O
    Total Standard Deviation in ln(k): 1.2413677393814242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O
Total Standard Deviation in ln(k): 1.2413677393814242""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O
Total Standard Deviation in ln(k): 1.2413677393814242
""",
)

entry(
    index = 284,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.65983e+11,'m^3/(mol*s)'), n=-0.84129, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13665755298418078, var=2.9143026642115575, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 3.7657098488134544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.7657098488134544""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.7657098488134544
""",
)

entry(
    index = 285,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(2.55114e+09,'m^3/(mol*s)'), n=-1.1, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.99323155384961e-13, var=2.385481894116226, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R
    Total Standard Deviation in ln(k): 3.0963143940546978"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R
Total Standard Deviation in ln(k): 3.0963143940546978""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R
Total Standard Deviation in ln(k): 3.0963143940546978
""",
)

entry(
    index = 286,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_5R!H->C",
    kinetics = ArrheniusBM(A=(3.41902e+08,'m^3/(mol*s)'), n=-0.65, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.6951989967662565e-10, var=0.8907254772281384, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_5R!H->C
    Total Standard Deviation in ln(k): 1.8920339578689276"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_5R!H->C
Total Standard Deviation in ln(k): 1.8920339578689276""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_5R!H->C
Total Standard Deviation in ln(k): 1.8920339578689276
""",
)

entry(
    index = 287,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_N-5R!H->C
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
    index = 288,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF",
    kinetics = ArrheniusBM(A=(2.17563e+11,'m^3/(mol*s)'), n=-1.53674, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11076293667129158, var=0.13376655749343178, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF
    Total Standard Deviation in ln(k): 1.01151286269961"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF
Total Standard Deviation in ln(k): 1.01151286269961""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF
Total Standard Deviation in ln(k): 1.01151286269961
""",
)

entry(
    index = 289,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-5R!H-2CF",
    kinetics = ArrheniusBM(A=(250896,'m^3/(mol*s)'), n=0.298496, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06243996161282631, var=0.8653650783542394, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-5R!H-2CF',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-5R!H-2CF
    Total Standard Deviation in ln(k): 2.0217891484895985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-5R!H-2CF
Total Standard Deviation in ln(k): 2.0217891484895985""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-5R!H-2CF
Total Standard Deviation in ln(k): 2.0217891484895985
""",
)

entry(
    index = 290,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-4R!H=3BrBrCCOO",
    kinetics = ArrheniusBM(A=(3.1002e+07,'m^3/(mol*s)'), n=-0.094897, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09812769830724073, var=0.8853225170864677, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-4R!H=3BrBrCCOO',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-4R!H=3BrBrCCOO
    Total Standard Deviation in ln(k): 2.132838887656121"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-4R!H=3BrBrCCOO
Total Standard Deviation in ln(k): 2.132838887656121""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-4R!H=3BrBrCCOO
Total Standard Deviation in ln(k): 2.132838887656121
""",
)

entry(
    index = 291,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO",
    kinetics = ArrheniusBM(A=(1.50003e+07,'m^3/(mol*s)'), n=-0.067291, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0022865824899212348, var=0.07749524453431202, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO
    Total Standard Deviation in ln(k): 0.5638226853346819"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO
Total Standard Deviation in ln(k): 0.5638226853346819""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO
Total Standard Deviation in ln(k): 0.5638226853346819
""",
)

entry(
    index = 292,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(5.749e+06,'m^3/(mol*s)'), n=0.214, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-4R!H-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
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
    index = 293,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=1.33725e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 294,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.51e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_N-4R!H->C
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
    index = 295,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_Sp-3C-1C_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(8.41487e+08,'m^3/(mol*s)'), n=-0.692606, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4860153208082551, var=0.496261552627412, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_Sp-3C-1C_Ext-2CF-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_Sp-3C-1C_Ext-2CF-R
    Total Standard Deviation in ln(k): 2.633396366652887"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_Sp-3C-1C_Ext-2CF-R
Total Standard Deviation in ln(k): 2.633396366652887""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_Sp-3C-1C_Ext-2CF-R
Total Standard Deviation in ln(k): 2.633396366652887
""",
)

entry(
    index = 296,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_Sp-3C#1C",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(700,'K'), Tmax=(1300,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_Sp-3C#1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_Sp-3C#1C
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
    index = 297,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_N-Sp-3C#1C",
    kinetics = ArrheniusBM(A=(7.23e+07,'m^3/(mol*s)'), n=7.56255e-09, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_N-Sp-3C#1C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_N-Sp-3C#1C
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_N-Sp-3C#1C
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_N-Sp-3C#1C
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 298,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.7313e+28,'m^3/(mol*s)'), n=-7.39166, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3166437141272633, var=29.409938906357223, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.667452211938421"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R
Total Standard Deviation in ln(k): 11.667452211938421""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R
Total Standard Deviation in ln(k): 11.667452211938421
""",
)

entry(
    index = 299,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.74e+37,'m^3/(mol*s)'), n=-10.5, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-2C-R
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
    index = 300,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_N-Sp-4C-2C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.4e+28,'m^3/(mol*s)'), n=-7.11, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_N-Sp-4C-2C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_N-Sp-4C-2C_Ext-4C-R
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
    index = 301,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.79114e+07,'m^3/(mol*s)'), n=0.21356, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00020750907699414265, var=0.015290320301034535, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 0.24841496044277087"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.24841496044277087""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 0.24841496044277087
""",
)

entry(
    index = 302,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(2.591e+07,'m^3/(mol*s)'), n=0.217, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
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
    index = 303,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(3.203e+07,'m^3/(mol*s)'), n=0.214, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_Sp-4C-3C_Ext-4C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R_Ext-11R!H-R
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
    index = 304,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.25e+08,'m^3/(mol*s)'), n=-0.119, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_4R!H->C_Sp-3C-2C_N-Sp-4C=3C_N-Sp-4C-3C_Ext-4C-R
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
    index = 305,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(1.9799e+06,'m^3/(mol*s)'), n=8.70341e-09, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 306,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(3.16153e+11,'m^3/(mol*s)'), n=-1.54858, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1332670387271525, var=0.8642583208512438, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R
    Total Standard Deviation in ln(k): 2.198553688369586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R
Total Standard Deviation in ln(k): 2.198553688369586""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R
Total Standard Deviation in ln(k): 2.198553688369586
""",
)

entry(
    index = 307,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.24e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-1C-R
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
    index = 308,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R_Ext-2CF-R_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(0.00243875,'m^3/(mol*s)'), n=2.77174, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R_Ext-2CF-R_Ext-2CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_3BrCClINOPSSi->Cl_Ext-2CF-R_Ext-1C-R_Ext-1C-R_Ext-2CF-R_Ext-2CF-R
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
    index = 309,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_5R!H->O_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_5R!H->O_Ext-2CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_5R!H->O_Ext-2CF-R
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
    index = 310,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(2.26848e+08,'m^3/(mol*s)'), n=-0.55, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.305460834090209e-17, var=0.18719384195212638, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O_Ext-2CF-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O_Ext-2CF-R
    Total Standard Deviation in ln(k): 0.8673667472246991"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O_Ext-2CF-R
Total Standard Deviation in ln(k): 0.8673667472246991""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O_Ext-2CF-R
Total Standard Deviation in ln(k): 0.8673667472246991
""",
)

entry(
    index = 311,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.39195e+11,'m^3/(mol*s)'), n=-0.855542, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9125875942573384, var=1.0150541438967988, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 4.312702149012238"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.312702149012238""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.312702149012238
""",
)

entry(
    index = 312,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.24e+08,'m^3/(mol*s)'), n=-0.75, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-1C-R
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
    index = 313,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.14759e+09,'m^3/(mol*s)'), n=-1.3, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=5.519561616726178, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R_Ext-1C-R
    Total Standard Deviation in ln(k): 4.70987392894025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.70987392894025""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.70987392894025
""",
)

entry(
    index = 314,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.98065e+08,'m^3/(mol*s)'), n=-0.75, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.305460834090209e-17, var=0.8575717470917588, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.8564883221612534"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.8564883221612534""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.8564883221612534
""",
)

entry(
    index = 315,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF_5R!H-inRing",
    kinetics = ArrheniusBM(A=(3.144e+13,'m^3/(mol*s)'), n=-2.163, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF_5R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF_5R!H-inRing
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
    index = 316,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF_N-5R!H-inRing",
    kinetics = ArrheniusBM(A=(1.307e+06,'m^3/(mol*s)'), n=0.192, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF_N-5R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-5R!H-2CF_N-5R!H-inRing
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
    index = 317,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-4R!H=3BrBrCCOO_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.02e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-4R!H=3BrBrCCOO_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_Sp-4R!H=3BrBrCCOO_Ext-5R!H-R
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
    index = 318,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO",
    kinetics = ArrheniusBM(A=(2.17712e+06,'m^3/(mol*s)'), n=0.213828, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0001742051180227286, var=0.09909663657032189, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO
    Total Standard Deviation in ln(k): 0.6315206507602252"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO
Total Standard Deviation in ln(k): 0.6315206507602252""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO
Total Standard Deviation in ln(k): 0.6315206507602252
""",
)

entry(
    index = 319,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO",
    kinetics = ArrheniusBM(A=(8.05579e+10,'m^3/(mol*s)'), n=-1.31825, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04628379485594601, var=0.016181722463235428, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO
    Total Standard Deviation in ln(k): 0.3713080775392354"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO
Total Standard Deviation in ln(k): 0.3713080775392354""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO
Total Standard Deviation in ln(k): 0.3713080775392354
""",
)

entry(
    index = 320,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C_Sp-4C-2CF",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C_Sp-4C-2CF',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C_Sp-4C-2CF
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
    index = 321,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C_N-Sp-4C-2CF",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C_N-Sp-4C-2CF',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_3CO->O_Ext-2CF-R_4R!H->C_N-Sp-4C-2CF
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
    index = 322,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(7.23e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_N-3BrCO->Br_N-3CO->O_N-Sp-3C-1C_N-Sp-3C#1C_Ext-2CF-R
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
    index = 323,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(5.06317e+29,'m^3/(mol*s)'), n=-7.6173, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.2910520355351487, var=10.734133404524984, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 14.837085962822576"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R_Ext-2C-R
Total Standard Deviation in ln(k): 14.837085962822576""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R_Ext-2C-R
Total Standard Deviation in ln(k): 14.837085962822576
""",
)

entry(
    index = 324,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(2.67335e+07,'m^3/(mol*s)'), n=0.213107, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004025751725425149, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 0.010114954083982785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.010114954083982785""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.010114954083982785
""",
)

entry(
    index = 325,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(2.591e+07,'m^3/(mol*s)'), n=0.217, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-11R!H-R
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
    index = 326,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R_6R!H->Cl",
    kinetics = ArrheniusBM(A=(2.8e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R_6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R_6R!H->Cl
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
    index = 327,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(1.4e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R_N-6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_5R!H->Cl_Ext-2CF-R_Ext-2CF-R_N-6R!H->Cl
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
    index = 328,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_5BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(8.91091e+09,'m^3/(mol*s)'), n=-1.08236, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0315988796402227, var=11.501395669676128, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_5BrCFINOPSSi->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_5BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 9.390756918241319"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 9.390756918241319""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 9.390756918241319
""",
)

entry(
    index = 329,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_N-5BrCFINOPSSi->Br",
    kinetics = ArrheniusBM(A=(1.12169e+13,'m^3/(mol*s)'), n=-2.01479, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.877006741979527, var=2.9584856719683473e-05, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_N-5BrCFINOPSSi->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_N-5BrCFINOPSSi->Br
    Total Standard Deviation in ln(k): 4.727001489333314"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_N-5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 4.727001489333314""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_N-5BrCFINOPSSi->Br
Total Standard Deviation in ln(k): 4.727001489333314
""",
)

entry(
    index = 330,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O_Ext-2CF-R_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(7.75e+08,'m^3/(mol*s)'), n=-0.75, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O_Ext-2CF-R_Ext-2CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_3BrCO->O_Ext-2CF-R_N-5R!H->O_Ext-2CF-R_Ext-2CF-R
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
    index = 331,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.045e+09,'m^3/(mol*s)'), n=-0.155, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-5R!H-R_Ext-5R!H-R_Ext-1C-R
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
    index = 332,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R_Ext-1C-R_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(1.24e+10,'m^3/(mol*s)'), n=-1.5, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R_Ext-1C-R_Ext-2CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_N-3BrCO->O_Ext-2CF-R_Ext-2CF-R_Ext-1C-R_Ext-2CF-R
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
    index = 333,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(2.04234e+06,'m^3/(mol*s)'), n=0.213743, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00019021667646345916, var=0.06095973860643739, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 0.49544754407416924"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 0.49544754407416924""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 0.49544754407416924
""",
)

entry(
    index = 334,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO_3BrCO-inRing",
    kinetics = ArrheniusBM(A=(5.781e+11,'m^3/(mol*s)'), n=-1.568, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO_3BrCO-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO_3BrCO-inRing
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
    index = 335,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO_N-3BrCO-inRing",
    kinetics = ArrheniusBM(A=(5.89e+07,'m^3/(mol*s)'), n=-0.278, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO_N-3BrCO-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_N-Sp-4R!H-3BrCO_N-3BrCO-inRing
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
    index = 336,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R_Ext-2C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.12e+41,'m^3/(mol*s)'), n=-10.8, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R_Ext-2C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_N-5CF->C_Sp-4C-2C_Ext-4C-R_Ext-2C-R_Ext-4C-R
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
    index = 337,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(2.591e+07,'m^3/(mol*s)'), n=0.217, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R
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
    index = 338,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_5BrCFINOPSSi->Br_Ext-2CF-R",
    kinetics = ArrheniusBM(A=(2.8e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_5BrCFINOPSSi->Br_Ext-2CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_5BrCFINOPSSi->Br_Ext-2CF-R
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
    index = 339,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_N-5BrCFINOPSSi->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.61e+20,'m^3/(mol*s)'), n=-4.16, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_N-5BrCFINOPSSi->Br_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_Ext-2CF-R_N-4R!H->O_4BrCClF->F_Ext-1C-R_N-5R!H->Cl_Ext-2CF-R_N-5BrCFINOPSSi->Br_Ext-1C-R
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
    index = 340,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.91473e+06,'m^3/(mol*s)'), n=0.213499, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00028436440044365876, var=0.015202055385746795, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 0.24789153336992423"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.24789153336992423""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.24789153336992423
""",
)

entry(
    index = 341,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(3.406e+06,'m^3/(mol*s)'), n=0.211, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-9R!H-R_Ext-10R!H-R
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
    index = 342,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.83408e+06,'m^3/(mol*s)'), n=0.21354, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00013833948832008065, var=0.00954512479524206, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.1962085087655991"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.1962085087655991""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.1962085087655991
""",
)

entry(
    index = 343,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(1.918e+06,'m^3/(mol*s)'), n=0.213, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-9R!H-R_Ext-10R!H-R
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
    index = 344,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R",
    kinetics = ArrheniusBM(A=(1.7321e+06,'m^3/(mol*s)'), n=0.213053, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.002012875862712629, var=0.0027626568967285335, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R
    Total Standard Deviation in ln(k): 0.11042832265502614"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.11042832265502614""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R
Total Standard Deviation in ln(k): 0.11042832265502614
""",
)

entry(
    index = 345,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.942e+06,'m^3/(mol*s)'), n=0.212, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-9R!H-R
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
    index = 346,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.674e+06,'m^3/(mol*s)'), n=0.22, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_N-Sp-3BrBrCCOO=1C_Ext-2CF-R_N-Sp-4R!H=3BrBrCCOO_Sp-4R!H-3BrCO_Ext-4R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-5R!H-R_Ext-10R!H-R_Ext-9R!H-R
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
    index = 347,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R",
    kinetics = ArrheniusBM(A=(2.591e+07,'m^3/(mol*s)'), n=0.217, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_Ext-2C-R_N-3C-inRing_Ext-3C-R_Ext-5R!H-R_Ext-6R!H-R_Ext-7R!H-R_Ext-8R!H-R_Ext-4R!H-R_Ext-10R!H-R_Ext-11R!H-R
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

