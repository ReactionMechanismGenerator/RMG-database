#!/usr/bin/env python
# encoding: utf-8

name = "Cation_NO_Substitution/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusChargeTransfer(A=(0.339735,'m^3/(mol*s)'), n=2.63972, Ea=(71.3307,'kJ/mol'), V0=(0,'V'), alpha=0.0277778, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=3.823952153053182e-15, var=9.193633917678232, Tref=1000.0, N=18, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 18 training reactions at node Root
    Total Standard Deviation in ln(k): 6.078558387753341"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root
Total Standard Deviation in ln(k): 6.078558387753341""",
    longDesc =
"""
BM rule fitted to 18 training reactions at node Root
Total Standard Deviation in ln(k): 6.078558387753341
""",
)

entry(
    index = 2,
    label = "Root_1NO->O",
    kinetics = ArrheniusChargeTransfer(A=(1.30887,'m^3/(mol*s)'), n=2.52389, Ea=(51.775,'kJ/mol'), V0=(0,'V'), alpha=0.0625, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=-2.249383619443048e-16, var=2.336282225810139, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1NO->O',), comment="""BM rule fitted to 8 training reactions at node Root_1NO->O
    Total Standard Deviation in ln(k): 3.0642178763170635"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1NO->O
Total Standard Deviation in ln(k): 3.0642178763170635""",
    longDesc =
"""
BM rule fitted to 8 training reactions at node Root_1NO->O
Total Standard Deviation in ln(k): 3.0642178763170635
""",
)

entry(
    index = 3,
    label = "Root_N-1NO->O",
    kinetics = ArrheniusChargeTransfer(A=(0.115488,'m^3/(mol*s)'), n=2.73237, Ea=(86.9753,'kJ/mol'), V0=(0,'V'), alpha=0.05, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=-7.422965944162058e-16, var=0.7852653031721386, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1NO->O',), comment="""BM rule fitted to 10 training reactions at node Root_N-1NO->O
    Total Standard Deviation in ln(k): 1.7764999259866798"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1NO->O
Total Standard Deviation in ln(k): 1.7764999259866798""",
    longDesc =
"""
BM rule fitted to 10 training reactions at node Root_N-1NO->O
Total Standard Deviation in ln(k): 1.7764999259866798
""",
)

entry(
    index = 4,
    label = "Root_1NO->O_Ext-3R-R",
    kinetics = ArrheniusChargeTransfer(A=(0.731943,'m^3/(mol*s)'), n=2.46517, Ea=(51.9321,'kJ/mol'), V0=(0,'V'), alpha=0.25, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=14.899976043759057, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1NO->O_Ext-3R-R',), comment="""BM rule fitted to 2 training reactions at node Root_1NO->O_Ext-3R-R
    Total Standard Deviation in ln(k): 7.738375049435379"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1NO->O_Ext-3R-R
Total Standard Deviation in ln(k): 7.738375049435379""",
    longDesc =
"""
BM rule fitted to 2 training reactions at node Root_1NO->O_Ext-3R-R
Total Standard Deviation in ln(k): 7.738375049435379
""",
)

entry(
    index = 5,
    label = "Root_1NO->O_3R->C",
    kinetics = ArrheniusChargeTransfer(A=(0.0537704,'m^3/(mol*s)'), n=2.99372, Ea=(52.8544,'kJ/mol'), V0=(0,'V'), alpha=0.166667, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=2.249383619443048e-16, var=0.6252581610901395, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1NO->O_3R->C',), comment="""BM rule fitted to 3 training reactions at node Root_1NO->O_3R->C
    Total Standard Deviation in ln(k): 1.585209527596837"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1NO->O_3R->C
Total Standard Deviation in ln(k): 1.585209527596837""",
    longDesc =
"""
BM rule fitted to 3 training reactions at node Root_1NO->O_3R->C
Total Standard Deviation in ln(k): 1.585209527596837
""",
)

entry(
    index = 6,
    label = "Root_1NO->O_N-3R->C",
    kinetics = ArrheniusChargeTransfer(A=(46.9384,'m^3/(mol*s)'), n=2.09322, Ea=(50.5908,'kJ/mol'), V0=(0,'V'), alpha=0.166667, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=2.249383619443048e-16, var=5.090793804312459, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1NO->O_N-3R->C',), comment="""BM rule fitted to 3 training reactions at node Root_1NO->O_N-3R->C
    Total Standard Deviation in ln(k): 4.5232411574409275"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1NO->O_N-3R->C
Total Standard Deviation in ln(k): 4.5232411574409275""",
    longDesc =
"""
BM rule fitted to 3 training reactions at node Root_1NO->O_N-3R->C
Total Standard Deviation in ln(k): 4.5232411574409275
""",
)

entry(
    index = 7,
    label = "Root_N-1NO->O_Ext-2R-R",
    kinetics = ArrheniusChargeTransfer(A=(0.3923,'m^3/(mol*s)'), n=2.66478, Ea=(99.8333,'kJ/mol'), V0=(0,'V'), alpha=0.25, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=2.81172952430381e-16, var=0.8047578317736759, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1NO->O_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1NO->O_Ext-2R-R
    Total Standard Deviation in ln(k): 1.7984136712681347"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1NO->O_Ext-2R-R
Total Standard Deviation in ln(k): 1.7984136712681347""",
    longDesc =
"""
BM rule fitted to 2 training reactions at node Root_N-1NO->O_Ext-2R-R
Total Standard Deviation in ln(k): 1.7984136712681347
""",
)

entry(
    index = 8,
    label = "Root_N-1NO->O_2R->C",
    kinetics = ArrheniusChargeTransfer(A=(0.873751,'m^3/(mol*s)'), n=2.65999, Ea=(93.4166,'kJ/mol'), V0=(0,'V'), alpha=0.166667, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=-7.497945398143493e-16, var=0.9378755998816197, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1NO->O_2R->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1NO->O_2R->C
    Total Standard Deviation in ln(k): 1.9414651894386081"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1NO->O_2R->C
Total Standard Deviation in ln(k): 1.9414651894386081""",
    longDesc =
"""
BM rule fitted to 3 training reactions at node Root_N-1NO->O_2R->C
Total Standard Deviation in ln(k): 1.9414651894386081
""",
)

entry(
    index = 9,
    label = "Root_N-1NO->O_N-2R->C",
    kinetics = ArrheniusChargeTransfer(A=(0.0210276,'m^3/(mol*s)'), n=2.80284, Ea=(77.9672,'kJ/mol'), V0=(0,'V'), alpha=0.1, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=2.5642973261650746e-15, var=0.65182806422055, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1NO->O_N-2R->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1NO->O_N-2R->C
    Total Standard Deviation in ln(k): 1.618540298175747"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1NO->O_N-2R->C
Total Standard Deviation in ln(k): 1.618540298175747""",
    longDesc =
"""
BM rule fitted to 5 training reactions at node Root_N-1NO->O_N-2R->C
Total Standard Deviation in ln(k): 1.618540298175747
""",
)

entry(
    index = 10,
    label = "Root_1NO->O_Ext-3R-R_2R->C",
    kinetics = ArrheniusChargeTransferBM(A=(0.137812,'m^3/(mol*s)'), n=2.70251, w0=(349800,'J/mol'), E0=(34980,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1NO->O_Ext-3R-R_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1NO->O_Ext-3R-R_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1NO->O_Ext-3R-R_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_1NO->O_Ext-3R-R_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_1NO->O_Ext-3R-R_N-2R->C",
    kinetics = ArrheniusChargeTransferBM(A=(3.88747,'m^3/(mol*s)'), n=2.22783, w0=(400300,'J/mol'), E0=(40030,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1NO->O_Ext-3R-R_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1NO->O_Ext-3R-R_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1NO->O_Ext-3R-R_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_1NO->O_Ext-3R-R_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_1NO->O_3R->C_2R->C",
    kinetics = ArrheniusChargeTransfer(A=(0.00621408,'m^3/(mol*s)'), n=3.375, Ea=(58.8965,'kJ/mol'), V0=(0,'V'), alpha=0.25, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=1.6870377145822858e-16, var=0.7135037538998786, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1NO->O_3R->C_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_1NO->O_3R->C_2R->C
    Total Standard Deviation in ln(k): 1.6933827077834618"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1NO->O_3R->C_2R->C
Total Standard Deviation in ln(k): 1.6933827077834618""",
    longDesc =
"""
BM rule fitted to 2 training reactions at node Root_1NO->O_3R->C_2R->C
Total Standard Deviation in ln(k): 1.6933827077834618
""",
)

entry(
    index = 13,
    label = "Root_1NO->O_3R->C_N-2R->C",
    kinetics = ArrheniusChargeTransferBM(A=(4.02602,'m^3/(mol*s)'), n=2.23116, w0=(400300,'J/mol'), E0=(40030,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1NO->O_3R->C_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1NO->O_3R->C_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1NO->O_3R->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_1NO->O_3R->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_1NO->O_N-3R->C_2R->C",
    kinetics = ArrheniusChargeTransfer(A=(9.68195,'m^3/(mol*s)'), n=2.46198, Ea=(51.4641,'kJ/mol'), V0=(0,'V'), alpha=0.25, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=8.435188572911429e-17, var=0.19634980008381608, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1NO->O_N-3R->C_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_1NO->O_N-3R->C_2R->C
    Total Standard Deviation in ln(k): 0.8883256884075514"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1NO->O_N-3R->C_2R->C
Total Standard Deviation in ln(k): 0.8883256884075514""",
    longDesc =
"""
BM rule fitted to 2 training reactions at node Root_1NO->O_N-3R->C_2R->C
Total Standard Deviation in ln(k): 0.8883256884075514
""",
)

entry(
    index = 15,
    label = "Root_1NO->O_N-3R->C_N-2R->C",
    kinetics = ArrheniusChargeTransferBM(A=(1103.21,'m^3/(mol*s)'), n=1.35569, w0=(400300,'J/mol'), E0=(40030,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1NO->O_N-3R->C_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1NO->O_N-3R->C_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1NO->O_N-3R->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_1NO->O_N-3R->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-1NO->O_Ext-2R-R_Ext-1N-R",
    kinetics = ArrheniusChargeTransferBM(A=(117.529,'m^3/(mol*s)'), n=2.07905, w0=(303700,'J/mol'), E0=(30370,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1NO->O_Ext-2R-R_Ext-1N-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-2R-R_Ext-1N-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-2R-R_Ext-1N-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_N-1NO->O_Ext-2R-R_Ext-1N-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-1NO->O_2R->C_Ext-1N-R",
    kinetics = ArrheniusChargeTransfer(A=(2.17011,'m^3/(mol*s)'), n=2.5453, Ea=(97.3379,'kJ/mol'), V0=(0,'V'), alpha=0.25, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=2.81172952430381e-17, var=0.32578247857116904, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1NO->O_2R->C_Ext-1N-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1NO->O_2R->C_Ext-1N-R
    Total Standard Deviation in ln(k): 1.1442498152233505"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1NO->O_2R->C_Ext-1N-R
Total Standard Deviation in ln(k): 1.1442498152233505""",
    longDesc =
"""
BM rule fitted to 2 training reactions at node Root_N-1NO->O_2R->C_Ext-1N-R
Total Standard Deviation in ln(k): 1.1442498152233505
""",
)

entry(
    index = 18,
    label = "Root_N-1NO->O_N-2R->C_3R->H",
    kinetics = ArrheniusChargeTransfer(A=(0.0395507,'m^3/(mol*s)'), n=2.73403, Ea=(82.3125,'kJ/mol'), V0=(0,'V'), alpha=0.166667, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=-6.748150858329144e-16, var=0.700188362203178, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1NO->O_N-2R->C_3R->H',), comment="""BM rule fitted to 3 training reactions at node Root_N-1NO->O_N-2R->C_3R->H
    Total Standard Deviation in ln(k): 1.6775073567792615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1NO->O_N-2R->C_3R->H
Total Standard Deviation in ln(k): 1.6775073567792615""",
    longDesc =
"""
BM rule fitted to 3 training reactions at node Root_N-1NO->O_N-2R->C_3R->H
Total Standard Deviation in ln(k): 1.6775073567792615
""",
)

entry(
    index = 19,
    label = "Root_N-1NO->O_N-2R->C_N-3R->H",
    kinetics = ArrheniusChargeTransfer(A=(0.00815164,'m^3/(mol*s)'), n=2.90606, Ea=(71.4493,'kJ/mol'), V0=(0,'V'), alpha=0.25, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=-2.81172952430381e-16, var=0.16223107893088848, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1NO->O_N-2R->C_N-3R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1NO->O_N-2R->C_N-3R->H
    Total Standard Deviation in ln(k): 0.8074655781874773"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1NO->O_N-2R->C_N-3R->H
Total Standard Deviation in ln(k): 0.8074655781874773""",
    longDesc =
"""
BM rule fitted to 2 training reactions at node Root_N-1NO->O_N-2R->C_N-3R->H
Total Standard Deviation in ln(k): 0.8074655781874773
""",
)

entry(
    index = 20,
    label = "Root_1NO->O_3R->C_2R->C_Ext-2C-R",
    kinetics = ArrheniusChargeTransferBM(A=(0.000236033,'m^3/(mol*s)'), n=3.84908, w0=(349800,'J/mol'), E0=(34980,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1NO->O_3R->C_2R->C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1NO->O_3R->C_2R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1NO->O_3R->C_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_1NO->O_3R->C_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_1NO->O_N-3R->C_2R->C_Ext-2C-R",
    kinetics = ArrheniusChargeTransferBM(A=(0.609636,'m^3/(mol*s)'), n=2.90468, w0=(349800,'J/mol'), E0=(34980,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1NO->O_N-3R->C_2R->C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1NO->O_N-3R->C_2R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1NO->O_N-3R->C_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_1NO->O_N-3R->C_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-1NO->O_2R->C_Ext-1N-R_Ext-5R!H-R",
    kinetics = ArrheniusChargeTransferBM(A=(1.61257,'m^3/(mol*s)'), n=2.55041, w0=(303700,'J/mol'), E0=(30370,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1NO->O_2R->C_Ext-1N-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1NO->O_2R->C_Ext-1N-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1NO->O_2R->C_Ext-1N-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_N-1NO->O_2R->C_Ext-1N-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-1NO->O_N-2R->C_3R->H_Ext-1N-R",
    kinetics = ArrheniusChargeTransfer(A=(0.00998483,'m^3/(mol*s)'), n=2.88005, Ea=(79.901,'kJ/mol'), V0=(0,'V'), alpha=0.25, electrons=1, T0=(1,'K'), uncertainty=RateUncertainty(mu=1.124691809721524e-16, var=2.344383112979754, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1NO->O_N-2R->C_3R->H_Ext-1N-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1NO->O_N-2R->C_3R->H_Ext-1N-R
    Total Standard Deviation in ln(k): 3.069525754438298"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1NO->O_N-2R->C_3R->H_Ext-1N-R
Total Standard Deviation in ln(k): 3.069525754438298""",
    longDesc =
"""
BM rule fitted to 2 training reactions at node Root_N-1NO->O_N-2R->C_3R->H_Ext-1N-R
Total Standard Deviation in ln(k): 3.069525754438298
""",
)

entry(
    index = 24,
    label = "Root_N-1NO->O_N-2R->C_N-3R->H_Ext-3C-R",
    kinetics = ArrheniusChargeTransferBM(A=(0.00331961,'m^3/(mol*s)'), n=3.0459, w0=(344200,'J/mol'), E0=(34420,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1NO->O_N-2R->C_N-3R->H_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1NO->O_N-2R->C_N-3R->H_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1NO->O_N-2R->C_N-3R->H_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_N-1NO->O_N-2R->C_N-3R->H_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-1NO->O_N-2R->C_3R->H_Ext-1N-R_Ext-5R!H-R",
    kinetics = ArrheniusChargeTransferBM(A=(0.00225166,'m^3/(mol*s)'), n=2.99604, w0=(344200,'J/mol'), E0=(34420,'J/mol'), V0=(0,'V'), alpha=0.5, electrons=0, Tmin=(300,'K'), Tmax=(3000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1NO->O_N-2R->C_3R->H_Ext-1N-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1NO->O_N-2R->C_3R->H_Ext-1N-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1NO->O_N-2R->C_3R->H_Ext-1N-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc =
"""
BM rule fitted to 1 training reactions at node Root_N-1NO->O_N-2R->C_3R->H_Ext-1N-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)
