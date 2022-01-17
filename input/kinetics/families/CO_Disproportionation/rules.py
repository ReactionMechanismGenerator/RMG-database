#!/usr/bin/env python
# encoding: utf-8

name = "CO_Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.33361e+08,'m^3/(mol*s)'), n=-0.309595, w0=(538.545,'kJ/mol'), E0=(51.3789,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05864831349114651, var=1.6783203272344693, Tref=1000.0, N=33, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 33 training reactions at node Root
    Total Standard Deviation in ln(k): 2.7444919241085404"""),
    rank = 11,
    shortDesc = """BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 2.7444919241085404""",
    longDesc = 
"""
BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 2.7444919241085404
""",
)

entry(
    index = 2,
    label = "Root_4R->F",
    kinetics = ArrheniusBM(A=(1.08671e+13,'m^3/(mol*s)'), n=-2.00013, w0=(540.5,'kJ/mol'), E0=(84.1736,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.649709551522148, var=0.15840278009985914, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->F',), comment="""BM rule fitted to 2 training reactions at node Root_4R->F
    Total Standard Deviation in ln(k): 9.968005989776463"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->F
Total Standard Deviation in ln(k): 9.968005989776463""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->F
Total Standard Deviation in ln(k): 9.968005989776463
""",
)

entry(
    index = 3,
    label = "Root_4R->F_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.56076e+06,'m^3/(mol*s)'), n=-0.37188, w0=(456.5,'kJ/mol'), E0=(52.9398,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->F_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_4R->F_2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->F_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->F_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_4R->F_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=-8.59568e-09, w0=(624.5,'kJ/mol'), E0=(114.655,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->F_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_4R->F_N-2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->F_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->F_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_N-4R->F",
    kinetics = ArrheniusBM(A=(2.33024e+08,'m^3/(mol*s)'), n=-0.309399, w0=(538.419,'kJ/mol'), E0=(51.3644,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05856825840630382, var=1.6788781475150028, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_N-4R->F',), comment="""BM rule fitted to 31 training reactions at node Root_N-4R->F
    Total Standard Deviation in ln(k): 2.744722347237623"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 2.744722347237623""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 2.744722347237623
""",
)

entry(
    index = 6,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.75239e+08,'m^3/(mol*s)'), n=-0.314126, w0=(552.375,'kJ/mol'), E0=(46.5938,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.010652616159008355, var=1.725812679743883, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R',), comment="""BM rule fitted to 20 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R
    Total Standard Deviation in ln(k): 2.660389645633036"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R
Total Standard Deviation in ln(k): 2.660389645633036""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R
Total Standard Deviation in ln(k): 2.660389645633036
""",
)

entry(
    index = 7,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_2Br1sCl1sF1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.5e+06,'m^3/(mol*s)'), n=2.69671e-08, w0=(463.5,'kJ/mol'), E0=(99.9016,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_2Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_2Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.75359e+08,'m^3/(mol*s)'), n=-0.314203, w0=(557.053,'kJ/mol'), E0=(46.6117,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.010595416104297059, var=1.7254871020785956, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 19 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 2.659997496207455"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 2.659997496207455""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 2.659997496207455
""",
)

entry(
    index = 9,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(9.47741e+17,'m^3/(mol*s)'), n=-3.53908, w0=(555.5,'kJ/mol'), E0=(94.7032,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6550614866404488, var=2.25204580030794, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R
    Total Standard Deviation in ln(k): 4.654352533618259"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.654352533618259""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.654352533618259
""",
)

entry(
    index = 10,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(6e+07,'m^3/(mol*s)'), n=-6.14542e-09, w0=(547.5,'kJ/mol'), E0=(83.1557,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.15372e+17,'m^3/(mol*s)'), n=-3.28099, w0=(559.5,'kJ/mol'), E0=(90.3331,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.5684434627638923, var=12.28832750633438, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 13.480916375343327"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 13.480916375343327""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 13.480916375343327
""",
)

entry(
    index = 12,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C_4BrCClHINOPSSi->C",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=-9.63322e-09, w0=(547.5,'kJ/mol'), E0=(96.3337,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C_4BrCClHINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C_4BrCClHINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C_4BrCClHINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C_4BrCClHINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C_N-4BrCClHINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.24e+17,'m^3/(mol*s)'), n=-3.29, w0=(571.5,'kJ/mol'), E0=(90.5728,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C_N-4BrCClHINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C_N-4BrCClHINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C_N-4BrCClHINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_Ext-5R!H-R_N-6R!H->C_N-4BrCClHINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C",
    kinetics = ArrheniusBM(A=(7.92257e+07,'m^3/(mol*s)'), n=-0.00236169, w0=(553.5,'kJ/mol'), E0=(93.7216,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0031797954615440265, var=1.0712626414179376, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C
    Total Standard Deviation in ln(k): 2.082926695239342"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C
Total Standard Deviation in ln(k): 2.082926695239342""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C
Total Standard Deviation in ln(k): 2.082926695239342
""",
)

entry(
    index = 15,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Ext-4BrCClHINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.2e+08,'m^3/(mol*s)'), n=-1.49446e-08, w0=(547.5,'kJ/mol'), E0=(80.4398,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Ext-4BrCClHINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Ext-4BrCClHINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Ext-4BrCClHINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Ext-4BrCClHINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi",
    kinetics = ArrheniusBM(A=(6.45242e+07,'m^3/(mol*s)'), n=0.00464431, w0=(559.5,'kJ/mol'), E0=(93.7216,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.7580366833041802e-09, var=1.100942056497115, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi
    Total Standard Deviation in ln(k): 2.103484041328291"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi
Total Standard Deviation in ln(k): 2.103484041328291""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi
Total Standard Deviation in ln(k): 2.103484041328291
""",
)

entry(
    index = 17,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi_4BrCClHINOPSSi->C",
    kinetics = ArrheniusBM(A=(4.3e+07,'m^3/(mol*s)'), n=7.322e-09, w0=(547.5,'kJ/mol'), E0=(82.6965,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi_4BrCClHINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi_4BrCClHINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi_4BrCClHINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi_4BrCClHINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi_N-4BrCClHINOPSSi->C",
    kinetics = ArrheniusBM(A=(9.03e+07,'m^3/(mol*s)'), n=-2.02476e-08, w0=(571.5,'kJ/mol'), E0=(86.6954,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi_N-4BrCClHINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi_N-4BrCClHINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi_N-4BrCClHINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_Sp-5C-4BrCClHINOPSSi_N-4BrCClHINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_N-Sp-5C-4BrCClHINOPSSi",
    kinetics = ArrheniusBM(A=(9.033e+07,'m^3/(mol*s)'), n=-1.66781e-08, w0=(547.5,'kJ/mol'), E0=(91.3422,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_N-Sp-5C-4BrCClHINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_N-Sp-5C-4BrCClHINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_N-Sp-5C-4BrCClHINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_5R!H->C_N-Sp-5C-4BrCClHINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C",
    kinetics = ArrheniusBM(A=(5.01833e+06,'m^3/(mol*s)'), n=0.144257, w0=(558.625,'kJ/mol'), E0=(39.6098,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.031627792693989576, var=0.7528364484010184, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C
    Total Standard Deviation in ln(k): 1.818898225301531"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C
Total Standard Deviation in ln(k): 1.818898225301531""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C
Total Standard Deviation in ln(k): 1.818898225301531
""",
)

entry(
    index = 21,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F",
    kinetics = ArrheniusBM(A=(3.90964e+07,'m^3/(mol*s)'), n=0.00827539, w0=(559.833,'kJ/mol'), E0=(89.1574,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03271880195959781, var=0.9745266199843224, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F
    Total Standard Deviation in ln(k): 2.0612447212958087"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F
Total Standard Deviation in ln(k): 2.0612447212958087""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F
Total Standard Deviation in ln(k): 2.0612447212958087
""",
)

entry(
    index = 22,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_2F1sH->F1s",
    kinetics = ArrheniusBM(A=(2.23e+07,'m^3/(mol*s)'), n=2.19991e-09, w0=(621.5,'kJ/mol'), E0=(90.0734,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_2F1sH->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_2F1sH->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_2F1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_2F1sH->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s",
    kinetics = ArrheniusBM(A=(3.74373e+11,'m^3/(mol*s)'), n=-1.13618, w0=(547.5,'kJ/mol'), E0=(106.144,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17783637696686197, var=0.7103023877912675, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s
    Total Standard Deviation in ln(k): 2.1364045491484918"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s
Total Standard Deviation in ln(k): 2.1364045491484918""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s
Total Standard Deviation in ln(k): 2.1364045491484918
""",
)

entry(
    index = 24,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R",
    kinetics = ArrheniusBM(A=(5.39841e+07,'m^3/(mol*s)'), n=0.0112234, w0=(547.5,'kJ/mol'), E0=(94.341,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06853172317168153, var=2.6111630214932533, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R
    Total Standard Deviation in ln(k): 3.411660411384654"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R
Total Standard Deviation in ln(k): 3.411660411384654""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R
Total Standard Deviation in ln(k): 3.411660411384654
""",
)

entry(
    index = 25,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_6R!H->Cl",
    kinetics = ArrheniusBM(A=(1.5e+07,'m^3/(mol*s)'), n=1.09487e-08, w0=(547.5,'kJ/mol'), E0=(78.6888,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_6R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_6R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_6R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl",
    kinetics = ArrheniusBM(A=(9e+07,'m^3/(mol*s)'), n=-2.44236e-09, w0=(547.5,'kJ/mol'), E0=(83.8218,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.0692985756485417e-09, var=3.070154873043183e-17, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl
    Total Standard Deviation in ln(k): 1.63072748866403e-08"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 1.63072748866403e-08""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl
Total Standard Deviation in ln(k): 1.63072748866403e-08
""",
)

entry(
    index = 27,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl_Ext-4BrCClHINOPSSi-R",
    kinetics = ArrheniusBM(A=(9e+07,'m^3/(mol*s)'), n=-7.25758e-09, w0=(547.5,'kJ/mol'), E0=(86.9454,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl_Ext-4BrCClHINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl_Ext-4BrCClHINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl_Ext-4BrCClHINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_5BrClFNO->F_N-2F1sH->F1s_Ext-4BrCClHINOPSSi-R_N-6R!H->Cl_Ext-4BrCClHINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F",
    kinetics = ArrheniusBM(A=(5.00624e+06,'m^3/(mol*s)'), n=0.144526, w0=(557.417,'kJ/mol'), E0=(39.592,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.031762824178166255, var=0.7521626821211684, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F
    Total Standard Deviation in ln(k): 1.818458956409249"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F
Total Standard Deviation in ln(k): 1.818458956409249""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F
Total Standard Deviation in ln(k): 1.818458956409249
""",
)

entry(
    index = 29,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_5BrClO->Br",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=-1.15233e-08, w0=(571.5,'kJ/mol'), E0=(80.71,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_5BrClO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_5BrClO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_5BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_5BrClO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br",
    kinetics = ArrheniusBM(A=(5.00756e+06,'m^3/(mol*s)'), n=0.1445, w0=(554.6,'kJ/mol'), E0=(39.5844,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03172617151314118, var=0.7523035110252831, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br
    Total Standard Deviation in ln(k): 1.8185296223725322"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br
Total Standard Deviation in ln(k): 1.8185296223725322""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br
Total Standard Deviation in ln(k): 1.8185296223725322
""",
)

entry(
    index = 31,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O",
    kinetics = ArrheniusBM(A=(4.90664e+07,'m^3/(mol*s)'), n=0.00528452, w0=(571.5,'kJ/mol'), E0=(52.975,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.580305765337455, var=4.65409296700803, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O
    Total Standard Deviation in ln(k): 10.808064842723315"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 10.808064842723315""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 10.808064842723315
""",
)

entry(
    index = 32,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O_5ClO->O",
    kinetics = ArrheniusBM(A=(5.12e+07,'m^3/(mol*s)'), n=-6.78941e-08, w0=(571.5,'kJ/mol'), E0=(53.0527,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O_5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O_5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O_5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O_5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O_N-5ClO->O",
    kinetics = ArrheniusBM(A=(3.2e+07,'m^3/(mol*s)'), n=2.49092e-08, w0=(571.5,'kJ/mol'), E0=(77.9587,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O_N-5ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O_N-5ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_4BrCClHINOPSSi->O_N-5ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O",
    kinetics = ArrheniusBM(A=(5.24514e+07,'m^3/(mol*s)'), n=-0.196046, w0=(543.333,'kJ/mol'), E0=(48.7677,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14105511612367885, var=0.42089153333875484, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O
    Total Standard Deviation in ln(k): 1.6550048518322276"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 1.6550048518322276""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 1.6550048518322276
""",
)

entry(
    index = 35,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C",
    kinetics = ArrheniusBM(A=(1.34164e+07,'m^3/(mol*s)'), n=3.06259e-08, w0=(547.5,'kJ/mol'), E0=(55.8558,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.08754115351393721, var=0.9121353074708806, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C
    Total Standard Deviation in ln(k): 2.13459042109891"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C
Total Standard Deviation in ln(k): 2.13459042109891""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C
Total Standard Deviation in ln(k): 2.13459042109891
""",
)

entry(
    index = 36,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C_Sp-5ClO-4C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=1.01362e-08, w0=(547.5,'kJ/mol'), E0=(78.8139,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C_Sp-5ClO-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C_Sp-5ClO-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C_Sp-5ClO-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C_Sp-5ClO-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C_N-Sp-5ClO-4C",
    kinetics = ArrheniusBM(A=(1.8e+07,'m^3/(mol*s)'), n=2.65791e-08, w0=(547.5,'kJ/mol'), E0=(71.238,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C_N-Sp-5ClO-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C_N-Sp-5ClO-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C_N-Sp-5ClO-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_4CN->C_N-Sp-5ClO-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->C",
    kinetics = ArrheniusBM(A=(7.1e+06,'m^3/(mol*s)'), n=-2.84625e-09, w0=(535,'kJ/mol'), E0=(33.6654,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_Ext-4BrCClHINOPSSi-R_N-2Br1sCl1sF1sHI1s->Cl1s_N-5R!H->C_N-5BrClFNO->F_N-5BrClO->Br_N-4BrCClHINOPSSi->O_N-4CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-4R->F_4BrCClHINOPSSi->O",
    kinetics = ArrheniusBM(A=(4.03705e+07,'m^3/(mol*s)'), n=-0.0402969, w0=(481.167,'kJ/mol'), E0=(68.8474,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.2998898630423388, var=6.539834357495051, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O
    Total Standard Deviation in ln(k): 10.905346776298199"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 10.905346776298199""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 10.905346776298199
""",
)

entry(
    index = 40,
    label = "Root_N-4R->F_4BrCClHINOPSSi->O_4O-u1",
    kinetics = ArrheniusBM(A=(3.3e+06,'m^3/(mol*s)'), n=1.00706e-08, w0=(436,'kJ/mol'), E0=(47.0391,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O_4O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_4O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_4O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_4O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1",
    kinetics = ArrheniusBM(A=(3.12378e+07,'m^3/(mol*s)'), n=-8.40405e-08, w0=(503.75,'kJ/mol'), E0=(40.7319,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0857911500003818, var=6.906821833814157, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1
    Total Standard Deviation in ln(k): 7.996729245952894"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1
Total Standard Deviation in ln(k): 7.996729245952894""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1
Total Standard Deviation in ln(k): 7.996729245952894
""",
)

entry(
    index = 42,
    label = "Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1_2Br1sCl1sF1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=-3.94335e-09, w0=(436,'kJ/mol'), E0=(53.781,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1_2Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1_2Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1_2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1_2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1_N-2Br1sCl1sF1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(3.01e+07,'m^3/(mol*s)'), n=-2.09368e-08, w0=(571.5,'kJ/mol'), E0=(84.5214,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1_N-2Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1_N-2Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1_N-2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_4BrCClHINOPSSi->O_N-4O-u1_N-2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O",
    kinetics = ArrheniusBM(A=(6.00686e+07,'m^3/(mol*s)'), n=0.000112225, w0=(525,'kJ/mol'), E0=(36.2756,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.00018576552062254652, var=1.3235720018631436, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O
    Total Standard Deviation in ln(k): 2.306846279764352"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 2.306846279764352""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O
Total Standard Deviation in ln(k): 2.306846279764352
""",
)

entry(
    index = 45,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.5e+07,'m^3/(mol*s)'), n=-1.46201e-08, w0=(661.5,'kJ/mol'), E0=(97.4612,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(6.00716e+07,'m^3/(mol*s)'), n=0.000117761, w0=(505.5,'kJ/mol'), E0=(33.0773,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0002752228620664441, var=1.3240886895969493, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 2.307521178013977"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 2.307521178013977""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 2.307521178013977
""",
)

entry(
    index = 47,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_4BrCClHN->C",
    kinetics = ArrheniusBM(A=(4e+07,'m^3/(mol*s)'), n=1.83841e-08, w0=(547.5,'kJ/mol'), E0=(86.287,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_4BrCClHN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_4BrCClHN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_4BrCClHN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_4BrCClHN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C",
    kinetics = ArrheniusBM(A=(9.01885e+07,'m^3/(mol*s)'), n=0.000218269, w0=(498.5,'kJ/mol'), E0=(52.0352,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.45271294379919386, var=0.9153354832685294, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C
    Total Standard Deviation in ln(k): 3.0554632411847225"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C
Total Standard Deviation in ln(k): 3.0554632411847225""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C
Total Standard Deviation in ln(k): 3.0554632411847225
""",
)

entry(
    index = 49,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H",
    kinetics = ArrheniusBM(A=(9.03018e+07,'m^3/(mol*s)'), n=1.07416e-07, w0=(536,'kJ/mol'), E0=(86.859,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10199109315961442, var=0.020821356062487906, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H
    Total Standard Deviation in ln(k): 0.5455344228005681"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H
Total Standard Deviation in ln(k): 0.5455344228005681""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H
Total Standard Deviation in ln(k): 0.5455344228005681
""",
)

entry(
    index = 50,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H_2Cl1sH->Cl1s",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=-2.4084e-08, w0=(514,'kJ/mol'), E0=(90.793,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H_2Cl1sH->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H_2Cl1sH->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H_2Cl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H_2Cl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H_N-2Cl1sH->Cl1s",
    kinetics = ArrheniusBM(A=(9.03e+07,'m^3/(mol*s)'), n=1.9881e-08, w0=(558,'kJ/mol'), E0=(85.6289,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H_N-2Cl1sH->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H_N-2Cl1sH->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H_N-2Cl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_4BrClH->H_N-2Cl1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H",
    kinetics = ArrheniusBM(A=(1.9633e+08,'m^3/(mol*s)'), n=-0.0207328, w0=(479.75,'kJ/mol'), E0=(66.1054,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.013799724606027793, var=2.202535911920206, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H
    Total Standard Deviation in ln(k): 3.009888590192312"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H
Total Standard Deviation in ln(k): 3.009888590192312""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H
Total Standard Deviation in ln(k): 3.009888590192312
""",
)

entry(
    index = 53,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_2Cl1sH->Cl1s",
    kinetics = ArrheniusBM(A=(1.62578e+08,'m^3/(mol*s)'), n=-7.54378e-05, w0=(420,'kJ/mol'), E0=(64.7552,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0461730789386792, var=8.801412695919307, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_2Cl1sH->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_2Cl1sH->Cl1s
    Total Standard Deviation in ln(k): 6.063495388361434"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_2Cl1sH->Cl1s
Total Standard Deviation in ln(k): 6.063495388361434""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_2Cl1sH->Cl1s
Total Standard Deviation in ln(k): 6.063495388361434
""",
)

entry(
    index = 54,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s",
    kinetics = ArrheniusBM(A=(1.7e+08,'m^3/(mol*s)'), n=2.09814e-09, w0=(539.5,'kJ/mol'), E0=(73.7231,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20750976509986754, var=0.08612060524197436, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s
    Total Standard Deviation in ln(k): 1.1096971382723972"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s
Total Standard Deviation in ln(k): 1.1096971382723972""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s
Total Standard Deviation in ln(k): 1.1096971382723972
""",
)

entry(
    index = 55,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_4BrCl->Cl",
    kinetics = ArrheniusBM(A=(1.7e+08,'m^3/(mol*s)'), n=2.50869e-08, w0=(556,'kJ/mol'), E0=(84.6674,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_4BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_4BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_N-4BrCl->Cl",
    kinetics = ArrheniusBM(A=(1.7e+08,'m^3/(mol*s)'), n=-8.68792e-11, w0=(523,'kJ/mol'), E0=(70.0941,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_N-4BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_N-4BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_N-4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-4BrCClHINOPSSi->O_N-2Br1sCl1sF1sHI1s->F1s_N-4BrCClHN->C_N-4BrClH->H_N-2Cl1sH->Cl1s_N-4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

