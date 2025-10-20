#!/usr/bin/env python
# encoding: utf-8

name = "PFAS_Hydrolysis/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(6.82721e-14,'m^3/(mol*s)'), n=5.25938, w0=(903929,'J/mol'), E0=(235805,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4646463729602328, var=131.60332055086977, Tref=1000.0, N=21, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 21 training reactions at node Root
    Total Standard Deviation in ln(k): 24.165471384934747"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root
Total Standard Deviation in ln(k): 24.165471384934747""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root
Total Standard Deviation in ln(k): 24.165471384934747
""",
)

entry(
    index = 2,
    label = "Root_3F1sH->F1s",
    kinetics = ArrheniusBM(A=(1.43026e-06,'m^3/(mol*s)'), n=3.12585, w0=(933500,'J/mol'), E0=(217653,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23400338658700143, var=96.14909818319292, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_3F1sH->F1s',), comment="""BM rule fitted to 15 training reactions at node Root_3F1sH->F1s
    Total Standard Deviation in ln(k): 20.245507622975488"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_3F1sH->F1s
Total Standard Deviation in ln(k): 20.245507622975488""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_3F1sH->F1s
Total Standard Deviation in ln(k): 20.245507622975488
""",
)

entry(
    index = 3,
    label = "Root_N-3F1sH->F1s",
    kinetics = ArrheniusBM(A=(7.86483e-18,'m^3/(mol*s)'), n=6.47761, w0=(830000,'J/mol'), E0=(316919,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.647119322044097, var=99.09415561292235, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3F1sH->F1s',), comment="""BM rule fitted to 6 training reactions at node Root_N-3F1sH->F1s
    Total Standard Deviation in ln(k): 21.58227325709331"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3F1sH->F1s
Total Standard Deviation in ln(k): 21.58227325709331""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3F1sH->F1s
Total Standard Deviation in ln(k): 21.58227325709331
""",
)

entry(
    index = 4,
    label = "Root_3F1sH->F1s_4R->F",
    kinetics = ArrheniusBM(A=(7.89242e-07,'m^3/(mol*s)'), n=3.21411, w0=(933500,'J/mol'), E0=(305935,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14236738744733418, var=184.8857697350717, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F',), comment="""BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_4R->F
    Total Standard Deviation in ln(k): 27.61663247716592"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_4R->F
Total Standard Deviation in ln(k): 27.61663247716592""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_4R->F
Total Standard Deviation in ln(k): 27.61663247716592
""",
)

entry(
    index = 5,
    label = "Root_3F1sH->F1s_N-4R->F",
    kinetics = ArrheniusBM(A=(3.59181e-07,'m^3/(mol*s)'), n=3.2926, w0=(933500,'J/mol'), E0=(183792,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.28430112644983524, var=28.68408588442464, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F',), comment="""BM rule fitted to 11 training reactions at node Root_3F1sH->F1s_N-4R->F
    Total Standard Deviation in ln(k): 11.451189536143948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_3F1sH->F1s_N-4R->F
Total Standard Deviation in ln(k): 11.451189536143948""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_3F1sH->F1s_N-4R->F
Total Standard Deviation in ln(k): 11.451189536143948
""",
)

entry(
    index = 6,
    label = "Root_N-3F1sH->F1s_4R->H",
    kinetics = ArrheniusBM(A=(3.78101e-15,'m^3/(mol*s)'), n=5.78564, w0=(830000,'J/mol'), E0=(360667,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5437450455495092, var=93.72082303415847, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3F1sH->F1s_4R->H',), comment="""BM rule fitted to 4 training reactions at node Root_N-3F1sH->F1s_4R->H
    Total Standard Deviation in ln(k): 20.773936749119244"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3F1sH->F1s_4R->H
Total Standard Deviation in ln(k): 20.773936749119244""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3F1sH->F1s_4R->H
Total Standard Deviation in ln(k): 20.773936749119244
""",
)

entry(
    index = 7,
    label = "Root_N-3F1sH->F1s_N-4R->H",
    kinetics = ArrheniusBM(A=(3.27443e-13,'m^3/(mol*s)'), n=5.0012, w0=(830000,'J/mol'), E0=(254455,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.576321192966173, var=0.8032918215985783, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3F1sH->F1s_N-4R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_N-4R->H
    Total Standard Deviation in ln(k): 3.2448180570772545"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_N-4R->H
Total Standard Deviation in ln(k): 3.2448180570772545""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_N-4R->H
Total Standard Deviation in ln(k): 3.2448180570772545
""",
)

entry(
    index = 8,
    label = "Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.05094e-07,'m^3/(mol*s)'), n=3.44969, w0=(933500,'J/mol'), E0=(350462,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11189665124220663, var=0.17688268050836667, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 1.1242872706635874"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.1242872706635874""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.1242872706635874
""",
)

entry(
    index = 9,
    label = "Root_3F1sH->F1s_N-4R->F_4CH->H",
    kinetics = ArrheniusBM(A=(3.68827e-06,'m^3/(mol*s)'), n=3.1992, w0=(933500,'J/mol'), E0=(232649,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17573628211819967, var=64.43688148616403, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_4CH->H',), comment="""BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H
    Total Standard Deviation in ln(k): 16.534075445017415"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H
Total Standard Deviation in ln(k): 16.534075445017415""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H
Total Standard Deviation in ln(k): 16.534075445017415
""",
)

entry(
    index = 10,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H",
    kinetics = ArrheniusBM(A=(1.75742e-09,'m^3/(mol*s)'), n=3.84234, w0=(933500,'J/mol'), E0=(151485,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3889347793999542, var=2.851040629309004, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H',), comment="""BM rule fitted to 7 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H
    Total Standard Deviation in ln(k): 4.362223216320071"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H
Total Standard Deviation in ln(k): 4.362223216320071""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H
Total Standard Deviation in ln(k): 4.362223216320071
""",
)

entry(
    index = 11,
    label = "Root_N-3F1sH->F1s_4R->H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.2318e-16,'m^3/(mol*s)'), n=5.89861, w0=(830000,'J/mol'), E0=(346478,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5821695507362918, var=167.64807135246494, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3F1sH->F1s_4R->H_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R
    Total Standard Deviation in ln(k): 27.41984353993678"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R
Total Standard Deviation in ln(k): 27.41984353993678""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R
Total Standard Deviation in ln(k): 27.41984353993678
""",
)

entry(
    index = 12,
    label = "Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R",
    kinetics = Arrhenius(A=(2.56e-13,'m^3/(mol*s)'), n=5.03, Ea=(241.31,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(3.75863e-08,'m^3/(mol*s)'), n=3.56448, w0=(933500,'J/mol'), E0=(343333,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12926701701687893, var=0.5979954658498232, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 1.8750564742577962"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 1.8750564742577962""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 1.8750564742577962
""",
)

entry(
    index = 14,
    label = "Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(6.1125e-06,'m^3/(mol*s)'), n=3.22, Ea=(360.945,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.23701e-06,'m^3/(mol*s)'), n=3.12799, w0=(933500,'J/mol'), E0=(219445,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19043643492197043, var=109.288690953402, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R
    Total Standard Deviation in ln(k): 21.436230898349724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R
Total Standard Deviation in ln(k): 21.436230898349724""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R
Total Standard Deviation in ln(k): 21.436230898349724
""",
)

entry(
    index = 16,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.63303e-09,'m^3/(mol*s)'), n=3.83601, w0=(933500,'J/mol'), E0=(154183,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.40397587267425245, var=1.4148391152270776, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R',), comment="""BM rule fitted to 6 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R
    Total Standard Deviation in ln(k): 3.399587185438597"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R
Total Standard Deviation in ln(k): 3.399587185438597""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R
Total Standard Deviation in ln(k): 3.399587185438597
""",
)

entry(
    index = 17,
    label = "Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(5.62741e-12,'m^3/(mol*s)'), n=4.88187, w0=(830000,'J/mol'), E0=(403251,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.43589851152997405, var=5.184484677090107, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 5.659896606344727"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 5.659896606344727""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 5.659896606344727
""",
)

entry(
    index = 18,
    label = "Root_N-3F1sH->F1s_4R->H_Ext-1C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(1.6075e-13,'m^3/(mol*s)'), n=5.03, Ea=(244.582,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3F1sH->F1s_4R->H_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_9R!H->C",
    kinetics = Arrhenius(A=(5.64167e-09,'m^3/(mol*s)'), n=3.77, Ea=(334.335,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_N-9R!H->C",
    kinetics = Arrhenius(A=(2.48333e-07,'m^3/(mol*s)'), n=3.36, Ea=(336.007,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.48217e-06,'m^3/(mol*s)'), n=3.2847, w0=(933500,'J/mol'), E0=(255143,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1540170364824897, var=1.3921655949535945, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 2.752365742891329"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 2.752365742891329""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 2.752365742891329
""",
)

entry(
    index = 22,
    label = "Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(4.305e-07,'m^3/(mol*s)'), n=3.26, Ea=(131.108,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.42581e-09,'m^3/(mol*s)'), n=3.84875, w0=(933500,'J/mol'), E0=(156339,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4452498067966145, var=1.0625970075483286, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C
    Total Standard Deviation in ln(k): 3.185246058202529"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 3.185246058202529""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 3.185246058202529
""",
)

entry(
    index = 24,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(1.285e-08,'m^3/(mol*s)'), n=3.6, Ea=(127.328,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C_Ext-7C-R",
    kinetics = Arrhenius(A=(1.21667e-12,'m^3/(mol*s)'), n=4.98, Ea=(448.65,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C_Ext-7C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C_Ext-7C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C_Ext-7C-R",
    kinetics = Arrhenius(A=(7.3e-07,'m^3/(mol*s)'), n=3.33, Ea=(257.047,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C_Ext-7C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C_Ext-7C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(1.45169e-09,'m^3/(mol*s)'), n=3.84467, w0=(933500,'J/mol'), E0=(158984,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.484123604760289, var=0.5794281111040456, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 2.742398825020564"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 2.742398825020564""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 2.742398825020564
""",
)

entry(
    index = 28,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(4.615e-09,'m^3/(mol*s)'), n=3.71, Ea=(128.99,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(1.68158e-09,'m^3/(mol*s)'), n=3.82474, w0=(933500,'J/mol'), E0=(161640,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5485726981941433, var=0.16989299674183217, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 2.204636633450245"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 2.204636633450245""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 2.204636633450245
""",
)

entry(
    index = 30,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = Arrhenius(A=(1.335e-09,'m^3/(mol*s)'), n=3.86, Ea=(130.288,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C",
    kinetics = ArrheniusBM(A=(1.49518e-09,'m^3/(mol*s)'), n=3.83388, w0=(933500,'J/mol'), E0=(162226,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6737934600289179, var=0.44436773180105216, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
    Total Standard Deviation in ln(k): 3.02932309725572"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 3.02932309725572""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 3.02932309725572
""",
)

entry(
    index = 32,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C",
    kinetics = Arrhenius(A=(2.24e-09,'m^3/(mol*s)'), n=3.8, Ea=(138.362,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C",
    kinetics = Arrhenius(A=(2.545e-09,'m^3/(mol*s)'), n=3.78, Ea=(140.221,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C",
    kinetics = Arrhenius(A=(9.35e-10,'m^3/(mol*s)'), n=3.88, Ea=(138.23,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

