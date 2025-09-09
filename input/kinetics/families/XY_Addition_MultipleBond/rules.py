#!/usr/bin/env python
# encoding: utf-8

name = "XY_Addition_MultipleBond/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = Arrhenius(A=(2.66085e-10,'m^3/(mol*s)'), n=4.42669, Ea=(171.978,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=5.177180883347416, var=64.2942429028851, Tref=1000.0, N=66, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 66 training reactions at node Root
    Total Standard Deviation in ln(k): 29.082697952358057"""),
    rank = 11,
    shortDesc = """BM rule fitted to 66 training reactions at node Root
Total Standard Deviation in ln(k): 29.082697952358057""",
    longDesc = 
"""
BM rule fitted to 66 training reactions at node Root
Total Standard Deviation in ln(k): 29.082697952358057
""",
)

entry(
    index = 2,
    label = "Root_2Br1sCl1sF1sH->H",
    kinetics = Arrhenius(A=(1.58276e-34,'m^3/(mol*s)'), n=11.4288, Ea=(151.279,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-2.433833076237378e-14, var=73.86978362074643, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H',), comment="""BM rule fitted to 20 training reactions at node Root_2Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 17.23020334425648"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 17.23020334425648""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 17.23020334425648
""",
)

entry(
    index = 3,
    label = "Root_N-2Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(2.29731e-49,'m^3/(mol*s)'), n=15.6164, w0=(767707,'J/mol'), E0=(160625,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.776128097485711, var=93.06426975247493, Tref=1000.0, N=46, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H',), comment="""BM rule fitted to 46 training reactions at node Root_N-2Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 21.289714638913296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 46 training reactions at node Root_N-2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 21.289714638913296""",
    longDesc = 
"""
BM rule fitted to 46 training reactions at node Root_N-2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 21.289714638913296
""",
)

entry(
    index = 4,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(2.55941e-54,'m^3/(mol*s)'), n=17.2502, w0=(804929,'J/mol'), E0=(232017,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3419709132277998, var=24.257662275855292, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H',), comment="""BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 10.732958286958103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 10.732958286958103""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 10.732958286958103
""",
)

entry(
    index = 5,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H",
    kinetics = Arrhenius(A=(1.01944e-25,'m^3/(mol*s)'), n=8.82369, Ea=(127.055,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-1.1350735802727993e-14, var=19.193810893548722, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H',), comment="""BM rule fitted to 13 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 8.78289306766849"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 8.78289306766849""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 8.78289306766849
""",
)

entry(
    index = 6,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(5.49061e-53,'m^3/(mol*s)'), n=16.6308, w0=(869553,'J/mol'), E0=(169169,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7091922133371322, var=37.065192968051534, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 19 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 13.986955699537232"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 13.986955699537232""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 13.986955699537232
""",
)

entry(
    index = 7,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(2.70098e-07,'m^3/(mol*s)'), n=3.69788, w0=(696037,'J/mol'), E0=(164022,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.583173144059783, var=49.78818623704376, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 27 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 15.610819056745607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 15.610819056745607""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 15.610819056745607
""",
)

entry(
    index = 8,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO",
    kinetics = ArrheniusBM(A=(2.16168e-58,'m^3/(mol*s)'), n=18.3254, w0=(871500,'J/mol'), E0=(178059,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.30150717791373915, var=0.572260816471435, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO
    Total Standard Deviation in ln(k): 2.27409615924338"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 2.27409615924338""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 2.27409615924338
""",
)

entry(
    index = 9,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO",
    kinetics = ArrheniusBM(A=(2.44327e-45,'m^3/(mol*s)'), n=14.7463, w0=(755000,'J/mol'), E0=(287438,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5500741645599186, var=0.7809346105465462, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO',), comment="""BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO
    Total Standard Deviation in ln(k): 3.153690397159337"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 3.153690397159337""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 3.153690397159337
""",
)

entry(
    index = 10,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(5.68921e-41,'m^3/(mol*s)'), n=13.2379, w0=(858500,'J/mol'), E0=(164199,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14839032529504767, var=11.381004502841146, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 7.13596302955658"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 7.13596302955658""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 7.13596302955658
""",
)

entry(
    index = 11,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO",
    kinetics = ArrheniusBM(A=(9.61531e-20,'m^3/(mol*s)'), n=7.04295, w0=(975000,'J/mol'), E0=(125345,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12913964844953596, var=3.93412042983633, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO',), comment="""BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO
    Total Standard Deviation in ln(k): 4.300786781022806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 4.300786781022806""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO
Total Standard Deviation in ln(k): 4.300786781022806
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
    kinetics = ArrheniusBM(A=(2.21233e-53,'m^3/(mol*s)'), n=16.7363, w0=(857542,'J/mol'), E0=(174555,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.28418931474287284, var=9.437735642130228, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 6.872769655650794"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 6.872769655650794""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 6.872769655650794
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
    kinetics = ArrheniusBM(A=(7.68088e-06,'m^3/(mol*s)'), n=3.26479, w0=(897333,'J/mol'), E0=(176845,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.702093691457001, var=129.1504194178612, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 27.05930201815207"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 27.05930201815207""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 27.05930201815207
""",
)

entry(
    index = 16,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(2.48825e-07,'m^3/(mol*s)'), n=3.71324, w0=(700692,'J/mol'), E0=(164267,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5909819726164884, var=50.79667488715543, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H',), comment="""BM rule fitted to 26 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 15.772984283233153"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 15.772984283233153""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 15.772984283233153
""",
)

entry(
    index = 17,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->H",
    kinetics = Arrhenius(A=(5.93272e-05,'m^3/(mol*s)'), n=2.63647, Ea=(84.7124,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R",
    kinetics = ArrheniusBM(A=(4.84146e-59,'m^3/(mol*s)'), n=18.4551, w0=(871500,'J/mol'), E0=(175560,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2651877928800594, var=0.19494373659092754, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R
    Total Standard Deviation in ln(k): 1.5514403049327863"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R
Total Standard Deviation in ln(k): 1.5514403049327863""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R
Total Standard Deviation in ln(k): 1.5514403049327863
""",
)

entry(
    index = 19,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(7.31994e-41,'m^3/(mol*s)'), n=13.4035, w0=(755000,'J/mol'), E0=(294061,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6210607838912646, var=1.08436214708499, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 3.648039212514916"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 3.648039212514916""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 3.648039212514916
""",
)

entry(
    index = 20,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O",
    kinetics = ArrheniusBM(A=(1.06063e-35,'m^3/(mol*s)'), n=11.6912, w0=(858500,'J/mol'), E0=(184096,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05338025195509204, var=5.703798020542565, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O
    Total Standard Deviation in ln(k): 4.921954949456289"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O
Total Standard Deviation in ln(k): 4.921954949456289""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O
Total Standard Deviation in ln(k): 4.921954949456289
""",
)

entry(
    index = 21,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(1.55859e-82,'m^3/(mol*s)'), n=25.2195, w0=(858500,'J/mol'), E0=(23926.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.032830167053758935, var=76.10005297221991, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O
    Total Standard Deviation in ln(k): 17.57086332998825"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O
Total Standard Deviation in ln(k): 17.57086332998825""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O
Total Standard Deviation in ln(k): 17.57086332998825
""",
)

entry(
    index = 22,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R",
    kinetics = ArrheniusBM(A=(3.34132e-20,'m^3/(mol*s)'), n=7.15479, w0=(975000,'J/mol'), E0=(126304,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16729852927301286, var=3.7714662648604422, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R',), comment="""BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R
    Total Standard Deviation in ln(k): 4.313596367672544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R
Total Standard Deviation in ln(k): 4.313596367672544""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R
Total Standard Deviation in ln(k): 4.313596367672544
""",
)

entry(
    index = 23,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(4.06843e-55,'m^3/(mol*s)'), n=17.2306, w0=(858500,'J/mol'), E0=(172876,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.017928336298055, var=2.580312030864462, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 3.265322128396655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 3.265322128396655""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 3.265322128396655
""",
)

entry(
    index = 24,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2028.12,'m^3/(mol*s)'), n=0.783933, w0=(852750,'J/mol'), E0=(253636,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.12660961887496, var=30.76618011360791, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C
    Total Standard Deviation in ln(k): 18.97552119011"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 18.97552119011""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 18.97552119011
""",
)

entry(
    index = 25,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(116.28,'m^3/(mol*s)'), n=1.10103, w0=(858500,'J/mol'), E0=(260251,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.4694708621506753, var=12.95537356936, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C
    Total Standard Deviation in ln(k): 10.907895846044102"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.907895846044102""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.907895846044102
""",
)

entry(
    index = 26,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d",
    kinetics = ArrheniusBM(A=(7.21367e-08,'m^3/(mol*s)'), n=3.97619, w0=(975000,'J/mol'), E0=(139605,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.001394183593169, var=42.86692184236834, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d
    Total Standard Deviation in ln(k): 23.17932321807511"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d
Total Standard Deviation in ln(k): 23.17932321807511""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d
Total Standard Deviation in ln(k): 23.17932321807511
""",
)

entry(
    index = 27,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d",
    kinetics = ArrheniusBM(A=(172.244,'m^3/(mol*s)'), n=0.999103, w0=(858500,'J/mol'), E0=(234498,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3362714967298155, var=9.479739799398276, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d',), comment="""BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d
    Total Standard Deviation in ln(k): 9.52988220761784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d
Total Standard Deviation in ln(k): 9.52988220761784""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d
Total Standard Deviation in ln(k): 9.52988220761784
""",
)

entry(
    index = 28,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(0.415543,'m^3/(mol*s)'), n=1.80827, w0=(693000,'J/mol'), E0=(204040,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20214638918965114, var=13.653478284966177, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 18 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 7.915524576093228"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 7.915524576093228""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 7.915524576093228
""",
)

entry(
    index = 29,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(2.06103e-44,'m^3/(mol*s)'), n=14.5192, w0=(718000,'J/mol'), E0=(1892.65,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.044514733206631, var=26.021507954036544, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 8 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 12.85081932582483"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 12.85081932582483""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 12.85081932582483
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
    kinetics = ArrheniusBM(A=(9.47816e-32,'m^3/(mol*s)'), n=10.7595, w0=(755000,'J/mol'), E0=(312570,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7795006201817324, var=0.012783944609335606, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C
    Total Standard Deviation in ln(k): 2.1852118630877944"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 2.1852118630877944""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->CO_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 2.1852118630877944
""",
)

entry(
    index = 33,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(5.26393e-32,'m^3/(mol*s)'), n=10.6207, w0=(858500,'J/mol'), E0=(200700,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07325318566393946, var=1.4281556375112925, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 2.5798212242040894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.5798212242040894""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.5798212242040894
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
    kinetics = ArrheniusBM(A=(2.02975e-21,'m^3/(mol*s)'), n=7.50323, w0=(975000,'J/mol'), E0=(128362,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18836928851633822, var=1.1216069408431177, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R',), comment="""BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R
    Total Standard Deviation in ln(k): 2.596423319119747"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R
Total Standard Deviation in ln(k): 2.596423319119747""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R
Total Standard Deviation in ln(k): 2.596423319119747
""",
)

entry(
    index = 36,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(3.42843e-55,'m^3/(mol*s)'), n=17.252, w0=(858500,'J/mol'), E0=(172847,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.002048662997994005, var=2.2460000058244503, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 3.0095758453026313"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 3.0095758453026313""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 3.0095758453026313
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
    kinetics = ArrheniusBM(A=(125.263,'m^3/(mol*s)'), n=1.1096, w0=(858500,'J/mol'), E0=(261859,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.2434896643647657, var=22.540240245490487, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 15.1547018038831"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 15.1547018038831""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 15.1547018038831
""",
)

entry(
    index = 40,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d_4COCdCddCtO2d->Cdd",
    kinetics = Arrhenius(A=(7.80335e-09,'m^3/(mol*s)'), n=4.28272, Ea=(163.976,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d_4COCdCddCtO2d->Cdd',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d_4COCdCddCtO2d->Cdd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d_4COCdCddCtO2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d_4COCdCddCtO2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d_N-4COCdCddCtO2d->Cdd",
    kinetics = Arrhenius(A=(0.140494,'m^3/(mol*s)'), n=1.80918, Ea=(156.088,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d_N-4COCdCddCtO2d->Cdd',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d_N-4COCdCddCtO2d->Cdd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d_N-4COCdCddCtO2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d_N-4COCdCddCtO2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(186.019,'m^3/(mol*s)'), n=0.987041, w0=(858500,'J/mol'), E0=(235948,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.6442454709320684, var=11.604313393790788, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 10.960421002741601"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 10.960421002741601""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 10.960421002741601
""",
)

entry(
    index = 43,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s",
    kinetics = ArrheniusBM(A=(0.00592533,'m^3/(mol*s)'), n=2.39423, w0=(657000,'J/mol'), E0=(201361,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20848739251088036, var=23.189029544171778, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s
    Total Standard Deviation in ln(k): 10.177637206351216"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 10.177637206351216""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 10.177637206351216
""",
)

entry(
    index = 44,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s",
    kinetics = ArrheniusBM(A=(12849.8,'m^3/(mol*s)'), n=0.363048, w0=(711000,'J/mol'), E0=(209847,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12971139412637492, var=2.188831054056839, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s',), comment="""BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s
    Total Standard Deviation in ln(k): 3.291853141201519"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 3.291853141201519""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 3.291853141201519
""",
)

entry(
    index = 45,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s",
    kinetics = ArrheniusBM(A=(1.05919e-40,'m^3/(mol*s)'), n=13.4921, w0=(709500,'J/mol'), E0=(10127.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-15.393784087985996, var=629.3077567938158, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s
    Total Standard Deviation in ln(k): 88.96864803513688"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 88.96864803513688""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 88.96864803513688
""",
)

entry(
    index = 46,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s",
    kinetics = ArrheniusBM(A=(2.90863e-47,'m^3/(mol*s)'), n=15.3082, w0=(720833,'J/mol'), E0=(4173.97,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-6.409555724783433, var=107.11497533304308, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s
    Total Standard Deviation in ln(k): 36.85269066482179"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 36.85269066482179""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s
Total Standard Deviation in ln(k): 36.85269066482179
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
    kinetics = ArrheniusBM(A=(4.7072e-32,'m^3/(mol*s)'), n=10.6641, w0=(858500,'J/mol'), E0=(205713,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10150844521883515, var=0.9739776605708645, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C
    Total Standard Deviation in ln(k): 2.233525538042242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C
Total Standard Deviation in ln(k): 2.233525538042242""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C
Total Standard Deviation in ln(k): 2.233525538042242
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
    kinetics = ArrheniusBM(A=(2.49268e-22,'m^3/(mol*s)'), n=7.74939, w0=(975000,'J/mol'), E0=(127992,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23701716010230015, var=0.7957009094345755, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C
    Total Standard Deviation in ln(k): 2.38378566757876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C
Total Standard Deviation in ln(k): 2.38378566757876""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C
Total Standard Deviation in ln(k): 2.38378566757876
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
    kinetics = ArrheniusBM(A=(1.09202e-56,'m^3/(mol*s)'), n=17.6793, w0=(858500,'J/mol'), E0=(169878,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13746040734588855, var=0.14567077168711792, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C
    Total Standard Deviation in ln(k): 1.110521948159881"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C
Total Standard Deviation in ln(k): 1.110521948159881""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C
Total Standard Deviation in ln(k): 1.110521948159881
""",
)

entry(
    index = 53,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(126843,'m^3/(mol*s)'), n=0.247015, w0=(858500,'J/mol'), E0=(289282,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.72867174806555, var=96.91116406985284, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C
    Total Standard Deviation in ln(k): 31.616392153520902"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C
Total Standard Deviation in ln(k): 31.616392153520902""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C
Total Standard Deviation in ln(k): 31.616392153520902
""",
)

entry(
    index = 54,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F",
    kinetics = ArrheniusBM(A=(8.1965,'m^3/(mol*s)'), n=1.36897, w0=(858500,'J/mol'), E0=(229320,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0484539841974599, var=1.7251977549763002, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F
    Total Standard Deviation in ln(k): 2.7548987218074164"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F
Total Standard Deviation in ln(k): 2.7548987218074164""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F
Total Standard Deviation in ln(k): 2.7548987218074164
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
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F",
    kinetics = ArrheniusBM(A=(6.05949,'m^3/(mol*s)'), n=1.35441, w0=(858500,'J/mol'), E0=(211109,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.035091495465056806, var=2.4739257353495345, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F
    Total Standard Deviation in ln(k): 3.241360879314767"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F
Total Standard Deviation in ln(k): 3.241360879314767""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F
Total Standard Deviation in ln(k): 3.241360879314767
""",
)

entry(
    index = 57,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_N-5R!H->F",
    kinetics = Arrhenius(A=(24.851,'m^3/(mol*s)'), n=1.25249, Ea=(211.863,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(0.00283925,'m^3/(mol*s)'), n=2.51449, w0=(657000,'J/mol'), E0=(210064,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27094505688514514, var=35.404389327176666, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R
    Total Standard Deviation in ln(k): 12.609258466587763"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 12.609258466587763""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 12.609258466587763
""",
)

entry(
    index = 59,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(7.85783,'m^3/(mol*s)'), n=1.416, Ea=(147.447,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(513.268,'m^3/(mol*s)'), n=0.74551, w0=(711000,'J/mol'), E0=(208005,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1754343593671949, var=3.30161023799614, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R
    Total Standard Deviation in ln(k): 4.083460364908345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 4.083460364908345""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 4.083460364908345
""",
)

entry(
    index = 61,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(3.258e+07,'m^3/(mol*s)'), n=-0.70794, w0=(711000,'J/mol'), E0=(214585,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12758931895869616, var=0.8149349892841977, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 2.1303257050851063"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.1303257050851063""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.1303257050851063
""",
)

entry(
    index = 62,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_3CtO2d->Ct",
    kinetics = Arrhenius(A=(2e+06,'m^3/(mol*s)'), n=0, Ea=(215.016,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_3CtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_3CtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_3CtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_3CtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_N-3CtO2d->Ct",
    kinetics = Arrhenius(A=(2.01929e-06,'m^3/(mol*s)'), n=3.68936, Ea=(144.378,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_N-3CtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_N-3CtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_N-3CtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_N-3CtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3CtO2d-R",
    kinetics = ArrheniusBM(A=(23.9497,'m^3/(mol*s)'), n=1.57664, w0=(699500,'J/mol'), E0=(220012,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11479703517840006, var=2.220048147829475, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3CtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3CtO2d-R
    Total Standard Deviation in ln(k): 3.27545514436329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3CtO2d-R
Total Standard Deviation in ln(k): 3.27545514436329""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3CtO2d-R
Total Standard Deviation in ln(k): 3.27545514436329
""",
)

entry(
    index = 65,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(2.04335e-42,'m^3/(mol*s)'), n=13.9684, w0=(763500,'J/mol'), E0=(15674,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-9.156993870339496, var=216.4544063432408, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 52.501965695382346"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 52.501965695382346""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 52.501965695382346
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
    kinetics = ArrheniusBM(A=(1.98356e-22,'m^3/(mol*s)'), n=7.78208, w0=(975000,'J/mol'), E0=(129881,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2546709907188625, var=1.7441814625705805, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 3.287479605730393"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 3.287479605730393""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->CO_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 3.287479605730393
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
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFILiNOPSSi->Br",
    kinetics = Arrhenius(A=(12.1292,'m^3/(mol*s)'), n=1.44664, Ea=(264.847,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFILiNOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFILiNOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFILiNOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFILiNOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFILiNOPSSi->Br",
    kinetics = ArrheniusBM(A=(295295,'m^3/(mol*s)'), n=-0.0463018, w0=(858500,'J/mol'), E0=(228940,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03209867194431734, var=38.44228536620417, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFILiNOPSSi->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFILiNOPSSi->Br
    Total Standard Deviation in ln(k): 12.510376884005163"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFILiNOPSSi->Br
Total Standard Deviation in ln(k): 12.510376884005163""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFILiNOPSSi->Br
Total Standard Deviation in ln(k): 12.510376884005163
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
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(14.8208,'m^3/(mol*s)'), n=1.21604, Ea=(156.314,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->C",
    kinetics = Arrhenius(A=(1.18878,'m^3/(mol*s)'), n=1.76475, Ea=(147.997,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 77,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.215821,'m^3/(mol*s)'), n=1.9749, w0=(657000,'J/mol'), E0=(231449,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15004193440222224, var=27.930040792529482, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C
    Total Standard Deviation in ln(k): 10.971790066553416"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.971790066553416""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.971790066553416
""",
)

entry(
    index = 78,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(24407.2,'m^3/(mol*s)'), n=0.242668, w0=(711000,'J/mol'), E0=(208940,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15215549666227554, var=3.4198574863954065, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl
    Total Standard Deviation in ln(k): 4.089628092084674"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl
Total Standard Deviation in ln(k): 4.089628092084674""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl
Total Standard Deviation in ln(k): 4.089628092084674
""",
)

entry(
    index = 79,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->Cl",
    kinetics = Arrhenius(A=(1.10391,'m^3/(mol*s)'), n=1.64361, Ea=(158.18,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(1.25612e+07,'m^3/(mol*s)'), n=-0.637747, Ea=(189.45,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 81,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_5R!H->C",
    kinetics = Arrhenius(A=(8.97967e+06,'m^3/(mol*s)'), n=-0.518739, Ea=(177.993,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_N-5R!H->C",
    kinetics = Arrhenius(A=(1.6085e+08,'m^3/(mol*s)'), n=-0.88707, Ea=(183.065,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(40.7026,'m^3/(mol*s)'), n=1.65435, Ea=(156.402,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_3CtO2d->Ct",
    kinetics = Arrhenius(A=(1.62705,'m^3/(mol*s)'), n=1.85266, Ea=(155.861,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_3CtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_3CtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_3CtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_3CtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_N-3CtO2d->Ct",
    kinetics = Arrhenius(A=(1.09358e-06,'m^3/(mol*s)'), n=3.74071, Ea=(154.488,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_N-3CtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_N-3CtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_N-3CtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-4COCdCddCtO2d-R_N-3CtO2d->Ct
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
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFILiNOPSSi->Br_Ext-4COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(22.8223,'m^3/(mol*s)'), n=1.20947, Ea=(130.798,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFILiNOPSSi->Br_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFILiNOPSSi->Br_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFILiNOPSSi->Br_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFILiNOPSSi->Br_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(0.825331,'m^3/(mol*s)'), n=1.69758, Ea=(158.663,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R",
    kinetics = Arrhenius(A=(3.63667,'m^3/(mol*s)'), n=1.59996, Ea=(202.541,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_2Br1sCl1s->Br1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(25761.7,'m^3/(mol*s)'), n=0.211092, w0=(711000,'J/mol'), E0=(206541,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16826880344622785, var=13.236564613316231, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
    Total Standard Deviation in ln(k): 7.716431107989357"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
Total Standard Deviation in ln(k): 7.716431107989357""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
Total Standard Deviation in ln(k): 7.716431107989357
""",
)

entry(
    index = 92,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(5.59096e+06,'m^3/(mol*s)'), n=-0.339093, Ea=(194.905,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(4061.36,'m^3/(mol*s)'), n=0.468599, w0=(711000,'J/mol'), E0=(200452,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18985986566821483, var=36.55501394603883, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 12.597811986024855"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.597811986024855""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.597811986024855
""",
)

entry(
    index = 94,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(0.0823032,'m^3/(mol*s)'), n=1.92336, Ea=(190.49,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Br1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

