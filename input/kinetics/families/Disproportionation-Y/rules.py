#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation-Y/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.95038e+09,'m^3/(mol*s)'), n=-0.548205, w0=(561.986,'kJ/mol'), E0=(67.5776,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.037955888107328244, var=0.5416415960068013, Tref=1000.0, N=42, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 42 training reactions at node Root
    Total Standard Deviation in ln(k): 1.5707774746612695"""),
    rank = 11,
    shortDesc = """BM rule fitted to 42 training reactions at node Root
Total Standard Deviation in ln(k): 1.5707774746612695""",
    longDesc = 
"""
BM rule fitted to 42 training reactions at node Root
Total Standard Deviation in ln(k): 1.5707774746612695
""",
)

entry(
    index = 2,
    label = "Root_4R->F",
    kinetics = ArrheniusBM(A=(6.43571e+14,'m^3/(mol*s)'), n=-2.67614, w0=(494.25,'kJ/mol'), E0=(64.7481,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22460824921085948, var=134.54106679976957, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->F',), comment="""BM rule fitted to 2 training reactions at node Root_4R->F
    Total Standard Deviation in ln(k): 23.817633138254063"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->F
Total Standard Deviation in ln(k): 23.817633138254063""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->F
Total Standard Deviation in ln(k): 23.817633138254063
""",
)

entry(
    index = 3,
    label = "Root_4R->F_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(6e+07,'m^3/(mol*s)'), n=8.65264e-08, w0=(540.5,'kJ/mol'), E0=(51.3672,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->F_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->F_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->F_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->F_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_N-4R->F",
    kinetics = ArrheniusBM(A=(1.91618e+09,'m^3/(mol*s)'), n=-0.545726, w0=(565.373,'kJ/mol'), E0=(67.529,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.045099733560703084, var=0.5365041707934532, Tref=1000.0, N=40, data_mean=0.0, correlation='Root_N-4R->F',), comment="""BM rule fitted to 40 training reactions at node Root_N-4R->F
    Total Standard Deviation in ln(k): 1.5817130897110032"""),
    rank = 11,
    shortDesc = """BM rule fitted to 40 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 1.5817130897110032""",
    longDesc = 
"""
BM rule fitted to 40 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 1.5817130897110032
""",
)

entry(
    index = 5,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H",
    kinetics = ArrheniusBM(A=(9.26217e+08,'m^3/(mol*s)'), n=-0.393254, w0=(587.271,'kJ/mol'), E0=(89.7327,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1228139103182426, var=0.43648628781354337, Tref=1000.0, N=35, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H',), comment="""BM rule fitted to 35 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H
    Total Standard Deviation in ln(k): 1.633048170813853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 35 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H
Total Standard Deviation in ln(k): 1.633048170813853""",
    longDesc = 
"""
BM rule fitted to 35 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H
Total Standard Deviation in ln(k): 1.633048170813853
""",
)

entry(
    index = 6,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.03325e+08,'m^3/(mol*s)'), n=-0.10198, w0=(502.214,'kJ/mol'), E0=(80.978,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.040303452153434116, var=0.44269224600189444, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 14 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 1.4351178847502755"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 1.4351178847502755""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 1.4351178847502755
""",
)

entry(
    index = 7,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.12169e+08,'m^3/(mol*s)'), n=-0.154964, w0=(502.944,'kJ/mol'), E0=(84.3246,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05546314533673813, var=0.2444209731576579, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R
    Total Standard Deviation in ln(k): 1.1304745998395005"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R
Total Standard Deviation in ln(k): 1.1304745998395005""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R
Total Standard Deviation in ln(k): 1.1304745998395005
""",
)

entry(
    index = 8,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(3.93828e+07,'m^3/(mol*s)'), n=2.18518e-08, w0=(502.625,'kJ/mol'), E0=(69.1925,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.9910962214145728e-08, var=0.09662781974709742, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl
    Total Standard Deviation in ln(k): 0.6231722624186179"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl
Total Standard Deviation in ln(k): 0.6231722624186179""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl
Total Standard Deviation in ln(k): 0.6231722624186179
""",
)

entry(
    index = 9,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.33333e+07,'m^3/(mol*s)'), n=-3.43268e-08, w0=(505.5,'kJ/mol'), E0=(81.7025,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=9.978460642146985e-10, var=9.686420317913478e-19, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R
    Total Standard Deviation in ln(k): 4.480203429618348e-09"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R
Total Standard Deviation in ln(k): 4.480203429618348e-09""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R
Total Standard Deviation in ln(k): 4.480203429618348e-09
""",
)

entry(
    index = 10,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.33333e+07,'m^3/(mol*s)'), n=1.64263e-09, w0=(505.5,'kJ/mol'), E0=(80.577,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=9.815060341590657e-10, var=3.386629381064704e-17, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.4132602008860625e-08"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.4132602008860625e-08""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.4132602008860625e-08
""",
)

entry(
    index = 11,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.33333e+07,'m^3/(mol*s)'), n=1.26221e-08, w0=(505.5,'kJ/mol'), E0=(80.0465,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-1R!H-R_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.9685e+07,'m^3/(mol*s)'), n=1.16228e-07, w0=(501.667,'kJ/mol'), E0=(65.0019,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.8958119496026825e-09, var=0.36033976299573556, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.2034085296664583"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.2034085296664583""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.2034085296664583
""",
)

entry(
    index = 13,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=1.49851e-09, w0=(505.5,'kJ/mol'), E0=(77.9047,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(2.5e+07,'m^3/(mol*s)'), n=-5.10956e-09, w0=(505.5,'kJ/mol'), E0=(80.5928,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=2.26005e-09, w0=(494,'kJ/mol'), E0=(71.8025,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Ext-2R!H-R_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=3.05625e-08, w0=(505.5,'kJ/mol'), E0=(83.5404,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=2.47284e-08, w0=(494,'kJ/mol'), E0=(79.2905,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_5R!H->Cl_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.41e+15,'m^3/(mol*s)'), n=-2.4, w0=(505.5,'kJ/mol'), E0=(105.001,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-1R!H-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.22097e+08,'m^3/(mol*s)'), n=-0.174178, w0=(501.667,'kJ/mol'), E0=(85.7864,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0625192598659511, var=0.4370683036957412, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.4824368122077785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.4824368122077785""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.4824368122077785
""",
)

entry(
    index = 20,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=6.19306e-09, w0=(505.5,'kJ/mol'), E0=(76.7391,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=-1.34015e-08, w0=(505.5,'kJ/mol'), E0=(79.1532,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=9.09485e-09, w0=(494,'kJ/mol'), E0=(74.9095,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=-2.2307e-08, w0=(505.5,'kJ/mol'), E0=(81.301,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=1.35671e-08, w0=(494,'kJ/mol'), E0=(81.2051,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s",
    kinetics = ArrheniusBM(A=(8.95305e+10,'m^3/(mol*s)'), n=-1.20015, w0=(643.976,'kJ/mol'), E0=(85.1517,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06441072249882406, var=0.5712339948626487, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s',), comment="""BM rule fitted to 21 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s
    Total Standard Deviation in ln(k): 1.6770152283032176"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 1.6770152283032176""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s
Total Standard Deviation in ln(k): 1.6770152283032176
""",
)

entry(
    index = 26,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(4.50652e+09,'m^3/(mol*s)'), n=-0.832314, w0=(633.333,'kJ/mol'), E0=(74.778,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4937709993731696, var=1.0096303708572736, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.2549957705541632"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.2549957705541632""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.2549957705541632
""",
)

entry(
    index = 27,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(5.20896e+09,'m^3/(mol*s)'), n=-0.851264, w0=(630.611,'kJ/mol'), E0=(75.3515,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7728621156845847, var=1.8845588549103955, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 4.693949603944338"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 4.693949603944338""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 4.693949603944338
""",
)

entry(
    index = 28,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(5.67638e+14,'m^3/(mol*s)'), n=-2.29036, w0=(619.417,'kJ/mol'), E0=(103.603,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5353761637582248, var=0.9750981963182922, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 3.3247832009256264"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 3.3247832009256264""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 3.3247832009256264
""",
)

entry(
    index = 29,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s",
    kinetics = ArrheniusBM(A=(6.69272e+10,'m^3/(mol*s)'), n=-1.30512, w0=(653,'kJ/mol'), E0=(64.1808,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2188447984073878, var=0.4569718037946039, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s
    Total Standard Deviation in ln(k): 1.9050559927345736"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s
Total Standard Deviation in ln(k): 1.9050559927345736""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s
Total Standard Deviation in ln(k): 1.9050559927345736
""",
)

entry(
    index = 30,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.94372e+10,'m^3/(mol*s)'), n=-1.22042, w0=(653,'kJ/mol'), E0=(58.2674,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1299023321238748, var=1.4143168727338034, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R
    Total Standard Deviation in ln(k): 2.710520064285751"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.710520064285751""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.710520064285751
""",
)

entry(
    index = 31,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.41e+15,'m^3/(mol*s)'), n=-2.4, w0=(653,'kJ/mol'), E0=(98.8175,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-1R!H-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.81e+16,'m^3/(mol*s)'), n=-2.92, w0=(653,'kJ/mol'), E0=(110.558,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_3Br1sF1s->F1s_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_N-3Br1sF1s->F1s",
    kinetics = ArrheniusBM(A=(1.41e+15,'m^3/(mol*s)'), n=-2.4, w0=(451.5,'kJ/mol'), E0=(103.865,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_N-3Br1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_N-3Br1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_N-3Br1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-1R!H-R_N-3Br1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.36e+13,'m^3/(mol*s)'), n=-2.26, w0=(653,'kJ/mol'), E0=(111.917,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07813132049106332, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 0.19630985048005858"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.19630985048005858""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_Sp-2R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 0.19630985048005858
""",
)

entry(
    index = 35,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(1.03371e+09,'m^3/(mol*s)'), n=-0.586164, w0=(641.5,'kJ/mol'), E0=(60.7739,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0816367458039413, var=0.6069530552278367, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.7669502559269081"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.7669502559269081""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.7669502559269081
""",
)

entry(
    index = 36,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_5R!H->C",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=-2.23028e-08, w0=(641.5,'kJ/mol'), E0=(113.162,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.44914e+11,'m^3/(mol*s)'), n=-1.38082, w0=(641.5,'kJ/mol'), E0=(64.2735,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2338061258533221, var=2.299491898063646, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C
    Total Standard Deviation in ln(k): 3.62744801131415"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 3.62744801131415""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C
Total Standard Deviation in ln(k): 3.62744801131415
""",
)

entry(
    index = 38,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(5.98e+14,'m^3/(mol*s)'), n=-2.31, w0=(641.5,'kJ/mol'), E0=(86.0231,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Ext-2R!H-R_N-Sp-2R!H-1R!H_N-5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(1.79842e+11,'m^3/(mol*s)'), n=-1.13254, w0=(671.5,'kJ/mol'), E0=(98.5833,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12263120431107348, var=0.8948267901291818, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 2.204503459202596"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.204503459202596""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.204503459202596
""",
)

entry(
    index = 40,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C",
    kinetics = ArrheniusBM(A=(1.42287e+10,'m^3/(mol*s)'), n=-0.866872, w0=(653,'kJ/mol'), E0=(67.0371,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0660571009065518, var=0.31018649060097847, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C
    Total Standard Deviation in ln(k): 1.2824975569546164"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C
Total Standard Deviation in ln(k): 1.2824975569546164""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C
Total Standard Deviation in ln(k): 1.2824975569546164
""",
)

entry(
    index = 41,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(6.27455e+09,'m^3/(mol*s)'), n=-0.729798, w0=(653,'kJ/mol'), E0=(64.5891,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13295319317704554, var=0.5428838170112513, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 1.811155083043796"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 1.811155083043796""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 1.811155083043796
""",
)

entry(
    index = 42,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.12e+15,'m^3/(mol*s)'), n=-2.27, w0=(653,'kJ/mol'), E0=(101.252,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_2R!H->C_Ext-1R!H-R_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=1.66049e-08, w0=(745.5,'kJ/mol'), E0=(107.344,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_Sp-2R!H-1R!H_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(3.59692e+09,'m^3/(mol*s)'), n=-0.781097, w0=(641.5,'kJ/mol'), E0=(76.0636,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06741528248568733, var=0.5918026928294308, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.7116020317652383"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.7116020317652383""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.7116020317652383
""",
)

entry(
    index = 45,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(8.20454e+08,'m^3/(mol*s)'), n=-0.586164, w0=(641.5,'kJ/mol'), E0=(70.9761,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.16983012841985937, var=1.1065354841142325, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 2.535529595232204"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.535529595232204""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 2.535529595232204
""",
)

entry(
    index = 46,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=6.07668e-08, w0=(641.5,'kJ/mol'), E0=(112.867,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.2285e+14,'m^3/(mol*s)'), n=-2.31, w0=(641.5,'kJ/mol'), E0=(97.8702,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.06795930538824446, var=0.9609060278364121, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 2.1359099087012114"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 2.1359099087012114""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->H_N-3Br1sCl1sF1s->Cl1s_N-Sp-2R!H-1R!H_Ext-1R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 2.1359099087012114
""",
)

entry(
    index = 48,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->H",
    kinetics = ArrheniusBM(A=(5.29656e+06,'m^3/(mol*s)'), n=6.89479e-08, w0=(412.084,'kJ/mol'), E0=(25.2371,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0004135414209481112, var=0.3980628128928112, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->H',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H
    Total Standard Deviation in ln(k): 1.2658708990546865"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H
Total Standard Deviation in ln(k): 1.2658708990546865""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H
Total Standard Deviation in ln(k): 1.2658708990546865
""",
)

entry(
    index = 49,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(8.16667e+06,'m^3/(mol*s)'), n=-1.28088e-09, w0=(406.21,'kJ/mol'), E0=(31.8129,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.054061953889780405, var=0.005845390032469305, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 0.28910637698202857"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 0.28910637698202857""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 0.28910637698202857
""",
)

entry(
    index = 50,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H_4BrClO->Br",
    kinetics = ArrheniusBM(A=(8.16667e+06,'m^3/(mol*s)'), n=-6.98157e-09, w0=(400.92,'kJ/mol'), E0=(31.7182,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H_4BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H_4BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H_4BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H_4BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H_N-4BrClO->Br",
    kinetics = ArrheniusBM(A=(8.16667e+06,'m^3/(mol*s)'), n=3.46973e-09, w0=(411.5,'kJ/mol'), E0=(37.7732,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H_N-4BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H_N-4BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H_N-4BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_Sp-2R!H-1R!H_N-4BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(3.9685e+06,'m^3/(mol*s)'), n=-1.66185e-08, w0=(416,'kJ/mol'), E0=(22.9494,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0630306970104995, var=0.43779269755804645, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.48481969091724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.48481969091724""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.48481969091724
""",
)

entry(
    index = 53,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2.5e+06,'m^3/(mol*s)'), n=-3.27277e-09, w0=(416,'kJ/mol'), E0=(34.8602,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=-3.46141e-09, w0=(416,'kJ/mol'), E0=(30.1176,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->H_N-Sp-2R!H-1R!H_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

