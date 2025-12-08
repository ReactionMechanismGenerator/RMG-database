#!/usr/bin/env python
# encoding: utf-8

name = "XY_Addition_MultipleBond/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = Arrhenius(A=(2.66085e-10,'m^3/(mol*s)'), n=4.42669, Ea=(171.978,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=5.17718088334744, var=64.29424290288505, Tref=1000.0, N=66, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 66 training reactions at node Root
    Total Standard Deviation in ln(k): 29.08269795235811"""),
    rank = 11,
    shortDesc = """BM rule fitted to 66 training reactions at node Root
Total Standard Deviation in ln(k): 29.08269795235811""",
    longDesc = 
"""
BM rule fitted to 66 training reactions at node Root
Total Standard Deviation in ln(k): 29.08269795235811
""",
)

entry(
    index = 2,
    label = "Root_2Br1sCl1sF1sH->H",
    kinetics = Arrhenius(A=(1.58276e-34,'m^3/(mol*s)'), n=11.4288, Ea=(151.279,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=9.627361891216246e-15, var=73.86978362074643, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H',), comment="""BM rule fitted to 20 training reactions at node Root_2Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 17.230203344256445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 17.230203344256445""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 17.230203344256445
""",
)

entry(
    index = 3,
    label = "Root_N-2Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(2.34181e-49,'m^3/(mol*s)'), n=15.614, w0=(767.707,'kJ/mol'), E0=(160.653,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.329971394019945, var=99.55227592072644, Tref=1000.0, N=46, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H',), comment="""BM rule fitted to 46 training reactions at node Root_N-2Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 23.34405868836938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 46 training reactions at node Root_N-2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 23.34405868836938""",
    longDesc = 
"""
BM rule fitted to 46 training reactions at node Root_N-2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 23.34405868836938
""",
)

entry(
    index = 4,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(2.56491e-54,'m^3/(mol*s)'), n=17.2499, w0=(804.929,'kJ/mol'), E0=(232.03,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.34070283932394124, var=24.258338167424263, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H',), comment="""BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 10.729909726667325"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 10.729909726667325""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 10.729909726667325
""",
)

entry(
    index = 5,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H",
    kinetics = Arrhenius(A=(1.01944e-25,'m^3/(mol*s)'), n=8.82369, Ea=(127.055,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=7.336451189568094e-15, var=19.193810893548754, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H',), comment="""BM rule fitted to 13 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 8.782893067668489"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 8.782893067668489""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 8.782893067668489
""",
)

entry(
    index = 6,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(5.51822e-53,'m^3/(mol*s)'), n=16.6302, w0=(869.553,'kJ/mol'), E0=(169.181,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7083651002462804, var=37.065324004281756, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 19 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 13.984899100150429"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 13.984899100150429""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 13.984899100150429
""",
)

entry(
    index = 7,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(2.72446e-07,'m^3/(mol*s)'), n=3.69681, w0=(696.037,'kJ/mol'), E0=(164.04,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5840965038370373, var=49.78909613958656, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 27 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 15.61326831397871"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 15.61326831397871""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 15.61326831397871
""",
)

entry(
    index = 8,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO",
    kinetics = ArrheniusBM(A=(2.16169e-58,'m^3/(mol*s)'), n=18.3254, w0=(871.5,'kJ/mol'), E0=(178.067,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3005390143336583, var=0.5722610548789053, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO
    Total Standard Deviation in ln(k): 2.2716639033342605"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 2.2716639033342605""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 2.2716639033342605
""",
)

entry(
    index = 9,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO",
    kinetics = ArrheniusBM(A=(2.44373e-45,'m^3/(mol*s)'), n=14.7462, w0=(755,'kJ/mol'), E0=(287.452,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5484638781943013, var=0.7807952012916518, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO',), comment="""BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO
    Total Standard Deviation in ln(k): 3.149486315554056"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 3.149486315554056""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 3.149486315554056
""",
)

entry(
    index = 10,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(5.75359e-41,'m^3/(mol*s)'), n=13.2365, w0=(858.5,'kJ/mol'), E0=(164.219,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1490622822498411, var=11.382008028677225, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 7.137949527939906"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 7.137949527939906""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 7.137949527939906
""",
)

entry(
    index = 11,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO",
    kinetics = ArrheniusBM(A=(9.61534e-20,'m^3/(mol*s)'), n=7.04295, w0=(975,'kJ/mol'), E0=(125.351,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12989841910502997, var=3.93417305952061, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO',), comment="""BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO
    Total Standard Deviation in ln(k): 4.302719836945651"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 4.302719836945651""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 4.302719836945651
""",
)

entry(
    index = 12,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO",
    kinetics = Arrhenius(A=(2.4889e-27,'m^3/(mol*s)'), n=9.43559, Ea=(127.721,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(2.21303e-53,'m^3/(mol*s)'), n=16.7362, w0=(857.542,'kJ/mol'), E0=(174.562,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.28328393174102057, var=9.437676734380057, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 6.870475603420472"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 6.870475603420472""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 6.870475603420472
""",
)

entry(
    index = 14,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct",
    kinetics = Arrhenius(A=(2.57016e+31,'m^3/(mol*s)'), n=-7.53001, Ea=(301.787,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(7.70013e-06,'m^3/(mol*s)'), n=3.26447, w0=(897.333,'kJ/mol'), E0=(176.857,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.7032922249873015, var=129.1552801218569, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 27.062742129353744"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 27.062742129353744""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 27.062742129353744
""",
)

entry(
    index = 16,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->Cl1s",
    kinetics = Arrhenius(A=(5.93272e-05,'m^3/(mol*s)'), n=2.63647, Ea=(84.7124,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s",
    kinetics = ArrheniusBM(A=(2.51173e-07,'m^3/(mol*s)'), n=3.71207, w0=(700.692,'kJ/mol'), E0=(164.286,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5919032312946797, var=50.79754729939995, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s',), comment="""BM rule fitted to 26 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s
    Total Standard Deviation in ln(k): 15.77542169920086"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 15.77542169920086""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 15.77542169920086
""",
)

entry(
    index = 18,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R",
    kinetics = ArrheniusBM(A=(4.84146e-59,'m^3/(mol*s)'), n=18.4551, w0=(871.5,'kJ/mol'), E0=(175.569,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2651877928800578, var=0.19494373659085024, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R
    Total Standard Deviation in ln(k): 1.5514403049326069"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R
Total Standard Deviation in ln(k): 1.5514403049326069""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R
Total Standard Deviation in ln(k): 1.5514403049326069
""",
)

entry(
    index = 19,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(7.32081e-41,'m^3/(mol*s)'), n=13.4035, w0=(755,'kJ/mol'), E0=(294.076,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6193762006569704, var=1.0840861330627762, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 3.6435408870101225"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 3.6435408870101225""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 3.6435408870101225
""",
)

entry(
    index = 20,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O",
    kinetics = ArrheniusBM(A=(1.06346e-35,'m^3/(mol*s)'), n=11.6908, w0=(858.5,'kJ/mol'), E0=(184.107,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05246974797050451, var=5.70403113214179, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O
    Total Standard Deviation in ln(k): 4.919765088282759"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O
Total Standard Deviation in ln(k): 4.919765088282759""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O
Total Standard Deviation in ln(k): 4.919765088282759
""",
)

entry(
    index = 21,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(1.55859e-82,'m^3/(mol*s)'), n=25.2195, w0=(858.5,'kJ/mol'), E0=(23.9269,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03283016705375803, var=76.10005297221957, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O
    Total Standard Deviation in ln(k): 17.570863329988207"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O
Total Standard Deviation in ln(k): 17.570863329988207""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O
Total Standard Deviation in ln(k): 17.570863329988207
""",
)

entry(
    index = 22,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R",
    kinetics = ArrheniusBM(A=(3.34094e-20,'m^3/(mol*s)'), n=7.15481, w0=(975,'kJ/mol'), E0=(126.31,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16807303343309712, var=3.7715255209217733, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R',), comment="""BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R
    Total Standard Deviation in ln(k): 4.3155729426351055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R
Total Standard Deviation in ln(k): 4.3155729426351055""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R
Total Standard Deviation in ln(k): 4.3155729426351055
""",
)

entry(
    index = 23,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(4.0685e-55,'m^3/(mol*s)'), n=17.2305, w0=(858.5,'kJ/mol'), E0=(172.883,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.01704719917875508, var=2.580288728089482, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 3.2630936748615724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 3.2630936748615724""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 3.2630936748615724
""",
)

entry(
    index = 24,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2029.19,'m^3/(mol*s)'), n=0.783867, w0=(852.75,'kJ/mol'), E0=(253.649,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.1266096188749666, var=30.766180113607938, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C
    Total Standard Deviation in ln(k): 18.975521190110026"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 18.975521190110026""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 18.975521190110026
""",
)

entry(
    index = 25,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(116.28,'m^3/(mol*s)'), n=1.10103, w0=(858.5,'kJ/mol'), E0=(260.264,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.4680390735472137, var=12.956441585601166, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C
    Total Standard Deviation in ln(k): 10.904595807762536"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.904595807762536""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.904595807762536
""",
)

entry(
    index = 26,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3COCdO2d->O2d",
    kinetics = ArrheniusBM(A=(7.21206e-08,'m^3/(mol*s)'), n=3.97622, w0=(975,'kJ/mol'), E0=(139.614,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.001394183593143, var=42.86692184236784, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3COCdO2d->O2d',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3COCdO2d->O2d
    Total Standard Deviation in ln(k): 23.179323218074966"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3COCdO2d->O2d
Total Standard Deviation in ln(k): 23.179323218074966""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3COCdO2d->O2d
Total Standard Deviation in ln(k): 23.179323218074966
""",
)

entry(
    index = 27,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d",
    kinetics = ArrheniusBM(A=(172.262,'m^3/(mol*s)'), n=0.99909, w0=(858.5,'kJ/mol'), E0=(234.51,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3350239751821102, var=9.480573374181999, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d',), comment="""BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d
    Total Standard Deviation in ln(k): 9.527019102599679"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d
Total Standard Deviation in ln(k): 9.527019102599679""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d
Total Standard Deviation in ln(k): 9.527019102599679
""",
)

entry(
    index = 28,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(0.415805,'m^3/(mol*s)'), n=1.80819, w0=(693,'kJ/mol'), E0=(204.05,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20328043161425546, var=13.653670461277366, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 18 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 7.918426060832425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 7.918426060832425""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 7.918426060832425
""",
)

entry(
    index = 29,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(2.05493e-44,'m^3/(mol*s)'), n=14.5196, w0=(718,'kJ/mol'), E0=(15.6242,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.3213944144642626, var=33.14536920495731, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 8 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 17.374313093503392"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 17.374313093503392""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 17.374313093503392
""",
)

entry(
    index = 30,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-5R!H-R",
    kinetics = Arrhenius(A=(1.61903e-58,'m^3/(mol*s)'), n=18.2608, Ea=(143.651,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R_5R!H->C",
    kinetics = Arrhenius(A=(2.00663e-58,'m^3/(mol*s)'), n=18.5017, Ea=(200.636,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(9.47816e-32,'m^3/(mol*s)'), n=10.7595, w0=(755,'kJ/mol'), E0=(312.585,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7795006201817322, var=0.012783944609339975, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C
    Total Standard Deviation in ln(k): 2.1852118630878326"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 2.1852118630878326""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 2.1852118630878326
""",
)

entry(
    index = 33,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(5.2637e-32,'m^3/(mol*s)'), n=10.6207, w0=(858.5,'kJ/mol'), E0=(200.708,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07231417844374075, var=1.428253691825844, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 2.5775441524923206"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.5775441524923206""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.5775441524923206
""",
)

entry(
    index = 34,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O_Ext-3COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(1.88854e-35,'m^3/(mol*s)'), n=11.7495, Ea=(119.448,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R",
    kinetics = ArrheniusBM(A=(2.02968e-21,'m^3/(mol*s)'), n=7.50324, w0=(975,'kJ/mol'), E0=(128.369,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18916385317036347, var=1.1216457973901264, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R',), comment="""BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R
    Total Standard Deviation in ln(k): 2.598456488943158"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R
Total Standard Deviation in ln(k): 2.598456488943158""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R
Total Standard Deviation in ln(k): 2.598456488943158
""",
)

entry(
    index = 36,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(3.42844e-55,'m^3/(mol*s)'), n=17.252, w0=(858.5,'kJ/mol'), E0=(172.854,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0011682825208951698, var=2.2459770539733976, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 3.0073484829026387"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 3.0073484829026387""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 3.0073484829026387
""",
)

entry(
    index = 37,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_3COCdCddCtO2d->Ct",
    kinetics = Arrhenius(A=(3.60487e+39,'m^3/(mol*s)'), n=-9.93467, Ea=(299.5,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_N-3COCdCddCtO2d->Ct",
    kinetics = Arrhenius(A=(3.14941,'m^3/(mol*s)'), n=1.63113, Ea=(223.345,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_N-3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_N-3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(125.266,'m^3/(mol*s)'), n=1.1096, w0=(858.5,'kJ/mol'), E0=(261.872,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.2421826978977215, var=22.54268793370237, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 15.151934732275484"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 15.151934732275484""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 15.151934732275484
""",
)

entry(
    index = 40,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3COCdO2d->O2d_4COCdCddCtO2d->CO",
    kinetics = Arrhenius(A=(0.140494,'m^3/(mol*s)'), n=1.80918, Ea=(156.088,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3COCdO2d->O2d_4COCdCddCtO2d->CO',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3COCdO2d->O2d_4COCdCddCtO2d->CO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3COCdO2d->O2d_4COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3COCdO2d->O2d_4COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3COCdO2d->O2d_N-4COCdCddCtO2d->CO",
    kinetics = Arrhenius(A=(7.80335e-09,'m^3/(mol*s)'), n=4.28272, Ea=(163.976,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3COCdO2d->O2d_N-4COCdCddCtO2d->CO',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3COCdO2d->O2d_N-4COCdCddCtO2d->CO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3COCdO2d->O2d_N-4COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3COCdO2d->O2d_N-4COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(186.02,'m^3/(mol*s)'), n=0.98704, w0=(858.5,'kJ/mol'), E0=(235.96,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.6430744841632048, var=11.605667867550023, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 10.957877367936758"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 10.957877367936758""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 10.957877367936758
""",
)

entry(
    index = 43,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(12854.2,'m^3/(mol*s)'), n=0.363006, w0=(711,'kJ/mol'), E0=(209.858,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13092432644114357, var=2.1888464166628343, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 3.2949111182562563"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 3.2949111182562563""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 3.2949111182562563
""",
)

entry(
    index = 44,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.00593305,'m^3/(mol*s)'), n=2.39407, w0=(657,'kJ/mol'), E0=(201.372,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20958359086901834, var=23.18946922170064, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 10.180482993984567"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 10.180482993984567""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 10.180482993984567
""",
)

entry(
    index = 45,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.90089e-47,'m^3/(mol*s)'), n=15.3086, w0=(720.833,'kJ/mol'), E0=(11.3747,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-6.410500481119907, var=107.12537872953199, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 36.856071974220036"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 36.856071974220036""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 36.856071974220036
""",
)

entry(
    index = 46,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.05566e-40,'m^3/(mol*s)'), n=13.4925, w0=(709.5,'kJ/mol'), E0=(6.36963,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-15.393784087985992, var=629.3077567938155, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 88.96864803513684"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 88.96864803513684""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 88.96864803513684
""",
)

entry(
    index = 47,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C_Ext-5BrClFILiNOPSSi-R_Ext-6R!H-R",
    kinetics = Arrhenius(A=(5.27052e-32,'m^3/(mol*s)'), n=10.824, Ea=(269.603,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C_Ext-5BrClFILiNOPSSi-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C_Ext-5BrClFILiNOPSSi-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C_Ext-5BrClFILiNOPSSi-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C_Ext-5BrClFILiNOPSSi-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C",
    kinetics = ArrheniusBM(A=(4.7072e-32,'m^3/(mol*s)'), n=10.6641, w0=(858.5,'kJ/mol'), E0=(205.722,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10150844521884211, var=0.9739776605707088, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C
    Total Standard Deviation in ln(k): 2.2335255380421013"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C
Total Standard Deviation in ln(k): 2.2335255380421013""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C
Total Standard Deviation in ln(k): 2.2335255380421013
""",
)

entry(
    index = 49,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_N-8R!H->C",
    kinetics = Arrhenius(A=(2.426e-34,'m^3/(mol*s)'), n=11.2313, Ea=(114.264,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.49261e-22,'m^3/(mol*s)'), n=7.74939, w0=(975,'kJ/mol'), E0=(127.998,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23781498123293465, var=0.7957877089024799, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C
    Total Standard Deviation in ln(k): 2.3858877775647116"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C
Total Standard Deviation in ln(k): 2.3858877775647116""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C
Total Standard Deviation in ln(k): 2.3858877775647116
""",
)

entry(
    index = 51,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_N-5R!H->C",
    kinetics = Arrhenius(A=(7.07779e-19,'m^3/(mol*s)'), n=6.81918, Ea=(114.076,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.09202e-56,'m^3/(mol*s)'), n=17.6793, w0=(858.5,'kJ/mol'), E0=(169.885,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13746040734589024, var=0.14567077168718653, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C
    Total Standard Deviation in ln(k): 1.1105219481600654"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C
Total Standard Deviation in ln(k): 1.1105219481600654""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C
Total Standard Deviation in ln(k): 1.1105219481600654
""",
)

entry(
    index = 53,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(126612,'m^3/(mol*s)'), n=0.247242, w0=(858.5,'kJ/mol'), E0=(289.294,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.72738913614625, var=96.91886788825437, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C
    Total Standard Deviation in ln(k): 31.613953910344684"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C
Total Standard Deviation in ln(k): 31.613953910344684""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C
Total Standard Deviation in ln(k): 31.613953910344684
""",
)

entry(
    index = 54,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F",
    kinetics = ArrheniusBM(A=(8.19921,'m^3/(mol*s)'), n=1.36893, w0=(858.5,'kJ/mol'), E0=(229.331,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04845398419745801, var=1.7251977549760897, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F
    Total Standard Deviation in ln(k): 2.754898721807251"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F
Total Standard Deviation in ln(k): 2.754898721807251""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F
Total Standard Deviation in ln(k): 2.754898721807251
""",
)

entry(
    index = 55,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_N-6R!H->F",
    kinetics = Arrhenius(A=(4.49727,'m^3/(mol*s)'), n=1.54397, Ea=(243.066,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_N-6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_N-6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F",
    kinetics = ArrheniusBM(A=(6.06161,'m^3/(mol*s)'), n=1.35437, w0=(858.5,'kJ/mol'), E0=(211.118,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03509149546505698, var=2.4739257353497903, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F
    Total Standard Deviation in ln(k): 3.241360879314931"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F
Total Standard Deviation in ln(k): 3.241360879314931""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F
Total Standard Deviation in ln(k): 3.241360879314931
""",
)

entry(
    index = 57,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d_Ext-4COCdCddCtO2d-R_N-5R!H->F",
    kinetics = Arrhenius(A=(24.851,'m^3/(mol*s)'), n=1.25249, Ea=(211.863,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d_Ext-4COCdCddCtO2d-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d_Ext-4COCdCddCtO2d-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d_Ext-4COCdCddCtO2d-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d_Ext-4COCdCddCtO2d-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(513.492,'m^3/(mol*s)'), n=0.745456, w0=(711,'kJ/mol'), E0=(208.015,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1766347080322537, var=3.301652160772779, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R
    Total Standard Deviation in ln(k): 4.086499442979435"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 4.086499442979435""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 4.086499442979435
""",
)

entry(
    index = 59,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(3.25796e+07,'m^3/(mol*s)'), n=-0.707939, w0=(711,'kJ/mol'), E0=(214.596,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12884402549098264, var=0.8149612978683681, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 2.1335074459390224"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.1335074459390224""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.1335074459390224
""",
)

entry(
    index = 60,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(0.00284365,'m^3/(mol*s)'), n=2.5143, w0=(657,'kJ/mol'), E0=(210.075,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27209888994523385, var=35.40550311300031, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R
    Total Standard Deviation in ln(k): 12.612345172222435"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 12.612345172222435""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 12.612345172222435
""",
)

entry(
    index = 61,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(7.85783,'m^3/(mol*s)'), n=1.416, Ea=(147.447,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3COCtO2d-R",
    kinetics = ArrheniusBM(A=(23.9499,'m^3/(mol*s)'), n=1.57664, w0=(699.5,'kJ/mol'), E0=(220.022,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11479703517839808, var=2.2200481478296994, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3COCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3COCtO2d-R
    Total Standard Deviation in ln(k): 3.275455144363436"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3COCtO2d-R
Total Standard Deviation in ln(k): 3.275455144363436""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3COCtO2d-R
Total Standard Deviation in ln(k): 3.275455144363436
""",
)

entry(
    index = 63,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(6.69408e-21,'m^3/(mol*s)'), n=7.80396, w0=(763.5,'kJ/mol'), E0=(85.9259,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-9.156993870339482, var=216.45440634323984, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 52.501965695382246"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 52.501965695382246""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 52.501965695382246
""",
)

entry(
    index = 64,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_3COCtO2d->O2d",
    kinetics = Arrhenius(A=(2.01929e-06,'m^3/(mol*s)'), n=3.68936, Ea=(144.378,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_3COCtO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_3COCtO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_3COCtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_3COCtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_N-3COCtO2d->O2d",
    kinetics = Arrhenius(A=(2e+06,'m^3/(mol*s)'), n=0, Ea=(215.016,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_N-3COCtO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_N-3COCtO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_N-3COCtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_N-3COCtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = Arrhenius(A=(6.67386e-32,'m^3/(mol*s)'), n=10.6691, Ea=(147.163,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = Arrhenius(A=(3.32008e-32,'m^3/(mol*s)'), n=10.6591, Ea=(146.583,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.98352e-22,'m^3/(mol*s)'), n=7.78209, w0=(975,'kJ/mol'), E0=(129.888,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2546709907188669, var=1.7441814625704168, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 3.28747960573028"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 3.28747960573028""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 3.28747960573028
""",
)

entry(
    index = 69,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(2.10439e-22,'m^3/(mol*s)'), n=7.76191, Ea=(106.982,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(8.98638e-58,'m^3/(mol*s)'), n=17.983, Ea=(122.1,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(1.12577e-55,'m^3/(mol*s)'), n=17.3962, Ea=(123.325,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFILiNOPSSi->F",
    kinetics = ArrheniusBM(A=(295240,'m^3/(mol*s)'), n=-0.046278, w0=(858.5,'kJ/mol'), E0=(228.949,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03209867194432285, var=38.44228536620481, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFILiNOPSSi->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFILiNOPSSi->F
    Total Standard Deviation in ln(k): 12.510376884005279"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFILiNOPSSi->F
Total Standard Deviation in ln(k): 12.510376884005279""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFILiNOPSSi->F
Total Standard Deviation in ln(k): 12.510376884005279
""",
)

entry(
    index = 73,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFILiNOPSSi->F",
    kinetics = Arrhenius(A=(12.1292,'m^3/(mol*s)'), n=1.44664, Ea=(264.847,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFILiNOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFILiNOPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFILiNOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFILiNOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(4.45749,'m^3/(mol*s)'), n=1.21594, Ea=(156.783,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(14.8208,'m^3/(mol*s)'), n=1.21604, Ea=(156.314,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3COCdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(24407.9,'m^3/(mol*s)'), n=0.242664, w0=(711,'kJ/mol'), E0=(208.95,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15340235221657536, var=3.4199113511921317, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl
    Total Standard Deviation in ln(k): 4.092790091183226"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl
Total Standard Deviation in ln(k): 4.092790091183226""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl
Total Standard Deviation in ln(k): 4.092790091183226
""",
)

entry(
    index = 77,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->Cl",
    kinetics = Arrhenius(A=(1.10391,'m^3/(mol*s)'), n=1.64361, Ea=(158.18,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 78,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(1.25612e+07,'m^3/(mol*s)'), n=-0.637747, Ea=(189.45,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->Cl",
    kinetics = Arrhenius(A=(1.6085e+08,'m^3/(mol*s)'), n=-0.88707, Ea=(183.065,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->Cl",
    kinetics = Arrhenius(A=(8.97967e+06,'m^3/(mol*s)'), n=-0.518739, Ea=(177.993,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 81,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->C",
    kinetics = Arrhenius(A=(1.18878,'m^3/(mol*s)'), n=1.76475, Ea=(147.997,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.215891,'m^3/(mol*s)'), n=1.97486, w0=(657,'kJ/mol'), E0=(231.46,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15132296425913053, var=27.931225295587012, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C
    Total Standard Deviation in ln(k): 10.975233393002227"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.975233393002227""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.975233393002227
""",
)

entry(
    index = 83,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3COCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(40.7026,'m^3/(mol*s)'), n=1.65435, Ea=(156.402,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3COCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3COCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3COCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3COCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_3COCtO2d->O2d",
    kinetics = Arrhenius(A=(1.09358e-06,'m^3/(mol*s)'), n=3.74071, Ea=(154.488,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_3COCtO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_3COCtO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_3COCtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_3COCtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-3COCtO2d->O2d",
    kinetics = Arrhenius(A=(1.62705,'m^3/(mol*s)'), n=1.85266, Ea=(155.861,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-3COCtO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-3COCtO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-3COCtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-3COCtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(1.62324e-22,'m^3/(mol*s)'), n=7.83496, Ea=(133.074,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 87,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(1.13304e-22,'m^3/(mol*s)'), n=7.82383, Ea=(109.166,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFILiNOPSSi->F_Ext-4COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(22.8223,'m^3/(mol*s)'), n=1.20947, Ea=(130.798,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFILiNOPSSi->F_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFILiNOPSSi->F_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFILiNOPSSi->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFILiNOPSSi->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(25761.1,'m^3/(mol*s)'), n=0.211095, w0=(711,'kJ/mol'), E0=(206.552,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1695122615051351, var=13.23696793291396, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
    Total Standard Deviation in ln(k): 7.719666492712838"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
Total Standard Deviation in ln(k): 7.719666492712838""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
Total Standard Deviation in ln(k): 7.719666492712838
""",
)

entry(
    index = 90,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(5.59096e+06,'m^3/(mol*s)'), n=-0.339093, Ea=(194.905,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(0.825331,'m^3/(mol*s)'), n=1.69758, Ea=(158.663,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R",
    kinetics = Arrhenius(A=(3.63667,'m^3/(mol*s)'), n=1.59996, Ea=(202.541,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(4061.16,'m^3/(mol*s)'), n=0.468605, w0=(711,'kJ/mol'), E0=(200.462,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18985986566823584, var=36.55501394603801, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 12.597811986024771"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.597811986024771""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.597811986024771
""",
)

entry(
    index = 94,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(0.0823032,'m^3/(mol*s)'), n=1.92336, Ea=(190.49,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

