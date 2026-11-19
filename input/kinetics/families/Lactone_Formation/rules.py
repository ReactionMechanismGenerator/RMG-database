#!/usr/bin/env python
# encoding: utf-8

name = "Lactone_Formation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = Arrhenius(A=(3.78157e+09,'s^-1'), n=0.978824, Ea=(255.875,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=1.852433568953098e-15, var=85.39031335855428, Tref=1000.0, N=17, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 17 training reactions at node Root
    Total Standard Deviation in ln(k): 18.525131225896594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root
Total Standard Deviation in ln(k): 18.525131225896594""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root
Total Standard Deviation in ln(k): 18.525131225896594
""",
)

entry(
    index = 2,
    label = "Root_6F1sH->F1s",
    kinetics = ArrheniusBM(A=(2.89232e+11,'s^-1'), n=0.455041, w0=(933500,'J/mol'), E0=(136963,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22460442912751302, var=2.68645075758266, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_6F1sH->F1s',), comment="""BM rule fitted to 12 training reactions at node Root_6F1sH->F1s
    Total Standard Deviation in ln(k): 3.8501728835779523"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_6F1sH->F1s
Total Standard Deviation in ln(k): 3.8501728835779523""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_6F1sH->F1s
Total Standard Deviation in ln(k): 3.8501728835779523
""",
)

entry(
    index = 3,
    label = "Root_N-6F1sH->F1s",
    kinetics = Arrhenius(A=(227460,'s^-1'), n=2.15, Ea=(336.615,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-3.5990137911088763e-16, var=90.82325827284195, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-6F1sH->F1s',), comment="""BM rule fitted to 5 training reactions at node Root_N-6F1sH->F1s
    Total Standard Deviation in ln(k): 19.105373329622687"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-6F1sH->F1s
Total Standard Deviation in ln(k): 19.105373329622687""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-6F1sH->F1s
Total Standard Deviation in ln(k): 19.105373329622687
""",
)

entry(
    index = 4,
    label = "Root_6F1sH->F1s_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.50598e+11,'s^-1'), n=0.436541, w0=(933500,'J/mol'), E0=(137932,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22119544507090022, var=2.9782245202109565, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R',), comment="""BM rule fitted to 11 training reactions at node Root_6F1sH->F1s_Ext-3C-R
    Total Standard Deviation in ln(k): 4.015445664716769"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_6F1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 4.015445664716769""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_6F1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 4.015445664716769
""",
)

entry(
    index = 5,
    label = "Root_N-6F1sH->F1s_Ext-3C-R",
    kinetics = Arrhenius(A=(627251,'s^-1'), n=1.995, Ea=(319.29,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-2.6992603433316573e-15, var=89.06593733433054, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-6F1sH->F1s_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R
    Total Standard Deviation in ln(k): 18.919637488778502"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 18.919637488778502""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 18.919637488778502
""",
)

entry(
    index = 6,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F",
    kinetics = ArrheniusBM(A=(2.23094e+12,'s^-1'), n=0.15285, w0=(933500,'J/mol'), E0=(140523,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4063913760121001, var=2.223396045737613, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F',), comment="""BM rule fitted to 7 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F
    Total Standard Deviation in ln(k): 4.010355650756558"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F
Total Standard Deviation in ln(k): 4.010355650756558""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F
Total Standard Deviation in ln(k): 4.010355650756558
""",
)

entry(
    index = 7,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F",
    kinetics = ArrheniusBM(A=(1.15982e+16,'s^-1'), n=-0.764887, w0=(933500,'J/mol'), E0=(148884,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05024486917294843, var=5.247011569321851, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F
    Total Standard Deviation in ln(k): 4.718360978074363"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F
Total Standard Deviation in ln(k): 4.718360978074363""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F
Total Standard Deviation in ln(k): 4.718360978074363
""",
)

entry(
    index = 8,
    label = "Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(9.28596e+06,'s^-1'), n=1.585, w0=(830000,'J/mol'), E0=(156150,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1702874213823726, var=0.05114146896546326, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 3.3937810627710583"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.3937810627710583""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 3.3937810627710583
""",
)

entry(
    index = 9,
    label = "Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R",
    kinetics = Arrhenius(A=(26400,'s^-1'), n=2.44, Ea=(368.245,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(2.93014e+11,'s^-1'), n=0.414585, w0=(933500,'J/mol'), E0=(141811,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.44330267199420137, var=0.9456486993014085, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C
    Total Standard Deviation in ln(k): 3.063319814835946"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C
Total Standard Deviation in ln(k): 3.063319814835946""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C
Total Standard Deviation in ln(k): 3.063319814835946
""",
)

entry(
    index = 11,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(3.19e+11,'s^-1'), n=0.34, Ea=(222,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.97606e+14,'s^-1'), n=-0.206667, w0=(933500,'J/mol'), E0=(153956,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09585625186061471, var=3.534872101432971, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 4.0099985033317305"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 4.0099985033317305""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 4.0099985033317305
""",
)

entry(
    index = 13,
    label = "Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R",
    kinetics = Arrhenius(A=(1.17e+07,'s^-1'), n=1.55, Ea=(266.433,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(1.9495e+11,'s^-1'), n=0.477025, w0=(933500,'J/mol'), E0=(139918,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4890706663515699, var=0.8574869722296913, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 3.085217328469786"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 3.085217328469786""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 3.085217328469786
""",
)

entry(
    index = 15,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = Arrhenius(A=(4.465e+10,'s^-1'), n=0.59, Ea=(237.41,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C",
    kinetics = ArrheniusBM(A=(2.07046e+15,'s^-1'), n=-0.52, w0=(933500,'J/mol'), E0=(160655,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.09676998542241934, var=4.079581474253008, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C
    Total Standard Deviation in ln(k): 4.292299332737232"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C
Total Standard Deviation in ln(k): 4.292299332737232""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C
Total Standard Deviation in ln(k): 4.292299332737232
""",
)

entry(
    index = 17,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C",
    kinetics = Arrhenius(A=(1.8e+12,'s^-1'), n=0.42, Ea=(202.372,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C",
    kinetics = ArrheniusBM(A=(7.68351e+10,'s^-1'), n=0.611782, w0=(933500,'J/mol'), E0=(136925,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5657130967592966, var=0.4689200465311816, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
    Total Standard Deviation in ln(k): 2.794186904292861"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 2.794186904292861""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 2.794186904292861
""",
)

entry(
    index = 19,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C",
    kinetics = Arrhenius(A=(5.3e+09,'s^-1'), n=0.85, Ea=(233.214,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C",
    kinetics = Arrhenius(A=(7.78e+15,'s^-1'), n=-0.84, Ea=(208.506,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C",
    kinetics = Arrhenius(A=(5.51e+14,'s^-1'), n=-0.2, Ea=(235.136,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C",
    kinetics = ArrheniusBM(A=(3.78062e+11,'s^-1'), n=0.398049, w0=(933500,'J/mol'), E0=(135675,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6711373854354776, var=0.513166205749247, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
    Total Standard Deviation in ln(k): 3.1223792404851305"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 3.1223792404851305""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 3.1223792404851305
""",
)

entry(
    index = 23,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C",
    kinetics = Arrhenius(A=(3.66e+07,'s^-1'), n=1.61, Ea=(231.308,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C",
    kinetics = ArrheniusBM(A=(1.49538e+11,'s^-1'), n=0.513264, w0=(933500,'J/mol'), E0=(131666,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8508919403261448, var=0.9936358957726975, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C
    Total Standard Deviation in ln(k): 4.136265172106335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C
Total Standard Deviation in ln(k): 4.136265172106335""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C
Total Standard Deviation in ln(k): 4.136265172106335
""",
)

entry(
    index = 25,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_N-12R!H->C",
    kinetics = Arrhenius(A=(3.35e+10,'s^-1'), n=0.7, Ea=(232.005,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_N-12R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_N-12R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_N-12R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_N-12R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_13R!H->C",
    kinetics = Arrhenius(A=(1.59e+10,'s^-1'), n=0.8, Ea=(233.056,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_13R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_13R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_13R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_13R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_N-13R!H->C",
    kinetics = Arrhenius(A=(1.045e+11,'s^-1'), n=0.55, Ea=(232.571,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_N-13R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_N-13R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_N-13R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_N-13R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

