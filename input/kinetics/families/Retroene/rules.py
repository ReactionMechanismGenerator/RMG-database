#!/usr/bin/env python
# encoding: utf-8

name = "Retroene/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(5.30387e-06,'s^-1'), n=5.05826, w0=(1111.63,'kJ/mol'), E0=(106.948,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.49083846839034484, var=86.39080258176443, Tref=1000.0, N=68, data_mean=0.0, correlation='Root',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 68 training reactions at node Root
    Total Standard Deviation in ln(k): 19.8666039936285"""),
    rank = 11,
    shortDesc = """BM rule fitted to 68 training reactions at node Root
Total Standard Deviation in ln(k): 19.8666039936285""",
    longDesc = 
"""
BM rule fitted to 68 training reactions at node Root
Total Standard Deviation in ln(k): 19.8666039936285
""",
)

entry(
    index = 2,
    label = "Root_4R!H->O",
    kinetics = Arrhenius(A=(2.46545e+14,'s^-1'), n=0.20628, Ea=(62.2385,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R!H->O',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_N-4R!H->O",
    kinetics = ArrheniusBM(A=(7.80097e+07,'s^-1'), n=1.18216, w0=(1112.05,'kJ/mol'), E0=(158.99,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10721418599405574, var=9.595762871638254, Tref=1000.0, N=67, data_mean=0.0, correlation='Root_N-4R!H->O',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 67 training reactions at node Root_N-4R!H->O
    Total Standard Deviation in ln(k): 6.4794559152553655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 67 training reactions at node Root_N-4R!H->O
Total Standard Deviation in ln(k): 6.4794559152553655""",
    longDesc = 
"""
BM rule fitted to 67 training reactions at node Root_N-4R!H->O
Total Standard Deviation in ln(k): 6.4794559152553655
""",
)

entry(
    index = 4,
    label = "Root_N-4R!H->O_1R!H->C",
    kinetics = ArrheniusBM(A=(8.75256e+09,'s^-1'), n=0.574336, w0=(1049.26,'kJ/mol'), E0=(169.141,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08372832466371198, var=2.556495467987206, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 31 training reactions at node Root_N-4R!H->O_1R!H->C
    Total Standard Deviation in ln(k): 3.415752528752392"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_N-4R!H->O_1R!H->C
Total Standard Deviation in ln(k): 3.415752528752392""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_N-4R!H->O_1R!H->C
Total Standard Deviation in ln(k): 3.415752528752392
""",
)

entry(
    index = 5,
    label = "Root_N-4R!H->O_N-1R!H->C",
    kinetics = ArrheniusBM(A=(8.06331e+07,'s^-1'), n=1.20797, w0=(1166.12,'kJ/mol'), E0=(151.886,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1894040580737342, var=22.041864973199182, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 36 training reactions at node Root_N-4R!H->O_N-1R!H->C
    Total Standard Deviation in ln(k): 9.887873116231741"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_N-4R!H->O_N-1R!H->C
Total Standard Deviation in ln(k): 9.887873116231741""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_N-4R!H->O_N-1R!H->C
Total Standard Deviation in ln(k): 9.887873116231741
""",
)

entry(
    index = 6,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C",
    kinetics = ArrheniusBM(A=(2.0166e+09,'s^-1'), n=0.752894, w0=(1054.3,'kJ/mol'), E0=(165.591,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12207433391659264, var=1.9840300323409745, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 27 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C
    Total Standard Deviation in ln(k): 3.1305010729850244"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 3.1305010729850244""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C
Total Standard Deviation in ln(k): 3.1305010729850244
""",
)

entry(
    index = 7,
    label = "Root_N-4R!H->O_1R!H->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.75681e+12,'s^-1'), n=0.0156162, w0=(1015.25,'kJ/mol'), E0=(221.487,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.317409309976192, var=63.387160042057275, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_N-2R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 4 training reactions at node Root_N-4R!H->O_1R!H->C_N-2R!H->C
    Total Standard Deviation in ln(k): 26.808671639758366"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R!H->O_1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 26.808671639758366""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R!H->O_1R!H->C_N-2R!H->C
Total Standard Deviation in ln(k): 26.808671639758366
""",
)

entry(
    index = 8,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(96603.7,'s^-1'), n=2.21009, w0=(1178.69,'kJ/mol'), E0=(155.216,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8059544570877398, var=10.320293479545374, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 18 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 8.465265453202461"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 8.465265453202461""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 8.465265453202461
""",
)

entry(
    index = 9,
    label = "Root_N-4R!H->O_N-1R!H->C_1NO->N",
    kinetics = Arrhenius(A=(9.54463e+09,'s^-1'), n=0.829688, Ea=(151.966,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_1NO->N',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_1NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_1NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_1NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N",
    kinetics = ArrheniusBM(A=(2.47493e+10,'s^-1'), n=0.336275, w0=(1157.5,'kJ/mol'), E0=(163.95,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4866998587573729, var=14.015057545701893, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 17 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N
    Total Standard Deviation in ln(k): 8.72792851957881"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N
Total Standard Deviation in ln(k): 8.72792851957881""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N
Total Standard Deviation in ln(k): 8.72792851957881
""",
)

entry(
    index = 11,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.67254e+07,'s^-1'), n=1.30235, w0=(1084.5,'kJ/mol'), E0=(164.609,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11727590765045849, var=1.3605501570117486, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 15 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.6330386690205194"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.6330386690205194""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.6330386690205194
""",
)

entry(
    index = 12,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C",
    kinetics = ArrheniusBM(A=(1.36723e+16,'s^-1'), n=-1.39306, w0=(968,'kJ/mol'), E0=(174.341,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9427687085947482, var=3.633162307202517, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 7 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C
    Total Standard Deviation in ln(k): 6.189962258468166"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C
Total Standard Deviation in ln(k): 6.189962258468166""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C
Total Standard Deviation in ln(k): 6.189962258468166
""",
)

entry(
    index = 13,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(9102.05,'s^-1'), n=2.23331, w0=(1084.5,'kJ/mol'), E0=(155.017,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.33482439496974453, var=2.0645146404798274, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 5 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C
    Total Standard Deviation in ln(k): 3.721754678075354"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 3.721754678075354""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 3.721754678075354
""",
)

entry(
    index = 14,
    label = "Root_N-4R!H->O_1R!H->C_N-2R!H->C_Ext-1C-R",
    kinetics = Arrhenius(A=(2.8e+12,'s^-1'), n=0, Ea=(272,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_N-2R!H->C_Ext-1C-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_N-2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_N-2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_N-2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_N-4R!H->O_1R!H->C_N-2R!H->C_2NOS->S",
    kinetics = Arrhenius(A=(5.6608e+10,'s^-1'), n=0, Ea=(160,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_N-2R!H->C_2NOS->S',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_N-2R!H->C_2NOS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_N-2R!H->C_2NOS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_N-2R!H->C_2NOS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-4R!H->O_1R!H->C_N-2R!H->C_N-2NOS->S",
    kinetics = ArrheniusBM(A=(1.48951e+11,'s^-1'), n=-0.120383, w0=(1020.5,'kJ/mol'), E0=(160.987,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.32075031216958483, var=4.636406728010417, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_N-2R!H->C_N-2NOS->S',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_N-2R!H->C_N-2NOS->S
    Total Standard Deviation in ln(k): 5.122564413660733"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_N-2R!H->C_N-2NOS->S
Total Standard Deviation in ln(k): 5.122564413660733""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_N-2R!H->C_N-2NOS->S
Total Standard Deviation in ln(k): 5.122564413660733
""",
)

entry(
    index = 17,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_1NO->N",
    kinetics = Arrhenius(A=(1.93151e+06,'s^-1'), n=1.81611, Ea=(228.248,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_1NO->N',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_1NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_1NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_1NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N",
    kinetics = ArrheniusBM(A=(1.55515e+09,'s^-1'), n=1.02193, w0=(1183,'kJ/mol'), E0=(153.303,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5273445406852786, var=3.2474917946603368, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 17 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N
    Total Standard Deviation in ln(k): 4.937678975630705"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N
Total Standard Deviation in ln(k): 4.937678975630705""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N
Total Standard Deviation in ln(k): 4.937678975630705
""",
)

entry(
    index = 19,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N_3R!H-inRing",
    kinetics = ArrheniusBM(A=(1.2965e+12,'s^-1'), n=-0.400746, w0=(1024.5,'kJ/mol'), E0=(146.036,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7517131973007273, var=87.46007632386218, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N_3R!H-inRing',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 2 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_3R!H-inRing
    Total Standard Deviation in ln(k): 20.637027540207946"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_3R!H-inRing
Total Standard Deviation in ln(k): 20.637027540207946""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_3R!H-inRing
Total Standard Deviation in ln(k): 20.637027540207946
""",
)

entry(
    index = 20,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing",
    kinetics = ArrheniusBM(A=(2.68528e+08,'s^-1'), n=0.958605, w0=(1175.23,'kJ/mol'), E0=(164.23,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3525505726674557, var=14.853211663321563, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 15 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing
    Total Standard Deviation in ln(k): 8.612027310789172"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing
Total Standard Deviation in ln(k): 8.612027310789172""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing
Total Standard Deviation in ln(k): 8.612027310789172
""",
)

entry(
    index = 21,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N",
    kinetics = ArrheniusBM(A=(19367.3,'s^-1'), n=2.2817, w0=(1084.5,'kJ/mol'), E0=(166.605,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5565341753175064, var=0.24718377473298897, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 5 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N
    Total Standard Deviation in ln(k): 2.3950328367861333"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N
Total Standard Deviation in ln(k): 2.3950328367861333""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N
Total Standard Deviation in ln(k): 2.3950328367861333
""",
)

entry(
    index = 22,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N",
    kinetics = ArrheniusBM(A=(3.99066e+06,'s^-1'), n=1.63957, w0=(1084.5,'kJ/mol'), E0=(156.167,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02434531845894637, var=1.0714238308106672, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 10 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N
    Total Standard Deviation in ln(k): 2.1362624999093742"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N
Total Standard Deviation in ln(k): 2.1362624999093742""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N
Total Standard Deviation in ln(k): 2.1362624999093742
""",
)

entry(
    index = 23,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R",
    kinetics = ArrheniusBM(A=(5.37759e+17,'s^-1'), n=-1.87431, w0=(968,'kJ/mol'), E0=(170.83,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1833960749951646, var=4.428724687442455, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 5 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R
    Total Standard Deviation in ln(k): 7.1922287957912205"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 7.1922287957912205""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 7.1922287957912205
""",
)

entry(
    index = 24,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-5C-R",
    kinetics = Arrhenius(A=(3.23333e+11,'s^-1'), n=0, Ea=(238,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-5C-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.70214e+06,'s^-1'), n=1.63471, w0=(1084.5,'kJ/mol'), E0=(156.992,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.45656472091591394, var=6.173520258389904, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 6.128226522968072"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 6.128226522968072""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 6.128226522968072
""",
)

entry(
    index = 26,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-4BrCClFILiNPSSi-R",
    kinetics = ArrheniusBM(A=(191.996,'s^-1'), n=2.68015, w0=(1084.5,'kJ/mol'), E0=(155.306,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2573514085044374, var=0.12946633204113422, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-4BrCClFILiNPSSi-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-4BrCClFILiNPSSi-R
    Total Standard Deviation in ln(k): 1.36794393205138"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 1.36794393205138""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 1.36794393205138
""",
)

entry(
    index = 27,
    label = "Root_N-4R!H->O_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->N",
    kinetics = Arrhenius(A=(7.8141e+10,'s^-1'), n=0, Ea=(181.5,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->N',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_N-2R!H->C_N-2NOS->S_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_N-4R!H->O_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->N",
    kinetics = Arrhenius(A=(4.1009e+10,'s^-1'), n=0, Ea=(174.05,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->N',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_N-2R!H->C_N-2NOS->S_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(8.34945e+08,'s^-1'), n=1.09902, w0=(1183,'kJ/mol'), E0=(140.068,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.5779390138558111, var=2.4308566970867074, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_Ext-2R!H-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 4 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_Ext-2R!H-R
    Total Standard Deviation in ln(k): 7.090294421895899"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_Ext-2R!H-R
Total Standard Deviation in ln(k): 7.090294421895899""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_Ext-2R!H-R
Total Standard Deviation in ln(k): 7.090294421895899
""",
)

entry(
    index = 30,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C",
    kinetics = ArrheniusBM(A=(5.87688e+08,'s^-1'), n=1.14684, w0=(1183,'kJ/mol'), E0=(159.017,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.47993816235194836, var=0.3791713969708127, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 12 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C
    Total Standard Deviation in ln(k): 2.4403283888343603"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C
Total Standard Deviation in ln(k): 2.4403283888343603""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C
Total Standard Deviation in ln(k): 2.4403283888343603
""",
)

entry(
    index = 31,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_N-7R!H->C",
    kinetics = Arrhenius(A=(6.63512e+11,'s^-1'), n=0, Ea=(151.042,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_N-7R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N_3R!H-inRing_Ext-4BrCClFILiNPSSi-R",
    kinetics = Arrhenius(A=(550000,'s^-1'), n=0.9, Ea=(205.016,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N_3R!H-inRing_Ext-4BrCClFILiNPSSi-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_3R!H-inRing_Ext-4BrCClFILiNPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_3R!H-inRing_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_3R!H-inRing_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R",
    kinetics = ArrheniusBM(A=(469719,'s^-1'), n=2.04105, w0=(1183,'kJ/mol'), E0=(172.778,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3203489855819182, var=0.3237660135180751, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 9 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R
    Total Standard Deviation in ln(k): 1.94560003966581"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 1.94560003966581""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 1.94560003966581
""",
)

entry(
    index = 34,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(6.76595e+09,'s^-1'), n=0.33585, w0=(1183,'kJ/mol'), E0=(159.331,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.23171115451802335, var=47.4036443053091, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 4 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R
    Total Standard Deviation in ln(k): 14.384850883636512"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 14.384850883636512""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 14.384850883636512
""",
)

entry(
    index = 35,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_5R!H->C",
    kinetics = Arrhenius(A=(3.33333e+07,'s^-1'), n=1.2, Ea=(184.096,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_5R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_N-5R!H->C",
    kinetics = Arrhenius(A=(3.96667e+10,'s^-1'), n=0.59, Ea=(208.363,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_N-5R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4BrCClFILiNPSSi-R",
    kinetics = ArrheniusBM(A=(18146.5,'s^-1'), n=2.36318, w0=(1084.5,'kJ/mol'), E0=(172.65,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4729038752967067, var=0.7277624016192566, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4BrCClFILiNPSSi-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4BrCClFILiNPSSi-R
    Total Standard Deviation in ln(k): 2.898419966761816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 2.898419966761816""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 2.898419966761816
""",
)

entry(
    index = 38,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R",
    kinetics = ArrheniusBM(A=(965027,'s^-1'), n=1.71749, w0=(1084.5,'kJ/mol'), E0=(164.336,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6691355606766685, var=0.10021204730729523, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R
    Total Standard Deviation in ln(k): 2.3158698063934877"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 2.3158698063934877""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 2.3158698063934877
""",
)

entry(
    index = 39,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R",
    kinetics = ArrheniusBM(A=(1.48286e+06,'s^-1'), n=1.77426, w0=(1084.5,'kJ/mol'), E0=(159.699,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10455984390053077, var=1.1567094178664674, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 4 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R
    Total Standard Deviation in ln(k): 2.4188142958145984"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 2.4188142958145984""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 2.4188142958145984
""",
)

entry(
    index = 40,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R",
    kinetics = ArrheniusBM(A=(5.30594e+07,'s^-1'), n=1.33225, w0=(1084.5,'kJ/mol'), E0=(155.438,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10036399890331829, var=1.4168522450847445, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 4 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R
    Total Standard Deviation in ln(k): 2.6384391448286095"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 2.6384391448286095""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R
Total Standard Deviation in ln(k): 2.6384391448286095
""",
)

entry(
    index = 41,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFILiOPSSi->C",
    kinetics = Arrhenius(A=(11.5839,'s^-1'), n=3.09547, Ea=(214.25,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFILiOPSSi->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFILiOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFILiOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_7BrCClFILiOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFILiOPSSi->C",
    kinetics = Arrhenius(A=(1.2535e+06,'s^-1'), n=1.80968, Ea=(236.043,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFILiOPSSi->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFILiOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFILiOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_N-7BrCClFILiOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.21085e+18,'s^-1'), n=-2.00119, w0=(968,'kJ/mol'), E0=(164.963,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3529490474545591, var=4.152754124412871, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-7R!H-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 4 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 7.484680232002102"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 7.484680232002102""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 7.484680232002102
""",
)

entry(
    index = 44,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_7R!H->C",
    kinetics = Arrhenius(A=(21.2645,'s^-1'), n=2.97303, Ea=(221.127,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_7R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(3.78363e+11,'s^-1'), n=0.169307, Ea=(240.476,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_N-7R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-4BrCClFILiNPSSi-R_7R!H->C",
    kinetics = Arrhenius(A=(6.80655,'s^-1'), n=3.07798, Ea=(218.469,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-4BrCClFILiNPSSi-R_7R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-4BrCClFILiNPSSi-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-4BrCClFILiNPSSi-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-4BrCClFILiNPSSi-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-4BrCClFILiNPSSi-R_N-7R!H->C",
    kinetics = Arrhenius(A=(2419.21,'s^-1'), n=2.3826, Ea=(221.139,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-4BrCClFILiNPSSi-R_N-7R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-4BrCClFILiNPSSi-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-4BrCClFILiNPSSi-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_N-5R!H->C_Ext-4BrCClFILiNPSSi-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_Ext-2R!H-R_Ext-4BrCClFILiNPSSi-R",
    kinetics = Arrhenius(A=(4.45626e+12,'s^-1'), n=0, Ea=(164.85,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_Ext-2R!H-R_Ext-4BrCClFILiNPSSi-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_Ext-2R!H-R_Ext-4BrCClFILiNPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_Ext-2R!H-R_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_Ext-2R!H-R_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_Ext-2R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(5.6202e+08,'s^-1'), n=1.15554, w0=(1183,'kJ/mol'), E0=(140.593,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.5863421086795069, var=2.050224061171546, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_Ext-2R!H-R_Ext-3R!H-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 2 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_Ext-2R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 6.856284861725482"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.856284861725482""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_Ext-2R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 6.856284861725482
""",
)

entry(
    index = 50,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R",
    kinetics = ArrheniusBM(A=(7.96786e+07,'s^-1'), n=1.37169, w0=(1183,'kJ/mol'), E0=(153.977,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0773380571599183, var=2.1714432161776456, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 7 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R
    Total Standard Deviation in ln(k): 5.661020592971476"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 5.661020592971476""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 5.661020592971476
""",
)

entry(
    index = 51,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-4BrCClFILiNPSSi-R",
    kinetics = ArrheniusBM(A=(2.42662e+09,'s^-1'), n=1.00906, w0=(1183,'kJ/mol'), E0=(164.656,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.450692648402451, var=0.0248889840073708, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-4BrCClFILiNPSSi-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 3 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-4BrCClFILiNPSSi-R
    Total Standard Deviation in ln(k): 1.4486654642836272"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 1.4486654642836272""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 1.4486654642836272
""",
)

entry(
    index = 52,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-3R!H-R",
    kinetics = Arrhenius(A=(1.32388e+12,'s^-1'), n=0, Ea=(187.025,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-3R!H-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C",
    kinetics = ArrheniusBM(A=(256073,'s^-1'), n=2.12413, w0=(1183,'kJ/mol'), E0=(171.888,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3934798856681917, var=0.1479784301545738, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 7 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C
    Total Standard Deviation in ln(k): 1.759823708991437"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C
Total Standard Deviation in ln(k): 1.759823708991437""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C
Total Standard Deviation in ln(k): 1.759823708991437
""",
)

entry(
    index = 54,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(7.92447e+11,'s^-1'), n=-2.49339e-07, w0=(1183,'kJ/mol'), E0=(196.122,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27845427020935715, var=0.04557061719277167, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_N-7R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 2 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_N-7R!H->C
    Total Standard Deviation in ln(k): 1.1275901650710636"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_N-7R!H->C
Total Standard Deviation in ln(k): 1.1275901650710636""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_N-7R!H->C
Total Standard Deviation in ln(k): 1.1275901650710636
""",
)

entry(
    index = 55,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(4.20001e+11,'s^-1'), n=0.32268, w0=(1183,'kJ/mol'), E0=(171.62,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.23079689079441648, var=0.5957102507474185, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 3 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 2.1271916873362033"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C
Total Standard Deviation in ln(k): 2.1271916873362033""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C
Total Standard Deviation in ln(k): 2.1271916873362033
""",
)

entry(
    index = 56,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C",
    kinetics = Arrhenius(A=(58002.5,'s^-1'), n=0.286, Ea=(158.771,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4BrCClFILiNPSSi-R_8R!H->C",
    kinetics = Arrhenius(A=(1708.21,'s^-1'), n=2.62955, Ea=(212.275,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4BrCClFILiNPSSi-R_8R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4BrCClFILiNPSSi-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4BrCClFILiNPSSi-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4BrCClFILiNPSSi-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4BrCClFILiNPSSi-R_N-8R!H->C",
    kinetics = Arrhenius(A=(85500.5,'s^-1'), n=2.19797, Ea=(217.237,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4BrCClFILiNPSSi-R_N-8R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4BrCClFILiNPSSi-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4BrCClFILiNPSSi-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-4BrCClFILiNPSSi-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C",
    kinetics = Arrhenius(A=(111514,'s^-1'), n=2.05353, Ea=(215.947,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(6.3077e+06,'s^-1'), n=1.41637, Ea=(213.544,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_7BrCClFILiOPSSi->C",
    kinetics = ArrheniusBM(A=(8655.91,'s^-1'), n=2.28998, w0=(1084.5,'kJ/mol'), E0=(149.794,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20820257256414182, var=3.556142232964992, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_7BrCClFILiOPSSi->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_7BrCClFILiOPSSi->C
    Total Standard Deviation in ln(k): 4.303598611942077"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_7BrCClFILiOPSSi->C
Total Standard Deviation in ln(k): 4.303598611942077""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_7BrCClFILiOPSSi->C
Total Standard Deviation in ln(k): 4.303598611942077
""",
)

entry(
    index = 62,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_N-7BrCClFILiOPSSi->C",
    kinetics = ArrheniusBM(A=(1.91883e+08,'s^-1'), n=1.29345, w0=(1084.5,'kJ/mol'), E0=(169.275,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.008953958190021602, var=0.18903777413776637, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_N-7BrCClFILiOPSSi->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_N-7BrCClFILiOPSSi->C
    Total Standard Deviation in ln(k): 0.8941256110044856"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_N-7BrCClFILiOPSSi->C
Total Standard Deviation in ln(k): 0.8941256110044856""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_N-7BrCClFILiOPSSi->C
Total Standard Deviation in ln(k): 0.8941256110044856
""",
)

entry(
    index = 63,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(168410,'s^-1'), n=2.00336, w0=(1084.5,'kJ/mol'), E0=(149.392,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1470976091671956, var=0.8170263346989156, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C
    Total Standard Deviation in ln(k): 2.1816621771182647"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 2.1816621771182647""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C
Total Standard Deviation in ln(k): 2.1816621771182647
""",
)

entry(
    index = 64,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(2.73944e+10,'s^-1'), n=0.599682, w0=(1084.5,'kJ/mol'), E0=(161.997,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.34354461429897054, var=2.7998101740922627, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 4.217627115769353"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 4.217627115769353""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C
Total Standard Deviation in ln(k): 4.217627115769353
""",
)

entry(
    index = 65,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-7R!H-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(2.56831e+17,'s^-1'), n=-1.83293, w0=(968,'kJ/mol'), E0=(155.988,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.7185179835837956, var=6.360293323616219, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-7R!H-R_Ext-8R!H-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 3 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-7R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 9.373750461258023"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 9.373750461258023""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-7R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 9.373750461258023
""",
)

entry(
    index = 66,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R",
    kinetics = Arrhenius(A=(1.39881e+12,'s^-1'), n=0, Ea=(167.36,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_Ext-2R!H-R_Ext-3R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-4BrCClFILiNPSSi-R",
    kinetics = ArrheniusBM(A=(1.70647e+12,'s^-1'), n=-0.00963958, w0=(1183,'kJ/mol'), E0=(155.567,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2601587167274369, var=0.0010734179904211348, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-4BrCClFILiNPSSi-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 2 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-4BrCClFILiNPSSi-R
    Total Standard Deviation in ln(k): 0.7193463696606417"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 0.7193463696606417""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 0.7193463696606417
""",
)

entry(
    index = 68,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.17803e+12,'s^-1'), n=-0.0711355, w0=(1183,'kJ/mol'), E0=(141.576,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2825947458663283, var=1.823716168221111, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 4 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 3.417332251985864"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 3.417332251985864""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 3.417332251985864
""",
)

entry(
    index = 69,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-8R!H-R",
    kinetics = ArrheniusBM(A=(1.91175e+12,'s^-1'), n=-0.0307894, w0=(1183,'kJ/mol'), E0=(160.263,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.30949230006020834, var=0.34956736994551824, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-8R!H-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 2 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 1.9629028743086638"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 1.9629028743086638""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 1.9629028743086638
""",
)

entry(
    index = 70,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_7C-inRing",
    kinetics = Arrhenius(A=(7.92445e+11,'s^-1'), n=0, Ea=(188.698,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_7C-inRing',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing",
    kinetics = ArrheniusBM(A=(205859,'s^-1'), n=2.15525, w0=(1183,'kJ/mol'), E0=(171.993,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3856238088146881, var=0.10483958078411568, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 6 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing
    Total Standard Deviation in ln(k): 1.6180160263125112"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing
Total Standard Deviation in ln(k): 1.6180160263125112""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing
Total Standard Deviation in ln(k): 1.6180160263125112
""",
)

entry(
    index = 72,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_N-7R!H->C_Ext-7BrClFILiNOPSSi-R_Ext-8R!H-R",
    kinetics = Arrhenius(A=(7.92445e+11,'s^-1'), n=0, Ea=(202.087,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_N-7R!H->C_Ext-7BrClFILiNOPSSi-R_Ext-8R!H-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_N-7R!H->C_Ext-7BrClFILiNOPSSi-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_N-7R!H->C_Ext-7BrClFILiNOPSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_N-7R!H->C_Ext-7BrClFILiNOPSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R",
    kinetics = ArrheniusBM(A=(4.01094e+10,'s^-1'), n=0.635, w0=(1183,'kJ/mol'), E0=(170.001,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2358830568284934, var=2.1156506938101853, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 2 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R
    Total Standard Deviation in ln(k): 3.5086136043882368"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 3.5086136043882368""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 3.5086136043882368
""",
)

entry(
    index = 74,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_7BrCClFILiOPSSi->C_8R!H->N",
    kinetics = Arrhenius(A=(6552.1,'s^-1'), n=2.29082, Ea=(214.941,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_7BrCClFILiOPSSi->C_8R!H->N',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_7BrCClFILiOPSSi->C_8R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_7BrCClFILiOPSSi->C_8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_7BrCClFILiOPSSi->C_8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_7BrCClFILiOPSSi->C_N-8R!H->N",
    kinetics = Arrhenius(A=(459.237,'s^-1'), n=2.68918, Ea=(213.037,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_7BrCClFILiOPSSi->C_N-8R!H->N',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_7BrCClFILiOPSSi->C_N-8R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_7BrCClFILiOPSSi->C_N-8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_7BrCClFILiOPSSi->C_N-8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_N-7BrCClFILiOPSSi->C_8R!H->N",
    kinetics = Arrhenius(A=(2.87851e+08,'s^-1'), n=1.30992, Ea=(238.61,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_N-7BrCClFILiOPSSi->C_8R!H->N',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_N-7BrCClFILiOPSSi->C_8R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_N-7BrCClFILiOPSSi->C_8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_N-7BrCClFILiOPSSi->C_8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 77,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_N-7BrCClFILiOPSSi->C_N-8R!H->N",
    kinetics = Arrhenius(A=(6.1395e+07,'s^-1'), n=1.36832, Ea=(234.848,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_N-7BrCClFILiOPSSi->C_N-8R!H->N',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_N-7BrCClFILiOPSSi->C_N-8R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_N-7BrCClFILiOPSSi->C_N-8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-4BrCClFILiNPSSi-R_N-7BrCClFILiOPSSi->C_N-8R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 78,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFILiOPSSi->C",
    kinetics = Arrhenius(A=(1017.11,'s^-1'), n=2.55399, Ea=(214.789,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFILiOPSSi->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFILiOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFILiOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_7BrCClFILiOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFILiOPSSi->C",
    kinetics = Arrhenius(A=(1.65185e+07,'s^-1'), n=1.51788, Ea=(236.313,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFILiOPSSi->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFILiOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFILiOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_8R!H->C_N-7BrCClFILiOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFILiOPSSi->C",
    kinetics = Arrhenius(A=(2.0173e+12,'s^-1'), n=0.0499164, Ea=(232.901,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFILiOPSSi->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFILiOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFILiOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_7BrCClFILiOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 81,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFILiOPSSi->C",
    kinetics = Arrhenius(A=(8.27867e+08,'s^-1'), n=1.04991, Ea=(238.94,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFILiOPSSi->C',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFILiOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFILiOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_Ext-1C-R_N-7R!H->N_Ext-2C-R_N-8R!H->C_N-7BrCClFILiOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.94997e+11,'s^-1'), n=-0.177939, w0=(968,'kJ/mol'), E0=(121.642,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.28501317521645, var=1.286709965420954, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 8.01527506043425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 8.01527506043425""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 8.01527506043425
""",
)

entry(
    index = 83,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-4BrCClFILiNPSSi-R_7C-inRing",
    kinetics = Arrhenius(A=(1.25594e+12,'s^-1'), n=0, Ea=(174.473,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-4BrCClFILiNPSSi-R_7C-inRing',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-4BrCClFILiNPSSi-R_7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-4BrCClFILiNPSSi-R_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-4BrCClFILiNPSSi-R_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-4BrCClFILiNPSSi-R_N-7C-inRing",
    kinetics = Arrhenius(A=(1.98582e+12,'s^-1'), n=0, Ea=(184.514,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-4BrCClFILiNPSSi-R_N-7C-inRing',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-4BrCClFILiNPSSi-R_N-7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-4BrCClFILiNPSSi-R_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-4BrCClFILiNPSSi-R_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R",
    kinetics = Arrhenius(A=(1.32702e+11,'s^-1'), n=0, Ea=(153.134,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H",
    kinetics = Arrhenius(A=(8.37297e+11,'s^-1'), n=0, Ea=(183.678,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 87,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H",
    kinetics = ArrheniusBM(A=(1.52578e+12,'s^-1'), n=-0.0173669, w0=(1183,'kJ/mol'), E0=(150.461,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2488646314503384, var=0.236345510915107, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 2 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
    Total Standard Deviation in ln(k): 1.5998975815172547"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 1.5998975815172547""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H
Total Standard Deviation in ln(k): 1.5998975815172547
""",
)

entry(
    index = 88,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-8R!H-R_Sp-9R!H-8R!H",
    kinetics = Arrhenius(A=(1.11936e+12,'s^-1'), n=0, Ea=(183.259,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-8R!H-R_Sp-9R!H-8R!H',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-8R!H-R_Sp-9R!H-8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-8R!H-R_Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-8R!H-R_Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-8R!H-R_N-Sp-9R!H-8R!H",
    kinetics = Arrhenius(A=(1.99053e+12,'s^-1'), n=0, Ea=(183.678,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-8R!H-R_N-Sp-9R!H-8R!H',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-8R!H-R_N-Sp-9R!H-8R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-7C-R",
    kinetics = ArrheniusBM(A=(9837.12,'s^-1'), n=2.48653, w0=(1183,'kJ/mol'), E0=(165.12,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9373446397586955, var=1.0760671056759732, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-7C-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 4 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-7C-R
    Total Standard Deviation in ln(k): 4.434722242798251"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-7C-R
Total Standard Deviation in ln(k): 4.434722242798251""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-7C-R
Total Standard Deviation in ln(k): 4.434722242798251
""",
)

entry(
    index = 91,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-4BrCClFILiNPSSi-R",
    kinetics = Arrhenius(A=(3.16053e+06,'s^-1'), n=1.87467, Ea=(202.966,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-4BrCClFILiNPSSi-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-4BrCClFILiNPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R",
    kinetics = Arrhenius(A=(6.96433e+12,'s^-1'), n=0, Ea=(207.183,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-3R!H-R_7R!H->C_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R",
    kinetics = Arrhenius(A=(6.5e+10,'s^-1'), n=0, Ea=(205,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_1R!H->C_2R!H->C_5R!H->C_Ext-4BrCClFILiNPSSi-R_Ext-7R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing",
    kinetics = Arrhenius(A=(1.32702e+12,'s^-1'), n=0, Ea=(182.841,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing",
    kinetics = Arrhenius(A=(1.32702e+12,'s^-1'), n=0, Ea=(183.259,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_Ext-2R!H-R_N-1NO->N_7R!H->C_Ext-7C-R_Ext-8R!H-R_N-Sp-9R!H=8R!H_N-7C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4BrCClFILiNPSSi-R",
    kinetics = Arrhenius(A=(7.94328e+11,'s^-1'), n=0, Ea=(191.627,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4BrCClFILiNPSSi-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4BrCClFILiNPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-4BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 97,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R",
    kinetics = Arrhenius(A=(7.92445e+11,'s^-1'), n=0, Ea=(194.138,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R",
    kinetics = Arrhenius(A=(7.92445e+11,'s^-1'), n=0, Ea=(194.138,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R',), solute=SoluteTSData(Sg_g=-2.4493769286399454,Bg_g=0.01616758955658365,Eg_g=-2.4134042226844743,Lg_g=-4.517147142688703,Ag_g=-0.34361684722897834,Cg_g=-1.0,Sh_g=0.0,Bh_g=0.0,Eh_g=0.0,Lh_g=0.0,Ah_g=0.0,Ch_g=0.0,K_g=0.0,Sg_h=0.0,Bg_h=0.0,Eg_h=0.0,Lg_h=0.0,Ag_h=0.0,Cg_h=0.0,Sh_h=-2.4493769286399454,Bh_h=0.01616758955658365,Eh_h=-2.4134042226844743,Lh_h=-4.517147142688703,Ah_h=-0.34361684722897834,Ch_h=-1.0,K_h=0.0,comment=None), comment="""BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R!H->O_N-1R!H->C_N-1NO->N_N-3R!H-inRing_Ext-4BrCClFILiNPSSi-R_7R!H->C_N-7C-inRing_Ext-7C-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

